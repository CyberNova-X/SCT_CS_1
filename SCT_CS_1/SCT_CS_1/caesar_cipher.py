"""
Caesar Cipher Encryption & Decryption Tool
Author: Gaurang Bhatt
Internship: SkillCraft Technology (Cyber Security Track)
Task 01: Implement Caesar Cipher
"""

from typing import Tuple

def normalize_shift(shift: int) -> int:
    """Normalize any integer shift to range 0..25"""
    return shift % 26

def shift_char(c: str, shift: int) -> str:
    """Shift a single alphabetic character by 'shift' preserving case; non-alpha returned unchanged."""
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + shift) % 26 + base)
    return c

def encrypt(text: str, shift: int) -> str:
    """Encrypts text using Caesar Cipher with given shift."""
    s = normalize_shift(shift)
    return ''.join(shift_char(ch, s) for ch in text)

def decrypt(text: str, shift: int) -> str:
    """Decrypts text using Caesar Cipher with given shift (inverse)."""
    s = normalize_shift(shift)
    return ''.join(shift_char(ch, -s) for ch in text)

def analyze(message: str) -> Tuple[bool, bool]:
    """Basic analysis: returns (has_alpha, has_nonalpha)"""
    has_alpha = any(ch.isalpha() for ch in message)
    has_non = any(not ch.isalpha() for ch in message)
    return has_alpha, has_non

if __name__ == "__main__":
    print("=== Caesar Cipher Tool ===")
    choice = input("Choose an option (E = Encrypt / D = Decrypt): ").strip().upper()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (any integer, e.g., 3 or -5): "))
        if choice == "E":
            encrypted = encrypt(message, shift)
            print(f"\n🔐 Encrypted Message: {encrypted}")
        elif choice == "D":
            decrypted = decrypt(message, shift)
            print(f"\n🔓 Decrypted Message: {decrypted}")
        else:
            print("❌ Invalid choice! Please choose 'E' or 'D'.")

        has_alpha, has_non = analyze(message)
        print("\n[Info] Message contained alphabets:", has_alpha, "| Non-alphabet chars:", has_non)
    except ValueError:
        print("❌ Shift value must be a number!")