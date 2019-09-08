my_str = input("Enter a string with spaces between letters : ")  

words = my_str.split()  
  
words.sort()   
for word in words:  
   print(word)