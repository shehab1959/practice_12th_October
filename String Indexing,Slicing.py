#### **String Indexing*
text = "Python"

print(text[0])      # Output: "P"
print(text[3])      # Output: "h"
print(text[2])      # Output: "y"
print(text[5])      # Output: "n"
print(text[-1])     # Output: "n"
print(text[-5]) #y

sen = "Shehab"
print(sen[-4]) #e




####String Slicing

#| Characters        | P     | y     | t     | h     | o     | n     |
#|-------------------|-------|-------|-------|-------|-------|-------|
#| **Index**         | 0     | 1     | 2     | 3     | 4     | 5     |

text = "Python"

print(text[1:4])    # Output: "yth" → from index 1 to 4 (4 excluded)
print(text[:3])     # Output: "Pyt" → from start (0) to index 3 (excluded)
print(text[3:])     # Output: "hon" → from index 3 to end

print(text[::-1])   # Output: "nohtyP" → reverse string
print(text[::2])    # Output: "Pto" → every 2nd character (step = 2)

sen = "Hejbulla"
print(sen[0:]) #Hejbulla
print(sen[0:5]) #Hejbu
print(sen[:6]) #Hejbul
print(sen[::-1]) #allubjeH
print(sen[::2]) #Hjul
print(sen[::-2]) #albe