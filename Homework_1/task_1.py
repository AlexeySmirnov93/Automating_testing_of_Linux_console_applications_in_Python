# Задание 1.
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст. 
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае. 
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.

# Задание 2. (повышенной сложности)
# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы, 
# в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string). 
# В этом режиме должно проверяться наличие слова в выводе.


import subprocess
import string

def is_text_in_command_output(command, text, word_mode=False):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            return False

        output = result.stdout

        if word_mode:
            translator = str.maketrans('', '', string.punctuation)
            words = output.split()
            words = [word.translate(translator) for word in words]

            if text in words:
                return True
            else:
                return False
        else:
            if text in output:
                return True
            else:
                return False
    except Exception as e:
        print(f"Ошибка при выполнении команды: {e}")
        return False

command = "ls -l"
text_to_find = "file.txt"

if is_text_in_command_output(command, text_to_find):
    print(f"Текст '{text_to_find}' найден в выводе команды.")
else:
    print(f"Текст '{text_to_find}' не найден в выводе команды.")

command = "echo 'This is a sample text with punctuation.'"
word_to_find = "sample"

if is_text_in_command_output(command, word_to_find, word_mode=True):
    print(f"Слово '{word_to_find}' найдено в выводе команды.")
else:
    print(f"Слово '{word_to_find}' не найдено в выводе команды.")