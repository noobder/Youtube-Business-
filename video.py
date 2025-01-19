import requests
import os
import random
import datetime
import videomerge
with open(r"C:\work\EHR\info.txt", "a") as f:
    f.write(f"{datetime.datetime.now()} - code is running\n")

API_KEY = "PASTE YOUR API ID FROM PIXBAY.COM"

def search_videos(topic, num_videos=40):
    url = f"https://pixabay.com/api/videos/?key={API_KEY}&q={topic}&per_page={num_videos}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        video_urls = [] 
        for video in data['hits']:
            video_urls.append(video['videos']['large']['url'])
        return video_urls
    else:
        print("Failed to fetch videos. Status code:", response.status_code)
        return []

def download_video(video_url, topic, index):
    output_directory = "SEPV"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    file_path = os.path.join(output_directory, f"{topic}_{index}.mp4")
    print(f"Downloading video to: {file_path}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(video_url, headers=headers)
    
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print("\nDownload completed.")
        return True  
    else:
        print(f"Failed to download video. Status code: {response.status_code}")
        return False  

if __name__ == "__main__":
    topics = [
        "meditation", "peace", "calm", "Tranquility", "scenery",
        "Relaxation", "Stillness", "Harmony", "Zen", "Mindfulness",
        "Quietude", "Composure", "Restfulness"
    ]  
    topic = random.choice(topics)
    print(f"Selected topic: {topic}")
    
    video_urls = search_videos(topic, num_videos=100)  
    
    if len(video_urls) >= 15:
        
        selected_videos = random.sample(video_urls, 15)

        successful_downloads = 0  
        for index, video_url in enumerate(selected_videos):
            if download_video(video_url, topic, index + 1):
                successful_downloads += 1

        print(f"Successfully downloaded {successful_downloads} videos.")
    else:
        print("Not enough videos found to download 15.")
 

    if successful_downloads == 15:
        print("All videos downloaded successfully. Proceeding to merge videos.")
        videomerge.vm()
    else:
        print(f"Only {successful_downloads} out of {len(video_urls)} videos were downloaded. Merging skipped.")
