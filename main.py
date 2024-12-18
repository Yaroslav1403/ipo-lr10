#Импортируем библиотеку для выполнения HTTP-запросов
import requests  
#Импортируем BeautifulSoup для парсинга HTML
from bs4 import BeautifulSoup  
#Импортируем модуль для работы с JSON-форматом
import json  

#Список для имен преподавателей
teaher1 = []  
#Список для должностей
post1 = []    
#Список для хранения словарей с данными о преподавателях
teacher_post = []  

#Имя файла для сохранения данных в формате JSON
json_file = "data.json"  
#Имя файла для сохранения HTML-страницы
index_file = "index.html"  
#URL-адрес страницы, с которой будем парсить данные
URL = "https://mgkct.minskedu.gov.by/о-колледже/педагогический-коллектив"

#Выполняем HTTP-запрос к указанному URL и получаем ответ
receive_information = requests.get(URL)
#Парсим HTML-код страницы с помощью BeautifulSoup
soup = BeautifulSoup(receive_information.text, 'lxml')

#Находим все элементы <h3>, содержащие имена преподавателей
teahers = soup.find_all('h3')
#Находим все элементы <li> с классом 'tss', содержащие должности
posts = soup.find_all('li', class_ = 'tss')

#Заполняем список имен преподавателей
for teaher in teahers:      
    #Добавляем текст из элемента <h3> в список
    teaher1.append(teaher.text)  

#Заполняем список должностей
for post in posts:  
    #Добавляем текст из элемента <li> в список
    post1.append(post.text)  

#Выводим информацию о преподавателях и их должностях на экран
for i in range(len(post1)):
    print(f"{1 + i} Teacher: {teaher1[i]}; Post: {post1[i].replace('Должность:', '')}") 

#Открываем файл для записи данных в формате JSON
with open(json_file, "w+", encoding='utf-8') as file:  
    for i in range(len(teaher1)):   
        #Создаем словарь с данными о преподавателе
        writer = {'Teacher': teaher1[i], 'Post': post1[i]}
        #Добавляем словарь в общий список
        teacher_post.append(writer)  
    #Сохраняем список словарей в JSON-файл
    json.dump(teacher_post, file, indent=5, ensure_ascii=False)

#Открываем файл для записи HTML-кода
with open(index_file, "w+", encoding = 'utf-8') as file:  
    file.write("<html><head><title>Преподаватели</title></head><body>\n") 
    #Записываем заголовок и ссылку на оригинальную страницу
    file.write('<h1><p align = "center"><a href = "https://mgkct.minskedu.gov.by/о-колледже/педагогический-коллектив">Преподаватели</a></p></h1>\n') 
    file.write('<body bgcolor = "#0077B6">\n') 
    #Начинаем создание таблицы с данными о преподавателях
    file.write('<table cellspacing = "3" bgcolor = "#9BE1BB" bordercolor = "#00B4D8" border = "3" align = "center">') 
    file.write("<tr>\n")
    file.write("<td>Преподаватель</td>\n<td>Post</td>") 

    #Читаем данные из JSON-файла и записываем их в HTML-таблицу
    with open(json_file, "r", encoding ='utf-8') as input:
        #Загружаем данные из JSON-файла
        teaher_list = json.load(input)  
        for i in range(len(teaher_list)): 
            #Записываем строки таблицы с данными о каждом преподавателе
            file.write(f"<tr>\n<td>{teaher_list[i]['Teacher']}</td>\n<td>{teaher_list[i]['Post'].replace('Должность:', '')}</td>")
    #Закрываем таблицу
    file.write("</table>\n")  
    #Закрываем HTML-документ
    file.write("</body></html>")  
