from server import HubServer



server = HubServer()



print(
    server.start()
)



print(
    server.register_route(
        "/projects",
        "ProjectRegistry"
    )
)


print(
    server.routes.list()
)