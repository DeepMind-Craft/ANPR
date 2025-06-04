def load_image(image_path):
    from PIL import Image
    return Image.open(image_path)

def draw_bounding_boxes(image, boxes, labels):
    import cv2
    for box, label in zip(boxes, labels):
        x1, y1, x2, y2 = box
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    return image

def preprocess_image(image):
    # Add any preprocessing steps if needed
    return image