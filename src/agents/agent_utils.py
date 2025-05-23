from crewai import Agent, Task, Crew
from src.llm import  get_llma_llm
import json
import logging

def run_agent_task(role, goal, backstory, prompt, expected_output):
    """
    Utility to run a CrewAI agent task with standardized error handling.
    """
    try:
        # Get the LLM instance
        llm = get_llma_llm()
        
        agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            verbose=True, 
            llm=llm
        )
        
        task = Task(
            description=prompt,
            agent=agent,
            expected_output=expected_output
        )
        
        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=True  
        )
        
        llm_response = crew.kickoff()[0]
        
        try:
            return json.loads(llm_response)
        except json.JSONDecodeError:
            logging.error(f"Failed to parse JSON from LLM response: {llm_response}")
            return {"error": "Invalid JSON response", "raw_response": llm_response}
            
    except Exception as e:
        logging.error(f"LLM connection or processing error in {role}: {str(e)}")
        return None
