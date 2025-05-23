from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="patients")

class TriageCase(Base):
    __tablename__ = "triage_cases"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    symptoms = Column(String, nullable=False)
    risk_level = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    patient = relationship("Patient", back_populates="triage_cases")

User.patients = relationship("Patient", back_populates="user")
Patient.triage_cases = relationship("TriageCase", back_populates="patient")
