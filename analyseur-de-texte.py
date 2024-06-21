import string
from collections import Counter

def clear_text(text):
    """enleve la ponctuation et les MAJ"""
    clear = str.maketrans("","",string.punctuation)
    return text.translate(clear).lower()

def count_words(text):
    """compte le nombre de mots dans le texte"""
    words = text.split()
    return len(words), Counter(words)

def count_characters(text):
    """compte le nombre de caractères"""
    return len(text)

def count_phrases(text):
    """compte le nombre de phrases"""
    sentences = text.split('. ')
    return len(sentences)

def calc_moy_mot(words):
    """calcule la longueur moyenne des mots"""
    total_moy = sum(len(word) for word in words)
    return total_moy / len(words) if words else 0

def lettre_frequence(text):
    """calcule la fréquence des lettres dans le texte."""
    return Counter(text)


text = input("Entrez un texte : ")
cleaned_text = clear_text(text)
    
num_words, word_counter = count_words(cleaned_text)
num_characters = count_characters(cleaned_text)
num_sentences = count_phrases(text)
avg_word_length = calc_moy_mot(cleaned_text.split())#la méthode split() permet obtenir une liste de mots.
letter_freq = lettre_frequence(cleaned_text)
    
print(f"Nombre de mots : {num_words}")
print(f"Nombre de caractères : {num_characters}")
print(f"Nombre de phrases : {num_sentences}")
print(f"Longueur moyenne des mots : {avg_word_length:.2f}")


print("\nMots les plus fréquents :")
for word, count in word_counter.most_common(5):
    print(f"{word}: {count} fois")
    
print("\nFréquence des lettres :")
for letter, count in letter_freq.items():
    if letter.isalpha():  # Afficher uniquement les lettres
        print(f"{letter}: {count} fois")
    
