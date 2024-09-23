![alt text](ing_icon/logo.svg "IMAGENING")

# Setting Up ImagenING
1. Install [Python](https://www.python.org/)
2. Clone the repository
3. Install all packages (preferably in your own venv)
   - `pip install streamlit`
   - `pip install streamlit_lottie`
   - `pip install streamlit_carousel`
   - `pip install pillow`
   - `pip install --upgrade google-cloud-aiplatform`
4. Install the [gcloud CLI](https://cloud.google.com/sdk/docs/install)
5. Create your own access token in the shell
   - `gcloud auth application-default login`
6. Run the application
   - `python -m streamlit run Create_your_image.py`

The image counter is stored in [image_counter.txt](image_counter.txt) and can be adjusted there.