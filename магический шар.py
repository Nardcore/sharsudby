import random
print('привет')
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print ('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input ('Как же зовут странник?\n')
print (f'Привет {name}')
more = 'да'
while more == 'да':
    question = input (f'{name} Задавай вопрос и я предскажу твою судьбу\n')
    print (random.choice (answers))
    more = input ('Хочешь задать еще вопрос? да или нет?\n').lower ()
    if more != 'да':
        print ('Возвращайся если возникнут вопросы!')
