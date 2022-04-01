from telebot import TeleBot
import time

bot = TeleBot('5233453489:AAFiUt9BL9gzD-7lU3pwVsPFlY_y2HFZ158')


@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    name = message.new_chat_members[0].first_name 
    bot.send_message(message.chat.id, f"*Привіт, {name}!\nВітаємо Вас в групі для спілкування людей з різних міст України!\nХОЧЕТЕ ЗНАЙТИ ЗЕМЛЯКІВ?\nТОДІ ЖМІТЬ ТУТ:\n https://t.me/c/1541405527/436203\nПравила чату викликаються по команді  /rules*\n", parse_mode= "Markdown")
    
@bot.message_handler(content_types = ['new_chat_members', 'left_chat_member'])
def delete(message):
    bot.delete_message(message.chat.id, message.message_id) 
    
@bot.message_handler(commands=["ping"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Бот запущен и успешно работает!')
    


@bot.message_handler(commands=["rules"])
def start(m, res=False):
    bot.send_message(m.chat.id, f'''
*ПРАВИЛА ЧАТА.*

Вам 18+ і Ви з України (громадянство, місце народження або проживання)

*Забороняється:*
1. Неповажне ставлення до учасників, образи.
2. Порнографія, в тому числі гіф і стікери порнографічного характеру.
3. Дискримінація за національною ознакою, статі, орієнтації, релігійними та політичними переконаннями.
4. Пропаганда наркотичних речовин, включаючи легкі.
5. Завантаження шокуючого контенту.

Видалення і блокування учасників виконується на розсуд адміністрації.

СПІЛКУВАННЯ В ЧАТІ ВІДБУВАЄТЬСЯ  БУДЬ-ЯКОЮ ЗРУЧНОЮ ДЛЯ УЧАСНИКІВ МОВОЮ

Приємного спілкування!''', parse_mode= "Markdown")

    
if __name__ == '__main__':
    bot.polling(none_stop=True)
    
    
    
    
   
 


