key="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"

from openai import OpenAI
client = OpenAI(api_key=key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)