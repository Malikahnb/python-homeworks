import string


def file_exists(filename):
    try:
        with open(filename, "r") as f:
            return True
    except FileNotFoundError:
        return False


def create_file_if_not_exists():
    if not file_exists("sample.txt"):
        print("sample.txt not found. Please enter a paragraph to create the file:")
        content = input("Enter text: ")
        with open("sample.txt", "w") as f:
            f.write(content)


def clean_word(word):
    return word.strip(string.punctuation).lower()


def count_word_frequency():
    create_file_if_not_exists()
    word_count = {}
    total_words = 0

    with open("sample.txt", "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                cleaned_word = clean_word(word)
                if cleaned_word:
                    total_words += 1
                    word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return total_words, sorted_words


def save_report(total_words, sorted_words, top_n=5):
    with open("word_count_report.txt", "w") as f:
        f.write("Word Count Report\n")
        f.write(f"Total Words: {total_words}\n")
        f.write("Top Words:\n")
        for word, count in sorted_words[:top_n]:
            f.write(f"{word} - {count}\n")


def main():
    total_words, sorted_words = count_word_frequency()
    print(f"Total words: {total_words}")

    top_n = input("Enter the number of top words to display (default 5): ")
    top_n = int(top_n) if top_n.isdigit() else 5

    print("Top common words:")
    for word, count in sorted_words[:top_n]:
        print(f"{word} - {count} times")

    save_report(total_words, sorted_words, top_n)
    print("Report saved to word_count_report.txt")


if __name__ == "__main__":
    main()
