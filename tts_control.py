from gtts import gTTS 
 

def createTTS(text: str):
    language = "de"
    
    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save("resources/tts.mp3") 
  
