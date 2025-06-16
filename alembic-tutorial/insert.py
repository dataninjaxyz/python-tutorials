from database import SessionLocal
from database import User

with SessionLocal() as sess:
    new_user = User(name="Data Ninja", email="demo@dataninja.xyz", password="VerySecretPassword")
    sess.add(new_user)
    sess.commit()
    