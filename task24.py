import os
os.system('cls')
def max_collected_berries(berries):
    n = len(berries)
    max_collected = 0

    for i in range(n):
        #вычисляю число ягод, которое можно собрать с текущего куста и соседних
        collected = berries[i] + berries[(i+1) % n] + berries[(i-1) % n]

        #обновляю максимальное число собранных ягод
        max_collected = max(max_collected, collected)

    return max_collected

#пример урожайности грядки тут количество ягод на каждом кусте
berries = [5, 7, 2, 10, 3]

result = max_collected_berries(berries)
print("Максимальное число ягод, которое можно собрать за один заход:", result)
