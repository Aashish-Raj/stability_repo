# Stability Image Upscaling Project

This project uses the Stability AI API to upscale images with fast, conservative, and creative options.

## Steps to Set Up and Run

1. **Create a Python Virtual Environment**  
   Create a virtual environment for the project:  
   `python -m venv env`

2. **Install Required Packages**  
   Activate the virtual environment and install the dependencies:  
   `pip install -r requirements.txt`

3. **Create a .env File**  
   Create a `.env` file in the project folder and add your Stability API key:  
   `STABILITY_API_KEY=<your_api_key>`

4. **Create the Output Folder**  
   Create a folder named `final_res` to store the output images:  
   `mkdir final_res`

5. **Place the Image for Upscaling**  
   Place the image you want to upscale in the same directory as the `stability_api.py` script.

6. **Run the Script**  
   Run the Python script to upscale your image:  
   `python stability_api.py`

7. **Check the Output**  
   The upscaled image will be saved in the `final_res` folder with the name:  
   - `blur_upscale_res1.png` (for fast upscaling)  
   - `blur_upscale_conservative_res1.png` (for conservative upscaling)  

## Notes
- The original image for upscaling should be placed in the same directory as `stability_api.py`.
- The script supports three upscaling modes: fast, conservative, and creative. Modify the script if needed to choose the desired method.
