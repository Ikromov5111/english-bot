from aiogram import types
from loader import dp
from .oxfordlook import getDefinitions
from googletrans import Translator

# # Echo bot
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)

@dp.message_handler(state=None)
async def tarjimon(message: types.Message):

    lang = Translator.translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(Translator.translator.translate(message.text,dest).text)
    else:
        if lang == 'en':
            word_id = message.text
            lookup = getDefinitions(word_id)
        else:
            word_id = Translator.translator.translate(message.text,dest ='en').text
            lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \n Definitions: \n {lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("bunday so'z topilmadi")
