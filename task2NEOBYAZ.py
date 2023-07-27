import os
os.system('cls')
import re

def parse_polynomial(polynomial_str):
    #извлекаю коэффициенты и степени многочлена
    coefficients = [int(coef) for coef in re.findall(r'-?\d+', polynomial_str)]
    degrees = [int(deg) for deg in re.findall(r'x\^(\d+)', polynomial_str)]
    
    #создаею словарь с коэффициентами по степеням
    polynomial_dict = {}
    for coef, deg in zip(coefficients, degrees):
        polynomial_dict[deg] = polynomial_dict.get(deg, 0) + coef
    
    return polynomial_dict

def add_polynomials(polynomial1, polynomial2):
    #объединяю словари многочленов и складываем коэффициенты по степеням
    result_polynomial = {}
    for deg in set(polynomial1.keys()) | set(polynomial2.keys()):
        result_polynomial[deg] = polynomial1.get(deg, 0) + polynomial2.get(deg, 0)
    
    return result_polynomial

def format_polynomial(polynomial):
    #форматирую многочлен для вывода
    terms = []
    for deg, coef in sorted(polynomial.items(), reverse=True):
        if deg == 0:
            terms.append(str(coef))
        elif deg == 1:
            terms.append(f"{coef}x")
        else:
            terms.append(f"{coef}x^{deg}")
    
    return " + ".join(terms)

def main():
    try:
        polynomial1_str = input("Введите первый многочлен: ")
        polynomial2_str = input("Введите второй многочлен: ")

        polynomial1 = parse_polynomial(polynomial1_str)
        polynomial2 = parse_polynomial(polynomial2_str)

        result_polynomial = add_polynomials(polynomial1, polynomial2)
        result_str = format_polynomial(result_polynomial)

        print("Сумма многочленов:", result_str)
        
    except ValueError:
        print("Ошибка! Неправильный формат многочлена.")

if __name__ == "__main__":
    main()
