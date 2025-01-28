def can_be_palindrome(string: str) -> bool:
    def ispalindrome(string: str, low: int, high: int) -> bool:
        while low < high:
            if string[low] != string[high]:
                return False
            low += 1
            high -= 1
        return True

    low, high = 0, len(string) - 1

    while low < high:
        if string[low] == string[high]:
            low += 1
            high -= 1
        else:
            # Check if removing one character makes it a palindrome
            return ispalindrome(string, low + 1, high) or ispalindrome(string, low, high - 1)
    
    return True  # Already a palindrome

print(can_be_palindrome('aac'))