
# Dictionary Application Using Hash Tables
# Collision Resolution: Separate Chaining

class Node:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.next = None


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, word):
        return sum(ord(char) for char in word.lower()) % self.size

    def add_word(self, word, meaning):
        index = self.hash_function(word)
        current = self.table[index]

        # Update meaning if the word already exists
        while current:
            if current.word == word.lower():
                current.meaning = meaning
                print("Meaning updated successfully.")
                return
            current = current.next

        # Insert at the beginning of the bucket's linked list
        new_node = Node(word.lower(), meaning)
        new_node.next = self.table[index]
        self.table[index] = new_node
        print("Word added successfully.")

    def search_word(self, word):
        index = self.hash_function(word)
        current = self.table[index]

        while current:
            if current.word == word.lower():
                print("Word:", current.word)
                print("Meaning:", current.meaning)
                return
            current = current.next

        print("Word not found.")

    def display(self):
        print("\n--- Dictionary Entries ---")
        found = False

        for head in self.table:
            current = head
            while current:
                print(f"{current.word}: {current.meaning}")
                found = True
                current = current.next

        if not found:
            print("Dictionary is empty.")


def main():
    dictionary = HashTable()

    while True:
        print("\n===== DICTIONARY APPLICATION =====")
        print("1. Add Word")
        print("2. Search Word")
        print("3. Display All Words")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            word = input("Enter word: ").strip()
            meaning = input("Enter meaning: ").strip()

            if word and meaning:
                dictionary.add_word(word, meaning)
            else:
                print("Word and meaning cannot be empty.")

        elif choice == "2":
            word = input("Enter word to search: ").strip()

            if word:
                dictionary.search_word(word)
            else:
                print("Please enter a word.")

        elif choice == "3":
            dictionary.display()

        elif choice == "4":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please select 1 to 4.")


if __name__ == "__main__":
    main()
