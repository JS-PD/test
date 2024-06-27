# youtube_pipline.ipynb
from vertexai.generative_models import GenerativeModel, Part
import vertexai
import os
from dotenv import load_dotenv

from google.cloud import storage
from pytube import YouTube

import streamlit as st

# API 키 정보 로드
load_dotenv()

video_url = st.text_input("Youtube URL을 입력하세요", 'https://youtu.be/WENUvclwo18?si=CngwTn2onM7PzZcP')

if video_url:
    st.video(video_url)

