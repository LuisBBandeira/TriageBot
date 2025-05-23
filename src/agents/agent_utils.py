from crewai import Agent, Task, Crew
from src.llm import  get_llma_llm
import json
import logging
import re

def run_agent_task(role, goal, backstory, prompt, expected_output):
    """
    Utility to run a CrewAI agent task with standardized error handling.
    """
    try:
        # Get the LLM instance
        llm = get_llma_llm()
        
        # Make the prompt more explicit about JSON format
        enhanced_prompt = f"""
{prompt}

IMPORTANT: You must respond ONLY with valid JSON. Do not include any explanatory text before or after the JSON.
Your response must start with {{ and end with }}.

Example format:
{{"symptom_summary": "description here", "classification": "category here"}}
"""
        
        agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            verbose=True, 
            llm=llm
        )
        
        task = Task(
            description=enhanced_prompt,
            agent=agent,
            expected_output=expected_output
        )
        
        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=True  
        )
        
        crew_output = crew.kickoff()
        llm_response = crew_output.raw
        
        json_match = re.search(r'\{.*\}', llm_response, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                pass
        
        try:
            return json.loads(llm_response)
        except json.JSONDecodeError:
            logging.error(f"Failed to parse JSON from LLM response: {llm_response}")
            
            return {
                "error": "Invalid JSON response", 
                "raw_response": llm_response,
                "fallback_parsing": True
            }
            
    except Exception as e:
        logging.error(f"LLM connection or processing error in {role}: {str(e)}")
        return None
