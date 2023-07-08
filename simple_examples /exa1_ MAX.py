## Данные Ключ имя - Значение зарплата
employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}
## Однострочник ищет самую высокую
top_earners = [(k, v) for k, v in employees.items() if v >= 100000]