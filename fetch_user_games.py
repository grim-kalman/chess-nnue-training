import os
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch_data(url):
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_user_archives(username):
    url = f"https://api.chess.com/pub/player/{username}/games/archives"
    data = fetch_data(url)
    return data.get("archives", [])

def get_user_games(archives):
    if not os.path.exists("games"):
        os.makedirs("games")
    
    for archive in archives:
        data = fetch_data(archive)
        games = data.get("games", [])
        for game in games:
            file_path = os.path.join("games", f"{game['uuid']}.txt")
            with open(file_path, 'w') as file:
                file.write(game.get("pgn", ""))

if __name__ == "__main__":
    username = "GrimKalman"
    archives = get_user_archives(username)
    get_user_games(archives)
