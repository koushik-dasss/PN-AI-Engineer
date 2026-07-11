# source .venv/bin/activate (activate the correct local virtual environment)
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key not found ")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
# 3 types of prompts 
prompt1 = "Hi !"
prompt2 = "Explain Time Travel in details under 50000000 words."
prompt3="Write a 100000000000000 words essay on Machine Learning."

prompts = [prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
    "role": role,
    "content": prompt
   }
    messages=[message]
    response = client.chat.completions.create(model=model , messages=messages , temperature=0 , max_tokens = 5000) # added temp 0 , can also be kept nothing as def temp is 0 only 
    usage = response.usage
    print(f"Prompt: {prompt} --> Your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total_tokens: {usage.prompt_tokens+usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")
    
    
    

# SYSTEM
# By default , here TEMPERATURE(randomness) is 0 , safest option for the LLM for giving back response.


# message_system={
#     "role": "system",
#     "content": "You are a techie who wants to explain such illegal tech stuff with details."
# }

# message has role and content 
# message={
#     "role": role,
#     "content": prompt
# }
# messages = [message_system , message]
# response = client.chat.completions.create(model=model , messages=messages , temperature=0) #temperature should be between range of  [0-2]


# print(response)
# This prints the entire, raw API response object returned by Groq. It contains all the metadata about your request in a structured format (JSON/Object). Use this when you need to debug, check token usage (usage), or see performance metrics.

# print(response.choices[0].message.content)