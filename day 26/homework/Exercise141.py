# 5) შექმენით სია რომელშიც იქნება მოთავსებული რენდომ რიცხვები შემდეგ კი ამ სიიდან ამოშალეთ ყველა ლუწი რიცხვი

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for elements in num:
    if elements %2 == 0:
        num.remove(elements)
print(num)