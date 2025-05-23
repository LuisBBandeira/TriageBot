from fastapi import FastAPI
from src.api.endpoints import auth, triage

# Initialize FastAPI app
app = FastAPI(
    title="AI-Powered Virtual Triage Nurse System",
    description="A CLI-based virtual triage system for symptom intake, risk assessment, and routing.",
    version="0.1.0",
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(triage.router, prefix="/triage", tags=["Triage"])

# Middleware and other configurations can be added here

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
