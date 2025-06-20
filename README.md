# 🔐 Brute Force Password Generator

This Python script is a **password list generator for brute-force attacks**. It generates **all possible combinations** of passwords using:

- ✅ Uppercase letters (A–Z)
- ✅ Lowercase letters (a–z)
- ✅ Numbers (0–9)
- ✅ Special characters (e.g., !@#$%^&*()_+[]{}|;:,.<>?/)

This tool is ideal for:

- Password strength testing  
- Penetration testing  
- Cybersecurity training and research

---
## 🎥 Demo Video

[![Watch the demo](https://img.youtube.com/vi/c1fCTHSMhU4/hqdefault.jpg)](https://www.youtube.com/watch?v=c1fCTHSMhU4)

...

## 📦 How to Use

### 1. Clone the repository
```bash
git clone https://github.com/Supravat2021/brute-force-password-generator.git
cd brute-force-password-generator
````

### 2. Run the script

```bash
python password_generator.py
```

### 3. Enter password length range

```
Enter minimum password length: 2
Enter maximum password length: 3
```

✅ Passwords will be:

* Printed in your terminal
* Saved to a file called `password_list.txt`

---

## ⚠️ WARNING: Exponential Generation

This tool uses **brute-force logic** to generate every possible combination.
The number of passwords **grows rapidly** as length increases:

| Password Length | Approx. Combinations |
| --------------- | -------------------- |
| 2               | \~9,000              |
| 3               | \~850,000            |
| 4               | \~81 million         |
| 5               | \~7+ billion ⚠️      |

### ❗ Use Responsibly

* For **educational and ethical** purposes only
* Avoid large lengths unless you're **saving to file only**
* Large outputs may **crash your system** if printed to terminal

---

## 📁 Output File

All generated passwords will be saved to:

```
password_list.txt
```

---

> ⚠️ **Disclaimer:** This tool is intended for educational, ethical hacking, and security research purposes only. Any unauthorized or malicious use is strictly prohibited.

