class JobManager:


    def __init__(self):

        self.jobs = []


    def submit(self, name, worker):

        job = {

            "name": name,

            "worker": worker,

            "status": "submitted"

        }

        self.jobs.append(job)

        return job



    def complete(self, name):

        for job in self.jobs:

            if job["name"] == name:

                job["status"] = "completed"

                return job


    def all(self):

        return self.jobs