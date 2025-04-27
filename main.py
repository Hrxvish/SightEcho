import time
import pyttsx3
from visiongcpapi import capture_image, get_labels_from_image
from cohere_response import get_explanation_from_labels

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1)
    
    # Set to male voice
    for voice in engine.getProperty('voices'):
        if 'male' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    
    engine.say(text)
    engine.runAndWait()

def main():
    try:
        while True:
            print("\n📸 Capturing image...")
            image_path = capture_image()
            
            print("🔍 Analyzing with Vision API...")
            labels = get_labels_from_image(image_path)

            print("🧠 Asking Cohere for smart explanation...")
            description = get_explanation_from_labels(labels)

            print("\n📝 Description for user:")
            print(description)

            print("\n🗣️ Speaking description out loud...")
            speak(description)

            print("\n⏳ Waiting before next capture...\n")
            time.sleep(1)  # wait 10 seconds before next cycle (change as needed)

    except KeyboardInterrupt:
        print("\n🛑 Stopped by user. Exiting...")

if __name__ == "__main__":
    main()








         # === ADMIN ONLY(Vishal)===
         #Team TECH TITANS 0078 
# DO NOT EDIT BELOW COMMENTS OR CODE WITHOUT PERMISSION
# CHANGES MUST BE MADE BY ADMINISTRATOR ONLY