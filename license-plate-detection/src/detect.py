from ultralytics import YOLO
import cv2
import os
import glob

def load_image(image_path):
    image = cv2.imread(image_path)
    return image

def draw_bounding_boxes(image, results):
    for result in results:
        x1, y1, x2, y2, conf, cls = result
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(image, f'License Plate: {conf:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

def detect_license_plates(model, image_path):
    image = load_image(image_path)
    results = model.predict(image)
    draw_bounding_boxes(image, results)
    return image

if __name__ == "__main__":
    model_path = "../models/yolov8n_custom.pt"
    model = YOLO(model_path)

    image_folder = "../data/sample_images/*"
    for image_path in glob.glob(image_folder):
        output_image = detect_license_plates(model, image_path)
        output_path = os.path.join("../data/sample_images/output", os.path.basename(image_path))
        cv2.imwrite(output_path, output_image)

    print("Detection completed and results saved.")