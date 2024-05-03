
import sys

from agent import RecursiveThoughtsAgent

def user_prompt():
    print("Welcome to the model interaction CLI.")
    while True:
        model_request = input("What model are you looking to serve? (Type 'help' for options or 'quit' to exit): ")
        if model_request.lower() == 'quit':
            print("Exiting the application.")
            break
        elif model_request.lower() == 'help':
            content_type = input("What type of content would you like to generate? ")
            handle_content_request(content_type)
        else:
            handle_model_request(model_request)

def handle_model_request(model_name):
    system_objective = f"Serve the model {model_name} effectively."
    agent = RecursiveThoughtsAgent(system_objective)
    initial_prompt = f"Set up and serve the model {model_name}."
    response, score = agent.recursive_thoughts(initial_prompt)
    print(f"Suggested Setup: {response}\nRelevance Score: {score:.2f}")

def handle_content_request(content_type):
    system_objective = f"Serve a model capable of generating {content_type} content."
    agent = RecursiveThoughtsAgent(system_objective)
    initial_prompt = f"Generate content related to {content_type}."
    response, score = agent.recursive_thoughts(initial_prompt)
    print(f"Suggested Content Generation Strategy: {response}\nRelevance Score: {score:.2f}")

if __name__ == "__main__":
    user_prompt()
