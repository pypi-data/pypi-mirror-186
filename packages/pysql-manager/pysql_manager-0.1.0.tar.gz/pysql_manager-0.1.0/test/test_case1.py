from pysql_manager import PySql
from pysql_manager.types import Column, IntegerType, StringType

class User:
    id = Column(col_type=IntegerType())
    name = Column(col_type=StringType(25))
    age = Column(col_type=IntegerType())
    __table__ = "User"

#
users = PySql("localhost", "root", "Probadhu@1122", "Test", User)
# data = [{"id": 13, "age": 26}, {"id": 14, "name": "Faisal", "age": 26}]
#
# users.insert(data, update_on_duplicate=["name", "age"])

# print(users.filter(named="Faisal").count())
users.filter(age=30).save_as_csv()

