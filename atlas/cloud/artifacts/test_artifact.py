from artifact_model import Artifact

from artifact_store import ArtifactStore

from artifact_validator import ArtifactValidator



artifact = Artifact(

    name="G-Unit-Trading-System",

    version="1.0.0",

    platform="MT4"

)



validator = ArtifactValidator()


print(
    validator.validate(artifact)
)



store = ArtifactStore()


print(
    store.save(artifact)
)


print(
    store.list()
)