from typing import Dict
from src.agents.agent_utils import run_agent_task
import json

class RiskAssessmentAgent:
    """
    Applies clinical guidelines to assess risk and suggest likely conditions using Crew AI.
    """

    def assess_risk(self, symptoms: Dict[str, str]) -> Dict[str, str]:
        """
        Assess the risk level based on symptoms and suggest likely conditions using Crew AI.

        Args:
            symptoms (Dict[str, str]): Structured symptom data.

        Returns:
            Dict[str, str]: Risk assessment and likely conditions.
        """
        prompt = (
            "Given the following structured symptom data, assess the risk level and suggest likely conditions. "
            "Respond in JSON with keys 'risk_level' and 'likely_conditions' (as a list).\n\n"
            f"Symptoms: {json.dumps(symptoms)}"
        )
        result = run_agent_task(
            role="Medical Risk Assessor",
            goal="Assess patient risk and suggest likely conditions based on symptoms.",
            backstory="You are an experienced medical AI assistant specializing in triage and risk assessment.",
            prompt=prompt,
            expected_output="A JSON object with the required fields as described in the prompt."
        )
        if result is None:
            return {
                "risk_level": "unknown",
                "likely_conditions": [],
                "error": "LLM connection or parsing error"
            }
        return result
