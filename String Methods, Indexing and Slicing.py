## **String Methods, Indexing and Slicing**
text = " heLLo world "
print(text.upper())      # Output: " HELLO WORLD "
print(text.lower())      # Output: " hello world "
print(text.title())      # Output: " Hello World "
print(text.strip())      # Output:  "heLLo world" -> remove spaces

text = "  hEjbuLlA aSAs ShEhAb  "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.title())


##
text = "Hello World"
print(text.replace("World", "Bangladesh"))  # Output: "Hello Bangladesh"
print(len(text))                            # Output: 11 -> length of string
print(text.startswith("Hello"))              # True
print(text.endswith("Python"))              # False


text = "Daffodil University"
print(text)
print(len(text)) #19
text1 = text.replace("Daffodil", "City")
print(text1)
print(len(text1)) #15


##
sentence = "python programming is fun"
print(sentence.capitalize()) # Output: "Python programming is fun"
print(sentence.title())      # Output: "Python Programming Is Fun"
print(sentence.count('o'))   # Output: 2 (counts occurrences of 'o')
print(sentence.find('gram')) # Output: 10 (finds position of substring)
print(sentence.split())      # Output: ["python", "programming", "is", "fun"]


sen = "the motor has no gurantee"
print(sen.capitalize())
print(sen.count("o")) #3
print(sen.find('tee')) #22
print(sen.split())


# chaining multiple methods at one time
text = " Java progRaMming "
result = text.strip().replace("Java", "Python").upper()
print(result)   # Output: "PYTHON PROGRAMMING"

text1 = "  mY goaL is to AchIeve gOOd reSult."
shehab = text1.strip().title().replace("my", "Our")
print(shehab) #My Goal Is To Achieve Good Result.

