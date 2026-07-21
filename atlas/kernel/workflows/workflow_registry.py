class WorkflowRegistry:
    
    def __init__(self):

        self._workflows = {}

    def register(self, workflow):

        self._workflows[
            workflow.descriptor.workflow_id
        ] = workflow

    def get(self, workflow_id):

        return self._workflows.get(workflow_id)

    def all(self):

        return list(self._workflows.values())

    def count(self):

        return len(self._workflows)