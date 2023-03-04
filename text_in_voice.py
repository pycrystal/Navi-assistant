

from gtts import gTTS #Подключили библиотеку
from playsound import playsound

ru = str('запускаю') #Задали текст на русском языке

tts_ru = gTTS(ru, lang='ru') #Обозначили язык нашего текста

with open('vs1.mp3', 'wb') as f: #Создали файл в который будем писать звук из текста

    tts_ru.write_to_fp(f) #Записываем в файл озвучку русского текста
playsound('vs1.mp3')#Читаем тест