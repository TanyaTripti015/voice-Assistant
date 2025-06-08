# Program to capture a single image from webcam in Python

import cv2  # Import OpenCV library

def click():
    cam_port = 0  # Default camera (change if multiple cameras are available)
    cam = cv2.VideoCapture(cam_port)

    if not cam.isOpened():
        print("Error: Could not access the camera.")
        return

    # Capture an image
    result, image = cam.read()

    if result:
        # Show captured image
        cv2.imshow("Assistant Friday", image)

        # Save the image to local storage
        cv2.imwrite("image.png", image)
        print("Image saved as image.png")

        # Wait for user input, then close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    else:
        print("No image detected. Please try again.")

    # Release the camera
    cam.release()

# Call the function
click()
