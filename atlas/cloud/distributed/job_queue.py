class JobQueue:

    def __init__(self):
        self.jobs = []


    def add(self, job):

        self.jobs.append(
            {
                "job": job,
                "status": "queued"
            }
        )

        return {
            "status": "queued",
            "job": job
        }


    def next(self):

        if len(self.jobs) == 0:
            return None

        task = self.jobs.pop(0)

        task["status"] = "running"

        return task


    def list(self):

        return self.jobs