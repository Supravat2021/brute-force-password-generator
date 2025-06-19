import itertools
import string

characters = string.ascii_letters + string.digits + string.punctuation

min_length = int(input("Enter minimum password length: "))
max_length = int(input("Enter maximum password length: "))

if min_length > max_length or min_length <= 0:
    print("❌ Invalid range. Minimum must be ≤ maximum and > 0.")
else:
    output_file = "password_list.txt"
    count = 0  

    with open(output_file, "w", encoding="utf-8") as f:
        for length in range(min_length, max_length + 1):
            for combo in itertools.product(characters, repeat=length):
                password = ''.join(combo)
                print(password)          
                f.write(password + "\n") 
                count += 1

    print(f"\n[✔] Total passwords generated: {count}")
    print(f"[✔] Saved to: {output_file}")
