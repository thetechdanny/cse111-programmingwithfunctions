# my_list = ['a', 'b', 'c']
# for i, item in enumerate(my_list):
#     print(f"{i} - {item}")

# for char in "hello":
#     print(char)

# i = 0
# while i < 5:
#     i += 1
#     print(i)
    
# print()

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# names = ["Alice", "Bob", "Danny"]
# scores = [90, 85, 90]
# state = ["Abia", "Abuja"]
# for name, score, state in zip(names, scores, state):
#     print(name, score, state)

# import datetime

# today = datetime.datetime.today()

# today2 = datetime.datetime.now().strftime('%Y-%m-%d')

# print(today2)

city_name = "Accra"
elevation = 61
population = 42000
with open ('cities.txt', 'at') as cities_file:
    print(city_name, file = cities_file)
    print(f"{elevation}, {population}", file = cities_file)