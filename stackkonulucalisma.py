import random


# Sesli ve sessiz harfleri tanımla
vowels = "aeiouıöü"
consonants = "bcdfghjklmnpqrstvwxyz"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.top = None  # Stack'in en üstündeki eleman
        self.length = 0  # Stack'in eleman sayısı

    # Ekleme yapılan kısım
    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top.prev = new_node
            self.top = new_node

        self.length += 1  # Stack'in eleman sayısını artır

    # Çıkarma yapılan kısım
    def pop(self):
        if self.top is None:
            self.length -= 1
            return None
        else:
            popped_data = self.top.data
            self.top = self.top.next
            if self.top is not None:
                self.top.prev = None

            self.length -= 1  # Stack'in eleman sayısını azalt
            return popped_data


# Rastgele harf dizisini oluşturan fonksiyon

def generate_random_letters():
    random_vowels = random.sample(vowels, 5)  # sessiz harflerden 5 tane seç
    random_consonants = random.sample(
        consonants, 5)  # sesli harflerden 5 tane seç
    random_letters = random_vowels + random_consonants  # diziyi birleştir
    random.shuffle(random_letters)  # diziyi karıştır
    return random_letters


# Stack oluştur
stack = Stack()
# Rastgele harf dizisini al
letters = generate_random_letters()

# Her harf için işlem yap
for letter in letters:
    if stack.length != 0:  # Stack boş değilse
        # Eğer önceki harf sessizse, şuanki harf sesli olmalı
        if stack.top.data not in vowels and letter in vowels:
            stack.pop()

        # Eğer önceki harf sesliyse, şuanki harf sessiz olmalı
        elif stack.top.data in vowels and letter not in vowels:
            stack.pop()

    # Stack'teki eleman sayısı 6'dan küçükse, yeni harfi ekle
    if stack.length < 6:
        stack.push(letter)
    print(f"Push: {letter}")

# Son durumu ekrana yazdır
# last in first out kuralına göre boşalt
print("\nFinal Stack:")
while stack.top is not None:
    popped_data = stack.pop()
    print(f"Pop: {popped_data}")
