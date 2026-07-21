from kernel.bootstrap.bootstrap import AtlasBootstrap

bootstrap = AtlasBootstrap()

runtime = bootstrap.boot()

print(type(runtime).__name__)