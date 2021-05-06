import pandas

data = pandas.read_csv(r"days\21-30\day26\nato alphabet project\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter the word: ").upper()
phonetic_words = [phonetic_dict[letter] for letter in word]

print(phonetic_words)
