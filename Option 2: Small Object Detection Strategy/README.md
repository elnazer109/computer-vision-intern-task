# Problem

The task focuses on detecting tiny metal **screws** (approximately **10×10 pixels**) from **high-resolution 4K images**.

The main challenge is that standard object detection models such as YOLO or SSD usually resize input images to smaller dimensions (e.g. 640×640).  
This resizing causes small objects to lose critical visual information or disappear completely.

As a result, traditional detection pipelines often fail to reliably detect very small objects.

---

# Proposed Solution: SAHI (Tiling / Image Slicing)

To address these challenges, a **tiling (slicing)** strategy is used.

Instead of feeding the entire 4K image into the detector at once, the image is divided into smaller **overlapping tiles**.

Each tile is processed independently using a standard object detection model, allowing small objects to remain visible at sufficient resolution.

---

## Pipeline Overview

High-Resolution Image (4K)
↓
Image Tiling / Slicing
↓
Object Detection on Each Tile
↓
Map Detections to Original Image
↓
Merge Results
↓
Non-Maximum Suppression
↓
Final Detections


---

# Handling Split Objects (Overlap)

A common issue in tiling-based detection is when an object lies on the border between two tiles and appears partially in each one.

To solve this problem, **overlapping tiles** are used (for example, 20% overlap).

This ensures that a screw cut in one tile will appear fully inside a neighboring tile.

After detection, overlapping predictions are merged using **Non-Maximum Suppression (NMS)** to remove duplicate detections.

---

# Trade-Off Analysis for Edge Devices (e.g. Raspberry Pi)

Running this pipeline on an edge device introduces additional constraints.

## Challenges
- Limited CPU and memory resources
- No dedicated GPU
- Increased inference time due to multiple tiles

## Possible Optimizations
- Use lightweight detection models.
- Increase tile size to reduce the number of slices
- Carefully reduce the overlap ratio


These trade-offs help balance detection accuracy and computational cost.

---

# Conclusion

The tiling-based detection strategy provides an effective solution for detecting very small objects in high-resolution images.

By preserving spatial details and combining overlapping predictions, the system significantly improves small object detection performance while remaining adaptable to resource-constrained edge devices.
