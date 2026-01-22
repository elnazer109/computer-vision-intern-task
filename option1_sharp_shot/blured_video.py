import numpy as np
import pandas as pd
import cv2
import os

# Create output folder for the selected top frames
os.makedirs("top_frames", exist_ok=True)

# Save frame indices and their sharpness scores to a CSV file
def create_csv(frames_dict, file_name):
    df = pd.DataFrame(list(frames_dict.items()), columns=["frame_index", "sharpness"])
    df.to_csv(file_name, index=False)

# Extract and save the selected frames as image files
def save_top_frames(video_path, top5):
    cap = cv2.VideoCapture(video_path)

    for idx in top5:
        # Jump directly to the frame index
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(idx))

        ret, frame = cap.read()
        if not ret:
            print(f"Frame {idx} could not be read.")
            continue

        # Save the original frame as JPG
        cv2.imwrite(f"top_frames/frame_{idx}.jpg", frame)

    cap.release()

# Select top frames with gap of ~1 second between them
def check_top_frames(sorted_frames, fps):
    selected = []

    for frame_idx in sorted_frames:
        is_far = True

        # Reject frames that are too close (within 1 second)
        for s in selected:
            if abs(frame_idx - s) < fps:
                is_far = False
                break

        if is_far:
            selected.append(frame_idx)

        if len(selected) == 5:
            break

    return selected

frames_dic = {}
video_path = "12310180_3840_2160_30fps.mp4"

# Open the video file
cap = cv2.VideoCapture(video_path)

# video metadata
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(round(cap.get(cv2.CAP_PROP_FPS)))

# Process each frame and compute its sharpness score
for i in range(num_frames):
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Laplacian highlights edges 
    lap = cv2.Laplacian(gray_frame, cv2.CV_64F)

    # Use Laplacian variance as a scalar sharpness score
    frames_dic[i] = lap.var()

cap.release()


create_csv(frames_dic, "blurred_frames.csv")

df = pd.read_csv("blurred_frames.csv")
# sort scores (highest sharpness first)
df_sorted = df.sort_values(by="sharpness", ascending=False)

top_frames = df_sorted["frame_index"].astype(int).tolist()

# Select the 5 sharpest frames with a 1-second gap between selections
top5 = check_top_frames(top_frames, fps)

# Save the selected frames to disk
save_top_frames(video_path, top5)
