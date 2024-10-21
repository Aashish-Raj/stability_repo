import requests
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()
stability_api_key = os.environ.get('STABILITY_API_KEY')

# Function to send POST request to Stability AI upscale API
def send_upscale_request(url, image, prompt, creativity=0.35, output_format='png'):
    """Helper function to send an upscale request to Stability AI."""
    response = requests.post(
        url,
        headers={
            "authorization": f"Bearer {stability_api_key}",
            "accept": "image/*"
        },
        files={
            "image": open(image, "rb")
        },
        data={
            "prompt": prompt,
            "output_format": output_format,
            "creativity": creativity,
        }
    )
    return response

# Function to save image from response
def save_image(response, file_path):
    """Saves the image from the API response to the specified file path."""
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Image saved successfully at {file_path}")

# Function for fast upscaling
def upscale_fast(image, save_path='final_res/blur_upscale_fast_res1.png'):
    """Upscales the image quickly with minimal alterations."""
    url = "https://api.stability.ai/v2beta/stable-image/upscale/fast"
    response = send_upscale_request(url, image, prompt="make the image more clear")

    if response.status_code == 200:
        save_image(response, save_path)
    else:
        print(f"Failed to upscale image. Status code: {response.status_code}")
        print("Error:", response.text)

# Function for conservative upscaling
def upscale_conservative(image, save_path='final_res/blur_upscale_conservative_res1.png'):
    """Upscales the image conservatively, focusing on preserving details."""
    url = "https://api.stability.ai/v2beta/stable-image/upscale/conservative"
    response = send_upscale_request(url, image, prompt="make the image more clear")

    if response.status_code == 200:
        save_image(response, save_path)
    else:
        print(f"Failed to upscale image. Status code: {response.status_code}")
        print("Error:", response.text)

# Function for creative upscaling
def upscale_creative(image):
    """Initiates creative upscaling and returns the generation ID."""
    url = "https://api.stability.ai/v2beta/stable-image/upscale/creative"
    response = send_upscale_request(url, image, prompt="make the image more clear")

    if response.status_code == 200:
        generation_id = response.json().get('id')
        print(f"Generation ID: {generation_id}")
        return generation_id
    else:
        print(f"Failed to initiate creative upscaling. Status code: {response.status_code}")
        print("Error:", response.text)
        return None

# Function to retrieve image by generation ID
def get_image_from_id(generation_id, save_path='final_res/blur_upscale_creative_res1.png'):
    """Fetches the upscaled image from the creative process by generation ID."""
    url = f"https://api.stability.ai/v2beta/stable-image/upscale/creative/result/{generation_id}"
    response = requests.get(
        url,
        headers={
            'accept': "image/*",  # Use 'application/json' for base64 encoded response
            'authorization': f"Bearer {stability_api_key}"
        }
    )

    if response.status_code == 202:
        print("Generation in progress, try again later.")
    elif response.status_code == 200:
        save_image(response, save_path)
    else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")
        print("Error:", response.text)

# Example usage:
upscale_fast("blur_img.png")
upscale_conservative("blur_img.png")

# Get generation ID and retrieve creative upscale
generation_id = upscale_creative("blur_img.png")
if generation_id:
    time.sleep(60)
    get_image_from_id(generation_id)
