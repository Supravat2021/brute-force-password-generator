# 🔐 Password Generator – Brute Force Wordlist Creator

This Python script is a **password list generator for brute-force attacks**, designed to create **all possible combinations** of passwords using:

- ✅ Uppercase letters (A–Z)
- ✅ Lowercase letters (a–z)
- ✅ Numbers (0–9)
- ✅ Special characters (e.g., !@#$%^&*()_+[]{}|;:,.<>?/)

It can be used for **testing password security**, penetration testing, or educational demonstrations of brute-force techniques.

---

## 📦 How to Use

### 1. Clone the repository
```bash
git clone https://github.com/your-username/password-generator.git
cd password-generator
````

### 2. Run the script

```bash
python password_generator.py
```

### 3. Enter input when prompted

```
Enter minimum password length: 2
Enter maximum password length: 3
```

The script will:

* ✅ Display each generated password in your terminal
* ✅ Save all passwords to a file named `password_list.txt`

---

## ⚠️ WARNING: Exponential Growth

This tool performs **brute-force generation**, meaning it creates every possible combination of characters for the specified length.
The number of generated passwords increases **exponentially**:

| Password Length | Approx. Number of Combinations |
| --------------- | ------------------------------ |
| 2               | \~9,000                        |
| 3               | \~850,000                      |
| 4               | \~81 million                   |
| 5               | \~7+ billion ⚠️                |

### ❗ Use Responsibly:

* This tool is for **educational and ethical use only**.
* It should not be used for unauthorized access or illegal activities.
* Avoid using large lengths unless you're writing to a file only.
* Terminal printing with large lengths may freeze or crash your system.

---

## 📁 Output

The generated passwords will be saved in:

```
password_list.txt
```

This file is created automatically in the same folder as the script.

---

> ⚠️ **Disclaimer:** This tool is for educational and cybersecurity testing purposes only. Misuse of this tool for illegal or unethical purposes is strictly prohibited.

