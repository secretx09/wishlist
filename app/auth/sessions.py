from fastapi import Cookie, Depends, HTTPException
from ..routes.users import get_db
from sqlalchemy.orm import Session
from uuid import uuid4
from app.models.session import Session as SessionModel 

def create_session(db:Session, user_id: int) -> str:
    session_id = str(uuid4())
    db_session = SessionModel(session_id=session_id, user_id=user_id)
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return session_id

def get_user_id_from_session(db:Session, session_id:str):
    session = db.query(SessionModel).filter(SessionModel.session_id == session_id).first()
    if session:
        return session.user_id
    return None

def  get_current_user(
        session_id: str = Cookie(None),
        db: Session = Depends(get_db)
    ):
    if session_id is None:
        raise HTTPException(status_code=401, detail="Not logged in")
    
    user_id = get_user_id_from_session(db, session_id)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid session")
    
    return user_id