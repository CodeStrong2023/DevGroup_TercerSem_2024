import google.generativeai as genai


genai.configure(api_key="AIzaSyAyC618r9y8RgDHKFzlpx0lVJ45kSY-E4c")
model = genai.GenerativeModel('gemini-pro')
