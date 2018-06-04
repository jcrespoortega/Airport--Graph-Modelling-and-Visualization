import csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community
from networkx.algorithms import approximation
from networkx.readwrite import json_graph
import json


#Diccionarios ciudad:
#Son necesarios para saber el número de vuelos que conectan en nuestra ventana temporal a dos ciudades.

g_Basel = {}
g_Manchester = {}
g_Gibraltar = {}
g_GeorgeTown = {}
g_Prague = {}
g_Bucarest = {}
g_Stockholm = {}
g_Zurich = {}
g_Ginebra = {}
g_Berna = {}
g_Porto = {}
g_Lisbon = {}
g_PontaDelgada = {}
g_Dublin = {}
g_Edinburgh = {}
g_Glasgow = {}
g_London = {}
g_Birmingham = {}
g_Bristol = {}
g_Liverpool = {}
g_Lanzarote = {}
g_Leon = {}
g_Logrono = {}
g_Menorca = {}
g_Badajoz = {}
g_Asturias = {}
g_Almeria = {}
g_Alicante = {}
g_Albacete = {}
g_Madrid = {}
g_Lieja = {}
g_Amberes = {}
g_Brussels = {}
g_Copenhagen = {}
g_Sofia = {}
g_Ibiza = {}
g_Jerez = {}
g_LaGomera = {}
g_Berlin = {}
g_Baden = {}
g_Friedrichshafen = {}
g_Mannheim = {}
g_Dortmund = {}
g_Dusseldorf = {}
g_Weeze = {}
g_Frankfurt = {}
g_Rostock = {}
g_Hamburg = {}
g_Saarbrucken = {}
g_Hannover = {}
g_Greven = {}
g_Stuttgart = {}
g_Lubeck = {}
g_Buren = {}
g_Bremen = {}
g_Luneort = {}
g_Cologne = {}
g_Dresde = {}
g_Erfurt = {}
g_Leipzig = {}
g_Sylt = {}
g_Memmingen = {}
g_Munich = {}
g_Nuremberg = {}
g_Istanbul = {}
g_Fuerteventura = {}
g_ElHierro = {}
g_LaPalma = {}
g_LaCoruna = {}
g_Huesca = {}
g_Granada = {}
g_Gerona = {}
g_GranCanaria = {}
g_Cordoba = {}
g_CiudadReal = {}
g_Burgos = {}
g_Bilbao = {}
g_Barcelona = {}
g_Pamplona = {}
g_Reus = {}
g_Sabadell = {}
g_SanSebastian = {}
g_SantiagodeCompostela = {}
g_Malaga = {}
g_Melilla = {}
g_Murcia = {}
g_PalmaMallorca = {}
g_Salamanca = {}
g_Santander = {}
g_Sevilla = {}
g_Tenerife = {}
g_Valencia = {}
g_Valladolid = {}
g_Vigo = {}
g_Vitoria = {}
g_Zaragoza = {}
g_Toulouse = {}
g_Athens = {}
g_Helsinki = {}
g_Beauvais = {}
g_Biarritz = {}
g_Pau = {}
g_Montpellier = {}
g_Niza = {}
g_Marseille = {}
g_SaintEtienne = {}
g_Lyon = {}
g_Estrasburg = {}
g_Burdeos = {}
g_Paris = {}
g_Rotterdam = {}
g_Eindhoven = {}
g_Eelde = {}
g_Budapest = {}
g_Amsterdam = {}
g_Cracovia = {}
g_Riga = {}
g_Luxembourg = {}
g_Bergen = {}
g_Oslo = {}
g_Varsovia = {}
g_Faro = {}
g_Terceira = {}
g_Madeira = {}
g_Verona = {}
g_Venice = {}
g_Pisa = {}
g_Turin = {}
g_Asis = {}
g_Catania = {}
g_Palermo = {}
g_Forli = {}
g_Bologna = {}
g_Miramare = {}
g_Parma = {}
g_Naples = {}
g_Genoa = {}
g_Florence = {}
g_ReggioCalabria = {}
g_Bari = {}
g_Milan = {}
g_Montichiari = {}
g_Bergamo = {}
g_Cagliari = {}
g_Alghero = {}
g_Ancona = {}
g_Rome = {}
g_Edmonton = {}
g_Ottawa = {}
g_GrandePrairie = {}
g_Dorval = {}
g_Mirabel = {}
g_Montreal = {}
g_Terranova = {}
g_Toronto = {}
g_Vancouver = {}
g_Winnipeg = {}
g_Veracruz= {}
g_Mérida= {}
g_Tampico= {}
g_Tamaulipas= {}
g_Villahermosa= {}
g_Hermosillo= {}
g_SanLuisPotosí= {}
g_Mazatlán= {}
g_SanMigueldeCozumel= {}
g_Cancun= {}
g_Queretana= {}
g_Puebla= {}
g_Huatulco= {}
g_Oaxaca= {}
g_NuevoLeón= {}
g_PuertoVallarta= {}
g_Guadalajara = {}
g_Acapulco= {}
g_Silao= {}
g_SanPedro= {}
g_Durango= {}
g_Culiacán= {}
g_Chihuahua= {}
g_ElPaso= {}
g_TuxtlaGutiérrez= {}
g_CiudaddelCarmen= {}
g_SanJosédelCabo= {}
g_LaPaz= {}
g_Tijuana= {}
g_Mexicali= {}
g_Aguascalientes= {}
g_CiudaddeMéxico = {}
g_Birmingham = {}
g_Anchorage= {}
g_Kingman = {}
g_Maricopa = {}
g_Prescott = {}
g_Tucson = {}
g_Fresno = {}
g_LosAngeles = {}
g_LongBeach = {}
g_Oakland = {}
g_Ontario = {}
g_SantaAna = {}
g_PalmSprings = {}
g_Sacramento = {}
g_SanBernardino = {}
g_SanDiego = {}
g_Carlsbad = {}
g_SanDiego = {}
g_SanFrancisco = {}
g_SanJose = {}
g_Charlotte = {}
g_Morrisville= {}
g_ColoradoSprings = {}
g_Denver = {}
g_DaytonaBeach= {}
g_FortLauderdale= {}
g_Melbourne= {}
g_Miami= {}
g_Duval= {}
g_FortMyers= {}
g_Sanford= {}
g_Orlando= {}
g_Tampa= {}
g_WestPalmBeach= {}
g_Atlanta= {}
g_Savannah= {}
g_Honolulu= {}
g_Midway= {}
g_Chicago= {}
g_Indianápolis= {}
g_Cincinnati= {}
g_Louisville= {}
g_Lafayette = {}
g_NewOrleans= {}
g_Baltimore= {}
g_Boston= {}
g_Detroit= {}
g_Michigan= {}
g_CapitolCity= {}
g_StPaul= {}
g_KansasCity= {}
g_SanLuis= {}
g_LasVegas= {}
g_Cheektowaga= {}
g_Newark= {}
g_NewYork= {}
g_Albany= {}
g_Albuquerque= {}
g_Cleveland= {}
g_Portland= {}
g_Philadelphia= {}
g_Memphis= {}
g_Austin= {}
g_Dallas_FortWorth= {}
g_Dallas= {}
g_Laredo= {}
g_McAllen= {}
g_Houston= {}
g_SaltLakeCity= {}
g_StGeorge= {}
g_Seattle= {}
g_Dulles= {}
g_Washington= {}
g_Milwaukee= {}
g_RockSprings= {}

#Definimos a que pais pertenece cada ciudad para luego asinar la bandera en la visualizacion.

alemania = ['Berlin','Baden-Baden','Friedrichshafen','Mannheim','Stuttgart','Bremen','Luneort','Cologne','Dortmund','Dusseldorf','Weeze','Greven','Buren','Dresde','Erfurt','Leipzig','Leipzig','Frankfurt','Hamburg','Hannover','Frankfurt','Lubeck','Sylt','Memmingen','Munich','Nuremberg','Rostock','Saarbrucken']

belgica = ['Brussels','Amberes','Lieja']

bulgaria = ['Sofia']

dinamarca = ['Copenhagen']

españa = ['Madrid','Albacete','Alicante','Almeria','Asturias','Badajoz','Barcelona','Bilbao','Burgos','CiudadReal','Cordoba','ElHierro','Fuerteventura','GranCanaria','Gerona','Granada','Huesca','Ibiza','Jerez','LaCoruna','LaGomera','LaPalma','Lanzarote','Leon','Logrono','Madrid','Menorca','Malaga','Melilla','Murcia','PalmaMallorca','Pamplona','Reus','Sabadell','SanSebastian','SantiagodeCompostela','Salamanca','Santander','Sevilla','Tenerife','Tenerife','Valencia','Valladolid','Vigo','Vitoria','Zaragoza']
francia =  ['Paris','Paris','Beauvais','Biarritz','Burdeos','Pau','Estrasburg','Lyon','SaintEtienne','Marseille','Niza','Montpellier','Toulouse']

finlandia = ['Helsinki']

grecia = ['Athens']

paises_bajos=['Amsterdam','Eindhoven','Eelde','Rotterdam']

hungria = ['Budapest']

letonia = ['Riga']

luxemburgo = ['Luxembourg']

noruega =['Bergen','Oslo']

polonia =['Cracovia', 'Varsovia']

portugal =['Faro','Terceira','Madeira','Porto','Lisbon','PontaDelgada']

reino_unido =['Dublin','Edinburgh','Glasgow','London','Birmingham','Bristol','Liverpool','Manchester','Newcastle','Gibraltar','GeorgeTown']

checa = ['Prague']

rumania = ['Bucarest']

suecia = ['Stockholm']

suiza = ['Zurich','Ginebra','Berna','Basel, Switzerland/Mulhouse']

turquia = ['Istanbul']

canada = ['Edmonton ', 'Ottawa','GrandePrairie','Dorval','Mirabel','Montreal', 'Terranova','Toronto','Vancouver', 'Winnipeg']

mexico = [ 'Veracruz','Mérida','Tampico','Tamaulipas','Villahermosa','Hermosillo', 'SanLuisPotosí','Mazatlán',

'SanMigueldeCozumel','Cancun', 'Queretana','Puebla','Huatulco','Oaxaca', 'NuevoLeón', 'PuertoVallarta',

'Guadalajara ', 'Acapulco', 'Silao', 'SanPedro','Durango',  'Culiacán',

'Chihuahua',' ElPaso', 'TuxtlaGutiérrez','CiudaddelCarmen','SanJosédelCabo',

'LaPaz', 'Tijuana', 'Mexicali', 'Aguascalientes','CiudaddeMéxico']

eeuu = [  'Birmingham', 'Anchorage', 'Kingman','Maricopa', 'Prescott', 'Tucson','Fresno'
, 'LosAngeles','LongBeach', 'Oakland', 'Ontario', 'SantaAna', 'PalmSprings','Sacramento', 'SanBernardino'
, 'SanDiego','Carlsbad', 'SanDiego',
 'SanFrancisco', 'SanJose', 'Charlotte', 'Morrisville ',
 'ColoradoSprings', 'Denver', 'DaytonaBeach','FortLauderdale','Melbourne', 'Miami','Duval', 'FortMyers'
,'Sanford', 'Orlando', 'Tampa', 'WestPalmBeach', 'Atlanta',
'Savannah', 'Honolulu','Midway','Chicago', 'Indianápolis','Cincinnati',
'Louisville', 'Lafayette','NewOrleans','Baltimore','Boston','Detroit', 'Michigan',
'CapitolCity','StPaul','KansasCity','SanLuis','LasVegas','Cheektowaga','Newark','NewYork',
'NewYork', 'Albany','Albuquerque','Cleveland', 'Portland','Philadelphia', 'Memphis','Austin',
'Dallas-FortWorth', 'Dallas', 'Laredo', 'McAllen', 'Houston','SaltLakeCity','StGeorge', 'Seattle',
'Dulles','Washington','Milwaukee','RockSprings']


bandera_espana = 'https://vignette.wikia.nocookie.net/es.harrypotter/images/6/6e/Bandera-Espa%C3%B1a-1024x768.jpg/revision/latest?cb=20140909153532'
bandera_italia = 'http://www.banderas-mundo.es/data/flags/normal/it.png'
bandera_francia = 'http://www.banderas-mundo.es/data/flags/big/fr.png'
bandera_alemania = 'http://www.banderas-mundo.es/data/flags/big/de.png'
bandera_suecia = 'http://www.banderas-mundo.es/data/flags/big/se.png'
bandera_suiza = 'http://www.banderas-mundo.es/data/flags/big/ch.png'
bandera_portugal = 'http://www.banderas-mundo.es/data/flags/big/pt.png'
bandera_reino = 'http://flags.fmcdn.net/data/flags/w580/gb.png'
bandera_hungria = 'http://www.banderas-mundo.es/data/flags/big/hu.png'
bandera_rumania = 'http://www.banderas-mundo.es/data/flags/big/ro.png'
bandera_luxemburgo= 'http://www.banderas-mundo.es/data/flags/big/lu.png'
bandera_letonia = 'http://www.banderas-mundo.es/data/flags/big/lv.png'
bandera_paises_bajos='http://www.banderas-mundo.es/data/flags/big/nl.png'
bandera_grecia = 'http://www.banderas-mundo.es/data/flags/big/gr.png'
bandera_finlandia ='http://www.banderas-mundo.es/data/flags/big/fi.png'
bandera_noruega = 'http://www.banderas-mundo.es/data/flags/big/no.png'
bandera_polonia = 'http://www.banderas-mundo.es/data/flags/big/pl.png'
bandera_turquia = 'http://www.banderas-mundo.es/data/flags/big/tr.png'
bandera_dinamarca = 'http://www.banderas-mundo.es/data/flags/big/dk.png'
bandera_belgica = 'http://www.banderas-mundo.es/data/flags/big/be.png'
bandera_chequia = 'http://www.banderas-mundo.es/data/flags/big/cz.png'
bandera_bulgaria = 'http://www.banderas-mundo.es/data/flags/big/bg.png'
bandera_canada = 'http://www.banderas-mundo.es/data/flags/big/ca.png'

bandera_mexico = 'http://www.banderas-mundo.es/data/flags/big/mx.png'

bandera_eeuu = 'http://www.banderas-mundo.es/data/flags/big/us.png'


america =  []
edges =[]
nodes = []
comprobacion = []
europa = []

#Definimos los nodos

with open('europa_final_1.csv', 'r') as data:
    spamreader = csv.reader(data)


    for row in spamreader:

        try:

            if row[1] == 'salida':

                m = (row[3].replace('\n', '').replace(' ', ''))
                place = m[5:]

                if row[0] == 'Berlin':
                    if not place in g_Berlin and place != 'no':
                        g_Berlin[place] = 1
                    else:
                        g_Berlin[place] += 1

                if row[0] == 'Baden-Baden':
                    if not place in g_Baden and place != 'no':
                        g_Baden[place] = 1
                    else:
                        g_Baden[place] += 1

                if row[0] == 'Friedrichshafen':
                    if not place in g_Friedrichshafen and place != 'no':
                        g_Friedrichshafen[place] = 1
                    else:
                        g_Friedrichshafen[place] += 1

                if row[0] == 'Mannheim':
                    if not place in g_Mannheim and place != 'no':
                        g_Mannheim[place] = 1
                    else:
                        g_Mannheim[place] += 1

                if row[0] == 'Dortmund':
                    if not place in g_Dortmund and place != 'no':
                        g_Dortmund[place] = 1
                    else:
                        g_Dortmund[place] += 1

                if row[0] == 'Dusseldorf':
                    if not place in g_Dusseldorf and place != 'no':
                        g_Dusseldorf[place] = 1
                    else:
                        g_Dusseldorf[place] += 1

                if row[0] == 'Weeze':
                    if not place in g_Weeze and place != 'no':
                        g_Weeze[place] = 1
                    else:
                        g_Weeze[place] += 1

                if row[0] == 'Frankfurt':
                    if not place in g_Frankfurt and place != 'no':
                        g_Frankfurt[place] = 1
                    else:
                        g_Frankfurt[place] += 1

                if row[0] == 'Rostock':
                    if not place in g_Rostock and place != 'no':
                        g_Rostock[place] = 1
                    else:
                        g_Rostock[place] += 1

                if row[0] == 'Hamburg':
                    if not place in g_Hamburg and place != 'no':
                        g_Hamburg[place] = 1
                    else:
                        g_Hamburg[place] += 1

                if row[0] == 'Greven':
                    if not place in g_Greven and place != 'no':
                        g_Greven[place] = 1
                    else:
                        g_Greven[place] += 1

                if row[0] == 'Stuttgart':
                    if not place in g_Stuttgart and place != 'no':
                        g_Stuttgart[place] = 1
                    else:
                        g_Stuttgart[place] += 1

                if row[0] == 'Lubeck':
                    if not place in g_Lubeck and place != 'no':
                        g_Lubeck[place] = 1
                    else:
                        g_Lubeck[place] += 1

                if row[0] == 'Buren':
                    if not place in g_Buren and place != 'no':
                        g_Buren[place] = 1
                    else:
                        g_Buren[place] += 1

                if row[0] == 'Bremen':
                    if not place in g_Bremen and place != 'no':
                        g_Bremen[place] = 1
                    else:
                        g_Bremen[place] += 1

                if row[0] == 'Luneort':
                    if not place in g_Luneort and place != 'no':
                        g_Luneort[place] = 1
                    else:
                        g_Luneort[place] += 1

                if row[0] == 'Cologne':
                    if not place in g_Cologne and place != 'no':
                        g_Cologne[place] = 1
                    else:
                        g_Cologne[place] += 1

                if row[0] == 'Dresde':
                    if not place in g_Dresde and place != 'no':
                        g_Dresde[place] = 1
                    else:
                        g_Dresde[place] += 1

                if row[0] == 'Leipzig':
                    if not place in g_Leipzig and place != 'no':
                        g_Leipzig[place] = 1
                    else:
                        g_Leipzig[place] += 1

                if row[0] == 'Erfurt':
                    if not place in g_Erfurt and place != 'no':
                        g_Erfurt[place] = 1
                    else:
                        g_Erfurt[place] += 1

                if row[0] == 'Memmingen':
                    if not place in g_Memmingen and place != 'no':
                        g_Memmingen[place] = 1
                    else:
                        g_Memmingen[place] += 1

                if row[0] == 'Sylt':
                    if not place in g_Sylt and place != 'no':
                        g_Sylt[place] = 1
                    else:
                        g_Sylt[place] += 1

                if row[0] == 'Munich':
                    if not place in g_Munich and place != 'no':
                        g_Munich[place] = 1
                    else:
                        g_Munich[place] += 1

                if row[0] == 'Nuremberg':
                    if not place in g_Nuremberg and place != 'no':
                        g_Nuremberg[place] = 1
                    else:
                        g_Nuremberg[place] += 1

                if row[0] == 'Istanbul':

                    if not place in g_Istanbul and place != 'no':
                        g_Istanbul[place] = 1
                    else:
                        g_Istanbul[place] += 1

                if row[0] == 'Lieja':
                    if not place in g_Lieja and place != 'no':
                        g_Lieja[place] = 1
                    else:
                        g_Lieja[place] += 1

                if row[0] == 'Amberes':
                    if not place in g_Amberes and place != 'no':
                        g_Amberes[place] = 1
                    else:
                        g_Amberes[place] += 1

                if row[0] == 'Brussels':
                    if not place in g_Brussels and place != 'no':
                        g_Brussels[place] = 1
                    else:
                        g_Brussels[place] += 1

                if row[0] == 'Sofia':
                    if not place in g_Sofia and place != 'no':
                        g_Sofia[place] = 1
                    else:
                        g_Sofia[place] += 1

                if row[0] == 'Copenhagen':
                    if not place in g_Copenhagen and place != 'no':
                        g_Copenhagen[place] = 1
                    else:
                        g_Copenhagen[place] += 1

                if row[0] == 'Ibiza':
                    if not place in g_Ibiza and place != 'no':
                        g_Ibiza[place] = 1
                    else:
                        g_Ibiza[place] += 1

                if row[0] == 'Jerez':
                    if not place in g_Jerez and place != 'no':
                        g_Jerez[place] = 1
                    else:
                        g_Jerez[place] += 1

                if row[0] == 'LaGomera':
                    if not place in g_LaGomera and place != 'no':
                        g_LaGomera[place] = 1
                    else:
                        g_LaGomera[place] += 1

                if row[0] == 'LaPalma':
                    if not place in g_LaPalma and place != 'no':
                        g_LaPalma[place] = 1
                    else:
                        g_LaPalma[place] += 1

                if row[0] == 'LaCoruna':
                    if not place in g_LaCoruna and place != 'no':
                        g_LaCoruna[place] = 1
                    else:
                        g_LaCoruna[place] += 1

                if row[0] == 'Huesca':
                    if not place in g_Huesca and place != 'no':
                        g_Huesca[place] = 1
                    else:
                        g_Huesca[place] += 1

                if row[0] == 'Granada':
                    if not place in g_Granada and place != 'no':
                        g_Granada[place] = 1
                    else:
                        g_Granada[place] += 1

                if row[0] == 'Gerona':
                    if not place in g_Gerona and place != 'no':
                        g_Gerona[place] = 1
                    else:
                        g_Gerona[place] += 1

                if row[0] == 'GranCanaria':
                    if not place in g_GranCanaria and place != 'no':
                        g_GranCanaria[place] = 1
                    else:
                        g_GranCanaria[place] += 1

                if row[0] == 'Fuerteventura':
                    if not place in g_Fuerteventura and place != 'no':
                        g_Fuerteventura[place] = 1
                    else:
                        g_Fuerteventura[place] += 1

                if row[0] == 'ElHierro':
                    if not place in g_ElHierro and place != 'no':
                        g_ElHierro[place] = 1
                    else:
                        g_ElHierro[place] += 1

                if row[0] == 'Cordoba':
                    if not place in g_Cordoba and place != 'no':
                        g_Cordoba[place] = 1
                    else:
                        g_Cordoba[place] += 1

                if row[0] == 'CiudadReal':
                    if not place in g_CiudadReal and place != 'no':
                        g_CiudadReal[place] = 1
                    else:
                        g_CiudadReal[place] += 1

                if row[0] == 'Burgos':
                    if not place in g_Burgos and place != 'no':
                        g_Burgos[place] = 1
                    else:
                        g_Burgos[place] += 1

                if row[0] == 'Bilbao':
                    if not place in g_Bilbao and place != 'no':
                        g_Bilbao[place] = 1
                    else:
                        g_Bilbao[place] += 1

                if row[0] == 'Barcelona':
                    if not place in g_Barcelona and place != 'no':
                        g_Barcelona[place] = 1
                    else:
                        g_Barcelona[place] += 1

                if row[0] == 'Badajoz':
                    if not place in g_Badajoz and place != 'no':
                        g_Badajoz[place] = 1
                    else:
                        g_Badajoz[place] += 1

                if row[0] == 'Asturias':
                    if not place in g_Asturias and place != 'no':
                        g_Asturias[place] = 1
                    else:
                        g_Asturias[place] += 1

                if row[0] == 'Almeria':
                    if not place in g_Almeria and place != 'no':
                        g_Almeria[place] = 1
                    else:
                        g_Almeria[place] += 1

                if row[0] == 'Alicante':
                    if not place in g_Alicante and place != 'no':
                        g_Alicante[place] = 1
                    else:
                        g_Alicante[place] += 1

                if row[0] == 'Albacete':
                    if not place in g_Albacete and place != 'no':
                        g_Albacete[place] = 1
                    else:
                        g_Albacete[place] += 1

                if row[0] == 'Madrid':
                    if not place in g_Madrid and place != 'no':
                        g_Madrid[place] = 1
                    else:
                        g_Madrid[place] += 1

                if row[0] == 'Lanzarote':
                    if not place in g_Lanzarote and place != 'no':
                        g_Lanzarote[place] = 1
                    else:
                        g_Lanzarote[place] += 1

                if row[0] == 'Leon':
                    if not place in g_Leon and place != 'no':
                        g_Leon[place] = 1
                    else:
                        g_Leon[place] += 1

                if row[0] == 'Logrono':
                    if not place in g_Logrono and place != 'no':
                        g_Logrono[place] = 1
                    else:
                        g_Logrono[place] += 1

                if row[0] == 'Menorca':
                    if not place in g_Menorca and place != 'no':
                        g_Menorca[place] = 1
                    else:
                        g_Menorca[place] += 1

                if row[0] == 'Malaga':
                    if not place in g_Malaga and place != 'no':
                        g_Malaga[place] = 1
                    else:
                        g_Malaga[place] += 1

                if row[0] == 'Melilla':
                    if not place in g_Melilla and place != 'no':
                        g_Melilla[place] = 1
                    else:
                        g_Melilla[place] += 1

                if row[0] == 'Murcia':
                    if not place in g_Murcia and place != 'no':
                        g_Murcia[place] = 1
                    else:
                        g_Murcia[place] += 1

                if row[0] == 'PalmaMallorca':
                    if not place in g_PalmaMallorca and place != 'no':
                        g_PalmaMallorca[place] = 1
                    else:
                        g_PalmaMallorca[place] += 1

                if row[0] == 'Pamplona':
                    if not place in g_Pamplona and place != 'no':
                        g_Pamplona[place] = 1
                    else:
                        g_Pamplona[place] += 1

                if row[0] == 'Reus':
                    if not place in g_Reus and place != 'no':
                        g_Reus[place] = 1
                    else:
                        g_Reus[place] += 1

                if row[0] == 'Sabadell':
                    if not place in g_Sabadell and place != 'no':
                        g_Sabadell[place] = 1
                    else:
                        g_Sabadell[place] += 1

                if row[0] == 'SanSebastian':
                    if not place in g_SanSebastian and place != 'no':
                        g_SanSebastian[place] = 1
                    else:
                        g_SanSebastian[place] += 1

                if row[0] == 'SantiagodeCompostela':
                    if not place in g_SantiagodeCompostela and place != 'no':
                        g_SantiagodeCompostela[place] = 1
                    else:
                        g_SantiagodeCompostela[place] += 1

                if row[0] == 'Salamanca':
                    if not place in g_Salamanca and place != 'no':
                        g_Salamanca[place] = 1
                    else:
                        g_Salamanca[place] += 1

                if row[0] == 'Santander':
                    if not place in g_Santander and place != 'no':
                        g_Santander[place] = 1
                    else:
                        g_Santander[place] += 1

                if row[0] == 'Sevilla':
                    if not place in g_Sevilla and place != 'no':
                        g_Sevilla[place] = 1
                    else:
                        g_Sevilla[place] += 1

                if row[0] == 'Tenerife':
                    if not place in g_Tenerife and place != 'no':
                        g_Tenerife[place] = 1
                    else:
                        g_Tenerife[place] += 1

                if row[0] == 'Valencia':
                    if not place in g_Valencia and place != 'no':
                        g_Valencia[place] = 1
                    else:
                        g_Valencia[place] += 1

                if row[0] == 'Valladolid':
                    if not place in g_Valladolid and place != 'no':
                        g_Valladolid[place] = 1
                    else:
                        g_Valladolid[place] += 1

                if row[0] == 'Vigo':
                    if not place in g_Vigo and place != 'no':
                        g_Vigo[place] = 1
                    else:
                        g_Vigo[place] += 1

                if row[0] == 'Vitoria':
                    if not place in g_Vitoria and place != 'no':
                        g_Vitoria[place] = 1
                    else:
                        g_Vitoria[place] += 1

                if row[0] == 'Zaragoza':
                    if not place in g_Zaragoza and place != 'no':
                        g_Zaragoza[place] = 1
                    else:
                        g_Zaragoza[place] += 1

                if row[0] == 'Toulouse':
                    if not place in g_Toulouse and place != 'no':
                        g_Toulouse[place] = 1
                    else:
                        g_Toulouse[place] += 1

                if row[0] == 'Montpellier':
                    if not place in g_Montpellier and place != 'no':
                        g_Montpellier[place] = 1
                    else:
                        g_Montpellier[place] += 1

                if row[0] == 'Niza':
                    if not place in g_Niza and place != 'no':
                        g_Niza[place] = 1
                    else:
                        g_Niza[place] += 1

                if row[0] == 'Marseille':
                    if not place in g_Marseille and place != 'no':
                        g_Marseille[place] = 1
                    else:
                        g_Marseille[place] += 1

                if row[0] == 'SaintEtienne':
                    if not place in g_SaintEtienne and place != 'no':
                        g_SaintEtienne[place] = 1
                    else:
                        g_SaintEtienne[place] += 1

                if row[0] == 'Lyon':
                    if not place in g_Lyon and place != 'no':
                        g_Lyon[place] = 1
                    else:
                        g_Lyon[place] += 1

                if row[0] == 'Estrasburg':
                    if not place in g_Estrasburg and place != 'no':
                        g_Estrasburg[place] = 1
                    else:
                        g_Estrasburg[place] += 1

                if row[0] == 'Pau':
                    if not place in g_Pau and place != 'no':
                        g_Pau[place] = 1
                    else:
                        g_Pau[place] += 1

                if row[0] == 'Burdeos':
                    if not place in g_Burdeos and place != 'no':
                        g_Burdeos[place] = 1
                    else:
                        g_Burdeos[place] += 1

                if row[0] == 'Biarritz':
                    if not place in g_Biarritz and place != 'no':
                        g_Biarritz[place] = 1
                    else:
                        g_Biarritz[place] += 1

                if row[0] == 'Beauvais':
                    if not place in g_Beauvais and place != 'no':
                        g_Beauvais[place] = 1
                    else:
                        g_Beauvais[place] += 1

                if row[0] == 'Paris':
                    if not place in g_Paris and place != 'no':
                        g_Paris[place] = 1
                    else:
                        g_Paris[place] += 1

                if row[0] == 'Helsinki':
                    if not place in g_Helsinki and place != 'no':
                        g_Helsinki[place] = 1
                    else:
                        g_Helsinki[place] += 1

                if row[0] == 'Athens':
                    if not place in g_Athens and place != 'no':
                        g_Athens[place] = 1
                    else:
                        g_Athens[place] += 1

                if row[0] == 'Rotterdam':
                    if not place in g_Rotterdam and place != 'no':
                        g_Rotterdam[place] = 1
                    else:
                        g_Rotterdam[place] += 1

                if row[0] == 'Eelde':
                    if not place in g_Eelde and place != 'no':
                        g_Eelde[place] = 1
                    else:
                        g_Eelde[place] += 1

                if row[0] == 'Eindhoven':
                    if not place in g_Eindhoven and place != 'no':
                        g_Eindhoven[place] = 1
                    else:
                        g_Eindhoven[place] += 1

                if row[0] == 'Amsterdam':
                    if not place in g_Amsterdam and place != 'no':
                        g_Amsterdam[place] = 1
                    else:
                        g_Amsterdam[place] += 1

                if row[0] == 'Budapest':
                    if not place in g_Budapest and place != 'no':
                        g_Budapest[place] = 1
                    else:
                        g_Budapest[place] += 1

                if row[0] == 'Riga':
                    if not place in g_Riga and place != 'no':
                        g_Riga[place] = 1
                    else:
                        g_Riga[place] += 1

                if row[0] == 'Luxembourg':
                    if not place in g_Luxembourg and place != 'no':
                        g_Luxembourg[place] = 1
                    else:
                        g_Luxembourg[place] += 1

                if row[0] == 'Bergen':
                    if not place in g_Bergen and place != 'no':
                        g_Bergen[place] = 1
                    else:
                        g_Bergen[place] += 1

                if row[0] == 'Oslo':
                    if not place in g_Oslo and place != 'no':
                        g_Oslo[place] = 1
                    else:
                        g_Oslo[place] += 1

                if row[0] == 'Varsovia':
                    if not place in g_Varsovia and place != 'no':
                        g_Varsovia[place] = 1
                    else:
                        g_Varsovia[place] += 1

                if row[0] == 'Cracovia':
                    if not place in g_Cracovia and place != 'no':
                        g_Cracovia[place] = 1
                    else:
                        g_Cracovia[place] += 1

                if row[0] == 'Faro':
                    if not place in g_Faro and place != 'no':
                        g_Faro[place] = 1
                    else:
                        g_Faro[place] += 1

                if row[0] == 'Terceira':
                    if not place in g_Terceira and place != 'no':
                        g_Terceira[place] = 1
                    else:
                        g_Terceira[place] += 1

                if row[0] == 'g_Madeira':
                    if not place in g_Madeira and place != 'no':
                        g_Madeira[place] = 1
                    else:
                        g_Madeira[place] += 1

                if row[0] == 'Porto':
                    if not place in g_Porto and place != 'no':
                        g_Porto[place] = 1
                    else:
                        g_Porto[place] += 1

                if row[0] == 'Lisbon':
                    if not place in g_Lisbon and place != 'no':
                        g_Lisbon[place] = 1
                    else:
                        g_Lisbon[place] += 1

                if row[0] == 'PontaDelgada':
                    if not place in g_PontaDelgada and place != 'no':
                        g_PontaDelgada[place] = 1
                    else:
                        g_PontaDelgada[place] += 1

                if row[0] == 'Dublin':
                    if not place in g_Dublin and place != 'no':
                        g_Dublin[place] = 1
                    else:
                        g_Dublin[place] += 1

                if row[0] == 'Edinburgh':
                    if not place in g_Edinburgh and place != 'no':
                        g_Edinburgh[place] = 1
                    else:
                        g_Edinburgh[place] += 1

                if row[0] == 'Glasgow':
                    if not place in g_Glasgow and place != 'no':
                        g_Glasgow[place] = 1
                    else:
                        g_Glasgow[place] += 1

                if row[0] == 'London':
                    if not place in g_London and place != 'no':
                        g_London[place] = 1
                    else:
                        g_London[place] += 1

                if row[0] == 'Birmingham':
                    if not place in g_Birmingham and place != 'no':
                        g_Birmingham[place] = 1
                    else:
                        g_Birmingham[place] += 1

                if row[0] == 'Bristol':
                    if not place in g_Bristol and place != 'no':
                        g_Bristol[place] = 1
                    else:
                        g_Bristol[place] += 1

                if row[0] == 'Liverpool':
                    if not place in g_Liverpool and place != 'no':
                        g_Liverpool[place] = 1
                    else:
                        g_Liverpool[place] += 1

                if row[0] == 'Manchester':
                    if not place in g_Manchester and place != 'no':
                        g_Manchester[place] = 1
                    else:
                        g_Manchester[place] += 1

                if row[0] == 'Gibraltar':
                    if not place in g_Gibraltar and place != 'no':
                        g_Gibraltar[place] = 1
                    else:
                        g_Gibraltar[place] += 1

                if row[0] == 'GeorgeTown':
                    if not place in g_GeorgeTown and place != 'no':
                        g_GeorgeTown[place] = 1
                    else:
                        g_GeorgeTown[place] += 1

                if row[0] == 'Prague':
                    if not place in g_Prague and place != 'no':
                        g_Prague[place] = 1
                    else:
                        g_Prague[place] += 1

                if row[0] == 'Bucarest':
                    if not place in g_Bucarest and place != 'no':
                        g_Bucarest[place] = 1
                    else:
                        g_Bucarest[place] += 1

                if row[0] == 'Stockholm':
                    if not place in g_Stockholm and place != 'no':
                        g_Stockholm[place] = 1
                    else:
                        g_Stockholm[place] += 1

                if row[0] == 'Zurich':
                    if not place in g_Zurich and place != 'no':
                        g_Zurich[place] = 1
                    else:
                        g_Zurich[place] += 1

                if row[0] == 'Ginebra':
                    if not place in g_Ginebra and place != 'no':
                        g_Ginebra[place] = 1
                    else:
                        g_Ginebra[place] += 1

                if row[0] == 'Berna':
                    if not place in g_Berna and place != 'no':
                        g_Berna[place] = 1
                    else:
                        g_Berna[place] += 1

                if row[0] == 'Basel':
                    if not place in g_Basel and place != 'no':
                        g_Basel[place] = 1
                    else:
                        g_Basel[place] += 1

                if row[0] == 'Verona':
                    if not place in g_Verona and place != 'no':
                        g_Verona[place] = 1
                    else:
                        g_Verona[place] += 1

                if row[0] == 'Venice':
                    if not place in g_Venice and place != 'no':
                        g_Venice[place] = 1
                    else:
                        g_Venice[place] += 1

                if row[0] == 'Pisa':
                    if not place in g_Pisa and place != 'no':
                        g_Pisa[place] = 1
                    else:
                        g_Pisa[place] += 1

                if row[0] == 'Turin':
                    if not place in g_Turin and place != 'no':
                        g_Turin[place] = 1
                    else:
                        g_Turin[place] += 1

                if row[0] == 'Asis':
                    if not place in g_Asis and place != 'no':
                        g_Asis[place] = 1
                    else:
                        g_Asis[place] += 1

                if row[0] == 'Catania':
                    if not place in g_Catania and place != 'no':
                        g_Catania[place] = 1
                    else:
                        g_Catania[place] += 1

                if row[0] == 'Palermo':
                    if not place in g_Palermo and place != 'no':
                        g_Palermo[place] = 1
                    else:
                        g_Palermo[place] += 1

                if row[0] == 'Forli':
                    if not place in g_Forli and place != 'no':
                        g_Forli[place] = 1
                    else:
                        g_Forli[place] += 1

                if row[0] == 'Bologna':
                    if not place in g_Bologna and place != 'no':
                        g_Bologna[place] = 1
                    else:
                        g_Bologna[place] += 1

                if row[0] == 'Miramare':
                    if not place in g_Miramare and place != 'no':
                        g_Miramare[place] = 1
                    else:
                        g_Miramare[place] += 1

                if row[0] == 'Parma':
                    if not place in g_Parma and place != 'no':
                        g_Parma[place] = 1
                    else:
                        g_Parma[place] += 1

                if row[0] == 'Naples':
                    if not place in g_Naples and place != 'no':
                        g_Naples[place] = 1
                    else:
                        g_Naples[place] += 1

                if row[0] == 'Genoa':
                    if not place in g_Genoa and place != 'no':
                        g_Genoa[place] = 1
                    else:
                        g_Genoa[place] += 1

                if row[0] == 'Florence':
                    if not place in g_Florence and place != 'no':
                        g_Florence[place] = 1
                    else:
                        g_Florence[place] += 1

                if row[0] == 'ReggioCalabria':
                    if not place in g_ReggioCalabria and place != 'no':
                        g_ReggioCalabria[place] = 1
                    else:
                        g_ReggioCalabria[place] += 1

                if row[0] == 'Bari':
                    if not place in g_Bari and place != 'no':
                        g_Bari[place] = 1
                    else:
                        g_Bari[place] += 1

                if row[0] == 'Milan':
                    if not place in g_Milan and place != 'no':
                        g_Milan[place] = 1
                    else:
                        g_Milan[place] += 1

                if row[0] == 'Montichiari':
                    if not place in g_Montichiari and place != 'no':
                        g_Montichiari[place] = 1
                    else:
                        g_Montichiari[place] += 1

                if row[0] == 'Bergamo':
                    if not place in g_Bergamo and place != 'no':
                        g_Bergamo[place] = 1
                    else:
                        g_Bergamo[place] += 1

                if row[0] == 'Cagliari':
                    if not place in g_Cagliari and place != 'no':
                        g_Cagliari[place] = 1
                    else:
                        g_Cagliari[place] += 1

                if row[0] == 'Alghero':
                    if not place in g_Alghero and place != 'no':
                        g_Alghero[place] = 1
                    else:
                        g_Alghero[place] += 1

                if row[0] == 'Ancona':
                    if not place in g_Ancona and place != 'no':
                        g_Ancona[place] = 1
                    else:
                        g_Ancona[place] += 1

                if row[0] == 'Rome':
                    if not place in g_Rome and place != 'no':
                        g_Rome[place] = 1
                    else:
                        g_Rome[place] += 1

        except:
            pass

with open('final_italia1.csv', 'r') as data:
    spamreader = csv.reader(data)


    for row in spamreader:

        try:

            if row[1] == 'salida':

                m = (row[3].replace('\n', '').replace(' ', ''))
                place = m[5:]


                if row[0] == 'Berlin':
                    if not place in g_Berlin and place != 'no':
                        g_Berlin[place] = 1
                    else:
                        g_Berlin[place] += 1

                if row[0] == 'Baden-Baden':
                    if not place in g_Baden and place != 'no':
                        g_Baden[place] = 1
                    else:
                        g_Baden[place] += 1

                if row[0] == 'Friedrichshafen':
                    if not place in g_Friedrichshafen and place != 'no':
                        g_Friedrichshafen[place] = 1
                    else:
                        g_Friedrichshafen[place] += 1

                if row[0] == 'Mannheim':
                    if not place in g_Mannheim and place != 'no':
                        g_Mannheim[place] = 1
                    else:
                        g_Mannheim[place] += 1

                if row[0] == 'Dortmund':
                    if not place in g_Dortmund and place != 'no':
                        g_Dortmund[place] = 1
                    else:
                        g_Dortmund[place] += 1

                if row[0] == 'Dusseldorf':
                    if not place in g_Dusseldorf and place != 'no':
                        g_Dusseldorf[place] = 1
                    else:
                        g_Dusseldorf[place] += 1

                if row[0] == 'Weeze':
                    if not place in g_Weeze and place != 'no':
                        g_Weeze[place] = 1
                    else:
                        g_Weeze[place] += 1

                if row[0] == 'Frankfurt':
                    if not place in g_Frankfurt and place != 'no':
                        g_Frankfurt[place] = 1
                    else:
                        g_Frankfurt[place] += 1

                if row[0] == 'Rostock':
                    if not place in g_Rostock and place != 'no':
                        g_Rostock[place] = 1
                    else:
                        g_Rostock[place] += 1

                if row[0] == 'Hamburg':
                    if not place in g_Hamburg and place != 'no':
                        g_Hamburg[place] = 1
                    else:
                        g_Hamburg[place] += 1

                if row[0] == 'Greven':
                    if not place in g_Greven and place != 'no':
                        g_Greven[place] = 1
                    else:
                        g_Greven[place] += 1

                if row[0] == 'Stuttgart':
                    if not place in g_Stuttgart and place != 'no':
                        g_Stuttgart[place] = 1
                    else:
                        g_Stuttgart[place] += 1

                if row[0] == 'Lubeck':
                    if not place in g_Lubeck and place != 'no':
                        g_Lubeck[place] = 1
                    else:
                        g_Lubeck[place] += 1

                if row[0] == 'Buren':
                    if not place in g_Buren and place != 'no':
                        g_Buren[place] = 1
                    else:
                        g_Buren[place] += 1

                if row[0] == 'Bremen':
                    if not place in g_Bremen and place != 'no':
                        g_Bremen[place] = 1
                    else:
                        g_Bremen[place] += 1

                if row[0] == 'Luneort':
                    if not place in g_Luneort and place != 'no':
                        g_Luneort[place] = 1
                    else:
                        g_Luneort[place] += 1

                if row[0] == 'Cologne':
                    if not place in g_Cologne and place != 'no':
                        g_Cologne[place] = 1
                    else:
                        g_Cologne[place] += 1

                if row[0] == 'Dresde':
                    if not place in g_Dresde and place != 'no':
                        g_Dresde[place] = 1
                    else:
                        g_Dresde[place] += 1

                if row[0] == 'Leipzig':
                    if not place in g_Leipzig and place != 'no':
                        g_Leipzig[place] = 1
                    else:
                        g_Leipzig[place] += 1

                if row[0] == 'Erfurt':
                    if not place in g_Erfurt and place != 'no':
                        g_Erfurt[place] = 1
                    else:
                        g_Erfurt[place] += 1

                if row[0] == 'Memmingen':
                    if not place in g_Memmingen and place != 'no':
                        g_Memmingen[place] = 1
                    else:
                        g_Memmingen[place] += 1

                if row[0] == 'Sylt':
                    if not place in g_Sylt and place != 'no':
                        g_Sylt[place] = 1
                    else:
                        g_Sylt[place] += 1

                if row[0] == 'Munich':
                    if not place in g_Munich and place != 'no':
                        g_Munich[place] = 1
                    else:
                        g_Munich[place] += 1

                if row[0] == 'Nuremberg':
                    if not place in g_Nuremberg and place != 'no':
                        g_Nuremberg[place] = 1
                    else:
                        g_Nuremberg[place] += 1

                if row[0] == 'Istanbul':

                    if not place in g_Istanbul and place != 'no':
                        g_Istanbul[place] = 1
                    else:
                        g_Istanbul[place] += 1

                if row[0] == 'Lieja':
                    if not place in g_Lieja and place != 'no':
                        g_Lieja[place] = 1
                    else:
                        g_Lieja[place] += 1

                if row[0] == 'Amberes':
                    if not place in g_Amberes and place != 'no':
                        g_Amberes[place] = 1
                    else:
                        g_Amberes[place] += 1

                if row[0] == 'Brussels':
                    if not place in g_Brussels and place != 'no':
                        g_Brussels[place] = 1
                    else:
                        g_Brussels[place] += 1

                if row[0] == 'Sofia':
                    if not place in g_Sofia and place != 'no':
                        g_Sofia[place] = 1
                    else:
                        g_Sofia[place] += 1

                if row[0] == 'Copenhagen':
                    if not place in g_Copenhagen and place != 'no':
                        g_Copenhagen[place] = 1
                    else:
                        g_Copenhagen[place] += 1

                if row[0] == 'Ibiza':
                    if not place in g_Ibiza and place != 'no':
                        g_Ibiza[place] = 1
                    else:
                        g_Ibiza[place] += 1

                if row[0] == 'Jerez':
                    if not place in g_Jerez and place != 'no':
                        g_Jerez[place] = 1
                    else:
                        g_Jerez[place] += 1

                if row[0] == 'LaGomera':
                    if not place in g_LaGomera and place != 'no':
                        g_LaGomera[place] = 1
                    else:
                        g_LaGomera[place] += 1

                if row[0] == 'LaPalma':
                    if not place in g_LaPalma and place != 'no':
                        g_LaPalma[place] = 1
                    else:
                        g_LaPalma[place] += 1

                if row[0] == 'LaCoruna':
                    if not place in g_LaCoruna and place != 'no':
                        g_LaCoruna[place] = 1
                    else:
                        g_LaCoruna[place] += 1

                if row[0] == 'Huesca':
                    if not place in g_Huesca and place != 'no':
                        g_Huesca[place] = 1
                    else:
                        g_Huesca[place] += 1

                if row[0] == 'Granada':
                    if not place in g_Granada and place != 'no':
                        g_Granada[place] = 1
                    else:
                        g_Granada[place] += 1

                if row[0] == 'Gerona':
                    if not place in g_Gerona and place != 'no':
                        g_Gerona[place] = 1
                    else:
                        g_Gerona[place] += 1

                if row[0] == 'GranCanaria':
                    if not place in g_GranCanaria and place != 'no':
                        g_GranCanaria[place] = 1
                    else:
                        g_GranCanaria[place] += 1

                if row[0] == 'Fuerteventura':
                    if not place in g_Fuerteventura and place != 'no':
                        g_Fuerteventura[place] = 1
                    else:
                        g_Fuerteventura[place] += 1

                if row[0] == 'ElHierro':
                    if not place in g_ElHierro and place != 'no':
                        g_ElHierro[place] = 1
                    else:
                        g_ElHierro[place] += 1

                if row[0] == 'Cordoba':
                    if not place in g_Cordoba and place != 'no':
                        g_Cordoba[place] = 1
                    else:
                        g_Cordoba[place] += 1

                if row[0] == 'CiudadReal':
                    if not place in g_CiudadReal and place != 'no':
                        g_CiudadReal[place] = 1
                    else:
                        g_CiudadReal[place] += 1

                if row[0] == 'Burgos':
                    if not place in g_Burgos and place != 'no':
                        g_Burgos[place] = 1
                    else:
                        g_Burgos[place] += 1

                if row[0] == 'Bilbao':
                    if not place in g_Bilbao and place != 'no':
                        g_Bilbao[place] = 1
                    else:
                        g_Bilbao[place] += 1

                if row[0] == 'Barcelona':
                    if not place in g_Barcelona and place != 'no':
                        g_Barcelona[place] = 1
                    else:
                        g_Barcelona[place] += 1

                if row[0] == 'Badajoz':
                    if not place in g_Badajoz and place != 'no':
                        g_Badajoz[place] = 1
                    else:
                        g_Badajoz[place] += 1

                if row[0] == 'Asturias':
                    if not place in g_Asturias and place != 'no':
                        g_Asturias[place] = 1
                    else:
                        g_Asturias[place] += 1

                if row[0] == 'Almeria':
                    if not place in g_Almeria and place != 'no':
                        g_Almeria[place] = 1
                    else:
                        g_Almeria[place] += 1

                if row[0] == 'Alicante':
                    if not place in g_Alicante and place != 'no':
                        g_Alicante[place] = 1
                    else:
                        g_Alicante[place] += 1

                if row[0] == 'Albacete':
                    if not place in g_Albacete and place != 'no':
                        g_Albacete[place] = 1
                    else:
                        g_Albacete[place] += 1

                if row[0] == 'Madrid':
                    if not place in g_Madrid and place != 'no':
                        g_Madrid[place] = 1
                    else:
                        g_Madrid[place] += 1

                if row[0] == 'Lanzarote':
                    if not place in g_Lanzarote and place != 'no':
                        g_Lanzarote[place] = 1
                    else:
                        g_Lanzarote[place] += 1

                if row[0] == 'Leon':
                    if not place in g_Leon and place != 'no':
                        g_Leon[place] = 1
                    else:
                        g_Leon[place] += 1

                if row[0] == 'Logrono':
                    if not place in g_Logrono and place != 'no':
                        g_Logrono[place] = 1
                    else:
                        g_Logrono[place] += 1

                if row[0] == 'Menorca':
                    if not place in g_Menorca and place != 'no':
                        g_Menorca[place] = 1
                    else:
                        g_Menorca[place] += 1

                if row[0] == 'Malaga':
                    if not place in g_Malaga and place != 'no':
                        g_Malaga[place] = 1
                    else:
                        g_Malaga[place] += 1

                if row[0] == 'Melilla':
                    if not place in g_Melilla and place != 'no':
                        g_Melilla[place] = 1
                    else:
                        g_Melilla[place] += 1

                if row[0] == 'Murcia':
                    if not place in g_Murcia and place != 'no':
                        g_Murcia[place] = 1
                    else:
                        g_Murcia[place] += 1

                if row[0] == 'PalmaMallorca':
                    if not place in g_PalmaMallorca and place != 'no':
                        g_PalmaMallorca[place] = 1
                    else:
                        g_PalmaMallorca[place] += 1

                if row[0] == 'Pamplona':
                    if not place in g_Pamplona and place != 'no':
                        g_Pamplona[place] = 1
                    else:
                        g_Pamplona[place] += 1

                if row[0] == 'Reus':
                    if not place in g_Reus and place != 'no':
                        g_Reus[place] = 1
                    else:
                        g_Reus[place] += 1

                if row[0] == 'Sabadell':
                    if not place in g_Sabadell and place != 'no':
                        g_Sabadell[place] = 1
                    else:
                        g_Sabadell[place] += 1

                if row[0] == 'SanSebastian':
                    if not place in g_SanSebastian and place != 'no':
                        g_SanSebastian[place] = 1
                    else:
                        g_SanSebastian[place] += 1

                if row[0] == 'SantiagodeCompostela':
                    if not place in g_SantiagodeCompostela and place != 'no':
                        g_SantiagodeCompostela[place] = 1
                    else:
                        g_SantiagodeCompostela[place] += 1

                if row[0] == 'Salamanca':
                    if not place in g_Salamanca and place != 'no':
                        g_Salamanca[place] = 1
                    else:
                        g_Salamanca[place] += 1

                if row[0] == 'Santander':
                    if not place in g_Santander and place != 'no':
                        g_Santander[place] = 1
                    else:
                        g_Santander[place] += 1

                if row[0] == 'Sevilla':
                    if not place in g_Sevilla and place != 'no':
                        g_Sevilla[place] = 1
                    else:
                        g_Sevilla[place] += 1

                if row[0] == 'Tenerife':
                    if not place in g_Tenerife and place != 'no':
                        g_Tenerife[place] = 1
                    else:
                        g_Tenerife[place] += 1

                if row[0] == 'Valencia':
                    if not place in g_Valencia and place != 'no':
                        g_Valencia[place] = 1
                    else:
                        g_Valencia[place] += 1

                if row[0] == 'Valladolid':
                    if not place in g_Valladolid and place != 'no':
                        g_Valladolid[place] = 1
                    else:
                        g_Valladolid[place] += 1

                if row[0] == 'Vigo':
                    if not place in g_Vigo and place != 'no':
                        g_Vigo[place] = 1
                    else:
                        g_Vigo[place] += 1

                if row[0] == 'Vitoria':
                    if not place in g_Vitoria and place != 'no':
                        g_Vitoria[place] = 1
                    else:
                        g_Vitoria[place] += 1

                if row[0] == 'Zaragoza':
                    if not place in g_Zaragoza and place != 'no':
                        g_Zaragoza[place] = 1
                    else:
                        g_Zaragoza[place] += 1

                if row[0] == 'Toulouse':
                    if not place in g_Toulouse and place != 'no':
                        g_Toulouse[place] = 1
                    else:
                        g_Toulouse[place] += 1

                if row[0] == 'Montpellier':
                    if not place in g_Montpellier and place != 'no':
                        g_Montpellier[place] = 1
                    else:
                        g_Montpellier[place] += 1

                if row[0] == 'Niza':
                    if not place in g_Niza and place != 'no':
                        g_Niza[place] = 1
                    else:
                        g_Niza[place] += 1

                if row[0] == 'Marseille':
                    if not place in g_Marseille and place != 'no':
                        g_Marseille[place] = 1
                    else:
                        g_Marseille[place] += 1

                if row[0] == 'SaintEtienne':
                    if not place in g_SaintEtienne and place != 'no':
                        g_SaintEtienne[place] = 1
                    else:
                        g_SaintEtienne[place] += 1

                if row[0] == 'Lyon':
                    if not place in g_Lyon and place != 'no':
                        g_Lyon[place] = 1
                    else:
                        g_Lyon[place] += 1

                if row[0] == 'Estrasburg':
                    if not place in g_Estrasburg and place != 'no':
                        g_Estrasburg[place] = 1
                    else:
                        g_Estrasburg[place] += 1

                if row[0] == 'Pau':
                    if not place in g_Pau and place != 'no':
                        g_Pau[place] = 1
                    else:
                        g_Pau[place] += 1

                if row[0] == 'Burdeos':
                    if not place in g_Burdeos and place != 'no':
                        g_Burdeos[place] = 1
                    else:
                        g_Burdeos[place] += 1

                if row[0] == 'Biarritz':
                    if not place in g_Biarritz and place != 'no':
                        g_Biarritz[place] = 1
                    else:
                        g_Biarritz[place] += 1

                if row[0] == 'Beauvais':
                    if not place in g_Beauvais and place != 'no':
                        g_Beauvais[place] = 1
                    else:
                        g_Beauvais[place] += 1

                if row[0] == 'Paris':
                    if not place in g_Paris and place != 'no':
                        g_Paris[place] = 1
                    else:
                        g_Paris[place] += 1

                if row[0] == 'Helsinki':
                    if not place in g_Helsinki and place != 'no':
                        g_Helsinki[place] = 1
                    else:
                        g_Helsinki[place] += 1

                if row[0] == 'Athens':
                    if not place in g_Athens and place != 'no':
                        g_Athens[place] = 1
                    else:
                        g_Athens[place] += 1

                if row[0] == 'Rotterdam':
                    if not place in g_Rotterdam and place != 'no':
                        g_Rotterdam[place] = 1
                    else:
                        g_Rotterdam[place] += 1

                if row[0] == 'Eelde':
                    if not place in g_Eelde and place != 'no':
                        g_Eelde[place] = 1
                    else:
                        g_Eelde[place] += 1

                if row[0] == 'Eindhoven':
                    if not place in g_Eindhoven and place != 'no':
                        g_Eindhoven[place] = 1
                    else:
                        g_Eindhoven[place] += 1

                if row[0] == 'Amsterdam':
                    if not place in g_Amsterdam and place != 'no':
                        g_Amsterdam[place] = 1
                    else:
                        g_Amsterdam[place] += 1

                if row[0] == 'Budapest':
                    if not place in g_Budapest and place != 'no':
                        g_Budapest[place] = 1
                    else:
                        g_Budapest[place] += 1

                if row[0] == 'Riga':
                    if not place in g_Riga and place != 'no':
                        g_Riga[place] = 1
                    else:
                        g_Riga[place] += 1

                if row[0] == 'Luxembourg':
                    if not place in g_Luxembourg and place != 'no':
                        g_Luxembourg[place] = 1
                    else:
                        g_Luxembourg[place] += 1

                if row[0] == 'Bergen':
                    if not place in g_Bergen and place != 'no':
                        g_Bergen[place] = 1
                    else:
                        g_Bergen[place] += 1

                if row[0] == 'Oslo':
                    if not place in g_Oslo and place != 'no':
                        g_Oslo[place] = 1
                    else:
                        g_Oslo[place] += 1

                if row[0] == 'Varsovia':
                    if not place in g_Varsovia and place != 'no':
                        g_Varsovia[place] = 1
                    else:
                        g_Varsovia[place] += 1

                if row[0] == 'Cracovia':
                    if not place in g_Cracovia and place != 'no':
                        g_Cracovia[place] = 1
                    else:
                        g_Cracovia[place] += 1

                if row[0] == 'Faro':
                    if not place in g_Faro and place != 'no':
                        g_Faro[place] = 1
                    else:
                        g_Faro[place] += 1

                if row[0] == 'Terceira':
                    if not place in g_Terceira and place != 'no':
                        g_Terceira[place] = 1
                    else:
                        g_Terceira[place] += 1

                if row[0] == 'g_Madeira':
                    if not place in g_Madeira and place != 'no':
                        g_Madeira[place] = 1
                    else:
                        g_Madeira[place] += 1

                if row[0] == 'Porto':
                    if not place in g_Porto and place != 'no':
                        g_Porto[place] = 1
                    else:
                        g_Porto[place] += 1

                if row[0] == 'Lisbon':
                    if not place in g_Lisbon and place != 'no':
                        g_Lisbon[place] = 1
                    else:
                        g_Lisbon[place] += 1

                if row[0] == 'PontaDelgada':
                    if not place in g_PontaDelgada and place != 'no':
                        g_PontaDelgada[place] = 1
                    else:
                        g_PontaDelgada[place] += 1

                if row[0] == 'Dublin':
                    if not place in g_Dublin and place != 'no':
                        g_Dublin[place] = 1
                    else:
                        g_Dublin[place] += 1

                if row[0] == 'Edinburgh':
                    if not place in g_Edinburgh and place != 'no':
                        g_Edinburgh[place] = 1
                    else:
                        g_Edinburgh[place] += 1

                if row[0] == 'Glasgow':
                    if not place in g_Glasgow and place != 'no':
                        g_Glasgow[place] = 1
                    else:
                        g_Glasgow[place] += 1

                if row[0] == 'London':
                    if not place in g_London and place != 'no':
                        g_London[place] = 1
                    else:
                        g_London[place] += 1

                if row[0] == 'Birmingham':
                    if not place in g_Birmingham and place != 'no':
                        g_Birmingham[place] = 1
                    else:
                        g_Birmingham[place] += 1

                if row[0] == 'Bristol':
                    if not place in g_Bristol and place != 'no':
                        g_Bristol[place] = 1
                    else:
                        g_Bristol[place] += 1

                if row[0] == 'Liverpool':
                    if not place in g_Liverpool and place != 'no':
                        g_Liverpool[place] = 1
                    else:
                        g_Liverpool[place] += 1

                if row[0] == 'Manchester':
                    if not place in g_Manchester and place != 'no':
                        g_Manchester[place] = 1
                    else:
                        g_Manchester[place] += 1

                if row[0] == 'Gibraltar':
                    if not place in g_Gibraltar and place != 'no':
                        g_Gibraltar[place] = 1
                    else:
                        g_Gibraltar[place] += 1

                if row[0] == 'GeorgeTown':
                    if not place in g_GeorgeTown and place != 'no':
                        g_GeorgeTown[place] = 1
                    else:
                        g_GeorgeTown[place] += 1

                if row[0] == 'Prague':
                    if not place in g_Prague and place != 'no':
                        g_Prague[place] = 1
                    else:
                        g_Prague[place] += 1

                if row[0] == 'Bucarest':
                    if not place in g_Bucarest and place != 'no':
                        g_Bucarest[place] = 1
                    else:
                        g_Bucarest[place] += 1

                if row[0] == 'Stockholm':
                    if not place in g_Stockholm and place != 'no':
                        g_Stockholm[place] = 1
                    else:
                        g_Stockholm[place] += 1

                if row[0] == 'Zurich':
                    if not place in g_Zurich and place != 'no':
                        g_Zurich[place] = 1
                    else:
                        g_Zurich[place] += 1

                if row[0] == 'Ginebra':
                    if not place in g_Ginebra and place != 'no':
                        g_Ginebra[place] = 1
                    else:
                        g_Ginebra[place] += 1

                if row[0] == 'Berna':
                    if not place in g_Berna and place != 'no':
                        g_Berna[place] = 1
                    else:
                        g_Berna[place] += 1

                if row[0] == 'Basel':
                    if not place in g_Basel and place != 'no':
                        g_Basel[place] = 1
                    else:
                        g_Basel[place] += 1

                if row[0] == 'Verona':
                    if not place in g_Verona and place != 'no':
                        g_Verona[place] = 1
                    else:
                        g_Verona[place] += 1

                if row[0] == 'Venice':
                    if not place in g_Venice and place != 'no':
                        g_Venice[place] = 1
                    else:
                        g_Venice[place] += 1

                if row[0] == 'Pisa':
                    if not place in g_Pisa and place != 'no':
                        g_Pisa[place] = 1
                    else:
                        g_Pisa[place] += 1

                if row[0] == 'Turin':
                    if not place in g_Turin and place != 'no':
                        g_Turin[place] = 1
                    else:
                        g_Turin[place] += 1

                if row[0] == 'Asis':
                    if not place in g_Asis and place != 'no':
                        g_Asis[place] = 1
                    else:
                        g_Asis[place] += 1

                if row[0] == 'Catania':
                    if not place in g_Catania and place != 'no':
                        g_Catania[place] = 1
                    else:
                        g_Catania[place] += 1

                if row[0] == 'Palermo':
                    if not place in g_Palermo and place != 'no':
                        g_Palermo[place] = 1
                    else:
                        g_Palermo[place] += 1

                if row[0] == 'Forli':
                    if not place in g_Forli and place != 'no':
                        g_Forli[place] = 1
                    else:
                        g_Forli[place] += 1

                if row[0] == 'Bologna':
                    if not place in g_Bologna and place != 'no':
                        g_Bologna[place] = 1
                    else:
                        g_Bologna[place] += 1

                if row[0] == 'Miramare':
                    if not place in g_Miramare and place != 'no':
                        g_Miramare[place] = 1
                    else:
                        g_Miramare[place] += 1

                if row[0] == 'Parma':
                    if not place in g_Parma and place != 'no':
                        g_Parma[place] = 1
                    else:
                        g_Parma[place] += 1

                if row[0] == 'Naples':
                    if not place in g_Naples and place != 'no':
                        g_Naples[place] = 1
                    else:
                        g_Naples[place] += 1

                if row[0] == 'Genoa':
                    if not place in g_Genoa and place != 'no':
                        g_Genoa[place] = 1
                    else:
                        g_Genoa[place] += 1

                if row[0] == 'Florence':
                    if not place in g_Florence and place != 'no':
                        g_Florence[place] = 1
                    else:
                        g_Florence[place] += 1

                if row[0] == 'ReggioCalabria':
                    if not place in g_ReggioCalabria and place != 'no':
                        g_ReggioCalabria[place] = 1
                    else:
                        g_ReggioCalabria[place] += 1

                if row[0] == 'Bari':
                    if not place in g_Bari and place != 'no':
                        g_Bari[place] = 1
                    else:
                        g_Bari[place] += 1

                if row[0] == 'Milan':
                    if not place in g_Milan and place != 'no':
                        g_Milan[place] = 1
                    else:
                        g_Milan[place] += 1

                if row[0] == 'Montichiari':
                    if not place in g_Montichiari and place != 'no':
                        g_Montichiari[place] = 1
                    else:
                        g_Montichiari[place] += 1

                if row[0] == 'Bergamo':
                    if not place in g_Bergamo and place != 'no':
                        g_Bergamo[place] = 1
                    else:
                        g_Bergamo[place] += 1

                if row[0] == 'Cagliari':
                    if not place in g_Cagliari and place != 'no':
                        g_Cagliari[place] = 1
                    else:
                        g_Cagliari[place] += 1

                if row[0] == 'Alghero':
                    if not place in g_Alghero and place != 'no':
                        g_Alghero[place] = 1
                    else:
                        g_Alghero[place] += 1

                if row[0] == 'Ancona':
                    if not place in g_Ancona and place != 'no':
                        g_Ancona[place] = 1
                    else:
                        g_Ancona[place] += 1

                if row[0] == 'Rome':
                    if not place in g_Rome and place != 'no':
                        g_Rome[place] = 1
                    else:
                        g_Rome[place] += 1

        except:
            pass

with open('eeuu.csv', 'r') as data:
    spamreader = csv.reader(data)


    for row in spamreader:

        try:

            if row[1] == 'salida':

                m = (row[3].replace('\n', '').replace(' ', ''))
                place = m[5:]

                if row[0] == 'Edmonton':
                    if not place in g_Edmonton and place != 'no':
                        g_Edmonton[place] = 1
                    else:
                        g_Edmonton[place] += 1

                if row[0] == 'Ottawa':
                    if not place in g_Ottawa and place != 'no':
                        g_Ottawa[place] = 1
                    else:
                        g_Ottawa[place] += 1

                if row[0] == 'GrandePrairie':
                    if not place in g_GrandePrairie and place != 'no':
                        g_GrandePrairie[place] = 1
                    else:
                        g_GrandePrairie[place] += 1

                if row[0] == 'Dorval':
                    if not place in g_Dorval and place != 'no':
                        g_Dorval[place] = 1
                    else:
                        g_Dorval[place] += 1

                if row[0] == 'Mirabel':
                    if not place in g_Mirabel and place != 'no':
                        g_Mirabel[place] = 1
                    else:
                        g_Mirabel[place] += 1

                if row[0] == 'Montreal':
                    if not place in g_Montreal and place != 'no':
                        g_Montreal[place] = 1
                    else:
                        g_Montreal[place] += 1

                if row[0] == 'Terranova':
                    if not place in g_Terranova and place != 'no':
                        g_Terranova[place] = 1
                    else:
                        g_Terranova[place] += 1

                if row[0] == 'Toronto':
                    if not place in g_Toronto and place != 'no':
                        g_Toronto[place] = 1
                    else:
                        g_Toronto[place] += 1

                if row[0] == 'Vancouver':
                    if not place in g_Vancouver and place != 'no':
                        g_Vancouver[place] = 1
                    else:
                        g_Vancouver[place] += 1

                if row[0] == 'Winnipeg':
                    if not place in g_Winnipeg and place != 'no':
                        g_Winnipeg[place] = 1
                    else:
                        g_Winnipeg[place] += 1

                if row[0] == 'Birmingham':
                    if not place in g_Birmingham and place != 'no':
                        g_Birmingham[place] = 1
                    else:
                        g_Birmingham[place] += 1

                if row[0] == 'Anchorage':
                    if not place in g_Anchorage and place != 'no':
                        g_Anchorage[place] = 1
                    else:
                        g_Anchorage[place] += 1

                if row[0] == 'Kingman':
                    if not place in g_Kingman and place != 'no':
                        g_Kingman[place] = 1
                    else:
                        g_Kingman[place] += 1

                if row[0] == 'Maricopa':
                    if not place in g_Maricopa and place != 'no':
                        g_Maricopa[place] = 1
                    else:
                        g_Maricopa[place] += 1

                if row[0] == 'Prescott':
                    if not place in g_Prescott and place != 'no':
                        g_Prescott[place] = 1
                    else:
                        g_Prescott[place] += 1

                if row[0] == 'Tucson':
                    if not place in g_Tucson and place != 'no':
                        g_Tucson[place] = 1
                    else:
                        g_Tucson[place] += 1

                if row[0] == 'Fresno':
                    if not place in g_Fresno and place != 'no':
                        g_Fresno[place] = 1
                    else:
                        g_Fresno[place] += 1

                if row[0] == 'LosAngeles':
                    if not place in g_LosAngeles and place != 'no':
                        g_LosAngeles[place] = 1
                    else:
                        g_LosAngeles[place] += 1

                if row[0] == 'LongBeach':
                    if not place in g_LongBeach and place != 'no':
                        g_LongBeach[place] = 1
                    else:
                        g_LongBeach[place] += 1

                if row[0] == 'Oakland':
                    if not place in g_Oakland and place != 'no':
                        g_Oakland[place] = 1
                    else:
                        g_Oakland[place] += 1

                if row[0] == 'Ontario':
                    if not place in g_Ontario and place != 'no':
                        g_Ontario[place] = 1
                    else:
                        g_Ontario[place] += 1

                if row[0] == 'PalmSprings':
                    if not place in g_PalmSprings and place != 'no':
                        g_PalmSprings[place] = 1
                    else:
                        g_PalmSprings[place] += 1

                if row[0] == 'Sacramento':
                    if not place in g_Sacramento and place != 'no':
                        g_Sacramento[place] = 1
                    else:
                        g_Sacramento[place] += 1

                if row[0] == 'SanBernardino':
                    if not place in g_SanBernardino and place != 'no':
                        g_SanBernardino[place] = 1
                    else:
                        g_SanBernardino[place] += 1

                if row[0] == 'SanDiego':
                    if not place in g_SanDiego and place != 'no':
                        g_SanDiego[place] = 1
                    else:
                        g_SanDiego[place] += 1

                if row[0] == 'Carlsbad':
                    if not place in g_Carlsbad and place != 'no':
                        g_Carlsbad[place] = 1
                    else:
                        g_Carlsbad[place] += 1

                if row[0] == 'SanDiego':
                    if not place in g_SanDiego and place != 'no':
                        g_SanDiego[place] = 1
                    else:
                        g_SanDiego[place] += 1

                if row[0] == 'SanFrancisco':
                    if not place in g_SanFrancisco and place != 'no':
                        g_SanFrancisco[place] = 1
                    else:
                        g_SanFrancisco[place] += 1

                if row[0] == 'SanJose':
                    if not place in g_SanJose and place != 'no':
                        g_SanJose[place] = 1
                    else:
                        g_SanJose[place] += 1

                if row[0] == 'Charlotte':
                    if not place in g_Charlotte and place != 'no':
                        g_Charlotte[place] = 1
                    else:
                        g_Charlotte[place] += 1

                if row[0] == 'Morrisville':
                    if not place in g_Morrisville and place != 'no':
                        g_Morrisville[place] = 1
                    else:
                        g_Morrisville[place] += 1

                if row[0] == 'ColoradoSprings':
                    if not place in g_ColoradoSprings and place != 'no':
                        g_ColoradoSprings[place] = 1
                    else:
                        g_ColoradoSprings[place] += 1

                if row[0] == 'Denver':
                    if not place in g_Denver and place != 'no':
                        g_Denver[place] = 1
                    else:
                        g_Denver[place] += 1

                if row[0] == 'DaytonaBeach':
                    if not place in g_DaytonaBeach and place != 'no':
                        g_DaytonaBeach[place] = 1
                    else:
                        g_DaytonaBeach[place] += 1

                if row[0] == 'FortLauderdale':
                    if not place in g_FortLauderdale and place != 'no':
                        g_FortLauderdale[place] = 1
                    else:
                        g_FortLauderdale[place] += 1

                if row[0] == 'Melbourne':
                    if not place in g_Melbourne and place != 'no':
                        g_Melbourne[place] = 1
                    else:
                        g_Melbourne[place] += 1

                if row[0] == 'Miami':
                    if not place in g_Miami and place != 'no':
                        g_Miami[place] = 1
                    else:
                        g_Miami[place] += 1

                if row[0] == 'Duval':
                    if not place in g_Duval and place != 'no':
                        g_Duval[place] = 1
                    else:
                        g_Duval[place] += 1

                if row[0] == 'FortMyers':
                    if not place in g_FortMyers and place != 'no':
                        g_FortMyers[place] = 1
                    else:
                        g_FortMyers[place] += 1

                if row[0] == 'Sanford':
                    if not place in g_Sanford and place != 'no':
                        g_Sanford[place] = 1
                    else:
                        g_Sanford[place] += 1

                if row[0] == 'Orlando':
                    if not place in g_Orlando and place != 'no':
                        g_Orlando[place] = 1
                    else:
                        g_Orlando[place] += 1

                if row[0] == 'Tampa':
                    if not place in g_Tampa and place != 'no':
                        g_Tampa[place] = 1
                    else:
                        g_Tampa[place] += 1

                if row[0] == 'WestPalmBeach':
                    if not place in g_WestPalmBeach and place != 'no':
                        g_WestPalmBeach[place] = 1
                    else:
                        g_WestPalmBeach[place] += 1

                if row[0] == 'Atlanta':
                    if not place in g_Atlanta and place != 'no':
                        g_Atlanta[place] = 1
                    else:
                        g_Atlanta[place] += 1

                if row[0] == 'Savannah':
                    if not place in g_Savannah and place != 'no':
                        g_Savannah[place] = 1
                    else:
                        g_Savannah[place] += 1

                if row[0] == 'Honolulu':
                    if not place in g_Honolulu and place != 'no':
                        g_Honolulu[place] = 1
                    else:
                        g_Honolulu[place] += 1

                if row[0] == 'Midway':
                    if not place in g_Midway and place != 'no':
                        g_Midway[place] = 1
                    else:
                        g_Midway[place] += 1

                if row[0] == 'Chicago':
                    if not place in g_Chicago and place != 'no':
                        g_Chicago[place] = 1
                    else:
                        g_Chicago[place] += 1

                if row[0] == 'Indianápolis':
                    if not place in g_Indianápolis and place != 'no':
                        g_Indianápolis[place] = 1
                    else:
                        g_Indianápolis[place] += 1

                if row[0] == 'Cincinnati':
                    if not place in g_Cincinnati and place != 'no':
                        g_Cincinnati[place] = 1
                    else:
                        g_Cincinnati[place] += 1

                if row[0] == 'Louisville':
                    if not place in g_Louisville and place != 'no':
                        g_Louisville[place] = 1
                    else:
                        g_Louisville[place] += 1

                if row[0] == 'Lafayette':
                    if not place in g_Lafayette and place != 'no':
                        g_Lafayette[place] = 1
                    else:
                        g_Lafayette[place] += 1

                if row[0] == 'NewOrleans':
                    if not place in g_NewOrleans and place != 'no':
                        g_NewOrleans[place] = 1
                    else:
                        g_NewOrleans[place] += 1

                if row[0] == 'Baltimore':
                    if not place in g_Baltimore and place != 'no':
                        g_Baltimore[place] = 1
                    else:
                        g_Baltimore[place] += 1

                if row[0] == 'Boston':
                    if not place in g_Boston and place != 'no':
                        g_Boston[place] = 1
                    else:
                        g_Boston[place] += 1

                if row[0] == 'Detroit':
                    if not place in g_Detroit and place != 'no':
                        g_Detroit[place] = 1
                    else:
                        g_Detroit[place] += 1

                if row[0] == 'Michigan':
                    if not place in g_Michigan and place != 'no':
                        g_Michigan[place] = 1
                    else:
                        g_Michigan[place] += 1

                if row[0] == 'CapitolCity':
                    if not place in g_CapitolCity and place != 'no':
                        g_CapitolCity[place] = 1
                    else:
                        g_CapitolCity[place] += 1

                if row[0] == 'StPaul':
                    if not place in g_StPaul and place != 'no':
                        g_StPaul[place] = 1
                    else:
                        g_StPaul[place] += 1

                if row[0] == 'KansasCity':
                    if not place in g_KansasCity and place != 'no':
                        g_KansasCity[place] = 1
                    else:
                        g_KansasCity[place] += 1

                if row[0] == 'SanLuis':
                    if not place in g_SanLuis and place != 'no':
                        g_SanLuis[place] = 1
                    else:
                        g_SanLuis[place] += 1

                if row[0] == 'LasVegas':
                    if not place in g_LasVegas and place != 'no':
                        g_LasVegas[place] = 1
                    else:
                        g_LasVegas[place] += 1

                if row[0] == 'Cheektowaga':
                    if not place in g_Cheektowaga and place != 'no':
                        g_Cheektowaga[place] = 1
                    else:
                        g_Cheektowaga[place] += 1

                if row[0] == 'Newark':
                    if not place in g_Newark and place != 'no':
                        g_Newark[place] = 1
                    else:
                        g_Newark[place] += 1

                if row[0] == 'NewYork':
                    if not place in g_NewYork and place != 'no':
                        g_NewYork[place] = 1
                    else:
                        g_NewYork[place] += 1

                if row[0] == 'Albany':
                    if not place in g_Albany and place != 'no':
                        g_Albany[place] = 1
                    else:
                        g_Albany[place] += 1

                if row[0] == 'Albuquerque':
                    if not place in g_Albuquerque and place != 'no':
                        g_Albuquerque[place] = 1
                    else:
                        g_Albuquerque[place] += 1

                if row[0] == 'Cleveland':
                    if not place in g_Cleveland and place != 'no':
                        g_Cleveland[place] = 1
                    else:
                        g_Cleveland[place] += 1

                if row[0] == 'Portland':
                    if not place in g_Portland and place != 'no':
                        g_Portland[place] = 1
                    else:
                        g_Portland[place] += 1

                if row[0] == 'Philadelphia':
                    if not place in g_Philadelphia and place != 'no':
                        g_Philadelphia[place] = 1
                    else:
                        g_Philadelphia[place] += 1

                if row[0] == 'Memphis':
                    if not place in g_Memphis and place != 'no':
                        g_Memphis[place] = 1
                    else:
                        g_Memphis[place] += 1

                if row[0] == 'Austin':
                    if not place in g_Austin and place != 'no':
                        g_Austin[place] = 1
                    else:
                        g_Austin[place] += 1

                if row[0] == 'Dallas_FortWorth':
                    if not place in g_Dallas_FortWorth and place != 'no':
                        g_Dallas_FortWorth[place] = 1
                    else:
                        g_Dallas_FortWorth[place] += 1

                if row[0] == 'Dallas':
                    if not place in g_Dallas and place != 'no':
                        g_Dallas[place] = 1
                    else:
                        g_Dallas[place] += 1

                if row[0] == 'Laredo':
                    if not place in g_Laredo and place != 'no':
                        g_Laredo[place] = 1
                    else:
                        g_Laredo[place] += 1

                if row[0] == 'McAllen':
                    if not place in g_McAllen and place != 'no':
                        g_McAllen[place] = 1
                    else:
                        g_McAllen[place] += 1

                if row[0] == 'Houston':
                    if not place in g_Houston and place != 'no':
                        g_Houston[place] = 1
                    else:
                        g_Houston[place] += 1

                if row[0] == 'SaltLakeCity':
                    if not place in g_SaltLakeCity and place != 'no':
                        g_SaltLakeCity[place] = 1
                    else:
                        g_SaltLakeCity[place] += 1

                if row[0] == 'StGeorge':
                    if not place in g_StGeorge and place != 'no':
                        g_StGeorge[place] = 1
                    else:
                        g_StGeorge[place] += 1

                if row[0] == 'Seattle':
                    if not place in g_Seattle and place != 'no':
                        g_Seattle[place] = 1
                    else:
                        g_Seattle[place] += 1

                if row[0] == 'Dulles':
                    if not place in g_Dulles and place != 'no':
                        g_Dulles[place] = 1
                    else:
                        g_Dulles[place] += 1

                if row[0] == 'Washington':
                    if not place in g_Washington and place != 'no':
                        g_Washington[place] = 1
                    else:
                        g_Washington[place] += 1

                if row[0] == 'Milwaukee':
                    if not place in g_Milwaukee and place != 'no':
                        g_Milwaukee[place] = 1
                    else:
                        g_Milwaukee[place] += 1

                if row[0] == 'RockSprings':
                    if not place in g_RockSprings and place != 'no':
                        g_RockSprings[place] = 1
                    else:
                        g_RockSprings[place] += 1

                if row[0] == 'Veracruz':
                    if not place in g_Veracruz and place != 'no':
                        g_Veracruz[place] = 1
                    else:
                        g_Veracruz[place] += 1

                if row[0] == 'Mérida':
                    if not place in g_Mérida and place != 'no':
                        g_Mérida[place] = 1
                    else:
                        g_Mérida[place] += 1

                if row[0] == 'Tampico':
                    if not place in g_Tampico and place != 'no':
                        g_Tampico[place] = 1
                    else:
                        g_Tampico[place] += 1

                if row[0] == 'Tamaulipas':
                    if not place in g_Tamaulipas and place != 'no':
                        g_Tamaulipas[place] = 1
                    else:
                        g_Tamaulipas[place] += 1

                if row[0] == 'Villahermosa':
                    if not place in g_Villahermosa and place != 'no':
                        g_Villahermosa[place] = 1
                    else:
                        g_Villahermosa[place] += 1

                if row[0] == 'Hermosillo':
                    if not place in g_Hermosillo and place != 'no':
                        g_Hermosillo[place] = 1
                    else:
                        g_Hermosillo[place] += 1

                if row[0] == 'SanLuisPotosí':
                    if not place in g_SanLuisPotosí and place != 'no':
                        g_SanLuisPotosí[place] = 1
                    else:
                        g_SanLuisPotosí[place] += 1

                if row[0] == 'Mazatlán':
                    if not place in g_Mazatlán and place != 'no':
                        g_Mazatlán[place] = 1
                    else:
                        g_Mazatlán[place] += 1

                if row[0] == 'SanMigueldeCozumel':
                    if not place in g_SanMigueldeCozumel and place != 'no':
                        g_SanMigueldeCozumel[place] = 1
                    else:
                        g_SanMigueldeCozumel[place] += 1

                if row[0] == 'Cancun':
                    if not place in g_Cancun and place != 'no':
                        g_Cancun[place] = 1
                    else:
                        g_Cancun[place] += 1

                if row[0] == 'Queretana':
                    if not place in g_Queretana and place != 'no':
                        g_Queretana[place] = 1
                    else:
                        g_Queretana[place] += 1

                if row[0] == 'Puebla':
                    if not place in g_Puebla and place != 'no':
                        g_Puebla[place] = 1
                    else:
                        g_Puebla[place] += 1

                if row[0] == 'Huatulco':
                    if not place in g_Huatulco and place != 'no':
                        g_Huatulco[place] = 1
                    else:
                        g_Huatulco[place] += 1

                if row[0] == 'Oaxaca':
                    if not place in g_Oaxaca and place != 'no':
                        g_Oaxaca[place] = 1
                    else:
                        g_Oaxaca[place] += 1

                if row[0] == 'NuevoLeón':
                    if not place in g_NuevoLeón and place != 'no':
                        g_NuevoLeón[place] = 1
                    else:
                        g_NuevoLeón[place] += 1

                if row[0] == 'PuertoVallarta':
                    if not place in g_PuertoVallarta and place != 'no':
                        g_PuertoVallarta[place] = 1
                    else:
                        g_PuertoVallarta[place] += 1

                if row[0] == 'Guadalajara':
                    if not place in g_Guadalajara and place != 'no':
                        g_Guadalajara[place] = 1
                    else:
                        g_Guadalajara[place] += 1

                if row[0] == 'Acapulco':
                    if not place in g_Acapulco and place != 'no':
                        g_Acapulco[place] = 1
                    else:
                        g_Acapulco[place] += 1

                if row[0] == 'Silao':
                    if not place in g_Silao and place != 'no':
                        g_Silao[place] = 1
                    else:
                        g_Silao[place] += 1

                if row[0] == 'SanPedro':
                    if not place in g_SanPedro and place != 'no':
                        g_SanPedro[place] = 1
                    else:
                        g_SanPedro[place] += 1

                if row[0] == 'Durango':
                    if not place in g_Durango and place != 'no':
                        g_Durango[place] = 1
                    else:
                        g_Durango[place] += 1

                if row[0] == 'Culiacán':
                    if not place in g_Culiacán and place != 'no':
                        g_Culiacán[place] = 1
                    else:
                        g_Culiacán[place] += 1

                if row[0] == 'Chihuahua':
                    if not place in g_Chihuahua and place != 'no':
                        g_Chihuahua[place] = 1
                    else:
                        g_Chihuahua[place] += 1

                if row[0] == 'ElPaso':
                    if not place in g_ElPaso and place != 'no':
                        g_ElPaso[place] = 1
                    else:
                        g_ElPaso[place] += 1

                if row[0] == 'TuxtlaGutiérrez':
                    if not place in g_TuxtlaGutiérrez and place != 'no':
                        g_TuxtlaGutiérrez[place] = 1
                    else:
                        g_TuxtlaGutiérrez[place] += 1

                if row[0] == 'CiudaddelCarmen':
                    if not place in g_CiudaddelCarmen and place != 'no':
                        g_CiudaddelCarmen[place] = 1
                    else:
                        g_CiudaddelCarmen[place] += 1

                if row[0] == 'SanJosédelCabo':
                    if not place in g_SanJosédelCabo and place != 'no':
                        g_SanJosédelCabo[place] = 1
                    else:
                        g_SanJosédelCabo[place] += 1

                if row[0] == 'LaPaz':
                    if not place in g_LaPaz and place != 'no':
                        g_LaPaz[place] = 1
                    else:
                        g_LaPaz[place] += 1

                if row[0] == 'Tijuana':
                    if not place in g_Tijuana and place != 'no':
                        g_Tijuana[place] = 1
                    else:
                        g_Tijuana[place] += 1

                if row[0] == 'Mexicali':
                    if not place in g_Mexicali and place != 'no':
                        g_Mexicali[place] = 1
                    else:
                        g_Mexicali[place] += 1

                if row[0] == 'Aguascalientes':
                    if not place in g_Aguascalientes and place != 'no':
                        g_Aguascalientes[place] = 1
                    else:
                        g_Aguascalientes[place] += 1

                if row[0] == 'CiudaddeMéxico':
                    if not place in g_CiudaddeMéxico and place != 'no':
                        g_CiudaddeMéxico[place] = 1
                    else:
                        g_CiudaddeMéxico[place] += 1

                if row[3] != 'lugar' and row[3].replace('\n', '').replace(' ', '') != 'Destino':
                    m = (row[3].replace('\n', '').replace(' ', ''))
                    nodes.append(m[5:])

        except:
            pass

with open('mexico.csv', 'r') as data:
    spamreader = csv.reader(data)


    for row in spamreader:

        try:

            if row[1] == 'salida':

                m = (row[3].replace('\n', '').replace(' ', ''))
                place = m[5:]

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-general-heriberto-jara/':
                    row[0] = 'Veracruz'
                    nodes.append('Veracruz')
                    america.append('Veracruz')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-manuel-crescencio-rejon/':
                    row[0] = 'Mérida'
                    nodes.append('Mérida')
                    america.append('Mérida')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-general-francisco-javier-mina/':
                    row[0] = 'Tampico'
                    nodes.append('Tampico')
                    america.append('Tampico')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-general-lucio-blanco/':
                    row[0] = 'Tamaulipas'
                    nodes.append('Tamaulipas')
                    america.append('Tamaulipas')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-carlos-rovirosa-perez/':
                    row[0] = 'Villahermosa'
                    nodes.append('Villahermosa')
                    america.append('Villahermosa')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-hermosillo/':
                    row[0] = 'Hermosillo'
                    nodes.append('Hermosillo')
                    america.append('Hermosillo')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-ponciano-arriaga/':
                    row[0] = 'SanLuisPotosí'
                    nodes.append('SanLuisPotosí')
                    america.append('SanLuisPotosí')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-general-rafael-buelna/':
                    row[0] = 'Mazatlán'
                    nodes.append('Mazatlán')
                    america.append('Mazatlán')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-federal-de-culiacan/':
                    row[0] = 'Culiacán'
                    nodes.append('Culiacán')
                    america.append('Culiacán')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-cozumel/':
                    row[0] = 'SanMigueldeCozumel'
                    nodes.append('SanMigueldeCozumel')
                    america.append('SanMigueldeCozumel')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-cancun/':
                    row[0] = 'Cancun'
                    nodes.append('Cancun')
                    america.append('Cancun')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-queretaro/':
                    row[0] = 'Queretana'
                    nodes.append('Queretana')
                    america.append('Queretana')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-puebla/':
                    row[0] = 'Puebla'
                    nodes.append('Puebla')
                    america.appen('Puebla')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-bahias-de-huatulco/':
                    row[0] = 'Huatulco'
                    nodes.append('Huatulco')
                    america.append('Huatulco')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-oaxaca/':
                    row[0] = 'Oaxaca'
                    nodes.append('Oaxaca')
                    america.append('Oaxaca')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-mariano-escobedo/':
                    row[0] = 'NuevoLeón'
                    nodes.append('NuevoLeón')
                    america.append('NuevoLeón')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-licenciado-gustavo-diaz-ordaz/':
                    row[0] = 'PuertoVallarta'
                    nodes.append('PuertoVallarta')
                    america.append('PuertoVallarta')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-guadalajara/':
                    row[0] = 'Guadalajara'
                    nodes.append('Guadalajara')
                    america.append('Guadalajara')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-acapulco/':
                    row[0] = 'Acapulco'
                    nodes.append('Acapulco')
                    america.append('Acapulco')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-del-bajio/':
                    row[0] = 'Silao'
                    nodes.append('Silao')
                    america.append('Silao')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-lic-adolfo-lopez-mateos/':
                    row[0] = 'SanPedro'
                    nodes.append('SanPedro')
                    america.append('SanPedro')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-general-guadalupe-victoria/':
                    row[0] = 'Durango'
                    nodes.append('Durango')
                    america.append('Durango')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-general-roberto-fierro-villalobos/':
                    row[0] = 'Chihuahua'
                    nodes.append('Chihuahua')
                    america.append('Chihuahua')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-abraham-gonzalez/':
                    row[0] = 'ElPaso'
                    nodes.append('ElPaso')
                    america.append('ElPaso')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-angel-albino-corzo/':
                    row[0] = 'TuxtlaGutiérrez'
                    nodes.append('TuxtlaGutiérrez')
                    america.append('TuxtlaGutiérrez')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-ciudad-del-carmen/':
                    row[0] = 'CiudaddelCarmen'
                    nodes.append('CiudaddelCarmen')
                    america.append('CiudaddelCarmen')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-los-cabos/':
                    row[0] = 'SanJosédelCabo'
                    nodes.append('SanJosédelCabo')
                    america.append('SanJosédelCabo')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-manuel-marquez-de-leon/':
                    row[0] = 'LaPaz'
                    nodes.append('LaPaz')
                    america.append('LaPaz')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-tijuana/':
                    row[0] = 'Tijuana'
                    nodes.append('Tijuana')
                    america.append('Tijuana')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-general-rodolfo-sanchez-taboada/':
                    row[0] = 'Mexicali'
                    nodes.append('Mexicali')
                    america.append('Mexicali')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-licenciado-jesus-teran-peredo/':
                    row[0] = 'Aguascalientes'
                    nodes.append('Aguascalientes')
                    america.append('Aguascalientes')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-la-ciudad-de-mexico/':
                    row[0] = 'CiudaddeMéxico'
                    nodes.append('CiudaddeMéxico')
                    america.append('CiudaddeMéxico')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-edmonton/':
                    row[0] = 'Edmonton'
                    nodes.append('Edmonton')
                    america.append('Edmonton')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-calgary/':
                    row[0] = 'Ottawa'
                    nodes.append('Ottawa')
                    america.append('Ottawa')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-de-grande-prairie/':
                    row[0] = 'GrandePrairie'
                    nodes.append('GrandePrairie')
                    america.append('GrandePrairie')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-ottawa-mcdonald-cartier/':
                    row[0] ='Ottawa'
                    nodes.append('Ottawa')
                    america.append('Ottawa')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-pierre-elliott-trudeau/':
                    row[0] = 'Dorval'
                    nodes.append('Dorval')
                    america.append('Dorval')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-montreal-mirabel/':
                    row[0] = 'Mirabel'
                    nodes.append('Mirabel')
                    america.append('Mirabel')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-de-montreal-saint-hubert/':
                    row[0] = 'Montreal'
                    nodes.append('Montreal')
                    america.append('Montreal')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-san-juan-de-terranova/':
                    row[0] = 'Terranova'
                    nodes.append('Terranova')
                    america.append('Terranova')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-toronto-pearson/':
                    row[0] = 'Toronto'
                    nodes.append('Toronto')
                    america.append('Toronto')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-vancouver/':
                    row[0] = 'Vancouver'
                    nodes.append('Vancouver')
                    america.append('Vancouver')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-james-armstrong-richardson/':
                    row[0] ='Winnipeg'
                    nodes.append('Winnipeg')
                    america.append('Winnipeg')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-birmingham-shuttlesworth/':
                    row[0] = 'Birmingham'
                    nodes.append('Birmingham')
                    america.append('Birmingham')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-ted-stevens-anchorage/':
                    row[0] = 'Anchorage'
                    nodes.append('Anchorage')
                    america.append('Anchorage')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-de-kingman-arizona/':
                    row[0] = 'Kingman'
                    nodes.append('Kingman')
                    america.append('Kingman')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-phoenix-sky-harbor/':
                    row[0] ='Maricopa'
                    nodes.append('Maricopa')
                    america.append('Maricopa')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-regional-de-prescott/':
                    row[0] = 'Prescott'
                    nodes.append('Prescott')
                    america.append('Prescott')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-tucson/':
                    row[0] = 'Tucson'
                    nodes.append('Tucson')
                    america.append('Tucson')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-fresno-yosemite/':
                    row[0] = 'Fresno'
                    nodes.append('Fresno')
                    america.append('Fresno')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-los-angeles/':
                    row[0] = 'LosAngeles'
                    nodes.append('LosAngeles')
                    america.append('LosAngeles')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-de-long-beach/':
                    row[0] = 'LongBeach'
                    nodes.append('LongBeach')
                    america.append('LongBeach')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-oakland/':
                    row[0] = 'Oakland'
                    nodes.append('Oakland')
                    america.append('Oakland')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-la-ontario/':
                    row[0] = 'Ontario'
                    nodes.append('Ontario')
                    america.append('Ontario')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-john-wayne/':
                    row[0] = 'SantaAna'
                    nodes.append('SantaAna')
                    america.append('SantaAna')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-palm-springs/':
                    row[0] = 'PalmSprings'
                    nodes.append('PalmSprings')
                    america.append('PalmSprings')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-sacramento/':
                    row[0] = 'Sacramento'
                    nodes.append('Sacramento')
                    america.append('Sacramento')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-san-bernardino/':
                    row[0] = 'SanBernardino'
                    nodes.append('SanBernardino')
                    america.append('SanBernardino')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-san-diego/':
                    row[0] = 'SanDiego'
                    nodes.append('SanDiego')
                    america.append('SanDiego')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-mcclellan-palomar/':
                    row[0] = 'Carlsbad'
                    nodes.append('Carlsbad')
                    america.appedn('Carlsbad')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-de-montgomery-field/':
                    row[0] = 'SanDiego'
                    nodes.append('SanDiego')
                    america.append('SanDiego')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-san-francisco/':
                    row[0] = 'SanFrancisco'
                    nodes.append('SanFrancisco')
                    america.append('SanFrancisco')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-san-jose/':
                    row[0] = 'SanJose'
                    nodes.append('SanJose')
                    america.append('SanJose')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-charlotte-douglas/':
                    row[0] = 'Charlotte'
                    nodes.append('Charlotte')
                    america.append('Charlotte')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-raleigh-durham/':
                    row[0] = 'Morrisville'
                    nodes.append('Morrisville')
                    america.append('Morrisville')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-de-colorado-springs/':
                    row[0] = 'ColoradoSprings'
                    nodes.append('ColoradoSprings')
                    america.append('ColoradoSprings')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-denver/':
                    row[0] = 'Denver'
                    nodes.append('Denver')
                    america.append('Denver')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-daytona-beach/':
                    row[0] = 'DaytonaBeach'
                    nodes.append('DaytonaBeach')
                    america.append('DaytonaBeach')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-fort-lauderdale-hollywood/':
                    row[0] = 'FortLauderdale'
                    nodes.append('FortLauderdale')
                    america.append('FortLauderdale')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-melbourne/':
                    row[0] = 'Melbourne'
                    nodes.append('Melbourne')
                    america.append('Melbourne')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-miami/':
                    row[0] = 'Miami'
                    nodes.append('Miami')
                    america.append('Miami')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-jacksonville/':
                    row[0] = 'Duval'
                    nodes.append('Duval')
                    america.append('Duval')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-southwest-florida/':
                    row[0] = 'FortMyers'
                    nodes.append('FortMyers')
                    america.append('FortMyers')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-sanford/':
                    row[0] = 'Sanford'
                    nodes.append('Sanford')
                    america.append('Sanford')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-orlando/':
                    row[0] = 'Orlando'
                    nodes.append('Orlando')
                    america.append('Orlando')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-tampa/':
                    row[0] = 'Tampa'
                    nodes.append('Tampa')
                    america.append('Tampa')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-palm-beach/':
                    row[0] = 'WestPalmBeach'
                    nodes.append('WestPalmBeach')
                    america.append('WestPalmBeach')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-hartsfield-jackson/':
                    row[0] = 'Atlanta'
                    nodes.append('Atlanta')
                    america.append('Atlanta')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-savannah-hilton-head/':
                    row[0] = 'Savannah'
                    nodes.append('Savannah')
                    america.append('Savannah')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-honolulu/':
                    row[0] = 'Honolulu'
                    nodes.append('Honolulu')
                    america.append('Honolulu')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-chicago-midway/':
                    row[0] = 'Midway'
                    nodes.append('Midway')
                    america.append('Midway')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-chicago-ohare/':
                    row[0] = 'Chicago'
                    nodes.append('Chicago')
                    america.append('Chicago')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-indianapolis/':
                    row[0] = 'Indianápolis'
                    nodes.append('Indianápolis')
                    america.append('Indianápolis')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-cincinnati-kentucky-norte/':
                    row[0] = 'Cincinnati'
                    nodes.append('Cincinnati')
                    america.append('Cincinnati')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-louisville/':
                    row[0] = 'Louisville'
                    nodes.append('Louisville')
                    america.append('Louisville')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-regional-de-lafayette/':
                    row[0] = 'Lafayette'
                    nodes.append('Lafayette')
                    america.append('Lafayette')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-louis-armstrong/':
                    row[0] = 'NewOrleans'
                    nodes.append('NewOrleans')
                    america.append('NewOrleans')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-baltimore-washington/':
                    row[0] = 'Baltimore'
                    nodes.append('Baltimore')
                    america.append('Baltimore')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-logan/':
                    row[0] = 'Boston'
                    nodes.append('Boston')
                    america.append('Boston')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-detroit/':
                    row[0] = 'Detroit'
                    nodes.append('Detroit')
                    america.append('Detroit')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-kalamazoo/':
                    row[0] = 'Michigan'
                    nodes.append('Michigan')
                    america.append('Michigan')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-capital-region/':
                    row[0] = 'CapitolCity'
                    nodes.append('CapitolCity')
                    america.append('CapitolCity')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-minneapolis-saint-paul/':
                    row[0] = 'StPaul'
                    nodes.append('StPaul')
                    america.append('StPaul')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-kansas-city/':
                    row[0] = 'KansasCity'
                    nodes.append('KansasCity')
                    america.append('KansasCity')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-saint-louis-lambert/':
                    row[0] = 'SanLuis'
                    nodes.append('SanLuis')
                    america.append('SanLuis')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-mccarran/':
                    row[0] = 'LasVegas'
                    nodes.append('LasVegas')
                    america.append('LasVegas')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-buffalo-niagara/':
                    row[0] = 'Cheektowaga'
                    nodes.append('Cheektowaga')
                    america.append('Cheektowaga')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-libertad-de-newark/':
                    row[0] = 'Newark'
                    nodes.append('Newark')
                    america.append('Newark')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-john-f-kennedy/':
                    row[0] = 'NewYork'
                    nodes.append('NewYork')
                    america.append('NewYork')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-laguardia/':
                    row[0] = 'NewYork'
                    nodes.append('NewYork')
                    america.append('NewYork')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-albany-alb/':
                    row[0] = 'Albany'
                    nodes.append('Albany')
                    america.append('Albany')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-albuquerque-sunport/':
                    row[0] = 'Albuquerque'
                    nodes.append('Albuquerque')
                    america.append('Albuquerque')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-cleveland-hopkins/':
                    row[0] = 'Cleveland'
                    nodes.append('Cleveland')
                    america.append('Cleveland')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-portland/':
                    row[0] = 'Portland'
                    nodes.append('Portland')
                    america.append('Portland')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-filadelfia/':
                    row[0] = 'Philadelphia'
                    nodes.append('Philadelphia')
                    america.append('Philadelphia')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-memphis/':
                    row[0] = 'Memphis'
                    nodes.append('Memphis')
                    america.appen('Memphis')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-austin-bergstrom/':
                    row[0] = 'Austin'
                    nodes.append('Austin')
                    america.appen('Austin')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-dallas-fort-worth/':
                    row[0] = 'Dallas-FortWorth'
                    nodes.append('Dallas-FortWorth')
                    america.append('Dallas-FortWorth')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-de-dallas-love-field/':
                    row[0] = 'Dallas'
                    nodes.append('Dallas')
                    america.append('Dallas')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-laredo/':
                    row[0] = 'Laredo'
                    nodes.append('Laredo')
                    america.append('Laredo')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-mc-allen-miller/':
                    row[0] = 'McAllen'
                    nodes.append('McAllen')
                    america.append('McAllen')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-intercontinental-george-bush/':
                    row[0] = 'Houston'
                    nodes.append('Houston')
                    america.append('Houston')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-salt-lake-city/':
                    row[0] = 'SaltLakeCity'
                    nodes.append('SaltLakeCity')
                    america.append('SaltLakeCity')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-municipal-de-st-george/':
                    row[0] = 'StGeorge'
                    nodes.append('StGeorge')
                    america.append('StGeorge')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-de-seattle-tacoma/':
                    row[0] = 'Seattle'
                    nodes.append('Seattle')
                    america.append('Seattle')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-washington-dulles/':
                    row[0] = 'Dulles'
                    nodes.append('Dulles')
                    america.append('Dulles')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-nacional-ronald-reagan-de-washington/':
                    row[0] = 'Washington'
                    nodes.append('Washington')
                    america.append('Washington')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-internacional-general-mitchell/':
                    row[0] = 'Milwaukee'
                    nodes.append('Milwaukee')
                    america.append('Milwaukee')

                if row[0] == 'https://www.aeropuertos.net/aeropuerto-de-rock-springs-sweetwater-county/':
                    row[0] = 'RockSprings'
                    nodes.append('RockSprings')
                    america.append('RockSprings')

                if row[0] == 'Edmonton':
                    if not place in g_Edmonton and place != 'no':
                        g_Edmonton[place] = 1
                    else:
                        g_Edmonton[place] += 1

                if row[0] == 'Ottawa':
                    if not place in g_Ottawa and place != 'no':
                        g_Ottawa[place] = 1
                    else:
                        g_Ottawa[place] += 1

                if row[0] == 'GrandePrairie':
                    if not place in g_GrandePrairie and place != 'no':
                        g_GrandePrairie[place] = 1
                    else:
                        g_GrandePrairie[place] += 1

                if row[0] == 'Dorval':
                    if not place in g_Dorval and place != 'no':
                        g_Dorval[place] = 1
                    else:
                        g_Dorval[place] += 1

                if row[0] == 'Mirabel':
                    if not place in g_Mirabel and place != 'no':
                        g_Mirabel[place] = 1
                    else:
                        g_Mirabel[place] += 1

                if row[0] == 'Montreal':
                    if not place in g_Montreal and place != 'no':
                        g_Montreal[place] = 1
                    else:
                        g_Montreal[place] += 1

                if row[0] == 'Terranova':
                    if not place in g_Terranova and place != 'no':
                        g_Terranova[place] = 1
                    else:
                        g_Terranova[place] += 1

                if row[0] == 'Toronto':
                    if not place in g_Toronto and place != 'no':
                        g_Toronto[place] = 1
                    else:
                        g_Toronto[place] += 1

                if row[0] == 'Vancouver':
                    if not place in g_Vancouver and place != 'no':
                        g_Vancouver[place] = 1
                    else:
                        g_Vancouver[place] += 1

                if row[0] == 'Winnipeg':
                    if not place in g_Winnipeg and place != 'no':
                        g_Winnipeg[place] = 1
                    else:
                        g_Winnipeg[place] += 1

                if row[0] == 'Birmingham':
                    if not place in g_Birmingham and place != 'no':
                        g_Birmingham[place] = 1
                    else:
                        g_Birmingham[place] += 1

                if row[0] == 'Anchorage':
                    if not place in g_Anchorage and place != 'no':
                        g_Anchorage[place] = 1
                    else:
                        g_Anchorage[place] += 1

                if row[0] == 'Kingman':
                    if not place in g_Kingman and place != 'no':
                        g_Kingman[place] = 1
                    else:
                        g_Kingman[place] += 1

                if row[0] == 'Maricopa':
                    if not place in g_Maricopa and place != 'no':
                        g_Maricopa[place] = 1
                    else:
                        g_Maricopa[place] += 1

                if row[0] == 'Prescott':
                    if not place in g_Prescott and place != 'no':
                        g_Prescott[place] = 1
                    else:
                        g_Prescott[place] += 1

                if row[0] == 'Tucson':
                    if not place in g_Tucson and place != 'no':
                        g_Tucson[place] = 1
                    else:
                        g_Tucson[place] += 1

                if row[0] == 'Fresno':
                    if not place in g_Fresno and place != 'no':
                        g_Fresno[place] = 1
                    else:
                        g_Fresno[place] += 1

                if row[0] == 'LosAngeles':
                    if not place in g_LosAngeles and place != 'no':
                        g_LosAngeles[place] = 1
                    else:
                        g_LosAngeles[place] += 1

                if row[0] == 'LongBeach':
                    if not place in g_LongBeach and place != 'no':
                        g_LongBeach[place] = 1
                    else:
                        g_LongBeach[place] += 1

                if row[0] == 'Oakland':
                    if not place in g_Oakland and place != 'no':
                        g_Oakland[place] = 1
                    else:
                        g_Oakland[place] += 1

                if row[0] == 'Ontario':
                    if not place in g_Ontario and place != 'no':
                        g_Ontario[place] = 1
                    else:
                        g_Ontario[place] += 1

                if row[0] == 'PalmSprings':
                    if not place in g_PalmSprings and place != 'no':
                        g_PalmSprings[place] = 1
                    else:
                        g_PalmSprings[place] += 1

                if row[0] == 'Sacramento':
                    if not place in g_Sacramento and place != 'no':
                        g_Sacramento[place] = 1
                    else:
                        g_Sacramento[place] += 1

                if row[0] == 'SanBernardino':
                    if not place in g_SanBernardino and place != 'no':
                        g_SanBernardino[place] = 1
                    else:
                        g_SanBernardino[place] += 1

                if row[0] == 'SanDiego':
                    if not place in g_SanDiego and place != 'no':
                        g_SanDiego[place] = 1
                    else:
                        g_SanDiego[place] += 1

                if row[0] == 'Carlsbad':
                    if not place in g_Carlsbad and place != 'no':
                        g_Carlsbad[place] = 1
                    else:
                        g_Carlsbad[place] += 1

                if row[0] == 'SanDiego':
                    if not place in g_SanDiego and place != 'no':
                        g_SanDiego[place] = 1
                    else:
                        g_SanDiego[place] += 1

                if row[0] == 'SanFrancisco':
                    if not place in g_SanFrancisco and place != 'no':
                        g_SanFrancisco[place] = 1
                    else:
                        g_SanFrancisco[place] += 1

                if row[0] == 'SanJose':
                    if not place in g_SanJose and place != 'no':
                        g_SanJose[place] = 1
                    else:
                        g_SanJose[place] += 1

                if row[0] == 'Charlotte':
                    if not place in g_Charlotte and place != 'no':
                        g_Charlotte[place] = 1
                    else:
                        g_Charlotte[place] += 1

                if row[0] == 'Morrisville':
                    if not place in g_Morrisville and place != 'no':
                        g_Morrisville[place] = 1
                    else:
                        g_Morrisville[place] += 1

                if row[0] == 'ColoradoSprings':
                    if not place in g_ColoradoSprings and place != 'no':
                        g_ColoradoSprings[place] = 1
                    else:
                        g_ColoradoSprings[place] += 1

                if row[0] == 'Denver':
                    if not place in g_Denver and place != 'no':
                        g_Denver[place] = 1
                    else:
                        g_Denver[place] += 1

                if row[0] == 'DaytonaBeach':
                    if not place in g_DaytonaBeach and place != 'no':
                        g_DaytonaBeach[place] = 1
                    else:
                        g_DaytonaBeach[place] += 1

                if row[0] == 'FortLauderdale':
                    if not place in g_FortLauderdale and place != 'no':
                        g_FortLauderdale[place] = 1
                    else:
                        g_FortLauderdale[place] += 1

                if row[0] == 'Melbourne':
                    if not place in g_Melbourne and place != 'no':
                        g_Melbourne[place] = 1
                    else:
                        g_Melbourne[place] += 1

                if row[0] == 'Miami':
                    if not place in g_Miami and place != 'no':
                        g_Miami[place] = 1
                    else:
                        g_Miami[place] += 1

                if row[0] == 'Duval':
                    if not place in g_Duval and place != 'no':
                        g_Duval[place] = 1
                    else:
                        g_Duval[place] += 1

                if row[0] == 'FortMyers':
                    if not place in g_FortMyers and place != 'no':
                        g_FortMyers[place] = 1
                    else:
                        g_FortMyers[place] += 1

                if row[0] == 'Sanford':
                    if not place in g_Sanford and place != 'no':
                        g_Sanford[place] = 1
                    else:
                        g_Sanford[place] += 1

                if row[0] == 'Orlando':
                    if not place in g_Orlando and place != 'no':
                        g_Orlando[place] = 1
                    else:
                        g_Orlando[place] += 1

                if row[0] == 'Tampa':
                    if not place in g_Tampa and place != 'no':
                        g_Tampa[place] = 1
                    else:
                        g_Tampa[place] += 1

                if row[0] == 'WestPalmBeach':
                    if not place in g_WestPalmBeach and place != 'no':
                        g_WestPalmBeach[place] = 1
                    else:
                        g_WestPalmBeach[place] += 1

                if row[0] == 'Atlanta':
                    if not place in g_Atlanta and place != 'no':
                        g_Atlanta[place] = 1
                    else:
                        g_Atlanta[place] += 1

                if row[0] == 'Savannah':
                    if not place in g_Savannah and place != 'no':
                        g_Savannah[place] = 1
                    else:
                        g_Savannah[place] += 1

                if row[0] == 'Honolulu':
                    if not place in g_Honolulu and place != 'no':
                        g_Honolulu[place] = 1
                    else:
                        g_Honolulu[place] += 1

                if row[0] == 'Midway':
                    if not place in g_Midway and place != 'no':
                        g_Midway[place] = 1
                    else:
                        g_Midway[place] += 1

                if row[0] == 'Chicago':
                    if not place in g_Chicago and place != 'no':
                        g_Chicago[place] = 1
                    else:
                        g_Chicago[place] += 1

                if row[0] == 'Indianápolis':
                    if not place in g_Indianápolis and place != 'no':
                        g_Indianápolis[place] = 1
                    else:
                        g_Indianápolis[place] += 1

                if row[0] == 'Cincinnati':
                    if not place in g_Cincinnati and place != 'no':
                        g_Cincinnati[place] = 1
                    else:
                        g_Cincinnati[place] += 1

                if row[0] == 'Louisville':
                    if not place in g_Louisville and place != 'no':
                        g_Louisville[place] = 1
                    else:
                        g_Louisville[place] += 1

                if row[0] == 'Lafayette':
                    if not place in g_Lafayette and place != 'no':
                        g_Lafayette[place] = 1
                    else:
                        g_Lafayette[place] += 1

                if row[0] == 'NewOrleans':
                    if not place in g_NewOrleans and place != 'no':
                        g_NewOrleans[place] = 1
                    else:
                        g_NewOrleans[place] += 1

                if row[0] == 'Baltimore':
                    if not place in g_Baltimore and place != 'no':
                        g_Baltimore[place] = 1
                    else:
                        g_Baltimore[place] += 1

                if row[0] == 'Boston':
                    if not place in g_Boston and place != 'no':
                        g_Boston[place] = 1
                    else:
                        g_Boston[place] += 1

                if row[0] == 'Detroit':
                    if not place in g_Detroit and place != 'no':
                        g_Detroit[place] = 1
                    else:
                        g_Detroit[place] += 1

                if row[0] == 'Michigan':
                    if not place in g_Michigan and place != 'no':
                        g_Michigan[place] = 1
                    else:
                        g_Michigan[place] += 1

                if row[0] == 'CapitolCity':
                    if not place in g_CapitolCity and place != 'no':
                        g_CapitolCity[place] = 1
                    else:
                        g_CapitolCity[place] += 1

                if row[0] == 'StPaul':
                    if not place in g_StPaul and place != 'no':
                        g_StPaul[place] = 1
                    else:
                        g_StPaul[place] += 1

                if row[0] == 'KansasCity':
                    if not place in g_KansasCity and place != 'no':
                        g_KansasCity[place] = 1
                    else:
                        g_KansasCity[place] += 1

                if row[0] == 'SanLuis':
                    if not place in g_SanLuis and place != 'no':
                        g_SanLuis[place] = 1
                    else:
                        g_SanLuis[place] += 1

                if row[0] == 'LasVegas':
                    if not place in g_LasVegas and place != 'no':
                        g_LasVegas[place] = 1
                    else:
                        g_LasVegas[place] += 1

                if row[0] == 'Cheektowaga':
                    if not place in g_Cheektowaga and place != 'no':
                        g_Cheektowaga[place] = 1
                    else:
                        g_Cheektowaga[place] += 1

                if row[0] == 'Newark':
                    if not place in g_Newark and place != 'no':
                        g_Newark[place] = 1
                    else:
                        g_Newark[place] += 1

                if row[0] == 'NewYork':
                    if not place in g_NewYork and place != 'no':
                        g_NewYork[place] = 1
                    else:
                        g_NewYork[place] += 1

                if row[0] == 'Albany':
                    if not place in g_Albany and place != 'no':
                        g_Albany[place] = 1
                    else:
                        g_Albany[place] += 1

                if row[0] == 'Albuquerque':
                    if not place in g_Albuquerque and place != 'no':
                        g_Albuquerque[place] = 1
                    else:
                        g_Albuquerque[place] += 1

                if row[0] == 'Cleveland':
                    if not place in g_Cleveland and place != 'no':
                        g_Cleveland[place] = 1
                    else:
                        g_Cleveland[place] += 1

                if row[0] == 'Portland':
                    if not place in g_Portland and place != 'no':
                        g_Portland[place] = 1
                    else:
                        g_Portland[place] += 1

                if row[0] == 'Philadelphia':
                    if not place in g_Philadelphia and place != 'no':
                        g_Philadelphia[place] = 1
                    else:
                        g_Philadelphia[place] += 1

                if row[0] == 'Memphis':
                    if not place in g_Memphis and place != 'no':
                        g_Memphis[place] = 1
                    else:
                        g_Memphis[place] += 1

                if row[0] == 'Austin':
                    if not place in g_Austin and place != 'no':
                        g_Austin[place] = 1
                    else:
                        g_Austin[place] += 1

                if row[0] == 'Dallas_FortWorth':
                    if not place in g_Dallas_FortWorth and place != 'no':
                        g_Dallas_FortWorth[place] = 1
                    else:
                        g_Dallas_FortWorth[place] += 1

                if row[0] == 'Dallas':
                    if not place in g_Dallas and place != 'no':
                        g_Dallas[place] = 1
                    else:
                        g_Dallas[place] += 1

                if row[0] == 'Laredo':
                    if not place in g_Laredo and place != 'no':
                        g_Laredo[place] = 1
                    else:
                        g_Laredo[place] += 1

                if row[0] == 'McAllen':
                    if not place in g_McAllen and place != 'no':
                        g_McAllen[place] = 1
                    else:
                        g_McAllen[place] += 1

                if row[0] == 'Houston':
                    if not place in g_Houston and place != 'no':
                        g_Houston[place] = 1
                    else:
                        g_Houston[place] += 1

                if row[0] == 'SaltLakeCity':
                    if not place in g_SaltLakeCity and place != 'no':
                        g_SaltLakeCity[place] = 1
                    else:
                        g_SaltLakeCity[place] += 1

                if row[0] == 'StGeorge':
                    if not place in g_StGeorge and place != 'no':
                        g_StGeorge[place] = 1
                    else:
                        g_StGeorge[place] += 1

                if row[0] == 'Seattle':
                    if not place in g_Seattle and place != 'no':
                        g_Seattle[place] = 1
                    else:
                        g_Seattle[place] += 1

                if row[0] == 'Dulles':
                    if not place in g_Dulles and place != 'no':
                        g_Dulles[place] = 1
                    else:
                        g_Dulles[place] += 1

                if row[0] == 'Washington':
                    if not place in g_Washington and place != 'no':
                        g_Washington[place] = 1
                    else:
                        g_Washington[place] += 1

                if row[0] == 'Milwaukee':
                    if not place in g_Milwaukee and place != 'no':
                        g_Milwaukee[place] = 1
                    else:
                        g_Milwaukee[place] += 1

                if row[0] == 'RockSprings':
                    if not place in g_RockSprings and place != 'no':
                        g_RockSprings[place] = 1
                    else:
                        g_RockSprings[place] += 1

                if row[0] == 'Veracruz':
                    if not place in g_Veracruz and place != 'no':
                        g_Veracruz[place] = 1
                    else:
                        g_Veracruz[place] += 1

                if row[0] == 'Mérida':
                    if not place in g_Mérida and place != 'no':
                        g_Mérida[place] = 1
                    else:
                        g_Mérida[place] += 1

                if row[0] == 'Tampico':
                    if not place in g_Tampico and place != 'no':
                        g_Tampico[place] = 1
                    else:
                        g_Tampico[place] += 1

                if row[0] == 'Tamaulipas':
                    if not place in g_Tamaulipas and place != 'no':
                        g_Tamaulipas[place] = 1
                    else:
                        g_Tamaulipas[place] += 1

                if row[0] == 'Villahermosa':
                    if not place in g_Villahermosa and place != 'no':
                        g_Villahermosa[place] = 1
                    else:
                        g_Villahermosa[place] += 1

                if row[0] == 'Hermosillo':
                    if not place in g_Hermosillo and place != 'no':
                        g_Hermosillo[place] = 1
                    else:
                        g_Hermosillo[place] += 1

                if row[0] == 'SanLuisPotosí':
                    if not place in g_SanLuisPotosí and place != 'no':
                        g_SanLuisPotosí[place] = 1
                    else:
                        g_SanLuisPotosí[place] += 1

                if row[0] == 'Mazatlán':
                    if not place in g_Mazatlán and place != 'no':
                        g_Mazatlán[place] = 1
                    else:
                        g_Mazatlán[place] += 1

                if row[0] == 'SanMigueldeCozumel':
                    if not place in g_SanMigueldeCozumel and place != 'no':
                        g_SanMigueldeCozumel[place] = 1
                    else:
                        g_SanMigueldeCozumel[place] += 1

                if row[0] == 'Cancun':
                    if not place in g_Cancun and place != 'no':
                        g_Cancun[place] = 1
                    else:
                        g_Cancun[place] += 1

                if row[0] == 'Queretana':
                    if not place in g_Queretana and place != 'no':
                        g_Queretana[place] = 1
                    else:
                        g_Queretana[place] += 1

                if row[0] == 'Puebla':
                    if not place in g_Puebla and place != 'no':
                        g_Puebla[place] = 1
                    else:
                        g_Puebla[place] += 1

                if row[0] == 'Huatulco':
                    if not place in g_Huatulco and place != 'no':
                        g_Huatulco[place] = 1
                    else:
                        g_Huatulco[place] += 1

                if row[0] == 'Oaxaca':
                    if not place in g_Oaxaca and place != 'no':
                        g_Oaxaca[place] = 1
                    else:
                        g_Oaxaca[place] += 1

                if row[0] == 'NuevoLeón':
                    if not place in g_NuevoLeón and place != 'no':
                        g_NuevoLeón[place] = 1
                    else:
                        g_NuevoLeón[place] += 1

                if row[0] == 'PuertoVallarta':
                    if not place in g_PuertoVallarta and place != 'no':
                        g_PuertoVallarta[place] = 1
                    else:
                        g_PuertoVallarta[place] += 1

                if row[0] == 'Guadalajara':
                    if not place in g_Guadalajara and place != 'no':
                        g_Guadalajara[place] = 1
                    else:
                        g_Guadalajara[place] += 1

                if row[0] == 'Acapulco':
                    if not place in g_Acapulco and place != 'no':
                        g_Acapulco[place] = 1
                    else:
                        g_Acapulco[place] += 1

                if row[0] == 'Silao':
                    if not place in g_Silao and place != 'no':
                        g_Silao[place] = 1
                    else:
                        g_Silao[place] += 1

                if row[0] == 'SanPedro':
                    if not place in g_SanPedro and place != 'no':
                        g_SanPedro[place] = 1
                    else:
                        g_SanPedro[place] += 1

                if row[0] == 'Durango':
                    if not place in g_Durango and place != 'no':
                        g_Durango[place] = 1
                    else:
                        g_Durango[place] += 1

                if row[0] == 'Culiacán':
                    if not place in g_Culiacán and place != 'no':
                        g_Culiacán[place] = 1
                    else:
                        g_Culiacán[place] += 1

                if row[0] == 'Chihuahua':
                    if not place in g_Chihuahua and place != 'no':
                        g_Chihuahua[place] = 1
                    else:
                        g_Chihuahua[place] += 1

                if row[0] == 'ElPaso':
                    if not place in g_ElPaso and place != 'no':
                        g_ElPaso[place] = 1
                    else:
                        g_ElPaso[place] += 1

                if row[0] == 'TuxtlaGutiérrez':
                    if not place in g_TuxtlaGutiérrez and place != 'no':
                        g_TuxtlaGutiérrez[place] = 1
                    else:
                        g_TuxtlaGutiérrez[place] += 1

                if row[0] == 'CiudaddelCarmen':
                    if not place in g_CiudaddelCarmen and place != 'no':
                        g_CiudaddelCarmen[place] = 1
                    else:
                        g_CiudaddelCarmen[place] += 1

                if row[0] == 'SanJosédelCabo':
                    if not place in g_SanJosédelCabo and place != 'no':
                        g_SanJosédelCabo[place] = 1
                    else:
                        g_SanJosédelCabo[place] += 1

                if row[0] == 'LaPaz':
                    if not place in g_LaPaz and place != 'no':
                        g_LaPaz[place] = 1
                    else:
                        g_LaPaz[place] += 1

                if row[0] == 'Tijuana':
                    if not place in g_Tijuana and place != 'no':
                        g_Tijuana[place] = 1
                    else:
                        g_Tijuana[place] += 1

                if row[0] == 'Mexicali':
                    if not place in g_Mexicali and place != 'no':
                        g_Mexicali[place] = 1
                    else:
                        g_Mexicali[place] += 1

                if row[0] == 'Aguascalientes':
                    if not place in g_Aguascalientes and place != 'no':
                        g_Aguascalientes[place] = 1
                    else:
                        g_Aguascalientes[place] += 1

                if row[0] == 'CiudaddeMéxico':
                    if not place in g_CiudaddeMéxico and place != 'no':
                        g_CiudaddeMéxico[place] = 1
                    else:
                        g_CiudaddeMéxico[place] += 1

                if row[3] != 'lugar' and row[3].replace('\n', '').replace(' ', '') != 'Destino':
                    m = (row[3].replace('\n', '').replace(' ', ''))
                    nodes.append(m[5:])

        except:
            pass

with open('caanda.csv', 'r') as data:
    spamreader = csv.reader(data)


    for row in spamreader:

        try:

            if row[1] == 'salida':

                m = (row[3].replace('\n', '').replace(' ', ''))
                place = m[5:]


                if row[0] == 'Edmonton':
                    if not place in g_Edmonton and place != 'no':
                        g_Edmonton[place] = 1
                    else:
                        g_Edmonton[place] += 1

                if row[0] == 'Ottawa':
                    if not place in g_Ottawa and place != 'no':
                        g_Ottawa[place] = 1
                    else:
                        g_Ottawa[place] += 1

                if row[0] == 'GrandePrairie':
                    if not place in g_GrandePrairie and place != 'no':
                        g_GrandePrairie[place] = 1
                    else:
                        g_GrandePrairie[place] += 1

                if row[0] == 'Dorval':
                    if not place in g_Dorval and place != 'no':
                        g_Dorval[place] = 1
                    else:
                        g_Dorval[place] += 1

                if row[0] == 'Mirabel':
                    if not place in g_Mirabel and place != 'no':
                        g_Mirabel[place] = 1
                    else:
                        g_Mirabel[place] += 1

                if row[0] == 'Montreal':
                    if not place in g_Montreal and place != 'no':
                        g_Montreal[place] = 1
                    else:
                        g_Montreal[place] += 1

                if row[0] == 'Terranova':
                    if not place in g_Terranova and place != 'no':
                        g_Terranova[place] = 1
                    else:
                        g_Terranova[place] += 1

                if row[0] == 'Toronto':
                    if not place in g_Toronto and place != 'no':
                        g_Toronto[place] = 1
                    else:
                        g_Toronto[place] += 1

                if row[0] == 'Vancouver':
                    if not place in g_Vancouver and place != 'no':
                        g_Vancouver[place] = 1
                    else:
                        g_Vancouver[place] += 1

                if row[0] == 'Winnipeg':
                    if not place in g_Winnipeg and place != 'no':
                        g_Winnipeg[place] = 1
                    else:
                        g_Winnipeg[place] += 1

                if row[0] == 'Birmingham':
                    if not place in g_Birmingham and place != 'no':
                        g_Birmingham[place] = 1
                    else:
                        g_Birmingham[place] += 1

                if row[0] == 'Anchorage':
                    if not place in g_Anchorage and place != 'no':
                        g_Anchorage[place] = 1
                    else:
                        g_Anchorage[place] += 1

                if row[0] == 'Kingman':
                    if not place in g_Kingman and place != 'no':
                        g_Kingman[place] = 1
                    else:
                        g_Kingman[place] += 1

                if row[0] == 'Maricopa':
                    if not place in g_Maricopa and place != 'no':
                        g_Maricopa[place] = 1
                    else:
                        g_Maricopa[place] += 1

                if row[0] == 'Prescott':
                    if not place in g_Prescott and place != 'no':
                        g_Prescott[place] = 1
                    else:
                        g_Prescott[place] += 1

                if row[0] == 'Tucson':
                    if not place in g_Tucson and place != 'no':
                        g_Tucson[place] = 1
                    else:
                        g_Tucson[place] += 1

                if row[0] == 'Fresno':
                    if not place in g_Fresno and place != 'no':
                        g_Fresno[place] = 1
                    else:
                        g_Fresno[place] += 1

                if row[0] == 'LosAngeles':
                    if not place in g_LosAngeles and place != 'no':
                        g_LosAngeles[place] = 1
                    else:
                        g_LosAngeles[place] += 1

                if row[0] == 'LongBeach':
                    if not place in g_LongBeach and place != 'no':
                        g_LongBeach[place] = 1
                    else:
                        g_LongBeach[place] += 1

                if row[0] == 'Oakland':
                    if not place in g_Oakland and place != 'no':
                        g_Oakland[place] = 1
                    else:
                        g_Oakland[place] += 1

                if row[0] == 'Ontario':
                    if not place in g_Ontario and place != 'no':
                        g_Ontario[place] = 1
                    else:
                        g_Ontario[place] += 1

                if row[0] == 'PalmSprings':
                    if not place in g_PalmSprings and place != 'no':
                        g_PalmSprings[place] = 1
                    else:
                        g_PalmSprings[place] += 1

                if row[0] == 'Sacramento':
                    if not place in g_Sacramento and place != 'no':
                        g_Sacramento[place] = 1
                    else:
                        g_Sacramento[place] += 1

                if row[0] == 'SanBernardino':
                    if not place in g_SanBernardino and place != 'no':
                        g_SanBernardino[place] = 1
                    else:
                        g_SanBernardino[place] += 1

                if row[0] == 'SanDiego':
                    if not place in g_SanDiego and place != 'no':
                        g_SanDiego[place] = 1
                    else:
                        g_SanDiego[place] += 1

                if row[0] == 'Carlsbad':
                    if not place in g_Carlsbad and place != 'no':
                        g_Carlsbad[place] = 1
                    else:
                        g_Carlsbad[place] += 1

                if row[0] == 'SanDiego':
                    if not place in g_SanDiego and place != 'no':
                        g_SanDiego[place] = 1
                    else:
                        g_SanDiego[place] += 1

                if row[0] == 'SanFrancisco':
                    if not place in g_SanFrancisco and place != 'no':
                        g_SanFrancisco[place] = 1
                    else:
                        g_SanFrancisco[place] += 1

                if row[0] == 'SanJose':
                    if not place in g_SanJose and place != 'no':
                        g_SanJose[place] = 1
                    else:
                        g_SanJose[place] += 1

                if row[0] == 'Charlotte':
                    if not place in g_Charlotte and place != 'no':
                        g_Charlotte[place] = 1
                    else:
                        g_Charlotte[place] += 1

                if row[0] == 'Morrisville':
                    if not place in g_Morrisville and place != 'no':
                        g_Morrisville[place] = 1
                    else:
                        g_Morrisville[place] += 1

                if row[0] == 'ColoradoSprings':
                    if not place in g_ColoradoSprings and place != 'no':
                        g_ColoradoSprings[place] = 1
                    else:
                        g_ColoradoSprings[place] += 1

                if row[0] == 'Denver':
                    if not place in g_Denver and place != 'no':
                        g_Denver[place] = 1
                    else:
                        g_Denver[place] += 1

                if row[0] == 'DaytonaBeach':
                    if not place in g_DaytonaBeach and place != 'no':
                        g_DaytonaBeach[place] = 1
                    else:
                        g_DaytonaBeach[place] += 1

                if row[0] == 'FortLauderdale':
                    if not place in g_FortLauderdale and place != 'no':
                        g_FortLauderdale[place] = 1
                    else:
                        g_FortLauderdale[place] += 1

                if row[0] == 'Melbourne':
                    if not place in g_Melbourne and place != 'no':
                        g_Melbourne[place] = 1
                    else:
                        g_Melbourne[place] += 1

                if row[0] == 'Miami':
                    if not place in g_Miami and place != 'no':
                        g_Miami[place] = 1
                    else:
                        g_Miami[place] += 1

                if row[0] == 'Duval':
                    if not place in g_Duval and place != 'no':
                        g_Duval[place] = 1
                    else:
                        g_Duval[place] += 1

                if row[0] == 'FortMyers':
                    if not place in g_FortMyers and place != 'no':
                        g_FortMyers[place] = 1
                    else:
                        g_FortMyers[place] += 1

                if row[0] == 'Sanford':
                    if not place in g_Sanford and place != 'no':
                        g_Sanford[place] = 1
                    else:
                        g_Sanford[place] += 1

                if row[0] == 'Orlando':
                    if not place in g_Orlando and place != 'no':
                        g_Orlando[place] = 1
                    else:
                        g_Orlando[place] += 1

                if row[0] == 'Tampa':
                    if not place in g_Tampa and place != 'no':
                        g_Tampa[place] = 1
                    else:
                        g_Tampa[place] += 1

                if row[0] == 'WestPalmBeach':
                    if not place in g_WestPalmBeach and place != 'no':
                        g_WestPalmBeach[place] = 1
                    else:
                        g_WestPalmBeach[place] += 1

                if row[0] == 'Atlanta':
                    if not place in g_Atlanta and place != 'no':
                        g_Atlanta[place] = 1
                    else:
                        g_Atlanta[place] += 1

                if row[0] == 'Savannah':
                    if not place in g_Savannah and place != 'no':
                        g_Savannah[place] = 1
                    else:
                        g_Savannah[place] += 1

                if row[0] == 'Honolulu':
                    if not place in g_Honolulu and place != 'no':
                        g_Honolulu[place] = 1
                    else:
                        g_Honolulu[place] += 1

                if row[0] == 'Midway':
                    if not place in g_Midway and place != 'no':
                        g_Midway[place] = 1
                    else:
                        g_Midway[place] += 1

                if row[0] == 'Chicago':
                    if not place in g_Chicago and place != 'no':
                        g_Chicago[place] = 1
                    else:
                        g_Chicago[place] += 1

                if row[0] == 'Indianápolis':
                    if not place in g_Indianápolis and place != 'no':
                        g_Indianápolis[place] = 1
                    else:
                        g_Indianápolis[place] += 1

                if row[0] == 'Cincinnati':
                    if not place in g_Cincinnati and place != 'no':
                        g_Cincinnati[place] = 1
                    else:
                        g_Cincinnati[place] += 1

                if row[0] == 'Louisville':
                    if not place in g_Louisville and place != 'no':
                        g_Louisville[place] = 1
                    else:
                        g_Louisville[place] += 1

                if row[0] == 'Lafayette':
                    if not place in g_Lafayette and place != 'no':
                        g_Lafayette[place] = 1
                    else:
                        g_Lafayette[place] += 1

                if row[0] == 'NewOrleans':
                    if not place in g_NewOrleans and place != 'no':
                        g_NewOrleans[place] = 1
                    else:
                        g_NewOrleans[place] += 1

                if row[0] == 'Baltimore':
                    if not place in g_Baltimore and place != 'no':
                        g_Baltimore[place] = 1
                    else:
                        g_Baltimore[place] += 1

                if row[0] == 'Boston':
                    if not place in g_Boston and place != 'no':
                        g_Boston[place] = 1
                    else:
                        g_Boston[place] += 1

                if row[0] == 'Detroit':
                    if not place in g_Detroit and place != 'no':
                        g_Detroit[place] = 1
                    else:
                        g_Detroit[place] += 1

                if row[0] == 'Michigan':
                    if not place in g_Michigan and place != 'no':
                        g_Michigan[place] = 1
                    else:
                        g_Michigan[place] += 1

                if row[0] == 'CapitolCity':
                    if not place in g_CapitolCity and place != 'no':
                        g_CapitolCity[place] = 1
                    else:
                        g_CapitolCity[place] += 1

                if row[0] == 'StPaul':
                    if not place in g_StPaul and place != 'no':
                        g_StPaul[place] = 1
                    else:
                        g_StPaul[place] += 1

                if row[0] == 'KansasCity':
                    if not place in g_KansasCity and place != 'no':
                        g_KansasCity[place] = 1
                    else:
                        g_KansasCity[place] += 1

                if row[0] == 'SanLuis':
                    if not place in g_SanLuis and place != 'no':
                        g_SanLuis[place] = 1
                    else:
                        g_SanLuis[place] += 1

                if row[0] == 'LasVegas':
                    if not place in g_LasVegas and place != 'no':
                        g_LasVegas[place] = 1
                    else:
                        g_LasVegas[place] += 1

                if row[0] == 'Cheektowaga':
                    if not place in g_Cheektowaga and place != 'no':
                        g_Cheektowaga[place] = 1
                    else:
                        g_Cheektowaga[place] += 1

                if row[0] == 'Newark':
                    if not place in g_Newark and place != 'no':
                        g_Newark[place] = 1
                    else:
                        g_Newark[place] += 1

                if row[0] == 'NewYork':
                    if not place in g_NewYork and place != 'no':
                        g_NewYork[place] = 1
                    else:
                        g_NewYork[place] += 1

                if row[0] == 'Albany':
                    if not place in g_Albany and place != 'no':
                        g_Albany[place] = 1
                    else:
                        g_Albany[place] += 1

                if row[0] == 'Albuquerque':
                    if not place in g_Albuquerque and place != 'no':
                        g_Albuquerque[place] = 1
                    else:
                        g_Albuquerque[place] += 1

                if row[0] == 'Cleveland':
                    if not place in g_Cleveland and place != 'no':
                        g_Cleveland[place] = 1
                    else:
                        g_Cleveland[place] += 1

                if row[0] == 'Portland':
                    if not place in g_Portland and place != 'no':
                        g_Portland[place] = 1
                    else:
                        g_Portland[place] += 1

                if row[0] == 'Philadelphia':
                    if not place in g_Philadelphia and place != 'no':
                        g_Philadelphia[place] = 1
                    else:
                        g_Philadelphia[place] += 1

                if row[0] == 'Memphis':
                    if not place in g_Memphis and place != 'no':
                        g_Memphis[place] = 1
                    else:
                        g_Memphis[place] += 1

                if row[0] == 'Austin':
                    if not place in g_Austin and place != 'no':
                        g_Austin[place] = 1
                    else:
                        g_Austin[place] += 1

                if row[0] == 'Dallas_FortWorth':
                    if not place in g_Dallas_FortWorth and place != 'no':
                        g_Dallas_FortWorth[place] = 1
                    else:
                        g_Dallas_FortWorth[place] += 1

                if row[0] == 'Dallas':
                    if not place in g_Dallas and place != 'no':
                        g_Dallas[place] = 1
                    else:
                        g_Dallas[place] += 1

                if row[0] == 'Laredo':
                    if not place in g_Laredo and place != 'no':
                        g_Laredo[place] = 1
                    else:
                        g_Laredo[place] += 1

                if row[0] == 'McAllen':
                    if not place in g_McAllen and place != 'no':
                        g_McAllen[place] = 1
                    else:
                        g_McAllen[place] += 1

                if row[0] == 'Houston':
                    if not place in g_Houston and place != 'no':
                        g_Houston[place] = 1
                    else:
                        g_Houston[place] += 1

                if row[0] == 'SaltLakeCity':
                    if not place in g_SaltLakeCity and place != 'no':
                        g_SaltLakeCity[place] = 1
                    else:
                        g_SaltLakeCity[place] += 1

                if row[0] == 'StGeorge':
                    if not place in g_StGeorge and place != 'no':
                        g_StGeorge[place] = 1
                    else:
                        g_StGeorge[place] += 1

                if row[0] == 'Seattle':
                    if not place in g_Seattle and place != 'no':
                        g_Seattle[place] = 1
                    else:
                        g_Seattle[place] += 1

                if row[0] == 'Dulles':
                    if not place in g_Dulles and place != 'no':
                        g_Dulles[place] = 1
                    else:
                        g_Dulles[place] += 1

                if row[0] == 'Washington':
                    if not place in g_Washington and place != 'no':
                        g_Washington[place] = 1
                    else:
                        g_Washington[place] += 1

                if row[0] == 'Milwaukee':
                    if not place in g_Milwaukee and place != 'no':
                        g_Milwaukee[place] = 1
                    else:
                        g_Milwaukee[place] += 1

                if row[0] == 'RockSprings':
                    if not place in g_RockSprings and place != 'no':
                        g_RockSprings[place] = 1
                    else:
                        g_RockSprings[place] += 1

                if row[0] == 'Veracruz':
                    if not place in g_Veracruz and place != 'no':
                        g_Veracruz[place] = 1
                    else:
                        g_Veracruz[place] += 1

                if row[0] == 'Mérida':
                    if not place in g_Mérida and place != 'no':
                        g_Mérida[place] = 1
                    else:
                        g_Mérida[place] += 1

                if row[0] == 'Tampico':
                    if not place in g_Tampico and place != 'no':
                        g_Tampico[place] = 1
                    else:
                        g_Tampico[place] += 1

                if row[0] == 'Tamaulipas':
                    if not place in g_Tamaulipas and place != 'no':
                        g_Tamaulipas[place] = 1
                    else:
                        g_Tamaulipas[place] += 1

                if row[0] == 'Villahermosa':
                    if not place in g_Villahermosa and place != 'no':
                        g_Villahermosa[place] = 1
                    else:
                        g_Villahermosa[place] += 1

                if row[0] == 'Hermosillo':
                    if not place in g_Hermosillo and place != 'no':
                        g_Hermosillo[place] = 1
                    else:
                        g_Hermosillo[place] += 1

                if row[0] == 'SanLuisPotosí':
                    if not place in g_SanLuisPotosí and place != 'no':
                        g_SanLuisPotosí[place] = 1
                    else:
                        g_SanLuisPotosí[place] += 1

                if row[0] == 'Mazatlán':
                    if not place in g_Mazatlán and place != 'no':
                        g_Mazatlán[place] = 1
                    else:
                        g_Mazatlán[place] += 1

                if row[0] == 'SanMigueldeCozumel':
                    if not place in g_SanMigueldeCozumel and place != 'no':
                        g_SanMigueldeCozumel[place] = 1
                    else:
                        g_SanMigueldeCozumel[place] += 1

                if row[0] == 'Cancun':
                    if not place in g_Cancun and place != 'no':
                        g_Cancun[place] = 1
                    else:
                        g_Cancun[place] += 1

                if row[0] == 'Queretana':
                    if not place in g_Queretana and place != 'no':
                        g_Queretana[place] = 1
                    else:
                        g_Queretana[place] += 1

                if row[0] == 'Puebla':
                    if not place in g_Puebla and place != 'no':
                        g_Puebla[place] = 1
                    else:
                        g_Puebla[place] += 1

                if row[0] == 'Huatulco':
                    if not place in g_Huatulco and place != 'no':
                        g_Huatulco[place] = 1
                    else:
                        g_Huatulco[place] += 1

                if row[0] == 'Oaxaca':
                    if not place in g_Oaxaca and place != 'no':
                        g_Oaxaca[place] = 1
                    else:
                        g_Oaxaca[place] += 1

                if row[0] == 'NuevoLeón':
                    if not place in g_NuevoLeón and place != 'no':
                        g_NuevoLeón[place] = 1
                    else:
                        g_NuevoLeón[place] += 1

                if row[0] == 'PuertoVallarta':
                    if not place in g_PuertoVallarta and place != 'no':
                        g_PuertoVallarta[place] = 1
                    else:
                        g_PuertoVallarta[place] += 1

                if row[0] == 'Guadalajara':
                    if not place in g_Guadalajara and place != 'no':
                        g_Guadalajara[place] = 1
                    else:
                        g_Guadalajara[place] += 1

                if row[0] == 'Acapulco':
                    if not place in g_Acapulco and place != 'no':
                        g_Acapulco[place] = 1
                    else:
                        g_Acapulco[place] += 1

                if row[0] == 'Silao':
                    if not place in g_Silao and place != 'no':
                        g_Silao[place] = 1
                    else:
                        g_Silao[place] += 1

                if row[0] == 'SanPedro':
                    if not place in g_SanPedro and place != 'no':
                        g_SanPedro[place] = 1
                    else:
                        g_SanPedro[place] += 1

                if row[0] == 'Durango':
                    if not place in g_Durango and place != 'no':
                        g_Durango[place] = 1
                    else:
                        g_Durango[place] += 1

                if row[0] == 'Culiacán':
                    if not place in g_Culiacán and place != 'no':
                        g_Culiacán[place] = 1
                    else:
                        g_Culiacán[place] += 1

                if row[0] == 'Chihuahua':
                    if not place in g_Chihuahua and place != 'no':
                        g_Chihuahua[place] = 1
                    else:
                        g_Chihuahua[place] += 1

                if row[0] == 'ElPaso':
                    if not place in g_ElPaso and place != 'no':
                        g_ElPaso[place] = 1
                    else:
                        g_ElPaso[place] += 1

                if row[0] == 'TuxtlaGutiérrez':
                    if not place in g_TuxtlaGutiérrez and place != 'no':
                        g_TuxtlaGutiérrez[place] = 1
                    else:
                        g_TuxtlaGutiérrez[place] += 1

                if row[0] == 'CiudaddelCarmen':
                    if not place in g_CiudaddelCarmen and place != 'no':
                        g_CiudaddelCarmen[place] = 1
                    else:
                        g_CiudaddelCarmen[place] += 1

                if row[0] == 'SanJosédelCabo':
                    if not place in g_SanJosédelCabo and place != 'no':
                        g_SanJosédelCabo[place] = 1
                    else:
                        g_SanJosédelCabo[place] += 1

                if row[0] == 'LaPaz':
                    if not place in g_LaPaz and place != 'no':
                        g_LaPaz[place] = 1
                    else:
                        g_LaPaz[place] += 1

                if row[0] == 'Tijuana':
                    if not place in g_Tijuana and place != 'no':
                        g_Tijuana[place] = 1
                    else:
                        g_Tijuana[place] += 1

                if row[0] == 'Mexicali':
                    if not place in g_Mexicali and place != 'no':
                        g_Mexicali[place] = 1
                    else:
                        g_Mexicali[place] += 1

                if row[0] == 'Aguascalientes':
                    if not place in g_Aguascalientes and place != 'no':
                        g_Aguascalientes[place] = 1
                    else:
                        g_Aguascalientes[place] += 1

                if row[0] == 'CiudaddeMéxico':
                    if not place in g_CiudaddeMéxico and place != 'no':
                        g_CiudaddeMéxico[place] = 1
                    else:
                        g_CiudaddeMéxico[place] += 1

                if row[3] != 'lugar' and row[3].replace('\n', '').replace(' ', '') != 'Destino':
                    m = (row[3].replace('\n', '').replace(' ', ''))
                    nodes.append(m[5:])

        except:
            pass

nodes = set(nodes)
print(len(nodes))

nodes_final = []


for i in nodes:
    if (i in europa or i in america):
        print(i)
        nodes_final.append(i)

print(nodes_final)
nodes_final= set(nodes_final)
print(len(nodes_final))

#Definición de edges

with open('europa_final_1.csv', 'r') as data:
    spamreader = csv.reader(data)

    for row in spamreader:

        try:
            if row[1] == 'salida':

                m = (row[3].replace('\n', '').replace(' ', ''))


                if m[5:] != 'no' and row[0] != 'aeropuerto' and row[0] in nodes_final and  m[5:] in nodes_final:

                    edge = (row[0], m[5:])
                    comprobacion.append(m[5:])
                    comprobacion.append(row[0])

                    if row[0] == 'Logroño':
                        row[0].replace('ñ', 'n')
                    if row[0] == 'LaCoruña':
                        row[0].replace('ñ', 'n')
                    if row[0] == 'Büren':
                        row[0].replace('ü', 'u')

                    if m[5:] == 'Logroño':
                        m[5:].replace('ñ', 'n')
                    if m[5:] == 'LaCoruña':
                        m[5:].replace('ñ', 'n')
                    if m[5:] == 'Büren':
                        m[5:].replace('ü', 'u')

                    edges.append(edge)

        except:
            pass

with open('final_italia1.csv', 'r') as data:
    spamreader = csv.reader(data)

    for row in spamreader:

        try:
            if row[1] == 'salida':

                m = (row[3].replace('\n', '').replace(' ', ''))


                if m[5:] != 'no' and row[0] != 'aeropuerto' and row[0] in nodes_final and  m[5:] in nodes_final:

                    edge = (row[0], m[5:])
                    comprobacion.append(m[5:])
                    comprobacion.append(row[0])

                    if row[0] == 'Logroño':
                        row[0].replace('ñ', 'n')
                    if row[0] == 'LaCoruña':
                        row[0].replace('ñ', 'n')
                    if row[0] == 'Büren':
                        row[0].replace('ü', 'u')

                    if m[5:] == 'Logroño':
                        m[5:].replace('ñ', 'n')
                    if m[5:] == 'LaCoruña':
                        m[5:].replace('ñ', 'n')
                    if m[5:] == 'Büren':
                        m[5:].replace('ü', 'u')

                    edges.append(edge)

        except:
            pass

with open('eeuu.csv', 'r') as data:
    spamreader = csv.reader(data)

    for row in spamreader:

        try:
            if row[1] == 'salida':

                m = (row[3].replace('\n', '').replace(' ', ''))



                if m[5:] != 'no' and row[0] != 'aeropuerto' and row[0] in nodes_final and  m[5:] in nodes_final:

                    edge = (row[0], m[5:])
                    comprobacion.append(m[5:])
                    comprobacion.append(row[0])


                    edges.append(edge)

        except:
            pass

with open('mexico.csv', 'r') as data:
    spamreader = csv.reader(data)

    for row in spamreader:

        try:
            if row[1] == 'salida':

                m = (row[3].replace('\n', '').replace(' ', ''))


                if m[5:] != 'no' and row[0] != 'aeropuerto' and row[0] in nodes_final and m[5:] in nodes_final:
                    edge = (row[0], m[5:])
                    comprobacion.append(m[5:])
                    comprobacion.append(row[0])

                    edges.append(edge)

        except:
            pass

with open('caanda.csv', 'r') as data:
    spamreader = csv.reader(data)

    for row in spamreader:

        try:
            if row[1] == 'salida':

                m = (row[3].replace('\n', '').replace(' ', ''))


                if m[5:] != 'no' and row[0] != 'aeropuerto' and row[0] in nodes_final and m[5:] in nodes_final:
                    edge = (row[0], m[5:])
                    comprobacion.append(m[5:])
                    comprobacion.append(row[0])

                    edges.append(edge)

        except:
            pass


print('edges')
print(edges)
print(len(edges))
porcion = 100

edges_final = []


#Pesamos mediante los diccionarios anteriores las aristas

for i in edges:

    if i[0] == 'Basel' and i[1] in g_Basel:
        value = porcion /g_Basel[i[1]]

    elif i[0] == 'Manchester' and i[1] in g_Manchester:
        value = porcion /g_Manchester[i[1]]

    elif i[0] == 'Gibraltar' and i[1] in g_Gibraltar:
        value = porcion /g_Gibraltar[i[1]]

    elif i[0] == 'GeorgeTown' and i[1] in g_GeorgeTown:
        value = porcion /g_GeorgeTown[i[1]]

    elif i[0] == 'Prague' and i[1] in g_Prague:
        value = porcion /g_Prague[i[1]]

    elif i[0] == 'Bucarest' and i[1] in g_Bucarest:
        value = porcion /g_Bucarest[i[1]]

    elif i[0] == 'Stockholm' and i[1] in g_Stockholm :
        value = porcion /g_Stockholm[i[1]]

    elif i[0] == 'Zurich' and i[1] in g_Zurich:
        value = porcion /g_Zurich[i[1]]

    elif i[0] == 'Ginebra' and i[1] in g_Ginebra:
        value = porcion /g_Ginebra[i[1]]

    elif i[0] == 'Berna' and i[1] in g_Berna:
        value = porcion /g_Berna[i[1]]

    elif i[0] == 'Porto' and i[1] in g_Porto:
        value = porcion /g_Porto[i[1]]

    elif i[0] == 'Lisbon' and i[1] in g_Lisbon:
        value = porcion /g_Lisbon[i[1]]

    elif i[0] == 'PontaDelgada' and i[1] in g_PontaDelgada:
        value = porcion /g_PontaDelgada[i[1]]

    elif i[0] == 'Dublin' and i[1] in g_Dublin:
        value = porcion /g_Dublin[i[1]]

    elif i[0] == 'Edinburgh' and i[1] in g_Eindhoven:
        value = porcion /g_Edinburgh[i[1]]

    elif i[0] == 'Glasgow' and i[1] in g_Glasgow:
        value = porcion /g_Glasgow[i[1]]

    elif i[0] == 'London' and i[1] in g_London:
        value = porcion /g_London[i[1]]

    elif i[0] == 'Birmingham' and i[1] in g_Birmingham:
        value = porcion /g_Birmingham[i[1]]

    elif i[0] == 'Bristol' and i[1] in g_Bristol:
        value = porcion /g_Bristol[i[1]]

    elif i[0] == 'Liverpool' and i[1] in g_Liverpool:
        value = porcion /g_Liverpool[i[1]]

    elif i[0] == 'Lanzarote' and i[1] in g_Lanzarote:
        value = porcion /g_Lanzarote[i[1]]

    elif i[0] == 'Leon' and i[1] in g_Leon:
        value = porcion /g_Leon[i[1]]

    elif i[0] == 'Logrono' and i[1] in g_Logrono:
        value = porcion /g_Logrono[i[1]]

    elif i[0] == 'Menorca' and i[1] in g_Menorca:
        value = porcion /g_Menorca[i[1]]

    elif i[0] == 'Badajoz' and i[1] in g_Badajoz:
        value = porcion /g_Badajoz[i[1]]

    elif i[0] == 'Asturias' and i[1] in g_Asturias:
        value = porcion /g_Asturias[i[1]]

    elif i[0] == 'Almeria' and i[1] in g_Almeria:
        value = porcion /g_Almeria[i[1]]

    elif i[0] == 'Alicante' and i[1] in g_Alicante:
        value = porcion /g_Alicante[i[1]]

    elif i[0] == 'Albacete' and i[1] in g_Albacete:
        value = porcion /g_Albacete[i[1]]

    elif i[0] == 'Madrid' and i[1] in g_Madrid:
        value = porcion /g_Madrid[i[1]]

    elif i[0] == 'Lieja' and i[1] in g_Lieja:
        value = porcion /g_Lieja[i[1]]

    elif i[0] == 'Amberes' and i[1] in g_Amberes:
        value = porcion /g_Amberes[i[1]]

    elif i[0] == 'Brussels' and i[1] in g_Brussels:
        value = porcion /g_Brussels[i[1]]

    elif i[0] == 'Copenhagen' and i[1] in g_Copenhagen:
        value = porcion /g_Copenhagen[i[1]]

    elif i[0] == 'Sofia' and i[1] in g_Sofia:
        value = porcion /g_Sofia[i[1]]

    elif i[0] == 'Ibiza' and i[1] in g_Ibiza:
        value = porcion /g_Ibiza[i[1]]

    elif i[0] == 'Jerez' and i[1] in g_Jerez:
        value = porcion /g_Jerez[i[1]]

    elif i[0] == 'LaGomera' and i[1] in g_LaGomera:
        value = porcion /g_LaGomera[i[1]]

    elif i[0] == 'Berlin' and i[1] in g_Berlin:
        value = porcion /g_Berlin[i[1]]

    elif i[0] == 'Baden' and i[1] in g_Baden:
        value = porcion /g_Baden[i[1]]

    elif i[0] == 'Friedrichshafen' and i[1] in g_Friedrichshafen:
        value = porcion /g_Friedrichshafen[i[1]]

    elif i[0] == 'Mannheim' and i[1] in g_Mannheim:
        value = porcion /g_Mannheim[i[1]]

    elif i[0] == 'Dortmund' and i[1] in g_Dublin:
        value = porcion /g_Dortmund[i[1]]

    elif i[0] == 'Dusseldorf' and i[1] in g_Dusseldorf:
        value = porcion /g_Dusseldorf[i[1]]

    elif i[0] == 'Weeze' and i[1] in g_Weeze:
        value = porcion /g_Weeze[i[1]]

    elif i[0] == 'Frankfurt' and i[1] in g_Frankfurt:
        value = porcion /g_Frankfurt[i[1]]

    elif i[0] == 'Rostock' and i[1] in g_Rostock:
        value = porcion /g_Rostock[i[1]]

    elif i[0] == 'Hamburg' and i[1] in g_Hamburg:
        value = porcion /g_Hamburg[i[1]]

    elif i[0] == 'Saarbrucken' and i[1] in g_Saarbrucken:
        value = porcion /g_Saarbrucken[i[1]]

    elif i[0] == 'Hannover' and i[1] in g_Hannover:
        value = porcion /g_Hannover[i[1]]

    elif i[0] == 'Greven' and i[1] in g_Greven:
        value = porcion /g_Greven[i[1]]

    elif i[0] == 'Stuttgart' and i[1] in g_Stuttgart:
        value = porcion /g_Stuttgart[i[1]]

    elif i[0] == 'Lubeck' and i[1] in g_Lubeck:
        value = porcion /g_Lubeck[i[1]]

    elif i[0] == 'Buren' and i[1] in g_Buren:
        value = porcion /g_Buren[i[1]]

    elif i[0] == 'Bremen' and i[1] in g_Bremen:
        value = porcion /g_Bremen[i[1]]

    elif i[0] == 'Luneort' and i[1] in g_Luneort:
        value = porcion /g_Luneort[i[1]]

    elif i[0] == 'Cologne' and i[1] in g_Cologne:
        value = porcion /g_Cologne[i[1]]

    elif i[0] == 'Dresde' and i[1] in g_Dresde:
        value = porcion /g_Dresde[i[1]]

    elif i[0] == 'Erfurt' and i[1] in g_Erfurt:
        value = porcion /g_Erfurt[i[1]]

    elif i[0] == 'Leipzig' and i[1] in g_Leipzig:
        value = porcion /g_Leipzig[i[1]]

    elif i[0] == 'Sylt' and i[1] in g_Sylt:
        value = porcion /g_Sylt[i[1]]

    elif i[0] == 'Memmingen' and i[1] in g_Memmingen:
        value = porcion /g_Memmingen[i[1]]

    elif i[0] == 'Munich' and i[1] in g_Munich:
        value = porcion /g_Munich[i[1]]

    elif i[0] == 'Nuremberg' and i[1] in g_Nuremberg:
        value = porcion /g_Nuremberg[i[1]]

    elif i[0] == 'Istanbul' and i[1] in g_Istanbul:
        value = porcion /g_Istanbul[i[1]]

    elif i[0] == 'Fuerteventura' and i[1] in g_Fuerteventura:
        value = porcion /g_Fuerteventura[i[1]]

    elif i[0] == 'ElHierro' and i[1] in g_ElHierro:
        value = porcion /g_ElHierro[i[1]]

    elif i[0] == 'LaPalma' and i[1] in g_LaPalma:
        value = porcion /g_LaPalma[i[1]]

    elif i[0] == 'LaCoruna' and i[1] in g_LaCoruna:
        value = porcion /g_LaCoruna[i[1]]

    elif i[0] == 'Huesca' and i[1] in g_Huesca:
        value = porcion /g_Huesca[i[1]]

    elif i[0] == 'Granada' and i[1] in g_Granada:
        value = porcion /g_Granada[i[1]]

    elif i[0] == 'Gerona' and i[1] in g_Gerona:
        value = porcion /g_Gerona[i[1]]

    elif i[0] == 'GranCanaria' and i[1] in g_GranCanaria:
        value = porcion /g_GranCanaria[i[1]]

    elif i[0] == 'Cordoba' and i[1] in g_Cordoba:
        value = porcion /g_Cordoba[i[1]]

    elif i[0] == 'CiudadReal' and i[1] in g_CiudadReal:
        value = porcion /g_CiudadReal[i[1]]

    elif i[0] == 'Burgos' and i[1] in g_Burgos:
        value = porcion /g_Burgos[i[1]]

    elif i[0] == 'Bilbao' and i[1] in g_Bilbao:
        value = porcion /g_Bilbao[i[1]]

    elif i[0] == 'Barcelona' and i[1] in g_Barcelona:
        value = porcion /g_Barcelona[i[1]]

    elif i[0] == 'Pamplona' and i[1] in g_Pamplona:
        value = porcion /g_Pamplona[i[1]]

    elif i[0] == 'Reus' and i[1] in g_Reus:
        value = porcion /g_Reus[i[1]]

    elif i[0] == 'Sabadell' and i[1] in g_Sabadell:
        value = porcion /g_Sabadell[i[1]]

    elif i[0] == 'SanSebastian' and i[1] in g_SanSebastian:
        value = porcion /g_SanSebastian[i[1]]

    elif i[0] == 'SantiagodeCompostela' and i[1] in g_SantiagodeCompostela:
        value = porcion /g_SantiagodeCompostela[i[1]]

    elif i[0] == 'Malaga' and i[1] in g_Malaga:
        value = porcion /g_Malaga[i[1]]

    elif i[0] == 'Melilla' and i[1] in g_Melilla:
        value = porcion /g_Melilla[i[1]]

    elif i[0] == 'Murcia' and i[1] in g_Murcia:
        value = porcion /g_Murcia[i[1]]

    elif i[0] == 'PalmaMallorca' and i[1] in g_PalmaMallorca:
        value = porcion /g_PalmaMallorca[i[1]]

    elif i[0] == 'Salamanca' and i[1] in g_Salamanca:
        value = porcion /g_Salamanca[i[1]]

    elif i[0] == 'Santander' and i[1] in g_Santander:
        value = porcion /g_Santander[i[1]]

    elif i[0] == 'Sevilla' and i[1] in g_Sevilla:
        value = porcion /g_Sevilla[i[1]]

    elif i[0] == 'Tenerife' and i[1] in g_Tenerife:
        value = porcion /g_Tenerife[i[1]]

    elif i[0] == 'Valencia' and i[1] in g_Valencia:
        value = porcion /g_Valencia[i[1]]

    elif i[0] == 'Valladolid' and i[1] in g_Valladolid:
        value = porcion /g_Valladolid[i[1]]

    elif i[0] == 'Vigo' and i[1] in g_Vigo:
        value = porcion /g_Vigo[i[1]]

    elif i[0] == 'Vitoria' and i[1] in g_Vitoria:
        value = porcion /g_Vitoria[i[1]]

    elif i[0] == 'Zaragoza' and i[1] in g_Zaragoza:
        value = porcion /g_Zaragoza[i[1]]

    elif i[0] == 'Toulouse' and i[1] in g_Toulouse:
        value = porcion /g_Toulouse[i[1]]

    elif i[0] == 'Athens' and i[1] in g_Athens:
        value = porcion /g_Athens[i[1]]

    elif i[0] == 'Helsinki' and i[1] in g_Helsinki:
        value = porcion /g_Helsinki[i[1]]

    elif i[0] == 'Beauvais' and i[1] in g_Beauvais:
        value = porcion /g_Beauvais[i[1]]

    elif i[0] == 'Biarritz' and i[1] in g_Biarritz:
        value = porcion /g_Biarritz[i[1]]

    elif i[0] == 'Pau' and i[1] in g_Pau:
        value = porcion /g_Pau[i[1]]

    elif i[0] == 'Montpellier' and i[1] in g_Montpellier:
        value = porcion /g_Montpellier[i[1]]

    elif i[0] == 'Niza' and i[1] in g_Niza:
        value = porcion /g_Niza[i[1]]

    elif i[0] == 'Marseille' and i[1] in g_Marseille:
        value = porcion /g_Marseille[i[1]]

    elif i[0] == 'SaintEtienne' and i[1] in g_SaintEtienne:
        value = porcion /g_SaintEtienne[i[1]]

    elif i[0] == 'Lyon' and i[1] in g_Lyon:
        value = porcion /g_Lyon[i[1]]

    elif i[0] == 'Estrasburg' and i[1] in g_Estrasburg:
        value = porcion /g_Estrasburg[i[1]]

    elif i[0] == 'Burdeos' and i[1] in g_Burdeos:
        value = porcion /g_Burdeos[i[1]]

    elif i[0] == 'Paris' and i[1] in g_Paris:
        value = porcion /g_Paris[i[1]]

    elif i[0] == 'Rotterdam' and i[1] in g_Rotterdam:
        value = porcion /g_Rotterdam[i[1]]

    elif i[0] == 'Eindhoven' and i[1] in g_Eindhoven:
        value = porcion /g_Eindhoven[i[1]]

    elif i[0] == 'Eelde' and i[1] in g_Eelde:
        value = porcion /g_Eelde[i[1]]

    elif i[0] == 'Budapest' and i[1] in g_Budapest:
        value = porcion /g_Budapest[i[1]]

    elif i[0] == 'Amsterdam' and i[1] in g_Amsterdam:
        value = porcion /g_Amsterdam[i[1]]

    elif i[0] == 'Cracovia' and i[1] in g_Cracovia:
        value = porcion /g_Cracovia[i[1]]

    elif i[0] == 'Riga' and i[1] in g_Riga:
        value = porcion /g_Riga[i[1]]

    elif i[0] == 'Luxembourg' and i[1] in g_Luxembourg:
        value = porcion /g_Luxembourg[i[1]]

    elif i[0] == 'Bergen' and i[1] in g_Bergen:
        value = porcion / g_Bergen[i[1]]

    elif i[0] == 'Oslo' and i[1] in g_Oslo:
        value = porcion /g_Oslo[i[1]]

    elif i[0] == 'Varsovia' and i[1] in g_Varsovia:
        value = porcion /g_Varsovia[i[1]]

    elif i[0] == 'Faro' and i[1] in g_Faro:
        value = porcion /g_Faro[i[1]]

    elif i[0] == 'Terceira' and i[1] in g_Terceira:
        value = porcion /g_Terceira[i[1]]

    elif i[0] == 'Madeira' and i[1] in g_Madeira:
        value = porcion /g_Madeira[i[1]]

    elif i[0] == 'Verona' and i[1] in g_Verona:
        value = porcion /g_Verona[i[1]]

    elif i[0] == 'Venice' and i[1] in g_Venice:
        value = porcion /g_Venice[i[1]]

    elif i[0] == 'Pisa' and i[1] in g_Pisa:
        value = porcion /g_Pisa[i[1]]

    elif i[0] == 'Turin' and i[1] in g_Turin:
        value = porcion /g_Turin[i[1]]

    elif i[0] == 'Asis' and i[1] in g_Asis:
        value = porcion /g_Asis[i[1]]

    elif i[0] == 'Catania' and i[1] in g_Catania:
        value = porcion /g_Catania[i[1]]

    elif i[0] == 'Palermo' and i[1] in g_Palermo:
        value = porcion /g_Palermo[i[1]]

    elif i[0] == 'Forli' and i[1] in g_Forli:
        value = porcion /g_Forli[i[1]]

    elif i[0] == 'Bologna' and i[1] in g_Bologna:
        value = porcion /g_Bologna[i[1]]

    elif i[0] == 'Miramare' and i[1] in g_Miramare:
        value = porcion /g_Miramare[i[1]]

    elif i[0] == 'Parma' and i[1] in g_Parma:
        value = porcion /g_Parma[i[1]]

    elif i[0] == 'Naples' and i[1] in g_Naples:
        value = porcion /g_Naples[i[1]]

    elif i[0] == 'Genoa' and i[1] in g_Genoa:
        value = porcion /g_Genoa[i[1]]

    elif i[0] == 'Florence' and i[1] in g_Florence:
        value = porcion /g_Florence[i[1]]

    elif i[0] == 'ReggioCalabria' and i[1] in g_ReggioCalabria:
        value = porcion /g_ReggioCalabria[i[1]]

    elif i[0] == 'Bari' and i[1] in g_Bari:
        value = porcion /g_Bari[i[1]]

    elif i[0] == 'Milan' and i[1] in g_Milan:
        value = porcion /g_Milan[i[1]]

    elif i[0] == 'Montichiari' and i[1] in g_Montichiari:
        value = porcion /g_Montichiari[i[1]]

    elif i[0] == 'Bergamo' and i[1] in g_Bergamo:
        value = porcion /g_Bergamo[i[1]]

    elif i[0] == 'Cagliari' and i[1] in g_Cagliari:
        value = porcion /g_Cagliari[i[1]]

    elif i[0] == 'Alghero' and i[1] in g_Alghero:
        value = porcion /g_Alghero[i[1]]

    elif i[0] == 'Ancona' and i[1] in g_Ancona:
        value = porcion /g_Ancona[i[1]]

    elif i[0] == 'Rome' and i[1] in g_Rome:
        value = porcion /g_Rome[i[1]]

    elif i[0] == 'Edmonton' and i[1] in g_Edmonton:
        value = porcion /g_Edmonton[i[1]]

    elif i[0] == 'Ottawa' and i[1] in g_Ottawa:
        value = porcion /g_Ottawa[i[1]]

    elif i[0] == 'GrandePrairie' and i[1] in g_GrandePrairie:
        value = porcion /g_GrandePrairie[i[1]]

    elif i[0] == 'Dorval' and i[1] in g_Dorval:
        value = porcion /g_Dorval[i[1]]

    elif i[0] == 'Mirabel' and i[1] in g_Mirabel:
        value = porcion /g_Mirabel[i[1]]

    elif i[0] == 'Montreal' and i[1] in g_Montreal:
        value = porcion /g_Montreal[i[1]]

    elif i[0] == 'Terranova' and i[1] in g_Terranova:
        value = porcion /g_Terranova[i[1]]

    elif i[0] == 'Toronto' and i[1] in g_Toronto:
        value = porcion /g_Toronto[i[1]]

    elif i[0] == 'Vancouver' and i[1] in g_Vancouver:
        value = porcion /g_Vancouver[i[1]]

    elif i[0] == 'Winnipeg' and i[1] in g_Winnipeg:
        value = porcion /g_Winnipeg[i[1]]

    elif i[0] == 'Veracruz' and i[1] in g_Veracruz:
        value = porcion /g_Veracruz[i[1]]

    elif i[0] == 'Mérida' and i[1] in g_Mérida:
        value = porcion /g_Mérida[i[1]]

    elif i[0] == 'Tampico' and i[1] in g_Tampico:
        value = porcion /g_Tampico[i[1]]

    elif i[0] == 'Tamaulipas' and i[1] in g_Tamaulipas:
        value = porcion /g_Tamaulipas[i[1]]

    elif i[0] == 'Villahermosa' and i[1] in g_Villahermosa:
        value = porcion /g_Villahermosa[i[1]]

    elif i[0] == 'Hermosillo' and i[1] in g_Hermosillo:
        value = porcion /g_Hermosillo[i[1]]

    elif i[0] == 'SanLuisPotosí' and i[1] in g_SanLuisPotosí:
        value = porcion /g_SanLuisPotosí[i[1]]

    elif i[0] == 'Mazatlán' and i[1] in g_Mazatlán:
        value = porcion /g_Mazatlán[i[1]]

    elif i[0] == 'SanMigueldeCozumel' and i[1] in g_SanMigueldeCozumel:
        value = porcion /g_SanMigueldeCozumel[i[1]]

    elif i[0] == 'Cancun' and i[1] in g_Cancun:
        value = porcion /g_Cancun[i[1]]

    elif i[0] == 'Queretana' and i[1] in g_Queretana:
        value = porcion /g_Queretana[i[1]]

    elif i[0] == 'Puebla' and i[1] in g_Puebla:
        value = porcion /g_Puebla[i[1]]

    elif i[0] == 'Huatulco' and i[1] in g_Huatulco:
        value = porcion /g_Huatulco[i[1]]

    elif i[0] == 'Oaxaca' and i[1] in g_Oaxaca:
        value = porcion /g_Oaxaca[i[1]]

    elif i[0] == 'NuevoLeón' and i[1] in g_NuevoLeón:
        value = porcion /g_NuevoLeón[i[1]]

    elif i[0] == 'PuertoVallarta' and i[1] in g_PuertoVallarta:
        value = porcion /g_PuertoVallarta[i[1]]

    elif i[0] == 'Guadalajara' and i[1] in g_Guadalajara:
        value = porcion /g_Guadalajara[i[1]]

    elif i[0] == 'Acapulco' and i[1] in g_Acapulco:
        value = porcion /g_Acapulco[i[1]]

    elif i[0] == 'Silao' and i[1] in g_Silao:
        value = porcion /g_Silao[i[1]]

    elif i[0] == 'SanPedro' and i[1] in g_SanPedro:
        value = porcion /g_SanPedro[i[1]]

    elif i[0] == 'Durango' and i[1] in g_Durango:
        value = porcion /g_Durango[i[1]]

    elif i[0] == 'Culiacán' and i[1] in g_Culiacán:
        value = porcion /g_Culiacán[i[1]]

    elif i[0] == 'Chihuahua' and i[1] in g_Chihuahua:
        value = porcion /g_Chihuahua[i[1]]

    elif i[0] == 'ElPaso' and i[1] in g_ElPaso:
        value = porcion /g_ElPaso[i[1]]

    elif i[0] == 'TuxtlaGutiérrez' and i[1] in g_TuxtlaGutiérrez:
        value = porcion /g_TuxtlaGutiérrez[i[1]]

    elif i[0] == 'CiudaddelCarmen' and i[1] in g_CiudaddelCarmen:
        value = porcion /g_CiudaddelCarmen[i[1]]

    elif i[0] == 'SanJosédelCabo' and i[1] in g_SanJosédelCabo:
        value = porcion /g_SanJosédelCabo[i[1]]

    elif i[0] == 'LaPaz' and i[1] in g_LaPaz:
        value = porcion /g_LaPaz[i[1]]

    elif i[0] == 'Tijuana' and i[1] in g_Tijuana:
        value = porcion /g_Tijuana[i[1]]

    elif i[0] == 'g_Mexicali' and i[1] in g_Mexicali:
        value = porcion /g_Mexicali[i[1]]

    elif i[0] == 'Aguascalientes' and i[1] in g_Aguascalientes:
        value = porcion /g_Aguascalientes[i[1]]

    elif i[0] == 'CiudaddeMéxico' and i[1] in g_CiudaddeMéxico:
        value = porcion /g_CiudaddeMéxico[i[1]]

    elif i[0] == 'g_Birmingham' and i[1] in g_Birmingham:
        value = porcion /g_Birmingham[i[1]]

    elif i[0] == 'Anchorage' and i[1] in g_Anchorage:
        value = porcion /g_Anchorage[i[1]]

    elif i[0] == 'g_Kingman' and i[1] in g_Kingman:
        value = porcion /g_Kingman[i[1]]

    elif i[0] == 'g_Maricopa' and i[1] in g_Maricopa:
        value = porcion /g_Maricopa[i[1]]

    elif i[0] == 'Prescott' and i[1] in g_Prescott:
        value = porcion /g_Prescott[i[1]]

    elif i[0] == 'Tucson' and i[1] in g_Tucson:
        value = porcion /g_Tucson[i[1]]

    elif i[0] == 'Fresno' and i[1] in g_Fresno:
        value = porcion /g_Fresno[i[1]]

    elif i[0] == 'LosAngeles' and i[1] in g_LosAngeles:
        value = porcion /g_LosAngeles[i[1]]

    elif i[0] == 'LongBeach' and i[1] in g_LongBeach:
        value = porcion /g_LongBeach[i[1]]

    elif i[0] == 'Oakland' and i[1] in g_Oakland:
        value = porcion /g_Oakland[i[1]]

    elif i[0] == 'Ontario' and i[1] in g_Ontario:
        value = porcion /g_Ontario[i[1]]

    elif i[0] == 'SantaAna' and i[1] in g_SantaAna:
        value = porcion /g_SantaAna[i[1]]

    elif i[0] == 'PalmSprings' and i[1] in g_PalmSprings:
        value = porcion /g_PalmSprings[i[1]]

    elif i[0] == 'Sacramento' and i[1] in g_Sacramento:
        value = porcion /g_Sacramento[i[1]]

    elif i[0] == 'SanBernardino' and i[1] in g_SanBernardino:
        value = porcion /g_SanBernardino[i[1]]

    elif i[0] == 'SanDiego' and i[1] in g_SanDiego:
        value = porcion /g_SanDiego[i[1]]

    elif i[0] == 'Carlsbad' and i[1] in g_Carlsbad:
        value = porcion /g_Carlsbad[i[1]]

    elif i[0] == 'SanDiego' and i[1] in g_SanDiego:
        value = porcion /g_SanDiego[i[1]]

    elif i[0] == 'SanFrancisco' and i[1] in g_SanFrancisco:
        value = porcion /g_SanFrancisco[i[1]]

    elif i[0] == 'SanJose' and i[1] in g_SanJose:
        value = porcion /g_SanJose[i[1]]

    elif i[0] == 'Charlotte' and i[1] in g_Charlotte:
        value = porcion /g_Charlotte[i[1]]

    elif i[0] == 'Morrisville' and i[1] in g_Morrisville:
        value = porcion /g_Morrisville[i[1]]

    elif i[0] == 'ColoradoSprings' and i[1] in g_ColoradoSprings:
        value = porcion /g_ColoradoSprings[i[1]]

    elif i[0] == 'Denver' and i[1] in g_Denver:
        value = porcion /g_Denver[i[1]]

    elif i[0] == 'DaytonaBeach' and i[1] in g_DaytonaBeach:
        value = porcion /g_DaytonaBeach[i[1]]

    elif i[0] == 'FortLauderdale' and i[1] in g_FortLauderdale:
        value = porcion /g_FortLauderdale[i[1]]

    elif i[0] == 'Melbourne' and i[1] in g_Melbourne:
        value = porcion /g_Melbourne[i[1]]

    elif i[0] == 'Miami' and i[1] in g_Miami:
        value = porcion /g_Miami[i[1]]

    elif i[0] == 'Duval' and i[1] in g_Duval:
        value = porcion /g_Duval[i[1]]

    elif i[0] == 'FortMyers' and i[1] in g_FortMyers:
        value = porcion /g_FortMyers[i[1]]

    elif i[0] == 'Sanford' and i[1] in g_Sanford:
        value = porcion /g_Sanford[i[1]]

    elif i[0] == 'Orlando' and i[1] in g_Orlando:
        value = porcion /g_Orlando[i[1]]

    elif i[0] == 'Tampa' and i[1] in g_Tampa:
        value = porcion /g_Tampa[i[1]]

    elif i[0] == 'WestPalmBeach' and i[1] in g_WestPalmBeach:
        value = porcion /g_WestPalmBeach[i[1]]

    elif i[0] == 'Atlanta' and i[1] in g_Atlanta:
        value = porcion /g_Atlanta[i[1]]

    elif i[0] == 'Savannah' and i[1] in g_Savannah:
        value = porcion /g_Savannah[i[1]]

    elif i[0] == 'Honolulu' and i[1] in g_Honolulu:
        value = porcion /g_Honolulu[i[1]]

    elif i[0] == 'Midway' and i[1] in g_Midway:
        value = porcion /g_Midway[i[1]]

    elif i[0] == 'Chicago' and i[1] in g_Chicago:
        value = porcion /g_Chicago[i[1]]

    elif i[0] == 'Indianápolis' and i[1] in g_Indianápolis:
        value = porcion/g_Indianápolis[i[1]]

    elif i[0] == 'Cincinnati' and i[1] in g_Cincinnati:
        value = porcion/g_Cincinnati[i[1]]

    elif i[0] == 'Louisville' and i[1] in g_Louisville:
        value = porcion/g_Louisville[i[1]]

    elif i[0] == 'Lafayette' and i[1] in g_Lafayette:
        value = porcion/g_Lafayette[i[1]]

    elif i[0] == 'NewOrleans' and i[1] in g_NewOrleans:
        value = porcion/g_NewOrleans[i[1]]

    elif i[0] == 'Baltimore' and i[1] in g_Baltimore:
        value = porcion/g_Baltimore[i[1]]

    elif i[0] == 'Boston' and i[1] in g_Boston:
        value = porcion/g_Boston[i[1]]

    elif i[0] == 'Detroit' and i[1] in g_Detroit:
        value = porcion/g_Detroit[i[1]]

    elif i[0] == 'Michigan' and i[1] in g_Michigan:
        value = porcion/g_Michigan[i[1]]

    elif i[0] == 'CapitolCity' and i[1] in g_CapitolCity:
        value = porcion/g_CapitolCity[i[1]]

    elif i[0] == 'StPaul' and i[1] in g_StPaul:
        value = porcion/g_StPaul[i[1]]

    elif i[0] == 'KansasCity' and i[1] in g_KansasCity:
        value = porcion/g_KansasCity[i[1]]

    elif i[0] == 'SanLuis' and i[1] in g_SanLuis:
        value = porcion/g_SanLuis[i[1]]

    elif i[0] == 'LasVegas' and i[1] in g_LasVegas:
        value = porcion/g_LasVegas[i[1]]

    elif i[0] == 'Cheektowaga' and i[1] in g_Cheektowaga:
        value = porcion/g_Cheektowaga[i[1]]

    elif i[0] == 'Newark' and i[1] in g_Newark:
        value = porcion/g_Newark[i[1]]

    elif i[0] == 'NewYork' and i[1] in g_NewYork:
        value = porcion/g_NewYork[i[1]]

    elif i[0] == 'Albany' and i[1] in g_Albany:
        value = porcion/g_Albany[i[1]]

    elif i[0] == 'Albuquerque' and i[1] in g_Albuquerque:
        value = porcion/g_Albuquerque[i[1]]

    elif i[0] == 'Cleveland' and i[1] in g_Cleveland:
        value = porcion/g_Cleveland[i[1]]

    elif i[0] == 'Portland' and i[1] in g_Portland:
        value = porcion/g_Portland[i[1]]

    elif i[0] == 'Philadelphia' and i[1] in g_Philadelphia:
        value = porcion/g_Philadelphia[i[1]]

    elif i[0] == 'Memphis' and i[1] in g_Memphis:
        value = porcion/g_Memphis[i[1]]

    elif i[0] == 'Austin' and i[1] in g_Austin:
        value = porcion/g_Austin[i[1]]

    elif i[0] == 'Dallas-FortWorth' and i[1] in g_Dallas_FortWorth:
        value = porcion/g_Dallas_FortWorth[i[1]]

    elif i[0] == 'Dallas' and i[1] in g_Dallas:
        value = porcion/g_Dallas[i[1]]

    elif i[0] == 'Laredo' and i[1] in g_Laredo:
        value = porcion/g_Laredo[i[1]]

    elif i[0] == 'McAllen' and i[1] in g_McAllen:
        value = porcion/g_McAllen[i[1]]

    elif i[0] == 'Houston' and i[1] in g_Houston:
        value = porcion/g_Houston[i[1]]

    elif i[0] == 'SaltLakeCity' and i[1] in g_SaltLakeCity:
        value = porcion/g_SaltLakeCity[i[1]]

    elif i[0] == 'StGeorge' and i[1] in g_StGeorge:
        value = porcion/g_StGeorge[i[1]]

    elif i[0] == 'Seattle' and i[1] in g_Seattle:
        value = porcion/g_Seattle[i[1]]

    elif i[0] == 'Dulles' and i[1] in g_Dulles:
        value = porcion/g_Dulles[i[1]]

    elif i[0] == 'Washington' and i[1] in g_Washington :
        value = porcion/g_Washington[i[1]]

    elif i[0] == 'g_Milwaukee' and i[1] in g_Milwaukee:
        value = porcion/g_Milwaukee[i[1]]

    elif i[0] == 'RockSprings' and i[1] in g_RockSprings :
        value = porcion/g_RockSprings[i[1]]

    else:
        value = 100

    value_f = 1/value

    edges2 = (i[0], i[1], {'weight': value_f})
    edges_final.append(edges2)


print(edges_final)
print(len(nodes_final))

#Comprobación de existencia de nodos para no tener nodos en el grafo que no formen parte de nuestra visualización.

nodes_final2 = []

for i in nodes_final:
    if i in comprobacion:
        nodes_final2.append(i)

print('filtrado')
print(len(nodes_final2))


g = nx.DiGraph()

g.add_nodes_from(nodes_final2)

g.add_edges_from(edges_final)


deggre_salida = []
deggre_entrada = []


for node in g.nodes():

    deg_entrada = (node, g.in_degree(node))
    deggre_entrada.append(deg_entrada)

    deg_salida = (node, g.out_degree(node))
    deggre_salida.append(deg_salida)


deggre_entrada.sort(key=lambda tup: tup[1])
print(deggre_entrada)


deggre_salida.sort(key=lambda tup: tup[1])
print(deggre_salida)

h = g.to_undirected()

for comp in nx.connected_component_subgraphs(h):

    degreeCent = nx.degree_centrality(comp)


print('indirectetd degree centrality')
print(degreeCent)

print('directetd pagerank')
pagerank_di = nx.pagerank(g)
print(pagerank_di)


print('community')
communities_generator = community.girvan_newman(g)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)

dt = sorted(map(sorted, next_level_communities))

#Asignamos a cada nodo su comunidad
comu = {}
com = 1
for i in dt:
    for j in nodes_final2:
        if j in i:
            comu[j] = com
    com = com + 1




g_json = json_graph.node_link_data(g)

with open('grafo_2.json', 'w') as f:
    print(json.dump(g_json, f, indent=1))

#Creamos el json que se utilizará para la visualización

with open('grafo_2.json', 'r') as p:
    p = p.read()
    data = json.loads(p)
    dict = {}
    list_ = []

    j = 0
    for i in data['nodes']:
        dict[i['id']] = j
        j = j + 1

    print(dict)

    for i in data['links']:

        if i['source'] in dict:
            i['source'] = dict[i['source']]
        if i['target'] in dict:
            i['target'] = dict[i['target']]

    for i in data['nodes']:

        if i['id'] in dinamarca:
            pais = 'Dinamarca'
            bandera = bandera_dinamarca
            continente = 'Europa'

        elif i['id'] in bulgaria:
            pais = 'Bulgaria'
            bandera = bandera_bulgaria
            continente = 'Europa'

        elif i['id'] in reino_unido:
            pais = 'Reino Unido'
            bandera = 'http://flags.fmcdn.net/data/flags/w580/gb.png'
            continente = 'Europa'

        elif i['id'] in checa:
            pais = 'Republica Checa'
            bandera = bandera_chequia
            continente = 'Europa'

        elif i['id'] in rumania:
            pais = 'Rumania'
            bandera = bandera_rumania
            continente = 'Europa'

        elif i['id'] in suecia:
            pais = 'Suecia'
            bandera = bandera_suecia
            continente = 'Europa'

        elif i['id'] in suiza:
            pais = 'Suiza'
            bandera = bandera_suiza
            continente = 'Europa'

        elif i['id'] in turquia:
            pais = 'Turquia'
            bandera = bandera_turquia
            continente = 'Europa'

        elif i['id'] in alemania:
            pais = 'Alemania'
            bandera = bandera_alemania
            continente = 'Europa'

        elif i['id'] in belgica:
            pais = 'Belgica'
            bandera = bandera_belgica
            continente = 'Europa'

        elif i['id'] in portugal:
            pais = 'Portugal'
            bandera = bandera_portugal
            continente = 'Europa'

        elif i['id'] in turquia:
            pais = 'Turquia'
            bandera = bandera_turquia
            continente = 'Europa'

        elif i['id'] in suiza:
            pais = 'Suiza'
            bandera = bandera_suiza
            continente = 'Europa'

        elif i['id'] in suecia:
            pais = 'Suecia'
            bandera = bandera_suecia
            continente = 'Europa'

        elif i['id'] in rumania:
            pais = 'Rumania'
            bandera = bandera_rumania
            continente = 'Europa'

        elif i['id'] in polonia:
            pais = 'Polonia'
            bandera = bandera_polonia
            continente = 'Europa'

        elif i['id'] in noruega:
            pais = 'Noruega'
            bandera = bandera_noruega
            continente = 'Europa'

        elif i['id'] in luxemburgo:
            pais = 'Luxemburgo'
            bandera = bandera_luxemburgo
            continente = 'Europa'

        elif i['id'] in letonia:
            pais = 'Letonia'
            bandera = bandera_letonia
            continente = 'Europa'

        elif i['id'] in hungria:
            pais = 'Hungria'
            bandera = bandera_hungria
            continente = 'Europa'

        elif i['id'] in paises_bajos:
            pais = 'Paises Bajos'
            bandera = bandera_paises_bajos
            continente = 'Europa'

        elif i['id'] in grecia:
            pais = 'Grecia'
            bandera = bandera_grecia
            continente = 'Europa'

        elif i['id'] in finlandia:
            pais= 'Finlandia'
            bandera = bandera_finlandia
            continente = 'Europa'

        elif i['id'] in francia:
            pais = 'Francia'
            bandera = bandera_francia
            continente = 'Europa'

        elif i['id'] in españa:
           pais = 'Espana'
           bandera = bandera_espana
           continente = 'Europa'

        elif i['id'] in canada:
            pais = 'Canada'
            bandera = bandera_canada
            continente = 'North America'

        elif i['id'] in eeuu:
            pais = 'EEUU'
            bandera = bandera_eeuu
            continente = 'North America'

        elif i['id'] in mexico:
            pais = 'Mexico'
            bandera = bandera_mexico
            continente = 'North America'

        else:
            pais = 'Italia'
            bandera = bandera_italia
            continente = 'Europa'

        list_.append({
            'id': i['id'],
            'pais': pais,
            'image': bandera,
            'continente': continente,
            'comunidad': comu[i['id']],
            'page_rank': pagerank_di[i['id']],
            'degree': degreeCent[i['id']]
        })


    data['nodes'] = list_

with open('grafo_fin2.json', 'w') as f:
    print(json.dump(data, f, indent=1))
