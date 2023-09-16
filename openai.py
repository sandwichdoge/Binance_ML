import openai

# Replace with your OpenAI API key
api_keys = ["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", "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"]

def generate_text_from_numbers(numbers):
    prompt = "Generate a text based on the following list of numbers:\n" + "\n".join(map(str, numbers))

    # TODO cycle through keys
  
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose the engine that suits your needs
        prompt=prompt,
        max_tokens=100  # You can adjust the max_tokens as needed
    )

    generated_text = response.choices[0].text.strip()
    return generated_text

# Example usage:
input_numbers = [1, 2, 3, 4, 5]
generated_text = generate_text_from_numbers(input_numbers)
print(generated_text)
