import os
from turbofiles import Client


def main():
    api_key = os.environ["TURBOFILES_API_KEY"]
    client = Client(api_key)
    try:
        download_url = client.compress("/path/to/file")
        print(f"Compressed file: {download_url}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
