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
prompt="Imagine yourself as  a world's best stock picker , financial analyst , basically you are global elite financer , who has complete knowledge on stock analysis wrt fundamental long term analysis and short term technical analaysis along with practical usage of both in picking such stocks who will play the game of long term , basically valuation analysis + business analysis , SIP , MF and other assets , asset management and all other things , teach me or give me a guide where I can learn how to do all these even if the market is bearish or crshed or sideways and how to spot a bull market stock even before it's growth stage or when it feels risky to invest in"
# message has role and content 
message={
    "role": role,
    "content": prompt
}
messages = [message]
response = client.chat.completions.create(model=model , messages=messages)
# print(response)
print(response.choices[0].message.content)