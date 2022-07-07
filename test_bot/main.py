from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import bot
from aiogram import types
from aiogram.types import *

dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_command(message: Message) -> None:
    """
    Функция для отображения стартового сообщения.
    :param message:
    :return: None
    """
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Начать тест", callback_data="START_TEST"))
    await message.answer('Привет! Это бот для проверки знаний в крипте для '
                         'вступления в комьюнити Banana Crypto. Далее тебе будет доступен тест на 20 вопросов. '
                         'На прохождение дается 1 час только 1 попытка. Рекомендуем сдать с первого раза) '
                         'Жми на кнопку "Начать тест" и пробуй свои силы.', reply_markup=keyboard)


@dp.callback_query_handler(text="START_TEST")
async def start_test_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    await query.message.answer('Привет! Это основной бот Banana Crypto! Выбери ниже, что тебя интересует:',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
                                   InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data="FAQ"),
                                   InlineKeyboardButton(text="О проекте", callback_data="DESCRIPTION"),
                                   InlineKeyboardButton(text="Магазин", callback_data="MARKET")
                               ])
                               )


@dp.callback_query_handler(text="FAQ")
async def faq_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    await query.message.answer('Часто задавемые вопросы:',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
                                   InlineKeyboardButton(text="О проекте", callback_data="DESCRIPTION"),
                                   InlineKeyboardButton(text="Магазин", callback_data="MARKET")
                               ])
                               )


@dp.callback_query_handler(text="DESCRIPTION")
async def description_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    await query.message.answer('Banana Crypto - это образовательный проект о заработке на криптовалютах от '
                               'Динара Фасхутдинова.Наша цель: сформировать самое сильное крипто-комьюнити на '
                               'русскоязычном рынке. Через наши программы прошло более 700 учеников и сформировало '
                               'сильное сообщество крипто-энтузиастов. Ниже ты можешь ознакомиться с участием нашем '
                               'наставничестве и/или комьюнити.',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
                                   InlineKeyboardButton(text="О комьюнити", callback_data="COMMUNITY"),
                                   InlineKeyboardButton(text="О наставничестве", callback_data="MENTORING"),
                                   InlineKeyboardButton(text="Социальные сети проекта", callback_data="SOCIAL_NET"),
                                   InlineKeyboardButton(text="Сайт проекта", callback_data="WEBSITE")
                               ])
                               )


@dp.callback_query_handler(text="SOCIAL_NET")
async def social_net_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    await query.message.answer('Инстаграм создателя проекта:  Instagram.com/dinar_banana')


@dp.callback_query_handler(text="MENTORING")
async def metorinf_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    await query.message.answer('Наставничество Banana Crypto - это 3-х месячная образовательная программа, '
                               'по освоению навыков заработка на криптовалюте с помощью опытных наставников.',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
                                   InlineKeyboardButton(text="Сайт проекта", callback_data="WEBSITE"),
                                   InlineKeyboardButton(text="Интервью с учениками", callback_data="INTERVIEW"),
                                   InlineKeyboardButton(text="Отзывы", callback_data="REVIEWS"),
                                   InlineKeyboardButton(text="Записаться на новый поток", callback_data="RECORD")
                               ])
                               )


@dp.callback_query_handler(text="RECORD")
async def record_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    # if record:
    #     await query.message.answer('Набор нового потока уже в самом разгаре! Нажимай по кнопке ниже и '
    #                                'наш менеджер поможет с выбором тарифа и оформлением заявки',
    #                                reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
    #                                    InlineKeyboardButton(text="Связь с менеджером", callback_data="CONNECTION")
    #                                ])
    #                                )
    # else:
    #     await query.message.answer('К сожалению, набора сейчас нет. Но вы можете попасть в предзапись '
    #                                'следующего потока на нашем сайте: https://bananacrypto.ru/ Мы уведомляем '
    #                                'участников предзаписи о ближайшем старте набора и даем лучшие '
    #                                'условия для участия.')


@dp.callback_query_handler(text="INTERVIEW")
async def interview_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    await query.message.answer('Мы взяли интервью у наших студентов, держи ссылку: '
                               'https://www.youtube.com/channel/UC0L0P92d6EOjvsOqBabUkHQ')


@dp.callback_query_handler(text="WEBSITE")
async def website_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    await query.message.answer('Вот ссылка для ознакомления с нашим сайтом: https://bananacrypto.ru/')


@dp.callback_query_handler(text="MARKET")
async def market_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    await query.message.answer('Здесь ты можешь ознакомиться с основными продуктами нашего проекта. '
                               'Комьюнити - это доступ в наше закрытое сообщество профессионалов с '
                               'ежемесячной подпиской. Доступ в него только после подтверждения уровня '
                               'знаний. Наставничество - основная образовательная программа по освоению '
                               'навыка заработка на криптовалюте.',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
                                   InlineKeyboardButton(text="О комьюнити", callback_data="COMMUNITY"),
                                   InlineKeyboardButton(text="О наставничестве", callback_data="MENTORING")
                               ])
                               )


@dp.callback_query_handler(text="COMMUNITY")
async def test_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    await query.message.answer('Для получения доступа к этому разделу требуется пройти тестирование на уровень '
                               'знаний в крипто-сфере. Переходи в бот-опросник, проходи тест. При успешной '
                               'сдаче здесь откроется дополнительное меню.',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
                                   InlineKeyboardButton(text="Пройти тест", callback_data="TEST")
                               ])
                               )


@dp.callback_query_handler(text="TEST")
async def test_func(query: CallbackQuery) -> None:
    """

    :param query:
    :return:
    """
    await query.message.answer('Вот ссылка на бота для прохождения теста. "ссылка на бота"')

# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)
