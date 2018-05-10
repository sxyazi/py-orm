from Model import BaseModel
from Types import IntField, CharField

class User(BaseModel):
    name = CharField(column='name', max_length=30)
    age  = IntField(column='age', min_value=18, max_value=100)

    class Meta:
        table = 'user'


if __name__ == '__main__':
    u = User()
    u.name = 'yazi'
    u.age  = 18
    print(u.insert())
