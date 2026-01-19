import numpy as np
import pandas as pd 
import cv2
import os 

os.makedirs("top_frames", exist_ok=True)

def create_csv(frames_dict, file_name):
    df = pd.DataFrame(
        list(frames_dict.items()),
        columns=["frame_index", "sharpness"]
    )
    df.to_csv(file_name, index=False)

def save_top_frames(VideoPath , top5):
    cap = cv2.VideoCapture(VideoPath)

    for i in top5:
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            print(f"frame {i} does not exist")
            continue

        cv2.imwrite(f"top_frames/frame_{i}.jpg", frame)

    cap.release()
    

def check_top_frames(top_frames, fps):
    selected = []

    for frame_idx in top_frames:
        is_far = True

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
VideoPath ="12310180_3840_2160_30fps.mp4"


cap = cv2.VideoCapture(VideoPath)

NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(round(cap.get(cv2.CAP_PROP_FPS)))


for i in range(NFrames):
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(gray_frame, cv2.CV_64F)
    frames_dic[i] = lap.var()

cap.release()


create_csv(frames_dic , "blurred_frames.csv")


# choose and validate frames with highest sharpness 
df = pd.read_csv("blurred_frames.csv")

df_sorted = df.sort_values(
    by="sharpness",
    ascending=False
)

top_frames = df_sorted["frame_index"].astype(int).tolist()

# get top 5 frames 
top5 = check_top_frames(top_frames,fps)

save_top_frames(VideoPath, top5)
