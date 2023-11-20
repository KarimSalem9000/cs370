import cv2
import numpy as np
from filterpy.kalman import KalmanFilter

# Load detections
detections_path = 'path/to/your/detections'  # Replace with the path to your detections directory
detection_files = [f for f in os.listdir(detections_path) if f.endswith('.jpg')]

# Initialize Kalman filter
kf = KalmanFilter(dim_x=4, dim_z=2)
kf.F = np.array([[1, 0, 1, 0],
                 [0, 1, 0, 1],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])
kf.H = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0]])
kf.P *= 1e3
kf.R = np.diag([1, 1])

# Process each detection
for detection_file in detection_files:
    detection_frame = cv2.imread(os.path.join(detections_path, detection_file))

    # Extract the bounding box from the detection frame
    bounding_box = get_bounding_box(detection_frame)  # Implement a function to extract the bounding box

    # Initialize Kalman filter with the bounding box coordinates
    kf.x = np.array([bounding_box[0], bounding_box[1], 0, 0])

    # Process the video
    video_path = 'path/to/your/videos/your_video.mp4'  # Replace with the path to your video
    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Predict the next state with the Kalman filter
        kf.predict()

        # Draw the predicted bounding box
        predicted_box = [int(x) for x in kf.x[:2]]
        cv2.rectangle(frame, (predicted_box[0], predicted_box[1]), (predicted_box[0] + bounding_box[2], predicted_box[1] + bounding_box[3]), (0, 255, 0), 2)

        # Draw the trajectory
        cv2.circle(frame, (predicted_box[0], predicted_box[1]), 2, (0, 0, 255), -1)

        # Display the frame
        cv2.imshow('Tracking', frame)
        out.write(frame)

        if cv2.waitKey(25) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
