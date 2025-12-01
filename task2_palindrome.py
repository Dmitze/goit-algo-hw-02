from collections import deque
import re

def is_palindrome(text):
    cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я]', '', text.lower())
    char_deque = deque(cleaned_text)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

# Тестування
test_strings = [
    "А роза упала на лапу Азора",
    "мадам",
    "hello",
    "12321"
]

for text in test_strings:
    result = is_palindrome(text)
    print(f"'{text[:20]}...' -> {'паліндром' if result else 'не паліндром'}")