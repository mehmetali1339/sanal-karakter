def cevap_uret(mesaj):
    return f"Mesajını aldım: {mesaj}"


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