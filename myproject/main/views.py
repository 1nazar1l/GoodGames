from django.shortcuts import render
from .models import JSONData


def index(request):
    json_data = JSONData()
    context = {
        'data': json_data.data
    }
    return render(request, 'main/index.html', context)


def game_page(request, game_id=None):

    def get_game_by_id(game_id):
        json_data = JSONData()
        data = json_data.data
        for i,game in enumerate(data['games']):
            if game['id'] == game_id:
                return game


    if request.method == 'GET' and request.GET.get('game_id'):
        # Получение game_id из GET-параметра
        game_id = request.GET.get('game_id')

        
    
    game = get_game_by_id(game_id)
    
    # Передайте данные об игре в контекст шаблона
    context = {
        'game': game
    }
    
    # Отрендерите шаблон страницы игры
    return render(request, 'main/game_page.html', context)
