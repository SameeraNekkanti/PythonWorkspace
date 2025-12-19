def reverse_str(s):
    if len(s)==1:
        return s
    return reverse_str(s[1:])+s[0]
print(reverse_str("hello ma"))

def is_palindrome(s):
    if len(s)==1:
        return True
    if s[0]!=s[-1]:
        return False
    return is_palindrome(s[1:-1])  #checks inner substring

print(is_palindrome("madam"))    
print(is_palindrome("hello"))

