from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    os.chdir('streamlit/Capital-Bike-Share-Data-Streamlit-Web-Application')
    Popen(["streamlit", "run", "demoStreamlit.py", "--browser.serverAddress=0.0.0.0", "--browser.gatherUsageStats=False", "--server.enableCORS=False"])
