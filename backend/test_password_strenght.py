import math
import json
import pandas as pd

def length_score(password: str):
    min_len = 8
    max_len = 26
    score = 0

    password_len = len(password)
    
    if password_len == max_len:
        score = 10
    elif password_len == min_len:
        score = 0
    else:
        score = math.floor((password_len - min_len) / 2)

    return score

def special_symbols_score(password: str):
    special_symbols = '?,.-^!°§*[]/+<>'
    fold_10th = len(special_symbols) / 10
    score = 0
    for special_symbol in special_symbols:
        if special_symbol in password:
            score += fold_10th

    return math.floor(score / len(special_symbols))

def personal_information_score(password: str, personal_information: json):
    name = str(personal_information['name'])
    surname = str(personal_information['surname'])
    date_of_birth = str(personal_information['date_of_birth'])
    favorite_music = str(personal_information['favorite_music'])
    place_of_birth = str(personal_information['place_of_birth']).replace(' ', '').replace('-', '').replace('\'', '')

    score = 0
   
    score += _return_info_in_password(name, password)
    score += _return_info_in_password(surname, password)
    score += _return_info_in_password(favorite_music, password)
    score += _return_info_in_password(place_of_birth, password)
    score += _date_of_birth_in_password(date_of_birth, password)

    return (10 - 2 * score)

def Capital_letter_score(password: str):
    score = 0
    for letter in password:
        if letter.isupper():
            return 10
    return score


def _return_info_in_password(info: str, password: str):
    score = 0
    lower_password = password.lower()
    if info.lower() in lower_password or info.lower()[::-1] in password:
        return 1

    return score



def _date_of_birth_in_password(date_of_birth: str, password: str):
    score = 0
    lower_password = password.lower()

    date_of_birth = date_of_birth.split('-')
    day = date_of_birth[0]
    month = date_of_birth[1]
    year = date_of_birth[2]

    if 1 <= int(day) <= 9:
        if day in lower_password:
            return 1
        else:
            score = 0
    else:
        if day in lower_password or day[::-1] in lower_password:
            return 1
        else:
            score = 0

    if 1 <= int(month) <= 9:
        if month in lower_password:
            return 1
        else:
            score = 0
    else:
        if month in lower_password or month[::-1] in lower_password:
            return 1
        else:
            score = 0

    
    if year in lower_password or year[2:] in lower_password or year[::-1] in lower_password:
        return 1
    else:
        score = 0
    
    return score


if __name__ == '__main__':
    pass



    