"""
Atlas Artifact Validator

Checks artifact integrity.
"""


class ArtifactValidator:


    def validate(self, artifact):


        errors = []


        if not artifact.name:

            errors.append(
                "missing_name"
            )


        if not artifact.version:

            errors.append(
                "missing_version"
            )


        return {

            "valid": len(errors) == 0,

            "errors": errors

        }