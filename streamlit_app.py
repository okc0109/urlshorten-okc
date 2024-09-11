import streamlit as st
import pyshorteners

# Streamlit 앱 제목
st.title("URL Shortener App")

# URL 입력
url = st.text_input("Enter the URL you want to shorten:")

# 버튼 클릭 시 동작
if st.button("Shorten URL"):
    if url:
        # pyshorteners를 이용해 URL 단축
        shortener = pyshorteners.Shortener()
        try:
            short_url = shortener.tinyurl.short(url)
            st.success(f"Shortened URL: {short_url}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a valid URL.")

# 설명 추가
st.write("This app uses the TinyURL service to shorten your URLs.")
