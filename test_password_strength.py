SCORE_BASE = 10


def length_score(_password: str):
    """
    This method assigns a score based on the length of the provided password
    :param _password: the provided password
    :return: the score based on the length of the password.
    """
    min_password_length: int = 8
    max_password_length: int = 26

    if not isinstance(password, str):
        raise ValueError("The password must be a string")

    default_value: float = (len(password) - min_password_length) / 2

    if len(password) == max_password_length:
        return 10
    elif len(password) == min_password_length:
        return 0
    else:
        return default_value


def special_symbols_score(_password: str) -> float:
    """
    This method assigns a score based on the usage of special symbols
    :param _password: the provided password
    :return: the score based on the usage of special symbols.
    """

    if not isinstance(password, str):
        raise ValueError("The password must be a string")

    special_symbols: str = '?,.-^!°§*[]/+<>'
    single_symbol_score: float = SCORE_BASE / len(special_symbols)
    score: float = sum(single_symbol_score for symbol in special_symbols if symbol in password)
    return score


def personal_information_score(_password: str, personal_information: dict) -> int:
    """
    This method assigns a score for the password provided based on the usage of either totality or partial part of
    personal information in it.
    :param _password: the password of which compute the score
    :param personal_information: the personal information
    :return:
    """

    if not isinstance(password, str):
        raise ValueError("The password must be a string")

    _name: str = personal_information['name']
    _surname: str = personal_information['surname']
    _date_of_birth: str = personal_information['date_of_birth']
    favorite_music: str = personal_information['favorite_music']
    _place_of_birth: str = personal_information['place_of_birth'].replace(' ', '').replace('-', '').replace('\'', '')

    name_score: int = _return_info_in_password(name, password)
    surname_score: int = _return_info_in_password(surname, password)
    favorite_music_score: int = _return_info_in_password(favorite_music, password)
    place_of_birth_score: int = _return_info_in_password(place_of_birth, password)
    date_of_birth_score: int = _date_of_birth_in_password(date_of_birth, password)

    return 10 - 2 * (name_score + surname_score + favorite_music_score + place_of_birth_score + date_of_birth_score)


def _return_info_in_password(information: str, _password: str) -> int:
    if not isinstance(information, str) or not isinstance(password, str):
        raise ValueError("Password and personal information must both be string")

    if information.lower() in password.lower() or information.lower()[::-1] in password.lower():
        return 1
    return 0


def _date_of_birth_in_password(_date_of_birth: str, _password: str) -> int:
    if not _is_date_valid(date_of_birth):
        raise ValueError("Incorrect date format")

    _day: int = int(date_of_birth.split('-')[0])
    _month: int = int(date_of_birth.split('-')[1])
    _year: int = int(date_of_birth.split('-')[2])

    if 1 <= _day <= 9:
        if str(day) in password.lower():
            return 1
    else:
        if str(day) in password.lower() or str(day)[::-1] in password.lower():
            return 1

    if 1 <= _month <= 9:
        if str(month) in password.lower():
            return 1
    else:
        if str(month) in password.lower() or str(month)[::-1] in password.lower():
            return 1

    if str(year) in password.lower() or str(year)[2:] in password.lower() or year[::-1] in password.lower():
        return 1
    return 0


def _is_date_valid(_date_of_birth: str) -> bool:
    if "-" in date_of_birth:
        _day: str = date_of_birth.split('-')[0]
        _month: str = date_of_birth.split('-')[1]
        _year: str = date_of_birth.split('-')[2]

        months_30_days: list[int] = [4, 6, 9, 11]
        months_31_days: list[int] = [1, 3, 5, 7, 8, 10, 12]
        month_28_days = 2

        if not year.isdigit() or int(year) < 1920 or int(year) > 2015:
            return False

        if day.isdigit():
            if month.isdigit():
                if int(month) in months_30_days and 1 <= int(day) <= 30:
                    return True
                elif int(month) in months_31_days and 1 <= int(day) <= 31:
                    return True
                elif int(month) == month_28_days and 1 <= int(day) <= 28:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print("Hello")
    print("Insert your personal information: \n")
    name: str = str(input("Name: "))
    surname: str = str(input("Surname: "))
    day: str = str(input("Day of birth: "))
    month: str = str(input("Month of birth: "))
    year: str = str(input("Year of birth: "))
    favorite_music_genre: str = str(input("Favorite music: "))
    place_of_birth: str = str(input("Place of birth: "))
    password: str = str(input("Password: "))

    date_of_birth = day + "-" + month + "-" + year

    personal_information_dictionary: dict = {
        'name': name,
        'surname': surname,
        'date_of_birth': date_of_birth,
        'place_of_birth': place_of_birth,
        'favorite_music': favorite_music_genre
    }

    length_password_score = length_score(password)
    special_symbols_in_password_score = special_symbols_score(password)
    personal_information_password_score = personal_information_score(
        password, personal_information_dictionary
    )

    total_score = length_password_score + special_symbols_in_password_score + personal_information_password_score
    print("Password security score: {.2f}".format(total_score * 10) + "%")
