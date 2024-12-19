"""
Program ini merupakan game sederhana yang meminta pemain untuk menebak kata yang dipilih secara acak oleh komputer.
Pemain diberikan kesempatan untuk menebak kata yang dipilih oleh komputer dengan batasan jumlah tebakan.
Jika pemain berhasil menebak kata yang dipilih oleh komputer, maka pemain dinyatakan menang.
Sebaliknya, jika pemain tidak berhasil menebak kata yang dipilih oleh komputer, maka pemain dinyatakan kalah.
Program ini memberikan ummpan balik setiap tebakan, membantu pengguna untuk menyelesaikan kata atau kalah dalam permainan berdasarkan tebakan mereka.

"""

import random

# Pembuka
name = input("What is your name? ")
print("Hello, " + name + ". You have 12 chances to guess the word. Let's start the game.")

# List kata yang akan ditebak
words = ['book', 'bottle', 'watch', 'laptop', 'phone', 'table', 'chair', 'pen', 'pencil', 'eraser', 'marker', 'paper', 'notebook', 'monitor', 'keyboard', 'mouse', 'speaker', 'headphone', 'camera', 'charger']
words = random.choice(words)

print("Guess the characters")
guesses = ''
turns = 12 # Jumlah tebakan minimum

# Looping yang berjalan selama pengguna masih memiliki sisa giliran
while turns > 0:
    # Memeriksa setiap karakter dalam kata
    failed = 0 # Jumlah tebakan yang salah
    for char in words:
        # Jika character telah ditebak (character ada di dalam tebakan) character ditampilkan
        if char in guesses:
            print(char)
        # Jika character belum ditebak, tampilkan garis bawah
        else:
            print("_")
            failed += 1
    
    # Periksa jika pengguna telah menang
    if failed == 0:
        print("You Win")
        print("The word is: ", words)
        break
    # Meminta tebakan berikutnya
    # Pengguna diminta menebak character. Character yang ditebak akan disimpan dalam variabel guesses
    guess = input("Guess a character:")
    guesses += guess

    # Menanganai tebakan yang salah
    # Jika tebakan tidak ada dalam kata, kurangi jumlah giliran. 
    # Pesan salah akan ditampilkan bersama jumlah tebakan tersisa
    if guesses not in words:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
            print("The word is: ", words)
            break