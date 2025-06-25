# Numbering System Converter (Python & C++)

A simple interactive console program to convert numbers between **Decimal**, **Binary**, **Octal**, and **Hexadecimal** systems.

This project is implemented in both:

* 🐍 **Python**
* 💻 **C++**

---

## 📂 Project Structure

```
/repo-root
│
├── converter_python.py      # Python version of the converter
├── converter_cpp.cpp        # C++ version of the converter
└── README.md                # This file
```

---

## 🎯 Features

✅ Converts between **Decimal, Binary, Octal, and Hexadecimal**
✅ Input validation for each number system
✅ Keeps hexadecimal letters in uppercase
✅ Interactive, menu-driven user experience

---

## 🐍 Python Version

### How to Run:

Make sure you have Python 3.x installed.

```bash
python converter_python.py
```

### Example Run:

```
* numbering system converter *
A) insert a new number
B) Exit program
Enter your choice: A
Please insert a number: DA457C
* Please select the base you want to convert a number from *
A) Decimal
B) Binary
C) Octal
D) Hexadecimal
Enter your choice: D
* Please select the base you want to convert a number to *
A) Decimal
B) Binary
C) Octal
D) Hexadecimal
Enter your choice: A
14332604
```

---

## 💻 C++ Version

### How to Compile & Run:

Use any C++ compiler (e.g., g++, clang++):

```bash
g++ converter_cpp.cpp -o converter
./converter
```

### Example Run:

```
* numbering system converter *
A) insert a new number
B) Exit program
Enter your choice: A
Please insert a number: 11001110
* Please select the base you want to convert a number from *
A) Decimal
B) Binary
C) Octal
D) Hexadecimal
Enter your choice: B
* Please select the base you want to convert a number to *
A) Decimal
B) Binary
C) Octal
D) Hexadecimal
Enter your choice: C
316
```

---

## 🧠 Authors

* **Yassin Ahmed**
* **Eyad Tamer**
* **Ziad Ahmed**

---

## 📢 Notes

* The Octal system in this project uses base **8**, but some examples in the comments mention base **9**, which might cause confusion. Adjust if needed.
* Hexadecimal outputs use uppercase letters (A-F) as per standard.
* Supports interactive conversion with input checks to ensure valid numbers.

---

## ✅ Future Improvements (Optional Ideas)

* Support floating point numbers for conversion
* GUI version using Tkinter (Python) or Qt (C++)
* Unit tests for better code reliability

---

## 🛠 Requirements

* Python 3.x for the Python version
* C++11 or newer compatible compiler for the C++ version

---

## 📄 License

Free to use for educational purposes. Contributions and suggestions are welcome!
