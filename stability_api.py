import requests
from dotenv import load_dotenv
import os

load_dotenv()
stability_api_key = os.environ.get('STABILITY_API_KEY')

# Function to upscale creative
def upscale_creative(image):
    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/upscale/cretive",
        headers={
            "authorization": f"Bearer {stability_api_key}",
            "accept": "image/*"
        },
        files={
            "image": open(image, "rb")
        },
        data={
            "prompt": "cute fluffy white kitten floating in space, pastel colors",
            "output_format": "png",
        },
    )

    # Check if the request was successful
    if response.status_code == 200:
        # print("resposne.joson----->>>", response.json())
        # print('response.content---->>>',response.content)

        # Save the image data to a local file
        with open('images\\blur_upscale_res1.png', 'wb') as file:
            file.write(response.content)
        print("Image saved successfully.")
    else:
        print(f"Failed to upscale image. Status code: {response.status_code}")
        print("Error:", response.text)

# Call the function to upscale creative
upscale_creative("images\\blur_upscale_test1.png")
