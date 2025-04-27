import io
import os
import cv2
import cohere
from google.cloud import vision

# Set your Cohere API key
co = cohere.Client("oDKYFa3FOakn5QS0gTNtz6Nbjy9IxeA5TMLILPQt")

# Set your Google Cloud credentials file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".json"

# Initialize Google Vision API client
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

def analyze_with_vision_api(image_path):
    print("🔍 Analyzing with Vision API...")
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]
    print(f"✅ Vision Labels: {labels}")
    return labels

def ask_cohere_to_explain(labels):
    # Convert the list of labels to a string for the prompt
    prompt = f"Describe these visual elements for a visually impaired user: {', '.join(labels)}"
    print("🧠 Asking Cohere for smart explanation...")
    
    # Using the chat method, which expects a message history
    conversation_history = [{"role": "system", "content": "You are an assistant helping visually impaired users."}]
    conversation_history.append({"role": "user", "content": prompt})

    # Now using the chat method with the correct format
    response = co.chat(
        model="xlarge",  # Replace with the model you are using
        messages=conversation_history
    )

    return response['message']['content'].strip()  # Extract the explanation from the response

def main():
    image_path = "captured_image.jpg"
    capture_image(image_path)
    labels = analyze_with_vision_api(image_path)
    description = ask_cohere_to_explain(labels)
    print("\n📝 Description for user:")
    print(description)

if __name__ == "__main__":
    main()









         # === ADMIN ONLY(Vishal)===
         #Team TECH TITANS 0078 
# DO NOT EDIT BELOW COMMENTS OR CODE WITHOUT PERMISSION
# CHANGES MUST BE MADE BY ADMINISTRATOR ONLY