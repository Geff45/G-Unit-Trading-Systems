"""
Atlas Cloud Configuration

Central configuration manager
for deployment environments.
"""


from dataclasses import dataclass, field


@dataclass
class CloudConfig:

    provider: str = "local"

    region: str = "default"

    environment: str = "development"

    workspace: str = "./atlas_workspace"

    credentials: dict = field(default_factory=dict)


    def set_provider(self, provider):

        self.provider = provider


    def get_provider(self):

        return self.provider


    def describe(self):

        return {

            "provider": self.provider,

            "region": self.region,

            "environment": self.environment,

            "workspace": self.workspace

        }