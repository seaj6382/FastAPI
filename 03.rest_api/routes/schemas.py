from pydantic import BaseModel
from typing import List
from typing import Optional

# schemas/item.py
# schemas/user.py

# pydantic -> 데이터 유효성 검즈
class ItemBase (BaseModel):
    title: str
    description: str

class Item (ItemBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode =True # orm 방식으로 데이터 필드 읽기가 가능

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None


class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int
    items: List[Item] =[]

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    hashed_password: str

# from typing import Optional
class UserUpdate(UserBase):
    email: str | None = None # 3.10부터.. 등장
    hashed_password: str | None = None # 3.10부터.. 등장
    # email: Optional[str] = None # 3.10부터.. 등장
    # password: Optional[str] = None