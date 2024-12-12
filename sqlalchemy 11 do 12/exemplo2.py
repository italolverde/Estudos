from database.config import start_db, destroy_db
from database.config import session
from database.models import User, Recipe


start_db()

user = session.query(User).first()
recipe = Recipe(name='papa', user_id=user.id)

session.add(recipe)

session.commit()

print(user.recipes)

# recipe2 = session.query(Recipe).first()
# print(recipe2.user)
print(recipe.user)

destroy_db()