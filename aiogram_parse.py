import asyncio, logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)

bot = Bot(token='6050659800:AAHPcJ1bs_ZfMvxorDIWnrpb5VWakVA34ew')

dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hello!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())