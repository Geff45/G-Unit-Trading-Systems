from kernel.security.permission import Permission
from kernel.security.security_gateway import SecurityGateway

gateway = SecurityGateway()

gateway.grant(

    "risk_engine",

    Permission.EXECUTE,

)

print(

    gateway.authorize(

        "risk_engine",

        Permission.EXECUTE,

    )

)

print(

    gateway.authorize(

        "trend_engine",

        Permission.EXECUTE,

    )

)