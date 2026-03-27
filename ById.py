import asyncio
import requests
id = "7f9d2acb-1c64-43a6-af66-72139f860863" #you can get from url directly 
api = "https://api.emergency-hamburg.com/public/servers"

async def monitor():
    r = requests.get(api).json() # getting all servers by public apo
    for s in r: # for 1 in all
          if s.get('privateServerId') == id: # search our server by If
              txt = f"{s['serverName']}\n {s['currentPlayers']}/{s['maxPlayers']}"
              print(txt)

if __name__ == '__main__':
    asyncio.run(monitor())
  
