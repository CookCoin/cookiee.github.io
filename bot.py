import asyncio

from aiogram import Router, Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder


def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlinekeyboardBuilder()
    builder.button(
        text="Podnali", web_app=WebAppinfo(
            url="..."
        )
    )
    return builder.as_markup()


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply(Hello)


async def main() -> None:
    bot = Bot(...)(parse_mode=ParseMode.HTML)


    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
