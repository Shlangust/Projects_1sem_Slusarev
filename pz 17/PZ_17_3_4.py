# перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему программе. Использовать функцию os.startfile().

import os
import random

# Путь к папке pz на рабочем столе в OneDrive
home_directory = os.path.join('C:\Projects_1sem_Slusarev')

# Список всех возможных папок pz* от pz1 до pz17
pz_folders = [f'pz {i}' for i in range(1, 18)]

# Выбор случайной папки из списка pz*
random_pz_folder = random.choice(pz_folders)

# Путь к случайной папке pz*
random_pz_directory = os.path.join(home_directory, random_pz_folder)

# Путь к папке report в случайной папке pz*
report_directory = os.path.join(random_pz_directory, 'report')

# Проверка существования папки report
if not os.path.exists(report_directory):
    print(f"The directory '{report_directory}' does not exist.")
    exit(1)

# Поиск PDF-файла в папке report
pdf_files = [os.path.join(report_directory, f) for f in os.listdir(report_directory) if f.endswith('.pdf')]

# Выбор случайного PDF-файла из найденных
if pdf_files:
    random_pdf_file = random.choice(pdf_files)
    try:
        os.startfile(random_pdf_file)
    except OSError as e:
        print(f"Error opening file '{random_pdf_file}': {e}")
else:
    print(f"No PDF files found in the 'report' directory of '{random_pz_folder}'.")