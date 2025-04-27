import io
import os
import cv2
from google.cloud import vision
from vertexai.preview.language_models import ChatModel
from vertexai import init

# Set your Google Cloud credentials file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".json"

# Initialize Vertex AI and Gemini
init(project="blinf", location="us-central1")
chat_model = ChatModel.from_pretrained("gemini-1.5-pro")

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

def analyze_with_vision_api(image_path):
    print("🔍 Analyzing with Vision API...")
    client = vision.ImageAnnotatorClient()
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]
    print(f"✅ Vision Labels: {labels}")
    return labels

def ask_gemini_to_explain(labels):
    prompt = f"Describe these visual elements for a visually impaired user: {', '.join(labels)}"
    print("🧠 Asking Gemini for smart explanation...")
    chat = chat_model.start_chat()
    response = chat.send_message(prompt)
    return response.text

def main():
    image_path = "captured_image.jpg"
    capture_image(image_path)
    labels = analyze_with_vision_api(image_path)
    description = ask_gemini_to_explain(labels)
    print("\n📝 Description for user:")
    print(description)

if __name__ == "__main__":
    main()












         # === ADMIN ONLY(Vishal)===
         #Team TECH TITANS 0078 
# DO NOT EDIT BELOW COMMENTS OR CODE WITHOUT PERMISSION
# CHANGES MUST BE MADE BY ADMINISTRATOR ONLY
