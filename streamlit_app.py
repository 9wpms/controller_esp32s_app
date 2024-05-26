import streamlit as st
import requests

# Define the ESP32 IP address
ESP32_IP = "http://172.20.10.3"

# Create a title for the web app
st.title("ESP32 Controller")

# Define functions to send start and stop requests
def send_start_request():
    response = requests.get(f"{ESP32_IP}/start")
    if response.status_code == 200:
        st.success("Started successfully")
    else:
        st.error("Failed to start")

def send_stop_request():
    response = requests.get(f"{ESP32_IP}/stop")
    if response.status_code == 200:
        st.success("Stopped successfully")
    else:
        st.error("Failed to stop")

# Create buttons to send the requests
if st.button("Start"):
    send_start_request()

if st.button("Stop"):
    send_stop_request()
