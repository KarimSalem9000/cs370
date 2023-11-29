
from gtts import gTTS
import os

def text_to_speech_from_file(file_path, language='en', output_file='output.mp3'):

    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            text = file.read()
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_file)
        os.system(f"start {output_file}") 

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    text_file_path = 'transcription.txt'
    text_to_speech_from_file(text_file_path, language='en', output_file='output.mp3')
