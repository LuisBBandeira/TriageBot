from fastapi import APIRouter, HTTPException
from src.agents.symptom_intake_agent import SymptomIntakeAgent
from src.agents.risk_assessment_agent import RiskAssessmentAgent
from src.agents.routing_agent import RoutingAgent

router = APIRouter()

# Initialize agents
symptom_agent = SymptomIntakeAgent()
risk_agent = RiskAssessmentAgent()
routing_agent = RoutingAgent()

@router.post("/symptom-intake")
async def symptom_intake(raw_input: str):
    """
    Endpoint to collect and classify symptoms.
    """
    if not raw_input:
        raise HTTPException(status_code=400, detail="Input cannot be empty.")
    structured_data = symptom_agent.collect_symptoms(raw_input)
    return {"structured_data": structured_data}

@router.post("/risk-assessment")
async def risk_assessment(symptoms: dict):
    """
    Endpoint to assess risk based on symptoms.
    """
    if not symptoms:
        raise HTTPException(status_code=400, detail="Symptoms cannot be empty.")
    risk_data = risk_agent.assess_risk(symptoms)
    return {"risk_data": risk_data}

@router.post("/route-case")
async def route_case(risk_data: dict):
    """
    Endpoint to determine escalation and provide a case summary.
    """
    if not risk_data:
        raise HTTPException(status_code=400, detail="Risk data cannot be empty.")
    routing_decision = routing_agent.route_case(risk_data)
    return {"routing_decision": routing_decision}
