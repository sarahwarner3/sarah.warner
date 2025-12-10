#Goal:
  #First ask the LLM to pick a business area that might be worth exploring for an Agentic AI opportunity.
  #Then ask the LLM to present a pain-point in that industry - something challenging that might be ripe for an Agentic solution.
  #Finally have the third LLM propose the Agentic AI solution.

#Import and setup
import os
from openai import OpenAI
from IPython.display import Markdown, display

openai_api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

#Step 1:
messages = [{"role": "user", "content": "What is an industry that might be worth exploring for an Agentic AI opportunity?"}]

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

business_idea = response.choices[0].message.content
print(business_idea)

#Step 2:
messages = [{"role": "user", "content": f"Present a pain-point in the {business_idea} industry that AI could help address."}]

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

pain_point = response.choices[0].message.content
print(pain_point)

#Step 3:
messages = [{"role": "user", "content": f"How can Agentic AI be used to find a solution for {pain_point}?"}]

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

solution = response.choices[0].message.content
print(solution)

