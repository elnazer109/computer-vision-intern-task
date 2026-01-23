# Problem
the task is about detecting tiny metal **screws** (10x10) pixels from **high resolution image(4K)** and the problem is tandard detection models (YOLO/SSD) often
fail because they resize images to smaller dimensions(e.g. 640x640) which causes small objects to lose critical visual information or disappear completely.
traditional detection pipelines often fail to detect tiny objects reliably.

# Proposed solution (Tiling / SAHI)
To address these challenges, a **tiling (slicing)** strategy is used.

Instead of feeding the entire 4K image into the detector at once, the image is divided into smaller overlapping tiles.

Each tile is processed independently using a standard object detection model.

### Pipeline Overview
`
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
`

# Handling split objects (overlap)


Trade-Off Analysis for Edge Devices (e.g. Raspberry Pi)

Running this pipeline on an edge device introduces additional constraints.

### Challenges:

- Limited CPU and memory

- No dedicated GPU

- Increased inference time due to multiple tiles

### Possible Optimizations:

- Use lightweight models (YOLOv8-nano, MobileNet-SSD).

- Increase tile size to reduce the number of slices.

- Reduce overlap ratio carefully.


These trade-offs help balance detection accuracy and computational cost.

### Conclusion

The tiling-based detection strategy provides an effective solution for detecting very small objects in high-resolution images.

By preserving spatial details and combining overlapping predictions, the system significantly improves small object recall while remaining flexible enough to adapt to resource-constrained edge devices.
