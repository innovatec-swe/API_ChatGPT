import openai
openai.api_key = "YOUR_API_KEY_HERE"

# Set up the API request parameters
prompt = "Write a short story about a man who can teleport anywhere in the world."
model = "text-davinci-002"
temperature = 0.7
max_tokens = 60

# Call the API to generate the text
response = openai.Completion.create(
  engine=model,
  prompt=prompt,
  temperature=temperature,
  max_tokens=max_tokens
)

# Print the generated text
print(response.choices[0].text)
