from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")  # lightweight model

    result = model.train(
        data="data.yaml",
        epochs=3,
        imgsz=416,             
        batch=8,
        device="cuda",
        workers=2,             

        name="yolov8n_custom",
        save=True,

        optimizer="SGD", #SGD = Stochastic Gradient Descent
        lr0=0.005,             
        momentum=0.9,
        weight_decay=0.0005,
        warmup_epochs=2,

        label_smoothing=0.0,
        nbs=32                 
    )

    print("Training completed.")
