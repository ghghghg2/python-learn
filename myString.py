# '' and "" is the same.
# ''' or """ for multiline.
# escape symbol: \
# r"..." to ignore the escape symbol. Note. r means 'raw' here.
# '+' for cascade string
# '*' for repeat string
# string indexing: 0 (left to right), -1 (right to left)
# sub-string indexing: str[head(include):(tail)(not include):(step)]

paragraph = \
'''This is a sentence. 
This is another sentence.'''
str1 = "123456789"
str2 = 'abcdefghi'

print('-----------')
print(paragraph)

print('-----------')
print(str1)

print('-----------')
print(str2)

print('-----------')
print("abcdef\rghi")

print('-----------')
print(r"abcdef\rghi")

print('-----------')
print(str1 + str2)

print('-----------')
print(str1 * 2)

print('-----------')
print(str1[0:-1])

print('-----------')
print(str1[2:5])

print('-----------')
print(str1[0:-1:2])

# Treat as end if the tail is not given
print('-----------')
print(str1[0::2])
 