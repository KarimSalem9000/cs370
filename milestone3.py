

import subprocess
import whisper
import openai

# Function to transcribe audio to text using OpenAI Whisper API
def transcribe_audio_to_text(x):
    model = whisper.load_model('base')
    result = model.transcribe(x)

    return result['text']

# Main function
def main():
    # Define the path for the audio file and output text file
    video_path = 'kamala.mp4'  # Replace with the path to your video file
    audio_path = 'audio.mp3'
    text_output_path = 'transcription.txt'

    # Extract audio from the video
    cmd = ['ffmpeg', '-i', video_path, '-vn', '-ar', '44100', '-ac', '1', '-b:a', '32k', '-f', 'mp3', audio_path]
    subprocess.call(cmd)

    # Transcribe the extracted audio to text
    transcription = transcribe_audio_to_text(audio_path)

    # Save the transcription to a text file
    with open(text_output_path, 'w') as text_file:
        text_file.write(transcription)

    print(f"Transcription saved to {text_output_path}")

if __name__ == "__main__":
    main()
