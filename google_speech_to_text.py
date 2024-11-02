from google.cloud import speech 
import io

def google_speech_to_text(audio_file_path):
    """
    Transcribe audio to text using Google Cloud Speech-to-Text API.
    """
    client = speech.SpeechClient()
    with io.open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))
