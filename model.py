from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("C:/Users/shibi/runs/detect/yolov8n_custom2/weights/best.pt")
    result = model.predict(
    source="video.webm",
    conf=0.25,
    save=True,
    save_txt=False,
    vid_stride=5,  # process every 5th frame
)