from event_bus import Event



def build_completed(data):

    return {

        "message":"Build finished",

        "data":data

    }



print(
    Event.subscribe(
        "build.complete",
        build_completed
    )
)



print(
    Event.publish(
        "build.complete",
        {
            "project":"G-Unit-Trading-System"
        }
    )
)



print(
    Event.unsubscribe(
        "build.complete",
        build_completed
    )
)