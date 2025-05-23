from typing import Dict
from src.agents.agent_utils import run_agent_task

class SymptomIntakeAgent:
    """
    Handles initial symptom collection and performs NLP classification of symptoms.
    """

    def collect_symptoms(self, raw_input: str) -> Dict[str, str]:
        """
        Process raw input to extract structured symptom data using an external LLM.

        Args:
            raw_input (str): The user's description of symptoms.

        Returns:
            Dict[str, str]: Structured symptom data.
        """
        prompt = (
            "You are a medical intake assistant.\n"
            "Given a patient's symptom description, extract:\n"
            "- A concise summary of the main symptoms.\n"
            "- The most specific classification from this list: "
            "[\"respiratory\", \"gastrointestinal\", \"dermatological\", \"neurological\", \"musculoskeletal\", \"general\", \"unknown\"].\n"
            "Respond in JSON with keys \"symptom_summary\" and \"classification\".\n\n"
            "Examples:\n"
            "Description: \"I've had a cough and trouble breathing for two days.\"\n"
            "{\n  \"symptom_summary\": \"Cough and shortness of breath for two days.\",\n  \"classification\": \"respiratory\"\n}\n\n"
            "Description: \"My stomach hurts and I've had diarrhea.\"\n"
            "{\n  \"symptom_summary\": \"Abdominal pain and diarrhea.\",\n  \"classification\": \"gastrointestinal\"\n}\n\n"
            "Description: \"I feel tired.\"\n"
            "{\n  \"symptom_summary\": \"Fatigue.\",\n  \"classification\": \"general\"\n}\n\n"
            "Description: \"I have a rash on my arm.\"\n"
            "{\n  \"symptom_summary\": \"Rash on arm.\",\n  \"classification\": \"dermatological\"\n}\n\n"
            f"Description: {raw_input}"
        )
        result = run_agent_task(
            role="Symptom Intake Specialist",
            goal="Handle initial symptom collection and perform NLP classification of symptoms.",
            backstory="You are a medical intake assistant skilled at extracting and classifying symptoms from patient descriptions.",
            prompt=prompt,
            expected_output="A JSON object with the required fields as described in the prompt."
        )
        if result is None:
            return {
                "symptom_summary": raw_input,
                "classification": "unknown",
                "error": "LLM connection or parsing error"
            }
        return result
