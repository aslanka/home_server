import requests
from dotenv import load_dotenv
import google.generativeai as genai
import os


load_dotenv()


url = os.getenv('NTFY_SERVER')
API_KEY = os.getenv('LLM_KEY')



genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')


#example prompt 
prompt = "write me a intresting fact in computer science I can learn from as a full-stack developer"
response = model.generate_content(prompt, stream=False)


response = requests.post(url, data=response.text)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
