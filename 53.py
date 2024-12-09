file = open("text.txt", "r", encoding= "utf-8") #Открытие файла text.txt для чтения
print("Количество слов:",len(file.read().split())) #читаем файл, считаем количество слов в файле, разбиваем строку на слова 
file.close() #закрываем файл 