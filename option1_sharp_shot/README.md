# Option 1 – Sharp Shot

This task focuses on analyzing a video and selecting the **top 5 sharpest frames** using classical Computer Vision techniques with OpenCV.

The goal is to automatically identify frames with the highest visual clarity while ensuring that the selected frames are not taken from the same moment in time.

---

## The solution follows these main steps:

1. Read the video frame by frame using OpenCV.
2. Convert each frame to grayscale.
3. Compute the **Laplacian** of each frame.
4. Calculate the **variance of the Laplacian** as a sharpness score.
5. Store frames with sharpness score in CSV file.
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



