import asyncio
import requests
name = "full name with space or flags if needs" # also can get from url directly
api = "https://api.emergency-hamburg.com/public/servers"

async def monitor():
    r = requests.get(api).json() # getting all servers by public api
    print(r)
    for s in r: # for 1 in all
          if s.get('serverName') == name: # search our server by If
              txt = f"{s['serverName']}\n {s['currentPlayers']}/{s['maxPlayers']}"
              print(txt)

if __name__ == '__main__':
    asyncio.run(monitor())
  
