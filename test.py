from twitchAPI import TwitchAPI

user_login = 'ninja'

controllerAPI = TwitchAPI()

def printResponse(query):
  response = controllerAPI.get_response(query)
  responseJSON = controllerAPI.printResponse(response)
  return responseJSON


#query = controllerAPI.get_user_streams_query(user_login)

#query = controllerAPI.get_user_query(user_login)

#query = controllerAPI.get_sub_count(38244180)

query = controllerAPI.get_user_videos_query(38244180)
jsonQuery = printResponse(query)

for resp in jsonQuery["data"]:
  print(resp["created_at"])
  print(resp["duration"])
  print(resp["view_count"])
  print("")