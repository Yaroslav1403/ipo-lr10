import requests  
from bs4 import BeautifulSoup 
import json  

teaher1 = []
post1 = []
teacher_post = []

json_file = "data.json"
index_file = "index.html"
URL = "https://mgkct.minskedu.gov.by/%D0%BE-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%B4%D0%B6%D0%B5/%D0%BF%D0%B5%D0%B4%D0%B0%D0%B3%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B8%D0%B2" 

receive_information = requests.get(URL) 
soup = BeautifulSoup(receive_information.text, 'lxml')
teahers = soup.find_all('h3') 
posts = soup.find_all('li', class_ = 'tss')

for teaher in teahers:      
    teaher1.append(teaher.text)  
for post in posts:  
    post1.append(post.text)

for i in range(len(post1)):
    print(f"{1 + i} Teacher: {teaher1[i]}; Post:{post1[i].replace('Должность:' , '')}") 
    
with open(json_file, "w+", encoding = 'utf-8') as file:  
    for i in range(len(teaher1)):   
        writer = {'Teacher': teaher1[i], 'Post': post1[i]}
        teacher_post.append(writer)
    json.dump(teacher_post, file, indent = 5, ensure_ascii = False)

with open(index_file, "w+" , encoding = 'utf-8') as file:  
    file.write("<html><head><title>Преподаватели</title></head><body>\n") 
    file.write('<h1><p align = "center" > <a href="https://mgkct.minskedu.gov.by/%D0%BE-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%B4%D0%B6%D0%B5/%D0%BF%D0%B5%D0%B4%D0%B0%D0%B3%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B8%D0%B2">Преподаватели</h1></a></p>\n') 
    file.write('<body bgcolor = "#0077B6">\n') 
    file.write('<table cellspacing = "3" BGCOLOR = "#9BE1BB" bordercolor = "#00B4D8"  border = "3" align = "center" ') 
    file.write("<table>\n") 
    file.write("<tr>\n")
    file.write("<td>Преподаватель</td>\n<td>Post</td>") 

    with open(json_file, "r", encoding = 'utf-8') as input:
        teaher_list =  json.load(input) 
        for i in range(len(teaher_list)): 
            file.write(f"<tr>\n<td>{teaher_list[i]['Teacher']}</td>\n<td>{teaher_list[i]['Post'].replace('Должность:' , '')}</td>")
    file.write("</table>\n") 
    file.write("</body></html>") 