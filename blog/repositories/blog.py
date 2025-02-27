from sqlalchemy.orm import Session
from fastapi import  HTTPException, status
from .. import models, schemas
def get_all(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    db.delete(blog)
    db.commit()
    
    return {"message": "Blog deleted successfully"}

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog.title = request.title
    blog.body = request.body
    
    db.commit()
    
    return {"message": "Blog updated successfully"}

def show_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    return blog