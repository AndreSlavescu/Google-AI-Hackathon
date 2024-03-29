from vertexai.preview.generative_models import GenerativeModel

gemini_pro_model = GenerativeModel("gemini-1.0-pro")
model_response = gemini_pro_model.generate_content("I want you to write me a python file that allows me to use llama 7B from huggingface.")
print("model_response\n",model_response.candidates[0].content.text)
