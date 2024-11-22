import os
import unittest
import tomlkit

from Translator import load_toml, convert_to_custom_format, save_custom_format

class TestTomlConverter(unittest.TestCase):
    def test_load_toml(self):
        test_path = 'test_input.toml'
        test_toml = load_toml(test_path)
        self.assertEqual(type(test_toml), tomlkit.toml_document.TOMLDocument)

    # Однострочные комментарии
    def test_comments(self):
        file = open('test_input.toml', 'w')
        file.write('#Hello\n')
        file.close()
        toml_data = load_toml('test_input.toml')
        result = convert_to_custom_format(toml_data)
        self.assertEqual(result, '//Hello\n')

    # Словари и вложенные словари
    def test_dict(self):
        file = open('test_input.toml', 'w')
        file.write('''
        [server] 
        host = "localhost"
        port = 8080
        ssl = 1
        [[server.users]]
            number = 20
        '''
                   )
        file.close()
        toml_data = load_toml('test_input.toml')
        result = convert_to_custom_format(toml_data)

        test_output = '$[\n  port: 8080 \n  ssl: 1 \n  $[\n    number: 20 \n  ]\n]\n'
        self.assertEqual(result, test_output)

    # Значения
    def test_keys(self):
        file = open('test_input.toml', 'w')
        file.write("Test1 = 1\nTest2 = 'string'\nTest3 = true")
        file.close()
        toml_data = load_toml('test_input.toml')
        result = convert_to_custom_format(toml_data)
        self.assertEqual(result, 'Test1 = 1\n')

    # Объявление константы на этапе трансляции и вычисление константного выражения на этапе трансляции (Max, Nod, +)
    def test_const(self):
        file = open('test_input.toml', 'w')
        file.write(''' 
        Test1 = 1\nTest2 = '?{Test1 + 5}'\nTest3 = '?{Test2 max 7}'\nTest4 = '?{Test3 mod 2}'
        ''')
        file.close()
        toml_data = load_toml('test_input.toml')
        result = convert_to_custom_format(toml_data)
        self.assertEqual(result, 'Test1 = 1\n\nTest2 = 6\n\nTest3 = 7\n\nTest4 = 1\n')

if __name__ == '__main__':
    unittest.main()