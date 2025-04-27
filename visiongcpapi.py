import io
import os
import cv2
from google.cloud import vision

# Set your Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "blinf.json"

client = vision.ImageAnnotatorClient()

def capture_image(filename="captured_image.jpg"):
    cap = cv2.VideoCapture(0)
    print("📸 Capturing image...")
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        print("✅ Image captured and saved.")
    else:
        print("❌ Failed to capture image.")
    cap.release()
    return filename

def get_labels_from_image(image_path):
    print("🔍 Analyzing with Vision API...")
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]
    print(f"✅ Vision Labels: {labels}")
    return labels










         # === ADMIN ONLY( Vishal ) ===
         #Team TECH TITANS 0078 
# DO NOT EDIT BELOW COMMENTS OR CODE WITHOUT PERMISSION
# CHANGES MUST BE MADE BY ADMINISTRATOR ONLY