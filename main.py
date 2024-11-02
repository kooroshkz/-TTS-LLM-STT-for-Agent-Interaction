from openai_api import get_openai_response
from google_tts import google_text_to_speech
from google_speech_to_text import google_speech_to_text

def main():
    user_input = input("Ask a question: ")
    response = get_openai_response(user_input)
    print("AI Response:", response)
    google_text_to_speech(response)

if __name__ == "__main__":
    main()
