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
                comment_new = f"// {comment[1:]}\n"
                custom_lines.append(comment_new)

        elif key != None:
            if isinstance(value, dict):
                custom_lines.append(f"$[")
                for sub_key, sub_value in value.items():
                    custom_lines.append(f"  {sub_key}: {sub_value} ")
                custom_lines.append("]\n")
            else:
                custom_lines.append(f"{key.key} = {value}\n")

    return '\n'.join(custom_lines)


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
