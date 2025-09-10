from openai import OpenAI

api_key = "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"

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def generate_recipe(ingredients):
    prompt = f"""
You are a helpful chef assistant. 
Write a simple, clear recipe using these ingredients: {', '.join(ingredients)}.

Structure the recipe as follows:
- Title
- Servings
- Total time
- Ingredients (bullet list)
- Step-by-step Instructions (numbered list)
- Tips (optional)

Keep the language easy to understand and the recipe concise.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=700  # Increase tokens to allow longer responses
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    ingredients = input("Enter ingredients separated by commas: ").split(",")
    ingredients = [i.strip() for i in ingredients]
    recipe = generate_recipe(ingredients)
    print("\nGenerated Recipe:\n")
    print(recipe)
