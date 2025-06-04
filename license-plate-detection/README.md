# License Plate Detection Project

This project implements a license plate detection system using a YOLOv8 model. The trained model can detect license plates in images and output the results with bounding boxes.

## Project Structure

```
license-plate-detection
├── models
│   └── yolov8n_custom.pt        # Trained YOLO model for license plate detection
├── src
│   ├── detect.py                 # Script for loading the model and performing inference
│   └── utils.py                  # Utility functions for image processing
├── data
│   ├── sample_images             # Directory containing sample images for testing
│   └── data.yaml                 # Configuration file for the dataset
├── requirements.txt              # Python dependencies for the project
└── README.md                     # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd license-plate-detection
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your images in the `data/sample_images` directory.

2. Run the detection script:
   ```
   python src/detect.py --source data/sample_images
   ```

3. The results will be saved in the output directory specified in the `detect.py` script.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- This project uses the YOLOv8 model for object detection.
- Special thanks to the contributors and the community for their support.