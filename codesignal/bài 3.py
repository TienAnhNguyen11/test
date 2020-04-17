def reverse(s):
    return s[::-1]

def checkPalindrome(s):
    rev= reverse(s)
    if s== rev:
        print("đúng")

    else:
        print("sai")

checkPalindrome("abc")
checkPalindrome("aba")
checkPalindrome("racecar")
