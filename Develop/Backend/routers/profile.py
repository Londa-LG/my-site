from typing import List
from connect import get_db
from models import ProfileModel
from schema import Profile, ProfileResponse
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter, status, Response

router = APIRouter(
    tags = ["Profile"],
    prefix = "/profile"
)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=ProfileResponse)
def create_profile(data: Profile, db: Session = Depends(get_db)):
    profile = ProfileModel(**data.dict())

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile

@router.get("/", response_model=List[ProfileResponse])
def get_profiles(db: Session = Depends(get_db)):
    profiles = db.query(ProfileModel).all()

    if not profiles:
        raise HTTPException(status_code=satus.HTTP_404_NOT_FOUND, detail="No profiles found")

    return profiles

@router.get("/{id}", response_model=ProfileResponse)
def get_profile(id: int, db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).filter(ProfileModel.id == id).first()
    
    if not profile:
        raise HTTPException(status_code=satus.HTTP_404_NOT_FOUND, detail="No profile found")

    return profile

@router.put("/{id}", response_model=ProfileResponse)
def update_profile(id: int, data: Profile, db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).filter(ProfileModel.id == id)

    if not profile.first():
        raise HTTPException(status_code=satus.HTTP_404_NOT_FOUND, detail="No profile found")

    profile.update(data.dict())
    db.commit()

    return profile.first()

@router.delete("/{id}", response_model=ProfileResponse)
def delete_profile(id: int, db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).filter(ProfileModel.id == id)
    
    if not profile.first():
        raise HTTPException(status_code=satus.HTTP_404_NOT_FOUND, detail="No profile found")

    profile.delete()
    db.commit()

    return Response(status_code = status.HTTP_204_NO_CONTENT)
