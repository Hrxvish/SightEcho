import cohere

co = cohere.Client("oDKYFa3FOakn5QS0gTNtz6Nbjy9IxeA5TMLILPQt")  # Replace with your real API key

def get_explanation_from_labels(labels):
    prompt = (
        f"Create a brief, clear 30-word description from these labels as if explaining an image to a blind person. "
        f"Only give useful details in plain language, like: 'A black car is 5 meters away on a busy road.' "
        f"Labels: {', '.join(labels)}"
    )

    print("🧠 Asking Cohere for smart explanation...")

    response = co.chat(
        model="command-r-plus",
        message=prompt
    )

    return response.text.strip()
















         # === ADMIN ONLY(Vishal)===
         #Team TECH TITANS 0078 
# DO NOT EDIT BELOW COMMENTS OR CODE WITHOUT PERMISSION
# CHANGES MUST BE MADE BY ADMINISTRATOR ONLY
