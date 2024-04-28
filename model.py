from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
)

class GeminiProInterface:
    def __init__(self):
        self.gemini_pro_model = GenerativeModel(
            model_name="gemini-1.5-pro-preview-0409",
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
        model_response = self.gemini_pro_model.generate_content(
            [prompt],
            generation_config=self.generation_config,
        )
        return model_response.text
