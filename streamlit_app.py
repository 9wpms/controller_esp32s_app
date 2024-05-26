import streamlit as st
import requests

# Update with the actual IP address of your ESP32-S
ESP32_IP = "http://172.20.10.3"

st.title("ESP32-S Controller")

def send_command(command):
    try:
        response = requests.get(f"{ESP32_IP}/{command}", timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed with status code {response.status_code}"
    except requests.Timeout:
        return "Error: Timeout while trying to connect to ESP32-S"
    except requests.RequestException as e:
        return f"Error: {e}"

if st.button('Start'):
    result = send_command('start')
    st.write(result)
    if "Started" in result:
        st.success("ESP32-S started successfully.")
    else:
        st.error(result)

if st.button('Stop'):
    result = send_command('stop')
    st.write(result)
    if "Stopped" in result:
        st.success("ESP32-S stopped successfully.")
    else:
        st.error(result)
