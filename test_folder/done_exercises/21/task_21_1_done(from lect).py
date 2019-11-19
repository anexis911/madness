# -*- coding: utf-8 -*-
'''
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

'''
import sys
import os
from jinja2 import Environment , FileSystemLoader
import yaml
TEMPLATE_DIR, template_file = os.path.split(sys.argv[1])
VARS_FILE = sys.argv[2]
env = Environment(loader = FileSystemLoader(TEMPLATE_DIR), trim_blocks = True, lstrip_blocks = True)
template = env.get_template(template_file)
vars_dict = yaml.load(open(VARS_FILE), Loader = yaml.FullLoader)
print(template.render(vars_dict))
