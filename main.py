import os
import random
import speech_recognition#Требуется для прослушки команд
import webbrowser#Требуется для открытия браузера
from playsound import playsound#Требуется для озвучивание текста
import time

print()

while True:
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5

    commands_dict = {#Все команды прописываются тут 
        'commands': {           
            'greeting': ['привет нави', 'привет navi', 'нави привет', 'navi привет', 'привет наве', 'привет', 'привет нами', 'привет навим', 'привет навушка', 'я дома' ],
            'create_task': ['добавить задачу', 'создать задачу', 'заметка', 'добавить заметку'],
            'brouser': ['запусти браузер', 'открой браузер', 'браузер', 'нави открой браузер', 'navi открой браузер', 'наве открой браузер', 'включи браузер', 'navi включи браузер' ],
            'study': ['NaVi Включи музыку', 'navi музыка', 'нави включи музыку', 'наве музыка', 'музыка', 'включи музыку', 'надя включи музыку', 'на avi Включи музыку', 'наве Включи музыку'],
            'where': ['нави','наве','navi','nave','нав', 'nav', 'ave', 'налим', 'навушка', 'навин', 'навим', 'новим', 'нарин'],
            'end': ['navi уйди', 'уйди navi', 'уйди', 'потеряйся', 'выключись', 'ну иди', 'ну уйди', 'пока navi', 'пока', 'выйди', 'до завтра', 'до завтра нави', 'до завтра navi'], 
            'mood': ['как дела', 'как настрой', 'как себя чувствуешь', 'navi как дела', 'наве как дела', 'всё в порядке','как себя чувствуешь','не расстраивайся', 'всё хорошо', 'как дела навек'],
            'thanks': ['молодец', 'а ты не плоха','хорошо постаралась','хорош','умница', 'спасибо', 'navi спасибо', 'спасибо navi', 'а ты молодец'],
            'ender': ['navi выключи компьютер', 'надя выключи компьютер', 'NaVi Выключи компьютер'],
            'vs': ['navi открой vscode', 'navi vscode', 'navi открой редактор', 'navi vscode', 'navi открой vs код', 'Ну и открой vs код', 'navi vs код'],
            'telegram': ['navi включи telegram', 'navi telegram', 'надя включи telegram', 'navi открой telegram', 'на аве открой Telegram']
        }
    }

    def listen_command():#распознает слова в тексте
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                

            return query
        except speech_recognition.UnknownValueError:
            return 'Не поняла что ты сказал'

    def greeting():#вызывывает ответ на приветствие 
        hello = ['voice/hello/hello.mp3', 'voice/hello/hello2.mp3', 'voice/hello/hello3.mp3']
        playsound(random.choice(hello))
        
    def vs():#включает VScode    
        vs = ['voice/vs/vs.mp3', 'voice/vs/vs1.mp3']
        playsound(random.choice(vs))
        os.system('/usr/share/code/code')
    
    def telegram():#включает Telegram    
        telegram = ['voice/vs/vs.mp3', 'voice/vs/vs1.mp3']
        playsound(random.choice(telegram))
        os.system('/home/desart/Telegram/Telegram')   

    def where():#ищет запрос в интернете
        ans = ['voice/where/where.mp3', 'voice/where/where1.mp3', 'voice/where/where2.mp3']
        playsound(random.choice(ans))
        query = listen_command()
        print(query)
        webbrowser.open ('https://www.google.com/search?q='+ query, new=2)
        playsound('voice/enternet/enternet1.mp3')
    
        
    
    def mood():#Отвечает на вопрос как дела
        ans = ['voice/mood/mood.mp3', 'voice/mood/mood1.mp3', 'voice/mood/mood2.mp3', 'voice/mood/mood3.mp3', 'voice/mood/mood4.mp3']
        playsound(random.choice(ans))   

    def thanks():#отвечает на похвалу
        ans = ['voice/thank/thanks.mp3', 'voice/thank/thanks1.mp3', 'voice/thank/thanks2.mp3', 'voice/thank/thanks3.mp3', 'voice/thank/thanks4.mp3']    
        playsound(random.choice(ans)) 

    def create_task():#создает todo-list
        with open('todo-list.txt', 'a') as file:
            playsound('voice/note/note.mp3')
            query = listen_command() 
            file.write(f'❗️ {query}\n')
            playsound('voice/note/notes.mp3')
        

    def brouser():#Открывает браузер
        webbrowser.open ('https://', new=1)
        playsound('voice/open/open.mp3')

    def ender():#Выключает компьютер
        playsound('voice/ender/ender.mp3')
        os.system('systemctl poweroff') 

    def study():#Включает музыку в браузере
        webbrowser.open ('https://www.youtube.com/live/jfKfPfyJRdk?feature=share', new=2)
        playsound('voice/music/music.mp3')
        
    def end():#Выключает голосового помощника
        playsound('voice/end/end.mp3')
        exit()

    def main():#Сравнивает команды с командами в списке
        query = listen_command()
        
        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())
            

    if __name__ == '__main__':
        main()



