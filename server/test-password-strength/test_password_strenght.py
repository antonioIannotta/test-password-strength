import math

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
    score = 0
    for special_symbol in special_symbols:
        if special_symbol in password:
            score += 10

    return math.floor(score / len(special_symbols))

def personal_information_score(personal_information: list[str]):
    pass




    