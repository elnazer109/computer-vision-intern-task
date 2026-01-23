# Problem

The task focuses on detecting tiny metal **screws** (approximately **10×10 pixels**) from **high-resolution 4K images**.

The main challenge is that standard object detection models such as YOLO or SSD usually resize input images to smaller dimensions.
This resizing causes small objects to lose critical visual information or disappear completely.

As a result, traditional detection pipelines often fail to reliably detect very small objects.

---

# Proposed Solution: SAHI (Tiling / Image Slicing)

To soultion of these challenges is a **tiling (slicing)** strategy.

Instead of feeding the entire 4K image into the detector at once, the image is divided into smaller **overlapping tiles**. Each tile is processed independently using a standard object detection model, allowing small objects to remain visible at sufficient resolution.

---

## Pipeline Overview

- High-Resolution Image (4K)
- Image Tiling / Slicing
- Object Detection on Each Tile
- Map Detections to Original Image
- Merge Results
- Non-Maximum Suppression
- Final Detections


---

# Handling Overlap:

A common issue in tiling-based detection is when an object lies on the border between two tiles and appears partially in each one. To solve this problem, **overlapping tiles** are used.
This ensures that a screw cut in one tile will **appear fully inside a neighboring tile**.

After detection, overlapping predictions are merged using **Non-Maximum Suppression (NMS)** to remove duplicate detections.

---

# Trade-Off Analysis for Edge Devices.

Running this pipeline on an edge device introduces additional constraints.

## Challenges
- Limited CPU and memory resources
- No dedicated GPU
- Increased inference time due to multiple tiles

## Possible Optimizations
- Use lightweight detection models or quantizing one.
- Increase tile size to reduce the number of slices
- reduce the overlap ratio


These trade-offs help balance detection accuracy and computational cost.

---

# Conclusion

The tiling-based detection strategy provides an effective solution for detecting very small objects in high-resolution images.

By preserving spatial details and combining overlapping predictions, the system significantly improves small object detection performance while remaining adaptable to resource-constrained edge devices.
