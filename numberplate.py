from ultralytics import YOLO
import cv2
import easyocr

if __name__ == "__main__":
    model = YOLO("C:/Users/shibi/runs/detect/yolov8n_custom2/weights/best.pt")
    reader = easyocr.Reader(['en'])  # English OCR reader

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from video!")
            break

        # YOLO detection
        results = model(frame, conf=0.55)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                plate_img = frame[y1:y2, x1:x2]

                # OCR on cropped plate
                ocr_result = reader.readtext(plate_img)

                if ocr_result:
                    plate_number = ocr_result[0][1]  # Get detected text
                    print("Detected Plate:", plate_number)

                    # Draw box and text
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, plate_number, (x1, y1 - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("License Plate Reader", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
