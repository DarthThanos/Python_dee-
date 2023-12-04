import openai
import requests
import json
from playsound import playsound

# Replace 'your_openai_api_key' with your actual OpenAI API key
openai.api_key = 'your_openai_api_key'

def ask_gpt4(question):
    """
    This function takes a question as input and sends it to GPT-4 to get a response.
    """
    try:
        response = openai.Completion.create(
            model="gpt4",  # Specify the GPT-4 model
            prompt=question,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in GPT-4 response: {e}")
        return None

def text_to_speech(text):
    """
    This function takes text and converts it to speech using OpenAI's TTS service.
    """
    try:
        # Specify the TTS model and voice details
        response = requests.post(
            "https://api.openai.com/v1/engines/tts-1-hd/speech",
            headers={
                "Authorization": f"Bearer {openai.api_key}"
            },
            json={
                "text": text,
                "voice": "female"  # Specify the female voice
            }
        )
        audio_response = response.content
        # Save the audio response to a file
        with open("response.mp3", "wb") as audio_file:
            audio_file.write(audio_response)
        # Play the audio file
        playsound("response.mp3")
    except Exception as e:
        print(f"Error in TTS request: {e}")

def main():
    """
    Main function to run the app.
    """
    question = input("Ask a question: ")
    response_text = ask_gpt4(question)
    if response_text:
        print(f"GPT-4 response: {response_text}")
        text_to_speech(response_text)
    else:
        print("No response from GPT-4.")

if __name__ == "__main__":
    main()
