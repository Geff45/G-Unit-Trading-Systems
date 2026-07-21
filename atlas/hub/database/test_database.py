from models import Project

from storage import Storage



project = Project(

    name="G-Unit-Trading-System",

    version="1.0.0",

    owner="G-Unit"

)



database = Storage()



print(
    database.save(
        project.describe()
    )
)



print(
    database.all()
)