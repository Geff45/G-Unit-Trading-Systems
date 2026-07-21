from service_manager import Service



print(
    Service.create(
        "Trading-AI-Engine"
    )
)



print(
    Service.start(
        "Trading-AI-Engine"
    )
)



print(
    Service.health(
        "Trading-AI-Engine"
    )
)



print(
    Service.stop(
        "Trading-AI-Engine"
    )
)