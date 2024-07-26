import json
import requests
import wikipediaapi
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from translate import Translator

def get_games_list(steam_api_key):
    url = f"https://api.steampowered.com/ISteamApps/GetAppList/v0002/?key={steam_api_key}format=json"

    response = requests.get(url)
    response.raise_for_status()
    games_list = response.json()["applist"]["apps"]
    return games_list

def get_game_by_id(game_id):
    url = "https://store.steampowered.com/api/appdetails?"
    appid = game_id
    params = {
        "appids": appid,
        '&l': 'ru',
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_game_info(game_json):
    names_add = 0
    if names_add == 0:
        for num,el in game_json.items():
            if el['success'] and el['data']['type'] == 'game':
                
                game_info = el['data']

                name = game_info['name']
                technics = get_technics(name)

                if game_info["release_date"]["coming_soon"]:
                    date = "Скоро выйдет"
                else:
                    date = game_info["release_date"]['date']

                author = "None"
                for num,item in game_info.items():
                    if num == 'developers':
                        author = game_info['developers'][0]


                description = game_info["about_the_game"]
                correct_desc = get_desc(description)

                req = game_info['pc_requirements']
                filtered_min = []
                filtered_recom = []
                if req.__class__ == dict:
                    filtered_recom = []
                    for num, item in req.items():
                        if num == 'minimum':
                            filtered_min = get_req(item)
                        elif num == 'recommended':
                            filtered_recom = get_req(item)




                img_url = game_info['header_image']

                names_add += 1
                generate_game_data(name, date, author, correct_desc, filtered_min, technics, img_url, filtered_recom)
            # print(name)
            # print(date)
            # print(author)
            # print(correct_desc)
            # print(filtered_min)
            # print(technics)
            # print(img_url)

def get_req(item):
    allreq = []
    filteredreq = []

    soup = BeautifulSoup(item, 'html.parser')

    allreq = soup.findAll('li')
    for data in allreq:
        if data.find('strong',) is not None:
            filteredreq.append(data.text)

    return filteredreq

def get_desc(description):
    desc_block = []
    ul_items = []

    soup = BeautifulSoup(description, 'html.parser')

    elements = [
        element.strip() 
        for element in soup.find_all(string=True) 
            if element.strip() and element.strip() != '<br/>' and element.strip() != 'Key features:'
    ]

    ul_tag = soup.find('ul', class_='bb_ul')
    if ul_tag:
        ul_items = [li.text for li in ul_tag.find_all('li')]

    elements = [e for e in elements if e not in ul_items]

    desc_block.append(elements)
    desc_block.append(ul_items)

    return desc_block

def get_technics(name):
    wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (nazarvusik77@gmail.com)', 'en', extract_format=wikipediaapi.ExtractFormat.HTML)

    name = name.replace(" ", "_")
    page_py = wiki_wiki.page(name)
    all_technics = ['Nintendo Switch','PlayStation 4','PlayStation 5','Xbox One','Windows','Linux','Android','macOS','iOS','Xbox 360']
    technics = []
    if page_py.exists():
        print("Существует")
        for techn in all_technics:
            if techn in page_py.text:
                print("Есть")
                technics.append(techn)
    else:
        print(f"Страница не существует. Name: {name}")
    print(technics)
    return technics

def search_game(name):
    add = 0
    with open('myproject/games.json', 'r', encoding='Utf-8') as f:
        data = json.load(f)
    for i, game in enumerate(data['games']):
        if name.lower() == game['name'].lower():
            add = add + 1
    if add >= 1:
        return False
    else:
        return True

def generate_game_data(name, date, author, correct_desc, filtered_min, technics, img_url, filtered_recom):
    with open('myproject/games.json', 'r', encoding='Utf-8') as f:
        data = json.load(f)

    data['games'].append({
        'name': name,
        'date': date,
        'author': author,
        'description': correct_desc,
        'requirements': {
            'min': filtered_min,
            'max': filtered_recom,
            'technic': technics
        },
        'img_url': img_url
    })

    with open('myproject/games.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    update_json()

    print(f'Done!!! - {name}')

def update_json():
    # Загрузка данных из JSON-файла
    with open('myproject/games.json', 'r', encoding='Utf-8') as f:
        data = json.load(f)

    # Присвоение id каждому элементу в массиве games
    for i, game in enumerate(data['games']):
        game['id'] = i

    # Запись обновленных данных в файл
    with open('myproject/games.json', 'w', encoding='Utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def translater(text):
    translator= Translator(to_lang="ru")
    translation = translator.translate(text)
    return translation

def add_games(name, names_add_1, names_add_2, game_block):
    lower_name = name.lower()
    lower_game_name = game_block['name'].lower()

    if lower_name in lower_game_name:
        result = search_game(lower_game_name)
        if result:
            names_add_1 += 1
            if names_add_1%2 != 0:
                # print(name,game_block['appid'])
                # print(names_add)
                game_id = game_block['appid']
                game_json = get_game_by_id(game_id)
                for num,el in game_json.items():
                    for num,i in el.items():
                        names_add_2 += 1
                        if names_add_2%2 != 0:
                            print(names_add_1)
                            if i:
                                get_game_info(game_json)
        else:
            print("Добавлена")

def main():
    name = "Craft"
    load_dotenv()
    steam_api_key = os.environ.get("STEAM_API_KEY")
    game_list = get_games_list(steam_api_key)
    names_add_1 = 0
    names_add_2 = 0
    for game_block in game_list:
        add_games(name, names_add_1, names_add_2, game_block)



if __name__ == '__main__':
    main()

