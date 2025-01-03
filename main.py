def count_words(text):
    return len(text.split())

def count_characters(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(report):
    return report["count"]

def main():
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_content = f.read()
        counts = count_characters(file_content)
        raw_report = [{"char": c, "count": n} for c, n in counts.items() if c.isalpha()]
        raw_report.sort(key=sort_on, reverse=True)

        print(f"--- Report for {file_name} ---")
        print(f"{count_words(file_content)} words")
        for count in raw_report:
            print(f"Character {count['char']}: {count['count']} time(s)")
        print("--- End report ---")


main()