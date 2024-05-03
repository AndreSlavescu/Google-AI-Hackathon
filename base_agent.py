from model import GeminiProInterface
from sentence_transformers import SentenceTransformer, util

class RecursiveThoughtsAgent:
    def __init__(self, system_objective):
        self.gemini_interface = GeminiProInterface()
        self.objective = system_objective
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def evaluate_response(self, response):
        response_embedding = self.model.encode(response, convert_to_tensor=True)
        objective_embedding = self.model.encode(self.objective, convert_to_tensor=True)
        similarity_score = util.pytorch_cos_sim(response_embedding, objective_embedding).item()
        return similarity_score

    def recursive_thoughts(self, prompt, depth=3, breadth=3):
        if depth == 0:
            return prompt, self.evaluate_response(prompt)
        
        try:
            responses = [self.gemini_interface.generate_response(prompt) for _ in range(breadth)]
        except Exception as e:
            print(f"Error generating responses: {e}")
            responses = [prompt] * breadth 

        scored_responses = [(response, self.evaluate_response(response)) for response in responses]
        best_response, best_score = max(scored_responses, key=lambda x: x[1])
        next_prompt, next_score = self.recursive_thoughts(best_response, depth - 1, breadth)
        return next_prompt, max(best_score, next_score)
