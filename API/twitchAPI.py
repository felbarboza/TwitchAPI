import requests, json, sys


class TwitchAPI:
  BASE_URL='https://api.twitch.tv/helix/'
  CLIENT_ID = 'ogjzlp3vmjzs8mfbut4kd2p1di4zop'
  SECRET = 'd10s1787s68ccssxvzl9fk7wf6zid9'
  ACCESS_TOKEN = ''
  HEADERS = ''
  INDENT = 2

  def __init__(self):
    AutURL ='https://id.twitch.tv/oauth2/token'
    AutParams = {'client_id': self.CLIENT_ID, 'client_secret': self.SECRET, 'grant_type': 'client_credentials'}
    AutCall = requests.post(url=AutURL, params=AutParams)
    data = AutCall.json()
    self.ACCESS_TOKEN = data['access_token']
    self.HEADERS = {'Client-ID': self.CLIENT_ID, 'Authorization': "Bearer " +  self.ACCESS_TOKEN }

  def get_response(self, query):
    url = self.BASE_URL + query
    response = requests.get(url, headers=self.HEADERS)
    return response

  def printResponse(self, response):
    #print(response.content)
    response_json = response.json()
    print_response = json.dumps(response_json, indent=self.INDENT)
    print(print_response)
    return response.json()

  def get_user_streams_query(self, user_login):
    return 'streams?user_login={0}'.format(user_login)

  def get_user_query(self, user):
    return 'streams?login={0}'.format(user)

  def get_streamers(self):
    return 'streams?language=pt'

  def get_streamer_config(self, name):
    return 'users?login={0}&first=1'.format(name)

  def get_user_videos_query(self, user_id, after):
    if(after==''):
      return 'videos?user_id={0}&first=100'.format(user_id)
    return 'videos?user_id={0}&first=100&after={1}'.format(user_id, after)

  def get_games_query(self):
    return 'games/top'

  def get_sub_count(self, user_id):
    return 'subscriptions?broadcaster_id={0}'.format(user_id)
  