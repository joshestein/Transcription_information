from collections import Counter
import glob

words = {}

def read_words(file):
    global words
    with open(file) as f:
        data = f.read().split()
        for word in data:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

def main():
    files = glob.glob("*.txt")
    for file in files:
        read_words(file)
    
    print(Counter(words).most_common(100))

if __name__ == '__main__':
    main()