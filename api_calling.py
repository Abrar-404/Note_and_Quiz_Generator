from google import genai
import os
from dotenv import load_dotenv
from gtts import gTTS
import io

# loading the environmental variables
load_dotenv()

api_key = os.getenv("GENAI_API_KEY")

# initializing a client
client = genai.Client(api_key=api_key)


# note generator
def note_generator(images):
      
  prompt= '"Generate a summary of the notes. Highlight the key points and important information to markdown from the notes. Use bullet points of the key points and important information to make it more readable. The summary should be concise and capture the main ideas presented in the notes."'
    
  response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images, prompt]
  )
  
  return response.text



# audio transcription
def audio_transcription(text):
  speech = gTTS(text, lang='en', slow=False)
  audio_buffer = io.BytesIO()
  speech.write_to_fp(audio_buffer)
  return audio_buffer


def quiz_generator(images, difficulty):
  prompt= f'Generate 3 quiz based on the {difficulty}. Make sure to add markdowns to differentiate the options. Also give the answer to the quiz and explain the answer in detail. The quiz should be based on the notes provided.'
    
  response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images, prompt]
  )
  
  return response.text