while True:
    x = input("Insert your sentence:")
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',]

    for i in x:
        if i.isalpha() == False:
            print("{} is not a letter.".format(i))
        else:
            if i in vowel_list:
                print("{} is a vowel.".format(i))
            else:
                print("{} is a consonant.".format(i))
