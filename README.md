# Dictionary Application Using Hash Tables with Collision Resolution

## 1. Description

The **Dictionary Application Using Hash Tables with Collision Resolution** is a Python-based project that demonstrates how hash tables can be used to store, search, and manage words and their meanings efficiently.

Each word is converted into a hash index using a hash function. The word and its meaning are stored at the corresponding index in the hash table. When two or more words generate the same index, a collision occurs. This project handles collisions using **separate chaining**, in which a linked list stores multiple entries at the same index.

The application provides a menu-driven interface that allows users to add words, search for words, update existing meanings, and display all dictionary entries.

## 2. Objectives

- To understand the concept of hashing and hash tables.
- To implement a hash function for generating table indices.
- To understand and handle collisions using separate chaining.
- To perform insertion, searching, and updating operations.
- To use linked lists for storing entries with the same hash index.
- To analyze the time and space complexity of hash table operations.

## 3. Problem Statement

A dictionary stores words along with their meanings. Searching for a word in a large collection using a simple sequential search may require checking many entries.

The objective of this project is to develop a dictionary application using a hash table that provides efficient insertion and searching. Since different words can produce the same hash index, a collision resolution technique is required.

The project uses **separate chaining** to handle collisions and enables users to add, search, update, and display dictionary entries.

## 4. Technologies Used

- **Programming Language:** Python
- **Data Structure:** Hash Table
- **Collision Resolution Technique:** Separate Chaining
- **Supporting Data Structure:** Linked List
- **Development Environment:** Visual Studio Code

## 5. Features

- Add a new word with its meaning.
- Search for a word in the dictionary.
- Update the meaning if a word already exists.
- Display all stored words and meanings.
- Handle hash collisions using separate chaining.
- Provide a simple menu-driven interface.
- Validate empty inputs and invalid menu choices.

## 6. Algorithm

### Hash Function

The hash function converts a word into an index in the hash table.

The index is calculated using the sum of the character Unicode values modulo the table size.

**Formula:**

`index = sum(ord(char) for char in word.lower()) % size`

### Separate Chaining

Separate chaining resolves collisions by maintaining a linked list at each hash table index. If multiple words generate the same index, their nodes are stored in the same linked list.

### Steps

1. Initialize a hash table of size 10.
2. Accept the user's menu choice.
3. For adding a word, calculate its hash index.
4. Check whether the word already exists at that index.
5. If it exists, update its meaning; otherwise, insert a new node.
6. For searching, calculate the index and traverse the linked list at that position.
7. For displaying, traverse all buckets and print the stored entries.
8. Repeat until the user chooses Exit.

## 7. Sample Input and Output

### Example 1: Add a Word

```text
===== DICTIONARY APPLICATION =====
1. Add Word
2. Search Word
3. Display All Words
4. Exit

Enter your choice (1-4): 1
Enter word: Python
Enter meaning: A programming language
Word added successfully.
```

### Example 2: Search for a Word

```text
Enter your choice (1-4): 2
Enter word to search: Python
Word: python
Meaning: A programming language
```

### Example 3: Display All Words

```text
Enter your choice (1-4): 3

--- Dictionary Entries ---
python: A programming language
```

*Note: The displayed order may vary depending on the hash indices and the insertion of entries.*

## 8. Complexity Analysis

Let `n` be the number of words stored in the dictionary and `m` be the size of the hash table.

| Operation | Average Case | Worst Case |
|---|---|---|
| Insertion | O(1) | O(n) |
| Searching | O(1) | O(n) |
| Updating | O(1) | O(n) |
| Display All Entries | O(n + m) | O(n + m) |

**Space Complexity:** O(n + m), because the hash table contains `m` buckets and the linked-list nodes store `n` entries.

Average-case constant-time performance assumes that the hash function distributes words reasonably evenly across the buckets.

## 9. Applications

- Implementing dictionary and glossary applications.
- Building symbol tables in compilers.
- Storing user records using keys.
- Implementing lookup tables in software.
- Managing contact information.
- Supporting caching and fast data retrieval.
- Demonstrating collision resolution in data structures.

## 10. Advantages

- Provides efficient average-case insertion and searching.
- Handles collisions using linked lists.
- Supports updating existing word meanings.
- Demonstrates the practical use of hashing.
- Uses a simple menu-driven interface.
- Does not rely on Python's built-in dictionary for the main hash table implementation.

## 11. Limitations

- The hash table uses a fixed size of 10 buckets.
- Performance may decrease when many words map to the same bucket.
- The dictionary data is not saved permanently after the program terminates.
- The hash function is simple and may not distribute all words evenly.
- The application supports word lookup but does not provide advanced features such as fuzzy searching or alphabetical sorting.

## 12. Future Scope

- Add file handling or database support for permanent storage.
- Increase or dynamically resize the hash table when required.
- Improve the hash function to distribute entries more evenly.
- Add alphabetical sorting of dictionary entries.
- Implement prefix-based and approximate word searching.
- Develop a graphical user interface for easier interaction.
- Add support for multiple languages.

## 13. Conclusion

The Dictionary Application Using Hash Tables with Collision Resolution demonstrates the practical implementation of hashing and separate chaining in Python. It uses a hash function to determine the storage location of each word and linked lists to handle collisions.

The application supports adding, searching, updating, and displaying dictionary entries. It helps explain how hash tables improve data retrieval efficiency and how collision resolution maintains correct storage when multiple keys map to the same index.

This project provides a useful foundation for understanding hash tables and their applications in computer science.

## 14. References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
2. Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). *Data Structures and Algorithms in Python*. Wiley.
3. Python Software Foundation. *Python Documentation*. https://docs.python.org/3/
4. GeeksforGeeks. *Hashing Data Structure*. https://www.geeksforgeeks.org/hashing-data-structure/
