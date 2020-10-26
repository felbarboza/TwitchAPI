from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

streamerslink = []
streamersname = []

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)

with open("russian.txt", 'r') as file:
  data = file.read()
  streamers = [line.strip() for line in data.split('\n') if line]

for line in streamers:
  streamersname.append(line.split(',')[0])
  streamerslink.append(line.split(',')[1])

with open('russian.csv', 'w', newline='') as file:
  writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
  writer.writerow(["Streamer", "Date", "Duration", "Viewers", "Language"])
  for streamerlink in streamerslink:
    streamername = streamersname[streamerslink.index(streamerlink)]
    print(streamername, streamerlink)
    try:
      driver.get(streamerlink+'/streams')
      dataControle = driver.find_element_by_xpath("//*[@id='streams']/tbody/tr[1]/td[1]/a/span").text
      print(dataControle)
      pagina=1
      ano = dataControle[dataControle.find(',')+2:dataControle.find(',')+6]
      while (int(ano)>2018):
        try:
          dataBase = driver.find_element_by_xpath("//*[@id='streams']/tbody/tr[1]/td[1]/a/span").text
          if(pagina<=5):
            driver.find_element_by_xpath("//*[@id='streams_paginate']/ul/li["+str(pagina)+"]/a").click()
          else:
            if(driver.find_element_by_xpath("//*[@id='streams_paginate']/ul/li[6]/a").text=='6'):
              driver.find_element_by_xpath("//*[@id='streams_paginate']/ul/li[6]/a").click()
            else:
              driver.find_element_by_xpath("//*[@id='streams_paginate']/ul/li[5]/a").click()
          if(pagina>2):
            if(dataBase==driver.find_element_by_xpath("//*[@id='streams']/tbody/tr[1]/td[1]/a/span").text):
              break
          for i in range(1,21):
            data = driver.find_element_by_xpath("//*[@id='streams']/tbody/tr["+str(i)+"]/td[1]/a/span").text
            data = data.replace('"', '')
            duracao = driver.find_element_by_xpath("//*[@id='streams']/tbody/tr["+str(i)+"]/td[2]/span").text
            viewers = driver.find_element_by_xpath("//*[@id='streams']/tbody/tr["+str(i)+"]/td[3]/span").text
            viewers = viewers.replace('"', '')
            viewers = viewers.replace(',', '.')
            writer.writerow([streamername, data, duracao, viewers, "russian"])
            ano= data[data.find(',')+2:data.find(',')+6]
          pagina+=1
        except:
          break
    except:
      print("Achou nao")
      continue  