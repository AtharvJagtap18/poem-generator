from transformers import pipeline, set_seed
import random

def load_generator(model_name="gpt2", seed=42):
    generator = pipeline('text-generation', model=model_name)
    set_seed(seed)
    return generator

def generate_prompt(topic, style):
    templates = {
        "romantic": f"Compose a romantic poem about {topic}, full of emotions and metaphors.",
        "haiku": f"Write a haiku about {topic}. Follow the 5-7-5 syllable structure.",
        "horror": f"Write a dark, eerie horror poem about {topic}, with vivid imagery.",
        "inspirational": f"Write an inspirational poem about {topic}, uplifting and poetic.",
        "default": f"Write a poem about {topic} in a creative and thoughtful way."
    }
    return templates.get(style.lower(), templates["default"])

def format_poem(raw_text):
    # Clean and attempt to make it more poetic by adding line breaks
    lines = raw_text.strip().split(". ")
    poem = "\n".join(line.strip() for line in lines if line)
    return poem

def generate_poem(topic, generator, style="default", max_length=100):
    prompt = generate_prompt(topic, style)
    output = generator(prompt, max_length=max_length, num_return_sequences=1, do_sample=True)[0]['generated_text']
    return format_poem(output)
