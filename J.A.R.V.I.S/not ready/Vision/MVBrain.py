import requests
import json
import base64
import cv2
import threading

def capture_image_and_save(image_path="captured_image.png"):
    droidcam_url = "http://192.168.43.1:4747/video"  # Replace with your DroidCam URL
    cap = cv2.VideoCapture(droidcam_url)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return False

    try:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(image_path, frame)
            print(f"Image captured and saved as {image_path}")
            return True
        else:
            print("Error: Could not capture image.")
            return False
    finally:
        cap.release()
        cv2.destroyAllWindows()

def encode_image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_string
    except FileNotFoundError:
        print("Error: Image file not found.")
        return None

def mobile_vision_brain(encoded_image):
    url = "https://api.deepinfra.com/v1/openai/chat/completions"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "x-deepinfra-source": "model-embed"
    }

    payload = {
        "model": "llava-hf/llava-1.5-7b-hf",
        "messages": [
            {
                "role": "user",
                "content": f"data:image/jpeg;base64,{encoded_image}"  # Pass the image directly
            }
        ]
    }

    print("Payload sent to API:")
    print(json.dumps(payload, indent=4))  # Debugging output

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        data = response.json()
        answer = data['choices'][0]['message']['content']
        return answer
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        print("Response:", response.text)
        return None


def print_animated_message(message):
    if message:
        for char in message:
            print(char, end='', flush=True)
    else:
        print("Error: Message is empty.")

if __name__ == "__main__":
    image_path = "captured_image.png"
    if capture_image_and_save(image_path):
        encoded_image = encode_image_to_base64(image_path)
        if encoded_image:
            message = mobile_vision_brain(encoded_image)

            thread = threading.Thread(target=print_animated_message, args=(message,))
            thread.start()
            thread.join()
