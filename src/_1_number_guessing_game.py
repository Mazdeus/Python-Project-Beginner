"""
Project : Number Guessing Game
Merupakan game sederhana yang meminta pemain untuk menebak angka yang dipilih secara acak oleh komputer.
Pemain diberikan kesempatan untuk menebak angka yang dipilih oleh komputer dengan batasan jumlah tebakan.
Jika pemain berhasil menebak angka yang dipilih oleh komputer, maka pemain dinyatakan menang.
Sebaliknya, jika pemain tidak berhasil menebak angka yang dipilih oleh komputer, maka pemain dinyatakan kalah.

Rumus menentukan Jumlah Tebakan Minimum:
Jumlah tebakan minimum = log 2 (Batas atas – batas bawah + 1)
"""

import random

print("Welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number between 1 to 100. Let's start the game.")

# Generate random number between 1 to 100
number_to_guess = random.randint(1, 100) # Fungsi randint ini menghasilkan sebuah bilangan bulat acak antara dua angka yang ditentukan, termasuk kedua batas tersebut.

# Jumlah tebakan minimum
chances = 7

# Counter untuk menghitung jumlah tebakan
guess_counter = 0

# Looping untuk memberikan kesempatan menebak sebanyak jumlah tebakan
while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Enter your guess: "))

    # Menampilkan tebakan yang dilakukan oleh pemain
    if my_guess == number_to_guess:
        print(f'The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt')
        break
    # Menampilkan pesan jika pemain gagal menebak angka yang dipilih oleh komputer serta sudah kehabisan kesempatan
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'You have exhausted all your chances. The number was {number_to_guess}')
    # Menampilkan petunjuk jika tebakan pemain terlalu tinggi atau terlalu rend
    elif my_guess > number_to_guess:
        print("Your guess is too high")
    # Menampilkan petunjuk jika tebakan pemain terlalu rendah
    else:
        print("Your guess is too low")
