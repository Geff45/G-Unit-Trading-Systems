"""
Atlas Event SDK

Central event communication system.
"""


class Event:


    listeners = {}



    @classmethod
    def subscribe(cls,event,callback):

        if event not in cls.listeners:

            cls.listeners[event] = []


        cls.listeners[event].append(callback)


        return {

            "status":"subscribed",

            "event":event

        }



    @classmethod
    def publish(cls,event,data=None):

        results = []


        for callback in cls.listeners.get(event,[]):

            results.append(
                callback(data)
            )


        return {

            "event":event,

            "listeners":len(results),

            "results":results

        }



    @classmethod
    def unsubscribe(cls,event,callback):

        if event in cls.listeners:

            cls.listeners[event].remove(callback)


        return {

            "status":"removed",

            "event":event

        }