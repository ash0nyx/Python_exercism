def convert(number):
    answer = ""
    if number % 3 == 0 : answer += "Pling"
    if number % 5 == 0 : answer += "Plang"
    if number % 7 == 0 : answer += "Plong"
    return answer if answer else str(number)