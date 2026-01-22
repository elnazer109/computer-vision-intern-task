import numpy as np
import pandas as pd 
import cv2
import os 

# create folder for top frames
os.makedirs("top_frames", exist_ok=True)

# create function to store frames and sharpness score 
def create_csv(frames_dict, file_name):
    df = pd.DataFrame(
        list(frames_dict.items()),
        columns=["frame_index", "sharpness"]
    )
    df.to_csv(file_name, index=False)

# create function to save top frames
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
    
# create function to check top frames
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

# read video using opencv
cap = cv2.VideoCapture(VideoPath)

# get total number of framres 
NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(round(cap.get(cv2.CAP_PROP_FPS)))

# loop through video to measure sharpness 
for i in range(NFrames):
    # read frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # trasform frame from RGB to Gray to measure sharpness 
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # measure sharpness using laplacian 
    lap = cv2.Laplacian(gray_frame, cv2.CV_64F)
    # store frame index and sharpness score 
    frames_dic[i] = lap.var()

cap.release()

# save frames and sharpness score 
create_csv(frames_dic , "blurred_frames.csv")


# choose and validate frames with highest sharpness 
df = pd.read_csv("blurred_frames.csv")

# sort frames by sharpness in descending order 
df_sorted = df.sort_values(
    by="sharpness",
    ascending=False
)
# get frame index with highest sharpness 
top_frames = df_sorted["frame_index"].astype(int).tolist()

# get top 5 frames 
top5 = check_top_frames(top_frames,fps)
# save top 5 frames 
save_top_frames(VideoPath, top5)
