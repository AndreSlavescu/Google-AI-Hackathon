from agent import GeminiProInterface
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
        print(f"\nDepth {depth}: Prompt: '{prompt}'")
        if depth == 0:
            final_request_model = GeminiProInterface(model_name="gemini-1.5-pro-preview-0409")
            final_response = final_request_model.generate_response(
                prompt=f"Given the following code example that was yielded so far, write the optimal final response. Remember it must be a valid python file:\n {prompt}")
            print(f"Final Response: '{final_response}'")
            return final_response, 1.0
        
        try:
            responses = [self.gemini_interface.generate_response(prompt) for _ in range(breadth)]
        except Exception as e:
            print(f"Error generating responses: {e}")
            responses = [prompt] * breadth 

        scored_responses = [(response, self.evaluate_response(response)) for response in responses]
        best_response, best_score = max(scored_responses, key=lambda x: x[1])

        print(f"Selected Best Response: '{best_response}' with score: {best_score}")

        next_prompt, next_score = self.recursive_thoughts(best_response, depth - 1, breadth)
        final_score = max(best_score, next_score)
        if depth == 3:
            print(f"\nTop-Level Thought Completion: '{next_prompt}' with final score: {final_score}")

        return next_prompt, max(best_score, next_score)
