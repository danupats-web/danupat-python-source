def check_palindrome(word):
    word_lower = word.lower()
    
    reversed_word = word_lower[::-1]
    
    if word_lower == reversed_word:
        print("Yes")
    else:
        print("No")

print("Check 'Sam': ", end="")
check_palindrome("Sam")  

print("Check 'DAD': ", end="")
check_palindrome("DAD")  

print("Check 'Mum': ", end="")
check_palindrome("Mum")  