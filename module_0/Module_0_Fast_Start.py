#!/usr/bin/env python
# coding: utf-8

# In[97]:


import numpy as np
def game_core_v3(number):
    '''Сначала устанавливаем число как середину диапозона 1-100, 
       а потом если загаданонное число больше значения середины, 
       то поиск осуществляется во втором (верхнем) диапозоне, 
       иначе — в первом (нижнем).
       Далее алгоритм повторяется: определение середины нового диапопзона,
       сравнение числа с серединой и движение к следующему диапозону.
       Процесс продолжается до тех пор, пока число не будет найдено.'''
    count = 0
    up_number = 101 # верхняя граница диапозона
    low_number = 0 # нижняя граница диапозона
    predict = 0
    while number != predict:
        count+=1
        predict = (up_number + low_number)//2 # середина диапозона
        if number > predict: 
            low_number = predict
        elif number < predict: 
            up_number = predict
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# In[98]:


number = 3    # загадали число
score_game(game_core_v3)

