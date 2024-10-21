import requests
from dotenv import load_dotenv
import os

load_dotenv()
stability_api_key = os.environ.get('STABILITY_API_KEY')

# Function to upscale fast
def upscale_fast(image):
    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/upscale/fast",
        headers={
            "authorization": f"Bearer {stability_api_key}",
            "accept": "image/*"
        },
        files={
            "image": open(image, "rb")
        },
         data = {
            "prompt": "make the  image  more  clear",
            "output_format": 'png',
            "creativity": 0.50,
        }

    )

    # Check if the request was successful
    if response.status_code == 200:
        # Save the image data to a local file
        with open('images\\blur_upscale_res1.png', 'wb') as file:
            file.write(response.content)
        print("Image saved successfully.")
    else:
        print(f"Failed to upscale image. Status code: {response.status_code}")
        print("Error:", response.text)

# Call the function to upscale fast
# upscale_fast("blur_upscale_test1.png")




# function to  cretive upscale
def upscale_conservative(image):
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/upscale/conservative",
        headers={
            "authorization": f"Bearer {stability_api_key}",
            "accept": "image/*"
        },
        files={
            "image": open(image, "rb"),
        },
         data = {
            "prompt": "make the  image  more  clear",
            "output_format": 'png',
            "creativity": 0.50,
        }

    )

    # Check if the request was successful
    if response.status_code == 200:
        # Save the image data to a local file
        with open('images\\blur_upscale_conservative_res1.png', 'wb') as file:
            file.write(response.content)
        print("Image saved successfully.")
    else:
        print(f"Failed to upscale image. Status code: {response.status_code}")
        print("Error:", response.text)

# Call the function to upscale fast
upscale_conservative("blur_upscale_test1.png")

# function fro  image to  image upscale
# def image_to_image_upscale(image_data):
#     response = requests.post(
#     # https://api.stability.ai/v2beta/stable-image/upscale/cretive",
#     # f"{API_HOST}/v1/generation/{UPSCALE_ENGINE_ID}/image-to-image/upscale",
#     f"https://api.stability.ai/v1/generation/v2beta/image-to-image/upscale",
#     headers={
#         "Accept": "image/png",
#         "Authorization": f"Bearer {stability_api_key}",
#     },
#     files={"image": ("upscale.png", image_data, "image/png")},
#     )
#     if response.status_code != 200:
#         raise Exception("Non-200 response: " + str(response.text))


# image_to_image_upscale(image_data)