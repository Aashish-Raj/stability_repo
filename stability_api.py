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
        with open('final_res\\blur_upscale_res1.png', 'wb') as file:
            file.write(response.content)
        print("Image saved successfully.")
    else:
        print(f"Failed to upscale image. Status code: {response.status_code}")
        print("Error:", response.text)

# Call the function to upscale fast
# upscale_fast("blur_img.png")




# function to  conservative upscale
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
        with open('final_res\\blur_upscale_conservative_res1.png', 'wb') as file:
            file.write(response.content)
        print("Image saved successfully.")
    else:
        print(f"Failed to upscale image. Status code: {response.status_code}")
        print("Error:", response.text)

# Call the function to upscale fast
# upscale_conservative("blur_img.png")

# function to  cretive upscale
def upscale_creative(image):
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/upscale/creative",
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
        }

    )
    
    print("Generation ID:", response.json().get('id'))
    return response.json().get('id')

    # # Check if the request was successful
    # if response.status_code == 200:
        
    #     print("Generation ID:", response.json().get('id'))
    #     # Save the image data to a local file
    #     # with open('images\\blur_upscale_creative_res1.png', 'wb') as file:
    #     #     file.write(response.content)
    #     # print("Image saved successfully.")
    # else:
    #     print(f"Failed to upscale image. Status code: {response.status_code}")
    #     print("Error:", response.text)

# Call the function to upscale fast
# id=upscale_creative("blur_img.png")
# print('id--->>',id)
id="4cb93251d974ed0dc6d652d8a7a53d14cbef174ae4662a017d53d7b6101542da"

# fetcht the  image wwoth the   genertion id
def get_image_fromId(id):
    response = requests.request(
    "GET",
    f"https://api.stability.ai/v2beta/stable-image/upscale/creative/result/{id}",
    headers={
        'accept': "image/*",  # Use 'application/json' to receive base64 encoded JSON
        'authorization': f"Bearer {stability_api_key}"
    },
)

    if response.status_code == 202:
        print("Generation in-progress, try again in 10 seconds.")
    elif response.status_code == 200:
        print("Generation complete!")
        with open("final_res\\blur_upscale_creative_res1.png", 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(str(response.json()))
    
# call the  funtion to get the image
# get_image_fromId("fdca9f89a8458c37d15674c4235a4fbd87d78e2f8bb21ff84f659bbb5195f881")
get_image_fromId(id)