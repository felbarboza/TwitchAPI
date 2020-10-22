from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

streamerslink = []
streamersname = []

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)


iterable = 1
while(iterable<=100):
  if(iterable==1):
    driver.get('https://twitchtracker.com/channels/rating')
  else:
    driver.get('https://twitchtracker.com/channels/rating?page='+str(iterable))
  for k in range(2, 12):
    streamerslink.append(driver.find_element_by_xpath("//*[@id='content-wrapper']/div[2]/div/div[1]/div["+str(k)+"]/div[3]/a").get_attribute('href'))
    streamersname.append(driver.find_element_by_xpath("//*[@id='content-wrapper']/div[2]/div/div[1]/div["+str(k)+"]/div[3]/a").text)
  iterable=iterable+1        

print(streamersname, streamerslink)                     

with open('data.csv', 'w', newline='') as file:
  writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
  writer.writerow(["Streamer", "Date", "Duration", "Viewers"])
  for streamerlink in streamerslink:
    streamername = streamersname[streamerslink.index(streamerlink)]
    print(streamername)
    try:
      driver.get(streamerlink+'/streams')
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
            writer.writerow([streamername, data, duracao, viewers])
            ano= data[data.find(',')+2:data.find(',')+6]
          pagina+=1
        except:
          break
    except:
      continue  