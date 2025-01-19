import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip

def mix():
    # Paths to input files and output directory
    video_path = "FULLV/be_calm.mp4"  # Ensure this path exists
    audio_folder = "AUDIO"     # Folder containing multiple .mp3 files
    output_path = "VIDEOS/be_calm.mp4"  # Output file path

    try:
        # Get a list of all .mp3 files in the folder
        audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.mp3')]

        if not audio_files:
            raise FileNotFoundError("No .mp3 files found in the specified folder.")

        # Randomly select an audio file
        random_audio = random.choice(audio_files)
        audio_path = os.path.join(audio_folder, random_audio)
        print(f"Selected audio: {random_audio}")

        # Load video and audio clips
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)

        # Set the audio of the video to the loaded audio
        video_with_audio = video_clip.set_audio(audio_clip)

        # Write the final output to a file
        video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")

        print("Video and audio mixed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
mix()
