from googletrans import Translator

translator = Translator()

# แปลข้อความจากภาษาอังกฤษเป็นภาษาไทย
english_text = "Hello, how are you?"
translated_text = translator.translate(english_text, dest='th')
print(translated_text.text)

# แปลข้อความจากภาษาไทยเป็นภาษาอังกฤษ
thai_text = "สวัสดีครับ สบายดีไหมครับ?"
translated_text = translator.translate(thai_text, dest='en')
print(translated_text.text)
