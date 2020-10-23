with open("portuguese.txt", 'r') as file:
  data = file.read()
  streamers = [line.strip() for line in data.split('\n') if line]
  print(streamers)