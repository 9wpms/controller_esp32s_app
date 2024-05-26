import streamlit as st
import requests

ESP32_IP = "http://172.20.10.3"  # Use http if the ESP32 is not configured for https

st.title("ESP32 Controller")

def send_start_request():
    try:
        response = requests.get(f"{ESP32_IP}/start", timeout=10)
        if response.status_code == 200:
            st.success("Started successfully")
        else:
            st.error(f"Failed to start: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

def send_stop_request():
    try:
        response = requests.get(f"{ESP32_IP}/stop", timeout=10)
        if response.status_code == 200:
            st.success("Stopped successfully")
        else:
            st.error(f"Failed to stop: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

if st.button("Start"):
    send_start_request()

if st.button("Stop"):
    send_stop_request()
