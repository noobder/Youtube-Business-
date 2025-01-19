def vm():
    import mixit
    import os
    import random
    import cv2

    source_folder = 'SEPV' 
    destination_folder = 'FULLV' 

    video_files = [f for f in os.listdir(source_folder) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]

    if not video_files:
        print("No video files found in the source folder!")
        return

    num_videos_to_select = min(20, len(video_files))
    selected_videos = random.sample(video_files, num_videos_to_select)

    captures = [cv2.VideoCapture(os.path.join(source_folder, video)) for video in selected_videos]

    if not captures or not all(capture.isOpened() for capture in captures):
        print("Failed to open one or more video files.")
        return

    frame_width = int(captures[0].get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(captures[0].get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(captures[0].get(cv2.CAP_PROP_FPS))

    output_path = os.path.join(destination_folder, 'Be_calm.mp4') 
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    writing_successful = True

    for capture in captures:
        while True:
            ret, frame = capture.read()
            if not ret:
                break
            out.write(frame)

    for capture in captures:
        capture.release()
    out.release()
    cv2.destroyAllWindows()

    if writing_successful:
        print("Video merging completed successfully. Proceeding to mix videos.")
        mixit.mix()
    else:
        print("Video merging failed. mixit.mix() will not be called.")
