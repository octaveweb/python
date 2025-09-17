import google.generativeai as genai

ask = str(input("Ask me any thing: "))

genai.configure(api_key="your-api-key")

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(f"{ask}")
print(response.text)

