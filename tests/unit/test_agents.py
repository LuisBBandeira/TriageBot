import pytest
from src.agents.symptom_intake_agent import SymptomIntakeAgent
from src.agents.risk_assessment_agent import RiskAssessmentAgent
from src.agents.routing_agent import RoutingAgent

def test_symptom_intake_agent():
    agent = SymptomIntakeAgent()
    raw_input = "I have a fever and a sore throat."
    result = agent.collect_symptoms(raw_input)
    assert "symptom_summary" in result
    assert "classification" in result

def test_risk_assessment_agent():
    agent = RiskAssessmentAgent()
    symptoms = {"symptom_summary": "fever and sore throat", "classification": "general_symptoms"}
    result = agent.assess_risk(symptoms)
    assert "risk_level" in result
    assert "likely_conditions" in result
    assert isinstance(result["likely_conditions"], list)

def test_routing_agent():
    agent = RoutingAgent()
    risk_data = {"risk_level": "low", "likely_conditions": ["common_cold"]}
    result = agent.route_case(risk_data)
    assert "escalate" in result
    assert "case_summary" in result
