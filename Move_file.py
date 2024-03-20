import os, shutil

from_dir = "C:/Users/User/Downloads"
to_dir = "C:/Users/User/Downloads/P_Arquivos_Documentos"

list_of_files = os.listdir(from_dir)

for file in list_of_files:
    name, extation = os.path.splitext(file)
    print("Arquivo:",name," Extensão:",extation)