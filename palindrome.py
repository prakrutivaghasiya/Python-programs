
def reverse(s): 
	return s[::-1] 

def isPalindrome(s): 

	rev = reverse(s) 

	if (s == rev): 
		return True
	return False


s = input("enter string :")
ans = isPalindrome(s) 

if ans == 1: 
	print("String is palindrome") 
else: 
	print("String is not palindrome") 
