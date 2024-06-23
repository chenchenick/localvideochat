import cv2
import os

def capture_image_from_webcam(save_path):
    # Create a VideoCapture object to access the webcam (0 is usually the default webcam)
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Capture a single frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame.")
        cap.release()
        return

    # Save the captured frame to the specified path
    cv2.imwrite(save_path, frame)
    print(f"Image saved to {save_path}")

    # Release the VideoCapture object
    cap.release()

if __name__ == "__main__":
    # Define the path where the image will be saved
    save_folder = "captured_images"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    save_path = os.path.join(save_folder, "webcam_image.jpg")
    capture_image_from_webcam(save_path)