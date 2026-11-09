def cevap_uret(mesaj):

    cevaplar = {
        "merhaba": "Merhaba, nasılsın?",
        "nasılsın": "İyiyim, teşekkür ederim!",
        "adın ne": "Ben Python ile yapılmış bir botum.",
        "ne yapıyorsun": "Seninle sohbet ediyorum.",
        "iyi geceler": "Sana da iyi geceler!"
    }

    mesaj = mesaj.lower().strip()

    return cevaplar.get(mesaj, "Bunu henüz anlamıyorum.")

def main():
    while True:
        mesaj = input("Sen: ")

        if mesaj == "/cikis":
            print("Bot: Görüşürüz!")
            break

        else:
            cevap = cevap_uret(mesaj)
            print("Bot:", cevap)

main()  