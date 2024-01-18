import os
import logging
import texts
from telegram import Update , InlineKeyboardButton, InlineKeyboardMarkup , constants
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = texts.text1
    keyboard = [
        [[ InlineKeyboardButton("How Do I Join A2SV Community Education?", callback_data="2")]],
        [[ InlineKeyboardButton("How Do I Join A2SV?", callback_data="1", url="https://t.me//CommunityTrial_bot?start")]]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard[0])

    
    # await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('assets/a2sv.jpg', 'rb'))
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, 
                                   reply_markup=reply_markup, parse_mode = constants.ParseMode.HTML)

    



async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() 
    text1 = texts.text1
    text2 = texts.text2
    text3 = texts.text3
    text4 = texts.text4
    text5 = texts.text5
    faq = texts.faq
    announcement = texts.announcements
    contest = texts.contest
    discussion = texts.discussion

    keyboard = [
       [ [ InlineKeyboardButton("How Do I Get Started?", callback_data="2")] ],
       [ [ InlineKeyboardButton("Step 2", callback_data="3")] ],
       [ [ InlineKeyboardButton("Step 3", callback_data="4")] ],
       [ [ InlineKeyboardButton("Guide", callback_data="5")] ],
    ]
    
    keyboard2 = [[ InlineKeyboardButton("FAQs", callback_data="faq"), InlineKeyboardButton("Announcements", callback_data="announcement")],
                 [ InlineKeyboardButton("Contests", callback_data="contest"), InlineKeyboardButton("Discussion", callback_data="discussion")],
                 [ InlineKeyboardButton("Go Back To The Group", url= "https://t.me/A2SVDiscussion", callback_data="go_back_to_the_group")]]
    
    reply_markup1 = InlineKeyboardMarkup(keyboard[0])
    reply_markup2 = InlineKeyboardMarkup(keyboard[1])
    reply_markup3 = InlineKeyboardMarkup(keyboard[2])
    reply_markup4 = InlineKeyboardButton(keyboard[3])
    reply_markup5 = InlineKeyboardMarkup(keyboard2)
    # reply_markup6 = InlineKeyboardButton(keyboard[4])

    if query.data == "1":
        pass
        # await context.bot.send_message(chat_id=query.message.chat_id, text=text1, reply_markup=reply_markup1, parse_mode= constants.ParseMode.HTML)
    elif query.data =="2":
        await context.bot.sendMessage(chat_id=query.message.chat_id, text=text2, reply_markup=reply_markup2, parse_mode= constants.ParseMode.HTML)
    elif query.data =="3":
         await context.bot.sendMessage(chat_id=query.message.chat_id, text=text3, reply_markup=reply_markup3, parse_mode= constants.ParseMode.HTML)
    elif query.data =="4":
         await context.bot.sendMessage(chat_id=query.message.chat_id, text=text4, reply_markup=reply_markup5, parse_mode= constants.ParseMode.HTML)
    elif query.data =="5":
         await context.bot.sendMessage(chat_id=query.message.chat_id, text=text5, reply_markup=reply_markup5, parse_mode= constants.ParseMode.HTML)
    elif query.data == "faq":
        await context.bot.sendMessage(chat_id=query.message.chat_id, text=faq, parse_mode= constants.ParseMode.HTML)

    elif query.data == "announcement":
        await context.bot.sendMessage(chat_id=query.message.chat_id, text=announcement,  parse_mode= constants.ParseMode.HTML)
  
    elif query.data == "contest":
        await context.bot.sendMessage(chat_id=query.message.chat_id, text=contest,  parse_mode= constants.ParseMode.HTML)
  
    elif query.data == "discussion":
        await context.bot.sendMessage(chat_id=query.message.chat_id, text=discussion, parse_mode= constants.ParseMode.HTML)
    
    



if __name__ == '__main__':
    application = ApplicationBuilder().token('6607983770:AAH0ZPcVGzsw_Pk56ElVUcja4dVgtju6aXI').build()
    

    TOKEN = "6607983770:AAH0ZPcVGzsw_Pk56ElVUcja4dVgtju6aXI"
    PORT = int(os.environ.get('PORT', '8443'))
    # add handlers
    
    start_handler = CommandHandler('start', start)
    button_handler = CallbackQueryHandler(button)

    application.add_handler(start_handler)
    application.add_handler(button_handler)

    application.run_webhook(
        listen="0.0.0.0",
        port=8443,
        webhook_url="https://41d5-197-156-86-205.ngrok-free.app"
    )
    
    # application.run_polling(allowed_updates=Update.ALL_TYPES)