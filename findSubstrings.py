# def generate_substrings(str):
#     substrings=[]
#     sub = set()
#     for i in range(0,len(str)):
#         for j in range(i+1,len(str)+1):
#             substrings.append(str[i:j])
#             sub.add(str[i:j])
#     print()
#     print("List:",substrings)
#     print()
#     print("Set:",sub)
#     print()

# generate_substrings("alanluke")

def is_vowel(char):
    return char.lower() in 'aeiou'

def is_consonant(char):
    return char.lower().isalpha() and not is_vowel(char)

def generate_substrings(string):
    substrings = []
    
    for i in range(0, len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            print(substring)
            if is_vowel(substring[0]) and is_consonant(substring[-1]):
                substrings.append(substring)

    return substrings

# Example usage:
input_string = "abc"
result = generate_substrings(input_string)
print(result)


