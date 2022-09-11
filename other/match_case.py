# match/case

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(4))

# def factorial(n):
#     match n:
#         case 0 | 1:
#             return 1
#         case _:
#             return n * factorial(n - 1)

# print(factorial(5))

# def act(command):
#     match command.split():
#         case "Cook", "breakfast":
#             return "Я люблю завтракать."
#         case "Cook", *wtv:
#             return "Что то готовится..."
#         case "Go", "North" | "East" | "South" | "West":
#             return "Хорошо, я пошел!"
#         case "Go", *wtv:
#             return "Неизвестное направление..."
#         case _:
#             return "Я не могу этого сделать..."

# print(act('Go North'))

def act(command):
    match command.split():
        case "Cook", "breakfast":
            return "Я люблю завтракать."
        case "Cook", *wtv:
            return f"Готовится {wtv}..."
        # результат совпадения записывается в переменную `direction`
        case "Go", "North" | "East" | "South" | "West"  as direction:
            return f"Хорошо, я пошел на {direction}!"
        case "Go", *wtv:
            return f"{wtv} - неизвестное направление."
        case _:
            return "Я не могу этого сделать..."

print(act('Go North'))