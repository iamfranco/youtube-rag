## YouTube Retrieval-Augmented Generation Streamlit App

A Streamlit app that takes a YouTube video URL (eg https://youtu.be/nnTsMXUmzWI), downloads the video transcript, and use the transcript as knowledge base for Retrieval-Augmented Generation.

![app demo gif](app-demo.gif)

### To access on streamlit cloud

https://iamfranco-youtube-rag.streamlit.app/

Note: the YouTube video transcript downloading functionality is flaky on streamlit cloud (because YouTube sometimes IP bans the streamlit cloud from accessing video transcript).

If it isn't working, then try run this locally. 

### To run locally

Create a virtual environment `.venv`
```
python -m venv .venv
```

Activate virtual environment `.venv`
```
.venv\Scripts\activate
```

Install requirements from `requirements.txt`
```
pip install -r requirements.txt
```

Start Streamlit App
```
streamlit run app.py
```