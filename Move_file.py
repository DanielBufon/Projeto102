import os 
import shutil

origem = "C:/Users/danie/Downloads/Imagens Aula 102"
destino = "C:/Users/danie/OneDrive/Área de Trabalho/Arquivos_Docuentos"

ListaDeArquivos = os.listdir(origem)

#print(ListaDeArquivos)

for FileName in ListaDeArquivos:
    name,extension = os.path.splitext(FileName)
    
    if extension == "":
        continue

    if extension in [".txt",".doc",".docx",".pdf"]:
        caminho1 = origem + "/" + FileName 
        caminho2 = destino + "/" + "Caminho"
        caminho3 = caminho2 + "/" + FileName

        if os.path.exists(caminho2):
            print ("movendo... " + FileName)
            shutil.move(caminho1,caminho3)

        else: 
            os.makedirs (caminho2)
            print ("movendo..." + FileName)
            shutil.move (caminho1,caminho3)