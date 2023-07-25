import os

# import casbin_sqlalchemy_adapter
# import casbin
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import declarative_base
# import asyncio
import traceback

import dotenv
import jwt

dotenv.load_dotenv()

# Base = declarative_base()


# class CasbinRule(Base):
#     __tablename__ = "casbin_rule"

#     id = Column(Integer, primary_key=True)
#     ptype = Column(String(255))
#     v0 = Column(String(255))
#     v1 = Column(String(255))
#     v2 = Column(String(255))
#     v3 = Column(String(255))
#     v4 = Column(String(255))
#     v5 = Column(String(255))

#     def __str__(self):
#         arr = [self.ptype]
#         for v in (self.v0, self.v1, self.v2, self.v3, self.v4, self.v5):
#             if v is None:
#                 break
#             arr.append(v)
#         return ", ".join(arr)

#     def __repr__(self):
#         return '<CasbinRule {}: "{}">'.format(self.id, str(self))

# async def create_database():
#     await adapter.create_table()


# adapter = casbin_sqlalchemy_adapter.Adapter("sqlite:///policy.db", CasbinRule)
# adapter.create_table()
# e = casbin.Enforcer("./auth/auth_model.conf", adapter)

JWT_SECRET = os.getenv("JWT_SECRET_KEY")


def authorize(token: str) -> str | None:
    try:
        # if e.enforce("deepak", "kuber", "delete"):
        print(type(JWT_SECRET))
        decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        print(decoded)
    except Exception:
        traceback.print_exc()
    return None
