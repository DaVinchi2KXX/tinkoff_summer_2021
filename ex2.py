vowels = ['a', 'e', 'i', 'o', 'u', 'y']
nickname = input()
if nickname[0] in vowels:
    counter = 0
else:
    counter = 1
letter_count = 0
for letter in nickname:
    if letter in vowels and counter == 0:
        counter += 1
        if letter == nickname[-1] and letter_count + 1 == len(nickname):
            print("YES")
            break
    elif counter == 1:
        counter -= 1
        if letter in vowels:
            print("NO")
            break
        else:
            if letter == nickname[-1] and letter_count + 1 == len(nickname):
                print("YES")
    else:
        print("NO")
        break
    letter_count += 1
