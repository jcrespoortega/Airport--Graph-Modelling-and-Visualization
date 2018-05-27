from bs4 import BeautifulSoup
import requests
import csv

list_csv_2 = []
index = ["aeropuerto",
         "tipo",
         "hora",
         "lugar",
         "aerolinea"
         ]

list_csv_2.append(index)

link = 'https://www.aeropuertos.net/europa/'

page = requests.get(link)

bsObj = BeautifulSoup(page.content, 'html.parser')

d = bsObj.find("tbody")

d2 = d.find_all('td')

for i in d2:

    try:
        link1 = i.find('a').attrs['href']
        print(link1)

        page = requests.get(link1)

        bsObj = BeautifulSoup(page.content, 'html.parser')

        d = bsObj.find("div", {"class": "column_inner"})
        d2 = d.find_all('ul')

        for i in d2:

            try:
                d3 = i.find_all('li')

                for j in d3:
                    link2 = j.find('a').attrs['href']
                    print(link2)

            except:

                pass

            page = requests.get(link2)

            bsObj2 = BeautifulSoup(page.content, 'html.parser')

            d4 = bsObj2.find_all("div", {"class": "icon"})

            try:
                link_llegadas = d4[0].find('a').attrs['href']

                link_salidas = d4[1].find('a').attrs['href']


            except:

                pass

            print(link_llegadas)
            print(link_salidas)

            try:
                page3 = requests.get(link_llegadas)

                bsObj3 = BeautifulSoup(page3.content, 'html.parser')

                tabla = bsObj3.find("iframe").attrs['src']

                page4 = requests.get(tabla)

                bsObj4 = BeautifulSoup(page4.content, 'html.parser')

                fila = bsObj4.find_all('tr')

                for j in fila:

                    fila2 = j.find_all('td')

                    try:
                        compannia = fila2[1].get_text()

                        destino = fila2[2].get_text()

                        hora = fila2[3].get_text()

                        salida = link2

                        type = 'llegada'

                        print(compannia)
                        print(destino)
                        print(hora)
                        print(salida)

                        value = [salida,
                                 type,
                                 hora,
                                 destino,
                                 compannia
                                 ]

                        list_csv_2.append(value)


                    except:

                        pass

                page4 = requests.get(link_salidas)

                bsObj4 = BeautifulSoup(page4.content, 'html.parser')

                tabla5 = bsObj4.find("iframe").attrs['src']

                page6 = requests.get(tabla5)

                bsObj5 = BeautifulSoup(page6.content, 'html.parser')

                fila5 = bsObj5.find_all('tr')

                for j in fila5:

                    fila2 = j.find_all('td')

                    try:
                        compannia = fila2[1].get_text()

                        destino = fila2[2].get_text()

                        hora = fila2[3].get_text()

                        type = 'salida'

                        salida = link2

                        print(compannia)
                        print(destino)
                        print(hora)
                        print(type)
                        print(salida)

                        value = [salida,
                                 type,
                                 hora,
                                 destino,
                                 compannia
                                 ]

                        list_csv_2.append(value)



                    except:
                        pass

            except:
                pass



    except:

        pass


comprobacion_csv = open('europa_final_3' + '.csv', 'w')

with comprobacion_csv:

    writer = csv.writer(comprobacion_csv)
    writer.writerows(list_csv_2)

comprobacion_csv.close()


