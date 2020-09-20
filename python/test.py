def unique_english_letters(word):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    for x in word:
        #print(x)
        if letters.find(x) >= 0:
            letters = letters.replace(x, "")
            print(x)
            print(len(letters))

            #letters[:i] + letters[i+1:]
    return 52 - len(letters)
# Uncomment these function calls to test your function:
#print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
#
numbers_a = [x+1 for x in range(12)]
print(numbers_a)
numbers_a = range(1,13)
print(numbers_a)
