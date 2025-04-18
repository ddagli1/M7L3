import speech_recognition as sr
import random
import time

def speech():
    recog=sr.Recognizer()
    mic=sr.Microphone()


    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        print("sAy something:")
        audio=recog.listen(audio_file)



    try:
        return recog.recognize_google(audio, language="en-US")
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError :
        return "Sorry, there was an error with the speech recognition service."
    

def play_game():
    levels = {
        "kolay": ["diary", "computer"],
        "orta": ["programming", "algorithm", "developer"],
        "zor": ["neural network", "machine learning", "artificial intelligence"]
    }

    print("zorluk seviyesini sec: kolay, orta, zor")    
    level=input("seviye: ").lower()

    if level not in levels:
        print("gecersiz seviye. lütfen tekrar deneyin.")
        return
    
    word= random.choice(levels[level])
    print(f"kelimeyi tahmin et:{word} ")
    time.sleep(2)

    spoken_word = speech()
    print(f"tahmin ettigin kelime: {spoken_word}")

    if spoken_word.lower() == word:
        print("tebrikler! dogru tahmin ettiniz.")
    else:
        print(f"yanlis tahmin. dogru kelime: {word}")


if __name__ == "__main__":
    play_game()