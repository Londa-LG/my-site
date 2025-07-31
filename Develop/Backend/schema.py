from typing import List
from pydantic import EmailStr, BaseModel

class Project(BaseModel):
    snapshot: str
    project_name: str
    summary: str
    link: str
    tech_str: str

class ProjectResponse(BaseModel):
    snapshot: str
    project_name: str
    summary: str
    link: str
    tech_str: str

class Profile(BaseModel):
    name: str
    surname: str
    initials: str
    email: EmailStr
    summary: str
    title: str
    tech: str

class ProfileResponse(BaseModel):
    name: str
    surname: str
    email: EmailStr
    summary: str
    title: str
    tech: str
