from google import genai
from google.genai import types
import pathlib
import os
from dotenv import load_dotenv

def main():
  load_dotenv()

  client = genai.Client(api_key=os.getenv('api_key'))

  # Retrieve and encode the PDF byte
  filepath = pathlib.Path(r'data\transcript.txt')

  with open("rules.txt", 'r', encoding='utf-8') as f:
    rules = f.read()
    
  prompt = rules

  print("Generating notes....")

  response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=[
        types.Part.from_bytes(
          data=filepath.read_bytes(),
          mime_type='text/plain',
        ),
        prompt])

  print("Generated")

  open("data/result.md", "w").close()

  print("Saving notes...")     

  with open("data/result.md", 'w', encoding='utf-8') as f:
      f.write(response.text)
      
  print("Saved")
  print("View result.txt to view results!")
    
if __name__ == "__main__":
  main()