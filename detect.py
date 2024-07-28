import argparse
from yolov5.detect import run as detect_run

def main(opt):
    detect_run(
        weights=opt.weights,
        source=opt.video,
        imgsz=640,
        project=opt.output,  # Output directory
        name='exp',  # Experiment name
        exist_ok=True  # Allow overwriting
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run YOLOv5 detection.")
    parser.add_argument('--weights', type=str, default='models/yolo_weights/yolov5s.pt', help='Path to the YOLOv5 weights file')
    parser.add_argument('--video', type=str, default='C:/Users/qures/OneDrive/Desktop/TruckDetectionProject/data/videos/sample_video1.mp4', help='Path to the input video file')
    parser.add_argument('--output', type=str, default='results/detections', help='Path to the output directory')

    opt = parser.parse_args()
    main(opt)
