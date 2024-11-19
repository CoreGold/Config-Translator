import os
import unittest
import tomlkit

from Translator import load_toml, convert_to_custom_format, save_custom_format  # замените 'your_module' на имя вашего модуля

class TestTomlConverter(unittest.TestCase):

    def test_load_toml(self):
        test_path = 'test_input.toml'
        test_toml = load_toml(test_path)
        self.assertEqual(type(test_toml), tomlkit.toml_document.TOMLDocument)

    def test_convert_to_custom_format(self):
        toml_data = load_toml('test_input.toml')
        with open('test_output.txt') as f:
            test_output = f.read()
        result = convert_to_custom_format(toml_data)
        self.assertEqual(result, test_output)


if __name__ == '__main__':
    unittest.main()