import google.generativeai as genai
import os
from dotenv import load_dotenv
from transcript import extract_transcript

load_dotenv()

# Configure Generative AI API
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
llm = genai.GenerativeModel('gemini-pro')


youtube_url = input()
transcript = extract_transcript(youtube_url)

prompt = (f"You are given with a Youtube video transcript, your work is to generate all the points from the youtube transcript"
          f"\n\n{transcript}")

newprompt = prompt.format(transcript)
response = llm.generate_content(newprompt)
summary = response.text.strip()
print(summary)