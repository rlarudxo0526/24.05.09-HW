from gtts import gTTS

tts = gTTS("안녕하세요. 저는 김경태입니다.", lang = 'ko')
tts.save("mysounds.mp3")
