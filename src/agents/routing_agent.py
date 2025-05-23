from typing import Dict
from src.agents.agent_utils import run_agent_task
import json

class RoutingAgent:
    """
    Decides when to escalate to human specialists and provides case summaries for handoff.
    """

    def route_case(self, risk_data: Dict[str, str]) -> Dict[str, str]:
        """
        Determine escalation and provide a case summary using an external LLM.

        Args:
            risk_data (Dict[str, str]): Risk assessment and likely conditions.

        Returns:
            Dict[str, str]: Routing decision and case summary.
        """
        prompt = (
            "Given the following risk assessment data, decide if escalation to a human specialist is needed and provide a case summary. "
            "Respond in JSON with keys 'escalate' (true/false) and 'case_summary'.\n\n"
            f"Risk Data: {json.dumps(risk_data)}"
        )
        result = run_agent_task(
            role="Case Routing Specialist",
            goal="Decide when to escalate to human specialists and provide case summaries for handoff.",
            backstory="You are an experienced medical AI assistant specializing in routing and escalation decisions.",
            prompt=prompt,
            expected_output="A JSON object with the required fields as described in the prompt."
        )
        if result is None:
            return {
                "escalate": False,
                "case_summary": "Unable to generate summary.",
                "error": "LLM connection or parsing error"
            }
        return result
