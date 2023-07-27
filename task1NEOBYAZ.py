import os
os.system('cls')
def decimal_to_binary(decimal: int) -> str:
    return bin(decimal)[2:]

def decimal_to_octal(decimal: int) -> str:
    return oct(decimal)[2:]

def main():
    try:
        decimal_number = int(input("Введите целое число: "))
        binary_representation = decimal_to_binary(decimal_number)
        octal_representation = decimal_to_octal(decimal_number)

        print("Двоичное представление:", binary_representation)
        print("Восьмеричное представление:", octal_representation)

        #проверка с помощью функций bin и oct
        print("Проверка с помощью функции bin:", bin(decimal_number)[2:])
        print("Проверка с помощью функции oct:", oct(decimal_number)[2:])
        
    except ValueError:
        print("Ошибка! Введите целое число.")

if __name__ == "__main__":
    main()
