from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

streamers=["alanzoka", "Cellbit", "XANDAOOGOD", "Gaules", "YoDa", "Baiano", "brtt", "jukes", "forever", "Smurfdomuca", "gafallen", "ziGueira", "adolfz", "fer", "Rakin", "aXtLOL", "SkipNhO", "jovirone", "calango", "jean_mago", "Felps", "RatoBorrachudo", "keiozin", "Hayashii", "hastad", "boltz", "pijack11"]

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)

with open('data2.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Streamer", "Date", "Duration", "Viewers"])
  for streamer in streamers:
    driver.get('https://twitchtracker.com/'+streamer+'/streams')
    dataControle = driver.find_element_by_xpath("//*[@id='streams']/tbody/tr[1]/td[1]/a/span").text
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
          writer.writerow([streamer, data, duracao, viewers])
          ano= data[data.find(',')+2:data.find(',')+6]
        pagina+=1
      except:
        break
      
        