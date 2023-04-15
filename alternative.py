#1. For the first task we want to alternate upper and lower on each character

#Firstly we define the sentence we want to apply the conditions to.
sentence = "Hello, I am Alex Maghakian!"
final_string = ""

#Secondly we apply the code to turn uppercase and lowercase every each character.

for i in range (len(sentence)) :
    if i % 2 == 1:

        final_string += sentence [i].lower()
        
    else:
        final_string += sentence [i].upper()
#Thridly we print the result
print (final_string)

# 2. For the second task, we want to apply uppercase and and lower to every each one word.

# We firstly plit the string into a list of words
words = sentence.split()

# We secondly through the words and convert alternate words to uppercase and lowercase
for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i].upper()
    else:
        words[i] = words[i].lower()

# We thridly join the words back into a string
new_string = ' '.join(words)
#We finally print the end result
print(new_string)