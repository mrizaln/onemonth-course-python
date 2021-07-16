# defining sing

def print_verse(bottles):
    print(bottles, "bottles of beer on the wall,", end=' ')
    print(bottles, "bottles of beer.")
    print("Take one down and pass it around,", end=' ')
    print(bottles - 1, "bottles of beer on the wall.\n")

def print_last_verse():
    print("No more bottles of beer on the wall,", end=' ') 
    print("no more bottles of beer.")
    print("Go to the store and buy some more,", end=' ')
    print("99 bottles of beer on the wall.\n")

def sing(bottles):
    for number in reversed(range(bottles + 1)):
        if number > 0:
            print_verse(number)
        else:
            print_last_verse()

# printing and executing

print("----------")
print("I used to play sports. Then I realized you can buy trophies. Now I am good at everything.")
print("----------")

bottles = 99
print("This should be ninety-nine:", bottles)
sing(bottles)

sentence = "I think it's interesting that 'cologne' rhymes with 'alone'"
words    = sentence.split()

print(f'"{sentence}" has {len(words)} words')
print("The words are:", words)
print("The sorted words are:", sorted(words))

print(words[0])
print(words[-1])
print(words[0], words[-1], sep = '\n')
