
def sum_digits(number):#Вычисляет сумму цифр числа.

    return sum(int(digit) for digit in str(abs(number)))
#print("Введите число ")
#num = int(input())
#print(sum_digits(num))

def main():
    max_number = None  # Число с максимальной суммой цифр
    max_sum = -1  # Максимальная сумма цифр
    
    print("Введите целые числа (0 для завершения):")
    while True:
        try:
            num = int(input())
            if num == 0:
                break
            
            current_sum = sum_digits(num)
            if current_sum > max_sum:
                max_sum = current_sum
                max_number = num
                
        except ValueError:
            print("Ошибка: введите целое число.")
    
    if max_number is not None:
        print(f"Число с максимальной суммой цифр: {max_number}")
    else:
        print("Не было введено ни одного числа.")

#if __name__ == "__main__":
main()
