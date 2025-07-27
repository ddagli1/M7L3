from speech import speech_en  # Ses tanıma fonksiyonu dış modülden import ediliyor
from random import choice     # Kelimeleri rastgele seçmek için 'choice' fonksiyonu kullanılıyor
import time                   # Zaman gecikmesi için 'time' modülü kullanılıyor

# Zorluk seviyelerine göre kelime listeleri
seviyeler = {
    "kolay": ["dairy", "mouse", "computer"],
    "orta": ["programming", "algorithm", "developer"],
    "zor": ["neural network", "machine learning", "artificial intelligence"]
}

# Oyun fonksiyonu: seçilen zorluk seviyesine göre oyunu başlatır
def play_game(level):
    words = seviyeler.get(level, [])  # Seçilen seviyeye göre kelime listesini al
    if not words:  # Geçersiz bir seviye girildiyse kullanıcıyı uyar
        print("Hatalı zorluk seviyesi.")
        return

    score = 0  # Doğru cevap sayısını tutan sayaç
    num_attempts = 3  # (Şu an kullanılmıyor ama her kelime için maksimum deneme hakkı olarak düşünülmüş)

    # Listedeki her kelime için döngü başlat
    for _ in range(len(words)):
        random_word = choice(words)  # Rastgele bir kelime seç
        print(f"Lütfen kelimeyi telaffuz edin: {random_word}")  # Kullanıcıdan kelimeyi söylemesi istenir
        
        recog_word = speech_en()  # Kullanıcının söylediği kelime tanınır (speech modülünden)
        print(recog_word)  # Tanınan kelime ekrana yazdırılır
        
        # Tanınan kelime doğruysa skor arttırılır, değilse uyarı verilir
        if random_word == recog_word:
            print("Doğru!")
            score += 1
        else:
            print(f"Bir yanlışlık var. Kelime: {random_word}")

        time.sleep(2)  # Yeni kelimeye geçmeden önce 2 saniye beklenir
        
    # Oyun tamamlandığında sonuç ekrana yazdırılır
    print(f"Oyun bitti! Skorunuz: {score}/{len(words)}")

# Kullanıcıdan zorluk seviyesini al
selected_level = input("Zorluk seviyesini seçin (kolay/orta/zor): ").lower()

# Oyunu başlat
play_game(selected_level)
