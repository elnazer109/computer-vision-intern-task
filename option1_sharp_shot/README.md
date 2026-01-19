# Option 1 – Sharp Shot

This task focuses on analyzing a video and selecting the **top 5 sharpest frames** using classical Computer Vision techniques with OpenCV.

The goal is to automatically identify frames with the highest visual clarity while ensuring that the selected frames are not taken from the same moment in time.

---

## Method Overview

1. Read the video frame by frame using OpenCV.
2. Convert each frame to grayscale.
3. Compute the **Laplacian** of each frame.
4. Calculate the **variance of the Laplacian** as a sharpness score.
5. Store frame indices and sharpness scores in a CSV file.
6. Sort frames by sharpness score in descending order.
7. Select the top 5 frames while enforcing a temporal gap between them.
8. Save the selected frames as images.

---

## Sharpness Measurement

Sharpness is measured using **Laplacian Variance**.

The Laplacian operator highlights areas of rapid intensity change (edges).  
Sharp images contain stronger edges, resulting in higher variance values.

- High variance → sharp image  
- Low variance → blurred image  

This method is widely used in autofocus systems and image quality assessment.

---

## Avoiding Frames from the Same Second

To ensure temporal diversity, the solution enforces a **minimum one-second gap** between selected frames.

If the video has `FPS` frames per second, two frames are only accepted if: `|frame_index₁ − frame_index₂| ≥ FPS`


This prevents selecting multiple sharp frames from the exact same moment.

---

## Output

The final output consists of:

- A CSV file containing sharpness scores for all frames.
- A folder containing the **top 5 sharpest frames**.

Frames are saved in **JPG format** to reduce file size while preserving sufficient visual quality.

---

## How to Run

1. Make sure the video file path is correctly set inside the script.

```bash
python blurred_video.py
