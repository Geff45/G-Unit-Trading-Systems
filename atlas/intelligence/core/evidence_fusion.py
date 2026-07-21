class EvidenceFusion:
    
    def fuse(

        self,

        evidence_list

    ):

        if not evidence_list:

            return 0.0

        total = 0.0

        weight = 0.0

        for evidence in evidence_list:

            score = (

                evidence.direction *

                evidence.confidence *

                evidence.weight
            )

            total += score

            weight += evidence.weight

        if weight == 0:

            return 0.0

        return total / weight