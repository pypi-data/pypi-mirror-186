from cryton_core.lib.util import constants, logger, states
from cryton_core.lib.models import stage, session, step, plan, run
from cryton_core.lib.services.scheduler import SchedulerService


class Event:
    def __init__(self, event_details: dict):
        """
        Class containing possible events.
        :param event_details: Received event details
        """
        self.event_details = event_details

    def trigger_stage(self) -> None:
        """
        Process trigger trying to start Stage execution.
        :return: None
        """
        logger.logger.debug("Processing trigger", event_v=self.event_details)

        # Get Stage execution
        trigger_id = self.event_details.get(constants.TRIGGER_ID)
        stage_ex_id = stage.StageExecutionModel.objects.get(trigger_id=trigger_id).id
        stage_ex = stage.StageExecution(stage_execution_id=stage_ex_id)

        # Validate if the Stage can be triggered
        states.StageStateMachine(stage_ex_id).validate_state(stage_ex.state, [states.AWAITING])

        # Custom actions for each trigger type
        if stage_ex.model.stage_model.trigger_type == constants.MSF_LISTENER:
            session_name = f"{stage_ex.model.stage_model.name}_session"
            session.create_session(stage_ex.model.plan_execution_id, self.event_details.get("parameters"), session_name)

        # Stop the trigger and start the Stage execution
        stage_ex.trigger.stop()
        stage_ex.execute()

    def update_scheduler(self) -> int:
        """
        Process scheduler control request.
        :return: -1 if failed, otherwise relevant data (e.g. ID of scheduled job)
        """
        logger.logger.debug("Processing scheduler event", event_v=self.event_details)
        scheduler_action = self.event_details.get(constants.EVENT_ACTION)
        scheduler_args = self.event_details.get('args')

        # TODO: It seems that only the `add_job` actually returns an ID, otherwise probably None, or raises an error
        #  should be reworked with the rework of the scheduler
        scheduler_obj = SchedulerService()
        ret_val = -1
        try:
            if scheduler_action == constants.ADD_JOB:
                ret_val = scheduler_obj.exposed_add_job(**scheduler_args)
            elif scheduler_action == constants.ADD_REPEATING_JOB:
                ret_val = scheduler_obj.exposed_add_repeating_job(**scheduler_args)
            elif scheduler_action == constants.RESCHEDULE_JOB:
                ret_val = scheduler_obj.exposed_reschedule_job(**scheduler_args)
            elif scheduler_action == constants.PAUSE_JOB:
                ret_val = scheduler_obj.exposed_pause_job(**scheduler_args)
            elif scheduler_action == constants.RESUME_JOB:
                ret_val = scheduler_obj.exposed_resume_job(**scheduler_args)
            elif scheduler_action == constants.REMOVE_JOB:
                ret_val = scheduler_obj.exposed_remove_job(**scheduler_args)
            elif scheduler_action == constants.GET_JOBS:
                ret_val = scheduler_obj.exposed_get_jobs()
            elif scheduler_action == constants.PAUSE_SCHEDULER:
                ret_val = scheduler_obj.exposed_pause_scheduler()
            elif scheduler_action == constants.RESUME_SCHEDULER:
                ret_val = scheduler_obj.exposed_resume_scheduler()
            elif scheduler_action == constants.EVENT_HEALTH_CHECK:
                ret_val = scheduler_obj.health_check()
        except Exception as ex:
            logger.logger.error("Scheduler could not process the request", error=str(ex))

        return ret_val if ret_val is not None else 0

    def handle_finished_step(self) -> None:
        """
        Check for FINISHED states.
        :return: None
        """
        step_ex_obj = step.StepExecution(step_execution_id=self.event_details["step_execution_id"])
        logger.logger.debug("Handling finished Step", step_execution_id=step_ex_obj.model.id)

        stage_ex_obj = stage.StageExecution(stage_execution_id=step_ex_obj.model.stage_execution_id)
        is_plan_dynamic = stage_ex_obj.model.stage_model.plan_model.dynamic
        if stage_ex_obj.all_steps_finished and not (is_plan_dynamic and stage_ex_obj.state == states.FINISHED):
            stage_ex_obj.finish()

            plan_ex_obj = plan.PlanExecution(plan_execution_id=stage_ex_obj.model.plan_execution_id)
            if plan_ex_obj.all_stages_finished and not (is_plan_dynamic and plan_ex_obj.state == states.FINISHED):
                plan_ex_obj.finish()

                run_obj = run.Run(run_model_id=plan_ex_obj.model.run_id)
                if run_obj.all_plans_finished and not (is_plan_dynamic and run_obj.state == states.FINISHED):
                    run_obj.finish()
