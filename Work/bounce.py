# bounce.py
#
# Exercise 1.5
# height = 100
# count = 1
# while count<=10:
#     height = (height *(3/5))
#     print(count,round(height,4))
#     count = count + 1

height =100
for i in range(1,11):
    height = height*(3/5)
    print(i, round(height,4))