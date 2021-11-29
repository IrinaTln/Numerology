dictionary={}

def main (file:str): #Вытаскиваем словарь для чтения.

    with open("info.txt") as file: 
        for line in file.readlines():     
            (key, val) = line.split(":")  #без : Питон не хочет выводить словарь
            dictionary[str(key)] = int(val)  
    print (dictionary)
    return dictionary

def get_name_number (dictionary, name:str): #Получаем число имени
    """Берем словарь, берем от пользователя имя,
       преобразуем имя в спискок, через цикл обращаемся по буквам-ключам к значениям,
       значения суммируем. Число больше 10, сначала делим на 10 без остатка, чтобы получить отдельно десятки,
       а потом делим на 10 и берем только остаток. Суммируем число имени. И так пока не придем к одному числу. 
    """
    name_list=list(name)
    print(name_list)
    name_numbers=0
    for i in name_list:
        name_numbers+=dictionary.get(i)
        
    print(name_numbers)

    amoind_sum_of_name_1=0
    amoind_sum_of_name_2=0
    last_sum=0
    c=0

    if name_numbers<10:
        print("Число имени - ", name_numbers)
    elif name_numbers>=10:
        amoind_sum_of_name_1=name_numbers%10
        amoind_sum_of_name_2=name_numbers//10
        last_sum=amoind_sum_of_name_1+amoind_sum_of_name_2
        if last_sum<10:
            print("Число вашего имени - ", last_sum)
        elif last_sum>=10:
            a=last_sum//10
            b=last_sum%10
            c=a+b
            print("Число вашего имени - ", c)

    return name_numbers, last_sum, c