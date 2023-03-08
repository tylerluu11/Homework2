word = str(input())
word1 = word.replace(' ','')
if word1 == word1[::-1]:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')