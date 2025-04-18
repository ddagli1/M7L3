import speech_recognition as speech_recog

def speech_tr():
    mic= speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file: 
        recog.adjust_for_ambient_noise(audio_file)
        audio= recog.listen(audio_file)
        return recog.recognize_google(audio, language="tr-TR")


mic= speech_recog.Microphone()
recog = speech_recog.Recognizer()

with mic as audio_file: 
        print("Bir şeyler konuşun...")
        recog.adjust_for_ambient_noise(audio_file)
        audio= recog.listen(audio_file)
        print("Sesler yazıya dökülüyor...")
        print(recog.recognize_google(audio, language="tr-TR")+ " dediniz")
