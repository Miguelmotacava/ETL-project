
#funciones

import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import selenium 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import multiprocessing
PATH=ChromeDriverManager().install(); 
opciones=Options()
driver=webdriver.Chrome(PATH, options = opciones);
driver.quit();
import multiprocess as mp
import warnings
opciones.headless=True

warnings.filterwarnings('ignore')


def data1(urls):
    
    #lee la url que queremos escrapear

    # quita la bandera de ser robot
    opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
    opciones.add_experimental_option('useAutomationExtension', False)
    opciones.headless=False
    
    driver=webdriver.Chrome(PATH, options = opciones)
    driver.get(urls)
    #html = req.get(urls).text
    #soup=bs(html, 'html.parser')
    try:
        acept = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/button[2]')
        acept.click()
    except:
        pass
    
    nombre = []
    med = []
    posi = []
    tipe = []
    precio = []
    skills = []
    weak = []
    rit = []
    disp = []
    pases = []
    dribs = []
    defes = []
    phys = []
    bases = []
    phys = []
    igss = []
    pops = []
    timess = []
    
    jogadores = driver.find_elements(By.TAG_NAME, 'tr')
    stats = [jogadores[i].text.strip() for i in range(3,len(jogadores))]
    stats_player = [] 
    for i in range(len(stats)):
        a = stats[1].find(' ')
        stats[i] = stats[i].replace('\n',' ')
        stats[i] =stats[i].replace('\\','')
        stats[i] = stats[i].replace("\'",'')
        stats_player.append(stats[i])
    st_pl = [i.split() for i in stats_player]
    
    #names
    names = driver.find_elements(By.CLASS_NAME, 'player_name_players_table.get-tp')
    names_players = [i.text for i in names]
    nombre =  names_players

    #datos num
    datos_num = []
    for i in range(len(st_pl)):
        tmp =[]
        for j in range(len(st_pl[i])):
            if st_pl[i][j].isnumeric() or st_pl[i][j].startswith('-'):
                tmp.append(st_pl[i][j])
        datos_num.append(tmp)
        
    # medias
    medias = [datos_num[i][0] for i in range(len(datos_num))]
    med =  medias
    # pos
    pos = driver.find_elements(By.CLASS_NAME, 'font-weight-bold')
    pos_player = [pos[i].text for i in range(7,len(pos)-4,2)]
    posi =  pos_player
    
    # tipo
    tipo = driver.find_elements(By.CLASS_NAME, 'mobile-hide-table-col')
    tipo_player = [tipo[i].text for i in range(1,len(tipo))]
    tipe =  tipo_player
    
    # precio
    precio = driver.find_elements(By.CLASS_NAME, 'ps4_color.font-weight-bold')
    precio_player = [i.text for i in precio]
    
    # skill
    skill = [datos_num[i][1] for i in range(len(datos_num))]
    skills =  skill
    
    # weak foot
    wf = [datos_num[i][2] for i in range(len(datos_num))]
    weak = wf
    
    # ritmo
    ritmo = [datos_num[i][3] for i in range(len(datos_num))]
    rit = ritmo
    
    # shot
    shot = [datos_num[i][4] for i in range(len(datos_num))]
    disp =  shot
    
    # pass
    pase = [datos_num[i][5] for i in range(len(datos_num))]
    pases =  pase
    
    # dribbling
    drib = [datos_num[i][6] for i in range(len(datos_num))]
    dribs =  drib

    # defense
    defense = [datos_num[i][7] for i in range(len(datos_num))] 
    defes =  defense

    # physic
    phy = [datos_num[i][8] for i in range(len(datos_num))]
    phys =  phy 

    # popularity
    pop = [datos_num[i][9] for i in range(len(datos_num))]
    pops = pop  

    # base stats
    base = [datos_num[i][10] for i in range(len(datos_num))]
    bases =  base

    # in game stats
    igs = [datos_num[i][-1] for i in range(len(datos_num))]
    igss = igs
    
    # time
    times = [time.asctime() for i in range(30)]
    timess = times
    
    
    #platarforma
    plat = [ 'play-station' for i in range(30)]
    
    
    
    driver.quit()
    
    data1 = {'name_player':nombre, 'media':med, 'posicion':posi, 'tipo':tipe, 'precio':precio_player, 'skill':skills, 'wf':weak, 'ritmo':rit, 'shot':disp, 'pas':pases, 'drib':dribs, 'def':defes, 'phy':phys, 'popularity':pops, 'base stats':bases, 'igs':igss,'plataforma': plat, 'time':timess}
    
    dt1 = pd.DataFrame(data1)
    
    return dt1

def data2(url):
    driver=webdriver.Chrome(PATH) 
    driver.get(url)
    html = req.get(url).text
    soup=bs(html, 'html.parser')
    try:
        acept = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div/div/div[5]/div[2]/a/span')
        acept.click()
    except:
        pass

    players = driver.find_elements(By.CLASS_NAME, 'col-name')
    pl = [players[i].text for i in range(2,len(players),2)]
    ts = [players[i].text.split('\n')[0] for i in range(3,len(players),2)]
    data = {'names': pl, 'equipos': ts}
    dt1 = pd.DataFrame(data)
    return dt1
