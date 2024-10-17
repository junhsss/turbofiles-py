import asyncio
import os
from turbofiles import AsyncClient


async def main():
    api_key = os.environ["TURBOFILES_API_KEY"]
    client = AsyncClient(api_key)
    try:
        download_url = await client.compress("/path/to/file")
        print(f"Compressed file: {download_url}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())
