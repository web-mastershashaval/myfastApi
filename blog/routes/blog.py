from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database
from blog.repositories import blog 

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

@router.get('/', response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id: int, db: Session = Depends(database.get_db)):
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)

@router.get('/{id}', response_model=schemas.ShowBlog)
def show_blog(id: int, db: Session = Depends(database.get_db)):
    return blog.show_blog(id, db)
