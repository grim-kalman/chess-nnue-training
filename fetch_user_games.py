import os
import requests

def get_user_archives(username):
    url = f"https://api.chess.com/pub/player/{username}/games/archives"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    data = response.json()
    return data.get("archives", [])

def get_user_games(archives):
    if not os.path.exists("games"):
        os.makedirs("games")
    
    for archive in archives:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(archive, headers=headers)
        if response.status_code != 200:
            continue

        data = response.json()
        games = data.get("games", [])
        for game in games:
            file_path = os.path.join("games", f"{game['uuid']}.txt")
            with open(file_path, 'w') as file:
                file.write(str(game.get("pgn", "")))

archives = get_user_archives("GrimKalman")
get_user_games(archives)