from kernel.workflows.workflow_manager import (
    WorkflowManager,
)


class WorkflowEngine:

    def __init__(self):

        self.manager = WorkflowManager()

    def register(self, workflow):

        self.manager.register(workflow)

    def run(self, workflow_id):

        self.manager.execute(workflow_id)