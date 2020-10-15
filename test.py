from twitchAPI import TwitchAPI
import csv
# 
streamers=["alanzoka", "Cellbit", "loud_coringa", "XANDAOOGOD", "Gaules", "NOBRU", "loud_bak", "YoDa", "loud_thurzin", "loud_babi", "Baiano", "brtt", "jukes", "forever", "Smurfdomuca", "gafallen", "ziGueira", "adolfz", "fer", "Rakin", "aXtLOL", "deercheerup", "SkipNhO", "jovirone", "calango", "jean_mago", "Felps", "tinows", "RatoBorrachudo", "keiozin", "Hayashii", "casimito", "hastad", "boltz", "loud_voltan", "pijack11"]
controllerAPI = TwitchAPI()

def printResponse(query):
  response = controllerAPI.get_response(query)
  responseJSON = controllerAPI.printResponse(response)
  return responseJSON


#query = controllerAPI.get_user_streams_query(user_login)

#query = controllerAPI.get_user_query(user_login)

#query = controllerAPI.get_sub_count(38244180)


with open('data2.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Streamer", "Date", "Duration", "Viewers"])
  for streamer in streamers:
    print(streamer)
    i=0
    streamerQuery = controllerAPI.get_user_streams_query(streamer)
    streamerQueryJSON = printResponse(streamerQuery)
    try:
      streamer_id=streamerQueryJSON["data"][0]["user_id"]
    except:
      print(streamerQueryJSON)
      continue
    print(streamer_id)
    cursor=''
    while(i<6):
      print(cursor)
      query = controllerAPI.get_user_videos_query(streamer_id, cursor) 
      jsonQuery = printResponse(query)
      #print(jsonQuery)
      try:
        cursor=jsonQuery["pagination"]["cursor"]
        for resp in jsonQuery["data"]:
          writer.writerow([resp["user_name"], resp["created_at"], resp["duration"], resp["view_count"]])
      except:
        print(jsonQuery)
      i=i+1
      

