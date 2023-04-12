import os
import shutil

from_dir = "C:/Users/Ana Clara/Downloads"
to_dir = "C:/Users/Ana Clara/Desktop/codes/projeto111/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file in list_of_files:
    name, extension = os.path.splitext(file)
    print(name)
    print(extension)
    if extension == "":
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file
        path2 = to_dir + '/' + "Arquivos_Documentos"
        path3 = to_dir + '/' + "Arquivos_Documentos" + '/' + file
        if os.path.exists(path2):
            print("movendo " + file)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("movendo " + file)
            shutil.move(path1, path3)

