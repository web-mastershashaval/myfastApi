from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return { 'data':'hello sambaman'}

@app.get('/about')
def about():
    return { 'date':{'about page'}}
