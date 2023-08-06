import asyncio
from enkanetwork import EnkaNetworkAPI

client = EnkaNetworkAPI(lang="it")

async def main():
    async with client:
        data = await client.fetch_user(183579315)
        print(data.characters[4].skills)
    

asyncio.run(main())