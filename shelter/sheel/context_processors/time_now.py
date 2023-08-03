from django.utils import timezone
from random import choice


def year(request):
    variables = [
        'А ЭТО ВЛАДИМИР...',
        'GPT не глупая, GPT починит',
        'X',
        'Современая поп культура фигня',
        'Мир, дружба, пиво',
        'Голова, глаза',
        'СБЭУ',

    ]
    var = choice(variables)
    year = timezone.now().year
    return {
        'year': year,
        'var': var,
    }
