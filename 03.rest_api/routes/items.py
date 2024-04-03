from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud_orm
from dependencies import get_db

router = APIRouter(prefix='/api/v1/')
# api/v1/item

# api/v1/item/{item_id}
@router.get('/{item_id}')
def get_item(item_id: int, db: Session = Depends(get_db)):
    return crud_orm.get_item(db, item_id)

@router.get('/')
def get_items(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    return crud_orm.get_itmes(db, skip, limit) # items

import schemas
@router.post('/')    
def create_item(owner_id: int, item_create: schemas.ItemCreate, db: Session=Depends(get_db)):
    return crud_orm.create_item(db, item_create, owner_id)

@router.put('/{item_id}')
def update_item(item_id: int, item_update: schemas.ItemUpdate, db: Session=Depends(get_db)):
    return crud_orm.update_item(db, item_update, item_id)

@router.delete('/{item_id}')
def delete_item(item_id: int, db: Session=Depends(get_db)):
    is_success = crud_orm.delete_item(db, item_id) #return True // None ..

    if not is_success:
        raise HTTPException(404, 'Fail to delete item')
    return {'msg':'Item delete success'}
