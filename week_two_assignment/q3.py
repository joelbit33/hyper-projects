def clean_string(string):
    punctuations = "!()-[]{};:'\,<>./?@#$%^&*_~"
    for i in string:
        if i in punctuations:
            string = string.replace(i, "")
    string_list = string.split()
    return string_list


user_sentence = input("Sentence here: ")

print(clean_string(user_sentence))
