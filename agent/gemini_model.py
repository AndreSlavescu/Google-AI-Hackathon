from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
)

class GeminiProInterface:
    def __init__(self, model_name="gemini-1.0-pro"):
        self.gemini_pro_model = GenerativeModel(
            model_name=model_name,
            system_instruction=[
                "You are an expert programmer with knowledge about all things related to model inference.",
                "You are to set up a robust pipeline capable for running inference with open source models found on huggingface.",
                "Only write code. No need for explanations."
            ],
        )
        self.generation_config = GenerationConfig(
            temperature=0.9,
            top_p=1.0,
            top_k=8,
            candidate_count=1,
            max_output_tokens=8192,
        )

    def generate_response(self, prompt):
        try:
            self.adjust_generation_settings(prompt)
            model_response = self.gemini_pro_model.generate_content(
                [prompt],
                generation_config=self.generation_config,
            )
            return model_response.text
        except Exception as e:
            print(f"Error in model generation: {e}")
            return prompt 

    def adjust_generation_settings(self, prompt):
        depth_indicator = len(prompt.split())  
        if depth_indicator > 100:
            self.generation_config.temperature = 0.5  
            self.generation_config.top_k = 20
        else:
            self.generation_config.temperature = 0.9  
            self.generation_config.top_k = 8
