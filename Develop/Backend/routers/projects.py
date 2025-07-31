from typing import List
from connect import get_db
from models import ProjectModel
from schema import Project, ProjectResponse
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Response

router = APIRouter(
    tags = ["Projects"],
    prefix = "/projects"
)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=ProjectResponse)
def create_project(data:Project, db: Session = Depends(get_db)):
    new_projects = ProjectModel(**data.dict())
    db.add(new_projects)
    db.commit()
    db.refresh(new_projects)

    return new_projects

@router.get("/", response_model=List[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(ProjectModel).all()

    if not projects:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No projects found")

    return projects

@router.get("/{id}", response_model=ProjectResponse)
def get_project(id: int, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).filter(ProjectModel.id == id).first()

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No project found")

    return project

@router.put("/{id}", response_model=ProjectResponse)
def update_project(id: int, data: Project, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).filter(ProjectModel.id == id)

    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No project found")

    project.update(data.dict())
    db.commit()

    return project.first()


@router.delete("/{id}", response_model=ProjectResponse)
def update_project(id: int, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).filter(ProjectModel.id == id)

    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No project found")
        
    project.delete()
    db.commit()

    return Response(status_code = status.HTTP_204_NO_CONTENT)
