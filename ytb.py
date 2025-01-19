def yt():
    import os
    import json
    import time
    import schedule 
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    import shutil
    import datetime

    CLIENT_SECRETS_FILE = "PASTE YOUR CLIENT SECRETS ID HERE"
    TOKEN_FILE = "token.json"
    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
    VIDEO_FOLDER = "VIDEOS"
    ARCHIVE_FOLDER = "ARCHIVE"

    def get_authenticated_service():
        credentials = None
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, 'r') as token:
                credentials = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
                credentials = flow.run_local_server(port=0)
            
            with open(TOKEN_FILE, 'w') as token:
                token.write(credentials.to_json())

        return build('youtube', 'v3', credentials=credentials)

    def upload_video(youtube, video_file, title, description, tags, category_id, privacy_status, audience):
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': category_id,
            },
            'status': {
                'privacyStatus': privacy_status,
            },
            'contentDetails': {
                'madeForKids': audience,  }
        }

        media = MediaFileUpload(video_file, chunksize=-1, resumable=True)

        request = youtube.videos().insert(
            part="snippet,status,contentDetails",
            body=body,
            media_body=media
        )
        
        response = None
        try:
            while response is None:
                status, response = request.next_chunk()
                if status:
                    print(f"Uploading... {int(status.progress() * 100)}% completed.")
                if 'id' in response:
                    print(f"Video uploaded successfully. Video ID: {response['id']}")
                    print("The video was successfully uploaded to YouTube with auto-generated thumbnails.")
                else:
                    print(f"An error occurred: {response}")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def delete_folder_contents(folder_paths):
        for folder_path in folder_paths:
            if os.path.exists(folder_path):
                for item in os.listdir(folder_path):
                    item_path = os.path.join(folder_path, item)
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                print(f'Contents deleted in folder: {folder_path}')
            else:
                print(f'Folder not found: {folder_path}')

    def process_video_upload():
        youtube = get_authenticated_service()

        video_files = [f for f in os.listdir(VIDEO_FOLDER) if os.path.isfile(os.path.join(VIDEO_FOLDER, f))]

        if not video_files:
            print("No videos to upload.")
            return

        video_file = video_files[0]
        video_file_path = os.path.join(VIDEO_FOLDER, video_file)

        title = f"{video_file}"
        description = "calm down....."
        tags = ["tag1", "tag2", "tag3"]
        category_id = "22"
        privacy_status = "public"
        audience = False  
        upload_video(youtube, video_file_path, title, description, tags, category_id, privacy_status, audience)

        archive_file_path = os.path.join(ARCHIVE_FOLDER, video_file)
        os.rename(video_file_path, archive_file_path)

    if __name__ == '__main__':
        os.makedirs(ARCHIVE_FOLDER, exist_ok=True)
        process_video_upload()
        folders_to_clean = ['FULLV', 'SEPV', 'ARCHIVE']
        delete_folder_contents(folders_to_clean)
        with open(r"C:\work\EHR\info.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - Code is completed and video is uploaded\n")
yt()
