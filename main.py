from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get('/')
def index():
    return { 'data':'hello sambaman'}

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f'Blog is created with the title{Blog.title}'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':{
        'name':'unpublished is here '
    }
    
    }

@app.get('/about/{id}')
def about(id: int):
    return { 'date':id}


@app.get('/blog/{id}/comments')
def comments():
    return {'data':{'1','2'}}