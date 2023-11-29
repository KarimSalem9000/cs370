
from gtts import gTTS
import os

def text_to_speech_from_file(file_path, language='en', output_file='output.mp3'):
    """
    Convert text from a file to speech and save it as an audio file.

    :param file_path: The path to the TXT file containing the text.
    :param language: The language of the text (default is English).
    :param output_file: The filename to save the speech audio (default is 'output.mp3').
    """
    try:
        # Read text from file
        with open(file_path, 'r', encoding='latin-1') as file:
            text = file.read()

        # Create gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the speech to an audio file
        tts.save(output_file)

        print(f"Speech saved to {output_file}")

        # Play the audio file (optional)
        os.system(f"start {output_file}")  # Works on Windows, modify for other operating systems

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage with a text file
    text_file_path = 'transcription.txt'
    text_to_speech_from_file(text_file_path, language='en', output_file='output.mp3')
