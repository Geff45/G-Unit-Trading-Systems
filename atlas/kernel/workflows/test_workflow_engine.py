from kernel.workflows.workflow import Workflow

from kernel.workflows.workflow_descriptor import (
    WorkflowDescriptor,
)

from kernel.workflows.workflow_engine import (
    WorkflowEngine,
)


class ResearchWorkflow(Workflow):

    def build(self):

        print()

        print("Research Workflow")

        print()

        print("Download Calendar")

        print("Download FRED")

        print("Download News")

        print("Run AI")

        print("Decision Council")

        print("Risk Engine")

        print("Trade Execution")


engine = WorkflowEngine()

workflow = ResearchWorkflow(

    WorkflowDescriptor(

        workflow_id="research",

        name="Research Workflow",

        version="1.0.0",

        description="Enterprise Research Workflow",
    )
)

engine.register(workflow)

engine.run("research")