from transformers import pipeline

def chat(prompt):
    chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
    response = chatbot(prompt, max_length=50, do_sample=True)
    return response[0]['generated_text']
