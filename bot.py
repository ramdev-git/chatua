from telebot import TeleBot 

bot = TeleBot('5233453489:AAFiUt9BL9gzD-7lU3pwVsPFlY_y2HFZ158')


@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    name = message.new_chat_members[0].first_name 
    bot.send_message(message.chat.id, f"Привіт, {name}!\nВітаємо Вас в групі для спілкування людей з різних міст України!\nХОЧЕТЕ ЗНАЙТИ ЗЕМЛЯКІВ?\nТОДІ ЖМІТЬ ТУТ:\n https://t.me/c/1541405527/436203\nПравила чату викликаються по команді  /rules \nРозробник: @ViacheslavUkraine \nПишіть мені якщо у вас є пропозиція! ")

@bot.message_handler(content_types = ['new_chat_members', 'left_chat_member'])
def delete(message):
    bot.delete_message(message.chat.id, message.message_id) 
    
@bot.message_handler(commands=["ping"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Бот запущен и успешно работает!')
    

if __name__ == '__main__':
    bot.polling(none_stop=True)
    
    
    
    
   
 


