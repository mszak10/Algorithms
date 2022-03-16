# firstNonRepeatChar.py -  takes a string input, and returns the first character that is not repeated in the string

def first_non_repeating_letter(string):
    if string == '':
        return ''
    else:
        for i, w in enumerate(string):
            if w.lower() not in string[i + 1:len(string)].lower() and w.lower() not in string[:i].lower():
                return w
        return ''


word = 'Go hang a salami, I\'m a lasagna hog!'
print(first_non_repeating_letter(word))
# outputs ,
