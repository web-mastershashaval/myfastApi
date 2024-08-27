from .. import schemas, database, models
from sqlalchemy.orm import Session
from fastapi import *



from fastapi import APIRouter
router = APIRouter( tags=['Authentication'])

@router.post('/login')
def login(request:schemas.login,db: Session = Depends(database.get_db())):
    user = db.query(models.User).filter(models.User.email == request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, default="Invalid credentials try again")
    return "login"
