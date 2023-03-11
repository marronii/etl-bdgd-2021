from glob import glob 
from os import getcwd,chdir,listdir,sep,mkdir

class Qgis_Automation:

    def __init__(self,path_default):
        #Directory Default 
        self.path_default = path_default
        self.len_path = len(path_default)
        self.path_destiny = 'C:/Users/your_directory/src/database/csv/'
        self.unidade_consumidora = ["UCAT_tab","UCMT_tab","UCBT_tab"]
        self.paths_layername = []
        self.diretory_export = ''
    
    def working_directory(self):
        chdir(self.path_default)
    
    def capture_paths(self):
        list_paths = listdir(self.path_default)
        return list_paths

    def create_path_layername(self,dist_directory,und_escolhida):

        try:    
            path_layername = getcwd() + sep + dist_directory
            path_layername = path_layername + "|layername=" + self.unidade_consumidora[und_escolhida]
            self.paths_layername.append(path_layername)   
        except:
            print(f"Erro no Criação do Path + Layername {dist_directory}")

    def create_dir(self,und_escolhida):
        new_diretory = self.unidade_consumidora[und_escolhida]
        directory = self.path_destiny  + new_diretory.lower() 
        self.diretory_export = directory
        mkdir(directory)

    def export_csv(self,path_layername,und_escolhida,ordem):

        posi_i = self.len_path
        loc = path_layername[posi_i:-15].find("_")
        posi_e = posi_i + loc

        #Qgis processing
        #Add Camada X/Y e ele vai buscar Dir e vai colar X/Y e vai exportar
        processing\
        .run("qgis:exportaddgeometrycolumns",
         {'INPUT':path_layername,'CALC_METHOD':1,'OUTPUT':f"{self.diretory_export}/{self.unidade_consumidora[und_escolhida]}_{path_layername[posi_i:posi_e],ordem}.csv"})
        
qgis_automation = Qgis_Automation('C:/Users/your_directory/src/database/gdb/2021-12-31/')
qgis_automation.working_directory()
paths_raw = qgis_automation.capture_paths()

#Escolher uma Unidade ==> Para Extração
und_escolhida = 0 #{'0':"UCAT",'1':"UCMT",'2':"UCBT"}

count_dist = 0

for dist_directory in paths_raw:
    
    try:
        qgis_automation.create_path_layername(dist_directory,und_escolhida)
        count_dist+=1
    except:
        print(f"Erro no Criação do Path + Layername {dist_directory}")
        continue

print(f"Total de Distribuidoras desse diretorio é ==> {count_dist} ")

#Criando uma pasta
qgis_automation.create_dir(und_escolhida)

ordem = 0
#Export CSV 
for path_layername in qgis_automation.paths_layername:

    try:
        qgis_automation.export_csv(path_layername,und_escolhida,ordem)
        ordem+=1
    except:
        print(f"Erro ao adicionar Vetor ou X/Y ou UC não existe\n"
              f"{path_layername}\n")

