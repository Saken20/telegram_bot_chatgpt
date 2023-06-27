import logging
import openai

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

API_TOKEN = '6221935907:AAHwaaHg33grUksbKIqLp7S3GATeLqQeAQE'
OPENAI_API_KEY = "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"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    await message.answer("Hi there! I'm ChatGPT bot powered by OpenAI.\nHow can I help you today?")

@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    """
    Command handler for help command
    """
    await message.answer("I'm here to answer your questions to the best of my abilities!\nFeel free to ask me anything.")

@dp.message_handler(content_types=['text'])
async def chat_handler(message: types.Message):
    """
    Handle all text messages
    """
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{message.text}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)