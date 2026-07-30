# Day 26 - NATO Phonetic Alphabet

## 📖 Overview

The NATO Phonetic Alphabet project is a Python application that converts any word entered by the user into its corresponding NATO phonetic alphabet code words. The program reads the NATO alphabet dataset from a CSV file using Pandas, creates a dictionary mapping each letter to its phonetic code, and then translates the user's input into a list of NATO code words.

For example, if the user enters **HELLO**, the program outputs:

```python
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

This project was developed as **Day 26** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on dictionary comprehensions, list comprehensions, reading CSV files with Pandas, and efficient data transformation.

---

## 🎯 Objective

Create a NATO Phonetic Alphabet Converter that:

- Read NATO phonetic alphabet data from a CSV file.
- Convert the CSV data into a Python dictionary.
- Accept a word from the user.
- Convert each letter into its NATO phonetic alphabet equivalent.
- Display the resulting list of code words.

---

## 🛠️ Concepts Practiced

- Pandas DataFrames
- Reading CSV Files
- Dictionary Comprehensions
- List Comprehensions
- User Input
- String Manipulation
- Data Mapping
- Iterating Through DataFrames
- Data Transformation
- Python Collections

---

## 📂 Files

```
Day-026-NATO-Phonetic-Alphabet/
├── nato_phonetic_alphabet.csv    # NATO alphabet dataset
├── main.py                       # Main program
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Install the required library:

```bash
pip install pandas
```

4. Run the program:

```bash
python main.py
```

---

## 🔤 How It Works

1. The program reads the **nato_phonetic_alphabet.csv** file using Pandas.
2. A dictionary is created where:
   - Key = Alphabet letter
   - Value = NATO code word
3. The user enters a word.
4. The input is converted to uppercase.
5. Each letter is looked up in the dictionary.
6. The corresponding NATO code words are stored in a list.
7. The final list is printed to the console.

### Example

**Input**

```
Enter a word: ChatGPT
```

**Output**

```python
['Charlie', 'Hotel', 'Alfa', 'Tango', 'Golf', 'Papa', 'Tango']
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

- Read CSV files using Pandas.
- Convert DataFrame data into Python dictionaries.
- Use dictionary comprehensions for efficient data mapping.
- Use list comprehensions to transform user input.
- Work with strings and character-by-character iteration.
- Build clean and concise Python programs.
- Combine user input with external datasets.
- Apply Python comprehensions to solve real-world problems efficiently.

---

## 🚀 Future Improvements

- Handle invalid characters such as numbers and symbols.
- Continue asking for input until the user chooses to exit.
- Display one NATO code word per line.
- Add pronunciation audio for each code word.
- Build a graphical user interface (GUI) using Tkinter.
- Allow users to convert entire sentences.
- Export the converted NATO words to a text file.
- Add error handling for missing or corrupted CSV files.