Automated Video Creation, Editing, and YouTube Upload System
Description
This project automates the process of creating, merging, and uploading videos to YouTube. It integrates audio and video collected from uncopyrighted sources, combines them using video editing tools, and uploads them programmatically with metadata like titles, descriptions, and tags. The process ensures minimal manual effort and is ideal for content creators aiming for efficient and consistent video uploads.

Features
Video Merging:

Merges multiple video clips from a source folder (SEPV) into a single output video using OpenCV.
Ensures seamless transitions and a consistent resolution.
Audio Integration:

Randomly selects a background music file from a predefined folder (AUDIO) and merges it with the generated video.
Uncopyrighted Video Sourcing:

(To be added) A feature to fetch uncopyrighted videos directly from websites like Pixabay and integrate them into the workflow.
YouTube Upload Automation:

Automatically uploads the generated video to a YouTube channel.
Uses the YouTube Data API v3 to set video metadata such as title, description, tags, category, and audience settings.
Scheduled Execution:

Utilizes Task Scheduler (Windows) or Cron Jobs (Linux) to automate the entire workflow at specific intervals.
Post-Upload Cleanup:

Automatically archives uploaded videos and cleans temporary folders to maintain workspace organization.
Tech Stack
Programming Language: Python
Libraries:
MoviePy
OpenCV
Google API Client (for YouTube Data API v3)
Tools:
FFMPEG (for video/audio processing)
Task Scheduler or Cron Jobs for scheduling
File Structure
mixit.py:

Merges background music with the final video output.
Ensures high-quality audio integration using MoviePy.
videomerge.py:

Selects a set of video files from the SEPV folder and merges them into a single video stored in the FULLV folder.
Calls the mixit.py script after merging.
ytb.py:

Handles YouTube video uploads using the YouTube Data API.
Archives uploaded videos to the ARCHIVE folder and cleans up temporary directories after upload.
Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone <repository-url>
cd <repository-folder>
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up the YouTube Data API:

Enable the YouTube Data API v3 in your Google Cloud Console.
Download the client_secrets.json file and place it in the project directory.
Update the CLIENT_SECRETS_FILE variable in ytb.py with the path to your client secrets file.
Organize folders:

Create the following folders in the project directory:
SEPV: For input video files to merge.
FULLV: For merged video output.
AUDIO: For background music files.
VIDEOS: For final videos ready for upload.
ARCHIVE: For storing uploaded videos.
Run the scripts:

Video merging and audio integration:
bash
Copy
Edit
python videomerge.py
YouTube upload:
bash
Copy
Edit
python ytb.py
(Optional) Automate the process using Task Scheduler or Cron Jobs:

Schedule videomerge.py and ytb.py to run at desired intervals.
