 #1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

#Пример: Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

accepted_str = input('Введите текст: ')
wanted = input('Введите искомый текст: ')

def get_string(accepted_str: str) -> str:
    result_list = [i for i in accepted_str.split() if wanted not in i ]
    return ' '.join(result_list)

result = get_string(accepted_str)
print(f'Введенная строка: {accepted_str}')
print(f'Слова в которых нет сочетания "{wanted}": {result}')