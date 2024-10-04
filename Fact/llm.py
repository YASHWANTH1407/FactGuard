
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() 

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

llm = genai.GenerativeModel('gemini-pro')

def summarize(transcript):
    summarize_prompt = (
        """Your Name is FactGuard, your role is to fact check the given data which is a youtube transcript, with the data you have to
    return the main points which are stated true and also same for false information, if the stated  data isnt in your 
    database use the context given from various sources, also dont forget to return the source documents,
    with working links of the websites with citations

    TRANSCRIPT : {}
    
    """
    )
    
    prompt = summarize_prompt.format(transcript)

    response = llm.generate_content(prompt)

    summary = response.text.strip()

    return summary
