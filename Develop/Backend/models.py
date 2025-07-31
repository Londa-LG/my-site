from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class ProjectModel(Base):
    __tablename__ = "Projects"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    snapshot: Mapped[str] = mapped_column(nullable=False)
    project_name: Mapped[str] = mapped_column(nullable=False)
    summary: Mapped[str] = mapped_column(nullable=False)
    link: Mapped[str] = mapped_column(nullable=False)
    tech_str: Mapped[str] = mapped_column(nullable=False)

class ProfileModel(Base):
    __tablename__= "Profile"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    initials: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    summary: Mapped[str] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    tech: Mapped[str] = mapped_column(nullable=False)
