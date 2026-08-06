# Weather App Skeleton

from openai import OpenAI
import streamlit as st


st.title("🌤️ Weather Forecast")


city = st.text_input("Enter your city name: ")

if st.button("Get weather Update"):
    if city == "":
        st.error("Enter your city name")
    else:
        # Connect to NVIDIA
        client = OpenAI(
        api_key=st.secrets["NVIDIA_API_KEY"],
        base_url="https://integrate.api.nvidia.com/v1"
        )

        # Ask the AI something

        prompt = f"""
        You are a weather assistant.

        For the city {city}, provide the weather in this format only:

        Temperature: 31°C
        Feels Like: 35°C
        Humidity: 78%
        Wind: 14 km/h
        Pressure: 1008 hPa
        Visibility: 8 km
        Weather: Cloudy

        Then give a short 2-line summary.
        """

        response = client.chat.completions.create(
        model="meta/llama-3.1-70b-instruct",
        messages=[
        {"role": "user", "content": prompt}
        ]
        )
        # Print the answer
        ai_reply= response.choices[0].message.content

        lines = ai_reply.split("\n")

        temperature = lines[0].split(":")[1].strip()
        humidity = lines[1].split(":")[1].strip()
        wind = lines[2].split(":")[1].strip()
        pressure = lines[3].split(":")[1].strip()
        visibility = lines[4].split(":")[1].strip()
        feels_like = lines[5].split(":")[1].strip()
        condition = lines[6].split(":")[1].strip()

        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)
        
        col1.metric("🌡 Temperature", temperature)
        col2.metric("🤒 Feels Like", feels_like)
        col3.metric("💧 Humidity", humidity)

        col4.metric("💨 Wind", wind)
        col5.metric("📍 Pressure", pressure)
        col6.metric("👀 Visibility", visibility)

        st.subheader("Summary")
        st.write(condition)
