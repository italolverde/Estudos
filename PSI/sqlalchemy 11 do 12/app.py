from database.config import start_db, destroy_db
from database.models import User
from database.config import session
from faker import Faker

gerador_faker = Faker()
start_db()

# user = User(name='romerito')
# print(user)

# for _ in range(100):
#     fake_name = gerador_faker.unique.name()
#     user = User(name=fake_name)
#     session.add(user)
# session.commit()


#destroy_db()