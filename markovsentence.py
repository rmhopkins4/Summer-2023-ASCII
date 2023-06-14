import re
from collections import defaultdict

def encode_word_frequencies(file_path):
    word_frequencies = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()

        # Remove punctuation and convert text to lowercase
        text = re.sub(r'[^\w\s]', '', text) # regex expression remove symbols
        text = text.lower()

        
        # Split the text into words
        words = text.split()

        # Encode the frequencies of words appearing after a certain word
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            word_frequencies[current_word][next_word] += 1

    return word_frequencies

# Example usage
file_path = "C:/Users/rmhop/Desktop/corpus.txt"  # Replace with the path to your input file
word_frequencies = encode_word_frequencies(file_path)

# Print the encoded word frequencies
for word, frequencies in word_frequencies.items():
    print(f'Word: {word}')
    for next_word, frequency in frequencies.items():
        print(f'  Next word: {next_word} - Frequency: {frequency}')
        
        
print(word_frequencies.get("homer"))
        