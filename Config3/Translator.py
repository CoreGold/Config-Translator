import tomlkit
import argparse


def load_toml(file_path):
    with open(file_path, 'r') as file:
            return tomlkit.load(file)

def convert_to_custom_format(data):
    custom_lines = []
    for key, value in data.body:
        if '#' in str(value):
            comment = str(value)
            if '#' in comment:
                comment_new = f"//{comment[1:]}\n"
                custom_lines.append(comment_new)

        if isinstance(value, int) or isinstance(value, dict) or isinstance(value, list):
            if key != None:
                if isinstance(value, list):
                    value = value.value[0].value
                if isinstance(value, dict):
                    custom_lines.append(f"$[")
                    for sub_key, sub_value in value.items():
                        if isinstance(sub_value, list):
                            deep = 2
                            custom_lines = sub_list_translator(sub_value, custom_lines, deep)
                        if isinstance(sub_value, int) and not isinstance(sub_value, bool):
                            custom_lines.append(f"  {sub_key}: {sub_value} ")
                    custom_lines.append("]\n")
                else:
                    custom_lines.append(f"{key.key} = {value}\n")
    return '\n'.join(custom_lines)

def sub_list_translator(sub_value, custom_lines, deep):
    for sub_list in sub_value:
        custom_lines.append('\n' + deep*' ' + "$[")
        for sub_sub_key, sub_sub_value in sub_list.items():
            if isinstance(sub_sub_value, list):
                sub_sub_value = sub_sub_value.value
                custom_lines = sub_list_translator(sub_sub_value, custom_lines, deep+2)
            if isinstance(sub_sub_value, int) and not isinstance(sub_sub_value, bool):
                custom_lines.append(f"    {sub_sub_key}: {sub_sub_value} ")
        custom_lines.append(deep*' ' + "]")
    return custom_lines

def save_custom_format(data, file_path):
    with open(file_path, 'w') as file:
        file.write(data)

def main(input_file, output_file):
    toml_data = load_toml(input_file)
    custom_format_data = convert_to_custom_format(toml_data)
    save_custom_format(custom_format_data, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Преобразователь TOML в учебный конфигурационный язык.')
    parser.add_argument('input_file', type=str, help='Путь к входному файлу TOML')
    parser.add_argument('output_file', type=str, help='Путь к выходному файлу для сохранения результата')
    args = parser.parse_args()

    try:
        main(args.input_file, args.output_file)
        print(f"Успешно преобразовано: {args.input_file} -> {args.output_file}")
    except Exception as e:
        print(f"Ошибка: {e}")