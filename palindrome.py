
def is_palindrome(data):
    '''funkcja do sprawdzenia'''
    if data == "":
        return
    elif not isinstance(data, str):
        return False
    else:
        lowercase_data = data.lower().replace(" ","")

        s = lowercase_data[::-1]
        s = s.replace(" ","")

        if lowercase_data == s:
            return s
        else:
            return False


test_cases = {
    "Anna" : "anna",
    "radar" : "radar",
    "Mateusz" : False,
    "" : None,
    "Mamuta tu mam" : "mamutatumam",
    22 : False,             # wartosci inne niz string nie sa palindromami
    "!12a 21!" : "!12a21!",
}

for data, expectation in test_cases.items():
    response = is_palindrome(data)
    assert response == expectation, \
        f"{expectation} from {data} nie jest rowne {response}"
