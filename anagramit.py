import os

def load_swedish_words(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip().lower() for word in file)


def find_words(letters, swedish_words):
    words_found = set()

    # Funktion för att kontrollera om ett ord finns i listan med svenska ord
    def is_swedish_word(word):
        return word.lower() in swedish_words

    # Funktion för att generera alla möjliga kombinationer av bokstäver
    def generate_combinations(letters, length):
        if length == 0:
            return ['']
        return [letter + rest for i, letter in enumerate(letters) for rest in generate_combinations(letters[:i] + letters[i+1:], length - 1)]

    # Generera och kontrollera alla möjliga ordkombinationer
    for i in range(3, 8):  # Ordlängd från 3 till 7 bokstäver
        combinations = generate_combinations(letters, i)
        for word in combinations:
            if is_swedish_word(word):
                words_found.add(word)

    return words_found

def present_results(words):
    index = 1
    for word in words:
        print("Ord", index, "av", len(words), ":", word)
        command = input("Välj 'n' för nästa ord, 'q' för att avsluta: ")
        if command.lower() == 'n':
            index += 1
        elif command.lower() == 'q':
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt kommando. Försök igen.")
    else:
        print("Inga fler ord.")


def main():
    input_letters = input("Ange 16 bokstäver med mellanslag mellan dem: ").split()
    
    # Kontrollera om antalet inmatade bokstäver är exakt 16
    if len(input_letters) != 16:
        print("Felaktigt antal bokstäver. Vänligen ange 16 bokstäver.")
        return
    
    # Läs in svenska ord från textfilen
    swedish_words = load_swedish_words("saol.txt")

    # Skapa en sträng av alla inmatade bokstäver
    all_letters = ''.join(input_letters)
    
    # Hitta svenska ord som kan bildas från alla inmatade bokstäver
    found_words = find_words(all_letters, swedish_words)
    
    # Skriv ut de hittade orden
    if found_words:
        present_results(found_words)
    else:
        print("Inga svenska ord kunde bildas från de givna bokstäverna.")

if __name__ == "__main__":
    main()
