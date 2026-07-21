class LoadBalancer:


    def select_worker(self, workers):

        if not workers:

            return None


        return workers[0]