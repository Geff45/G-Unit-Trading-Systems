from kernel.workflows.workflow_registry import (
    WorkflowRegistry,
)


class WorkflowManager:

    def __init__(self):

        self.registry = WorkflowRegistry()

    def register(self, workflow):

        self.registry.register(workflow)

    def execute(self, workflow_id):

        workflow = self.registry.get(workflow_id)

        workflow.build()