import argparse
import re
import tomllib
from typing import Any, Dict

def toml_to_study_language(toml_text, toml_file):
    # Функция для обработки словарей
    a = 1
    def convert_dict(dict):
        items = []
        for key, value in dict.items():
            if isinstance(value, dict):
                items.append(f"{key} : ${{{convert_dict(value)}}}")
            else:
                items.append(f"{key} : {value}")
        return "$[" + ", ".join(items) + "]"

    print(convert_dict(toml_file))

    # Замена однострочных комментариев
    toml_text = re.sub(r'#(.*)', lambda m: r'//' + m.group(1), toml_text)

    #toml_text = re.sub(r'#|(.*?)|#', lambda m: '|#n' + m.group(1).strip() + 'n#|', toml_text)


    # Словарь для хранения констант
    constants = {}

    # Возвращаем преобразованный текст
    return toml_text.strip()


def evaluate_expression(expression: str, constants: Dict[str, Any]) -> Any:
    # Заменяем имена констант на их значения
    for name in constants:
        expression = expression.replace(name, constants[name])

    # Поддерживаем базовые операции: сложение и функции max(), mod()
    try:
        # Обработка max() функции
        expression = re.sub(r'max(([^)]+))', lambda m: str(max(map(int, m.group(1).split(',')))), expression)

        # Обработка mod() функции
        expression = re.sub(r'mod(([^)]+))',
                            lambda m: str(int(m.group(1).split(',')[0]) % int(m.group(1).split(',')[1])), expression)

        # Выполнение простого сложения
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка вычисления: {e}"


def main():
    parser = argparse.ArgumentParser(description='Convert TOML to custom configuration language.')
    parser.add_argument('input_file', help='Path to the input TOML file')
    parser.add_argument('output_file', help='Path to the output configuration file')

    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as infile:
            toml_content = infile.read()
        with open(args.input_file, 'rb') as f:
            toml_file = tomllib.load(f)

        transformed_content = toml_to_study_language(toml_content, toml_file)









        with open(args.output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(transformed_content)

        print(f"Conversion successful. Output written to {args.output_file}")
    except FileNotFoundError:
        print(f"Error: File {args.input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
