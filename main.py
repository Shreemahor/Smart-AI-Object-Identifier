import cv2
import numpy as np
from picamera2 import Picamera2
import time

from lcd_simple_test import lcd

try:
    from tensorflow.lite.python.interpreter import Interpreter
except ImportError:
    print("TensorFlow not found")
    exit(1)


class ObjectDetector:
    def __init__(self, model_path='detect.tflite', labels_path='labelmap.txt'):
        """
        Initialize the object detector
        """
        self.model_path = model_path
        self.labels_path = labels_path
        
        # Load labels
        self.labels = self.load_labels()
        
        # Initialize TFLite interpreter
        self.interpreter = Interpreter(model_path=self.model_path)
        self.interpreter.allocate_tensors()
        
        # Get input and output details
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        
        # Get input shape
        self.input_shape = self.input_details[0]['shape']
        self.height = self.input_shape[1]
        self.width = self.input_shape[2]
        
        print(f"Model loaded. Input shape: {self.input_shape}")
        
    def load_labels(self):
        """Load labels from file"""
        try:
            with open(self.labels_path, 'r') as f:
                labels = [line.strip() for line in f.readlines()]
            # Remove first label if it's '???'
            if labels[0] == '???':
                labels.pop(0)
            return labels
        except FileNotFoundError:
            print(f"Labels file not found: {self.labels_path}")
            print("Using default COCO labels...")
            # Return some common COCO labels
            return ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 
                   'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 
                   'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog']
    
    def detect_objects(self, frame, threshold=0.5):
        """
        Detect objects in a frame
        Returns:
            List of detections with (label, confidence, bbox)
        """
        # Preprocess image
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(img, (self.width, self.height))
        input_data = np.expand_dims(img_resized, axis=0)
        
        # Normalize if needed (depends on model)
        if self.input_details[0]['dtype'] == np.float32:
            input_data = (np.float32(input_data) - 127.5) / 127.5
        
        # Run inference
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        
        # Get results
        boxes = self.interpreter.get_tensor(self.output_details[0]['index'])[0]
        classes = self.interpreter.get_tensor(self.output_details[1]['index'])[0]
        scores = self.interpreter.get_tensor(self.output_details[2]['index'])[0]
        
        detections = []
        for i in range(len(scores)):
            if scores[i] > threshold:
                class_id = int(classes[i])
                label = self.labels[class_id] if class_id < len(self.labels) else f"Class {class_id}"
                confidence = scores[i]
                bbox = boxes[i]
                detections.append((label, confidence, bbox))
        
        return detections


def main():
    """Main function to run object detection"""
    
    print("Initializing camera...")
    
    # Initialize Picamera2 for Arducam
    picam2 = Picamera2()
    
    # Configure camera
    config = picam2.create_preview_configuration(
        main={"size": (640, 480), "format": "RGB888"}
    )
    picam2.configure(config)
    picam2.start()
    
    print("Camera started. Waiting for it to warm up...")
    time.sleep(2)
    
    # Initialize object detector
    print("Loading object detection model...")
    try:
        detector = ObjectDetector()
    except FileNotFoundError:
        print("\nERROR: Model files not found!")
        print("Please download the TensorFlow Lite model that is used for the recognition:")
        print("1. Download it from: https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip")
        print("2. Extract and place 'detect.tflite' and 'labelmap.txt' in this directory")
        picam2.stop()
        return
    
    print("\nStarting object detection...")
    print("Press Ctrl+C to exit\n")
    
    try:
        frame_count = 0
        while True:
            # Capture frame
            frame = picam2.capture_array()
            
            # Flip frame vertically
            frame = cv2.flip(frame, 0)
            
            # Convert RGB to BGR for OpenCV
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Detect objects
            detections = detector.detect_objects(frame_bgr, threshold=0.5)
            
            # Print detections
            if detections and frame_count % 10 == 0:  # Print every 10 frames
                print(f"\n--- Frame {frame_count} ---")
                for label, confidence, bbox in detections:
                    print(f"  {label}: {confidence*100:.1f}%")
                    lcd.clear()
                    lcd.write_string(label)
            
            # Draw boxes on frame
            h, w = frame_bgr.shape[:2]
            for label, confidence, bbox in detections:
                ymin, xmin, ymax, xmax = bbox
                xmin = int(xmin * w)
                xmax = int(xmax * w)
                ymin = int(ymin * h)
                ymax = int(ymax * h)
                
                # Draw rectangle
                cv2.rectangle(frame_bgr, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                
                # Draw label
                label_text = f"{label}: {confidence*100:.0f}%"
                cv2.putText(frame_bgr, label_text, (xmin, ymin - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Display frame (optional - comment out if running headless)
            try:
                cv2.imshow('Object Detection', frame_bgr)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except:
                # If display fails , just continue
                pass
            
            frame_count += 1
            time.sleep(0.1)  # Small delay to reduce CPU usage
            
    except KeyboardInterrupt:
        print("\n\nStopping...")
    finally:
        picam2.stop()
        cv2.destroyAllWindows()
        print("bye!")


if __name__ == "__main__":
    main()
