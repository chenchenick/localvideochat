import cv2
import time
import os
import base64
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)

def capture_image(image_data):
    logging.debug(f"Received image data: {image_data[:100]}...")  # Log the first 100 characters of the image data

    # Decode the base64 image data
    img_data = base64.b64decode(image_data)
    nparr = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if frame is not None:
        timestamp = int(time.time())
        filename = f"captured_images/image_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        return True, filename
    else:
        logging.error("Failed to decode image data.")
        return False, None