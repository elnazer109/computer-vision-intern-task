# Decision Log – Sharp Shot Task

This section explains the main technical decisions made during the implementation of the sharp frame selection task.

---

## 1. Choosing Laplacian Variance for Sharpness Measurement

**Decision:**  
Use the variance of the Laplacian operator to estimate image sharpness.

**Reason:**  
The Laplacian highlights areas of rapid intensity change (edges).  
Sharp frames contain strong edges, which result in higher variance values, while blurred frames produce lower variance.

This method is:
- Simple and fast
- efficient
- used in blur detection systems

---

## 2. Converting Frames to Grayscale

**Decision:**  
Convert frames to grayscale before applying the Laplacian.

**Reason:**  
Sharpness is primarily related to intensity changes, not color information.  
Using grayscale reduces computational cost and removes unnecessary color noise.

---

## 3. Processing Video Frame-by-Frame

**Decision:**  
Read and analyze the video sequentially frame by frame.

**Reason:**  
to avoid loading the entire video into memory, making the solution memory-efficient and scalable for longer videos.

---

## 4. Storing Sharpness Scores in a CSV File

**Decision:**  
Store frame indices and sharpness scores in a CSV file.

**Reason:**  
CSV format allows:
- Easy inspection and debugging
- Simple sorting and filtering using pandas
- Reusability for further analysis without reprocessing the video

---

## 5. Selecting Top Frames Based on Sharpness Ranking

**Decision:**  
Sort all frames by sharpness score in descending order.

**Reason:**  
This ensures that the frames with the highest visual clarity are prioritized.

---

## 6. Enforcing a Temporal Gap Between Selected Frames

**Decision:**  
Ensure at least a one-second gap between selected frames using the video FPS value.

**Reason:**  
Without this constraint, multiple sharp frames could be selected from the same moment.  
Using FPS as a minimum gap guarantees temporal diversity between the selected frames.

---

## 7. Saving Selected Frames as JPG Images

**Decision:**  
Save the selected frames in JPG format.

**Reason:**  
JPG provides a good balance between image quality and file size, making it suitable for storage and review while keeping disk usage low.

---

## Conclusion

The design choices prioritize simplicity, efficiency, and reliability.  
The final pipeline achieves accurate sharp frame selection while remaining lightweight and easy to extend.
