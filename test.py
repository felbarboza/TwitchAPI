from twitchAPI import TwitchAPI

user_login = 'ninja'

controllerAPI = TwitchAPI()

def printResponse(query):
  response = controllerAPI.get_response(query)
  controllerAPI.printResponse(response)

# query = controllerAPI.get_user_query(user_login)
# printResponse(query)

#query = controllerAPI.get_user_streams_query(user_login)
#printResponse(query)

query = controllerAPI.get_games_query()
printResponse(query)