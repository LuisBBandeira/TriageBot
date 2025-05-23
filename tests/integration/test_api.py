from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_symptom_intake_endpoint():
    response = client.post("/triage/symptom-intake", json={"raw_input": "I have a headache and nausea."})
    assert response.status_code == 200
    data = response.json()
    assert "structured_data" in data
    assert data["structured_data"]["symptom_summary"] == "I have a headache and nausea."

def test_risk_assessment_endpoint():
    symptoms = {"symptom_summary": "headache and nausea", "classification": "general_symptoms"}
    response = client.post("/triage/risk-assessment", json=symptoms)
    assert response.status_code == 200
    data = response.json()
    assert "risk_data" in data
    assert data["risk_data"]["risk_level"] == "low"

def test_route_case_endpoint():
    risk_data = {"risk_level": "low", "likely_conditions": ["migraine"]}
    response = client.post("/triage/route-case", json=risk_data)
    assert response.status_code == 200
    data = response.json()
    assert "routing_decision" in data
    assert data["routing_decision"]["escalate"] is False
