from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import bot
from aiogram.types import *

dp = Dispatcher(bot)
record = True  # переменная для имитации получение инфы о наборе(идет или нет)


@dp.message_handler(commands='start')
async def start_command(message: Message) -> None:
    """
    Функция для отображения стартового сообщения.
    :param message:
    :return: None
    """

    await message.answer('Привет 👋. Это основной бот проекта Banana Crypto. '
                         'Здесь ты можешь узнать более подробно о проекте и его продуктах. '
                         'Нажимай "Начать" и начнем общение.', reply_markup=
                         InlineKeyboardMarkup(row_width=1).add(
                             *[InlineKeyboardButton(text="Начать!", callback_data="WELCOME")]))


@dp.callback_query_handler(text="WELCOME")
async def welcome_func(query: CallbackQuery) -> None:
    """
    Приветсвенная функция, показывающая основное меню.
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
    if record:
        await query.message.answer('Набор нового потока уже в самом разгаре! Нажимай по кнопке ниже и '
                                   'наш менеджер поможет с выбором тарифа и оформлением заявки',
                                   reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
                                       InlineKeyboardButton(text="Связь с менеджером", callback_data="CONNECTION")
                                   ])
                                   )
    else:
        await query.message.answer('К сожалению, набора сейчас нет. Но вы можете попасть в предзапись '
                                   'следующего потока на нашем сайте: https://bananacrypto.ru/ Мы уведомляем '
                                   'участников предзаписи о ближайшем старте набора и даем лучшие '
                                   'условия для участия.')


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
    Функция для отправки информации о продуктах компании.
    :param query:
    :return: None
    Attributes:
        keyboard(InlineKeyboardMarkup): клавиатура, которая меняется в зависимости от уровня пользователя
    """
    # Проверка из бд уровня пользователя
    lvl = 2
    if lvl == 1:
        keyboard = InlineKeyboardMarkup(row_width=1).add(*[
            InlineKeyboardButton(text="О комьюнити", callback_data="COMMUNITY"),
            InlineKeyboardButton(text="О наставничестве", callback_data="MENTORING")
        ])
    else:
        keyboard = InlineKeyboardMarkup(row_width=1).add(*[
            InlineKeyboardButton(text="Вступить в комьюнити", callback_data="JOIN_COMMUNITY"),
            InlineKeyboardButton(text="О наставничестве", callback_data="MENTORING")
        ])

    await query.message.answer('Здесь ты можешь ознакомиться с основными продуктами нашего проекта. '
                               'Комьюнити - это доступ в наше закрытое сообщество профессионалов с '
                               'ежемесячной подпиской. Доступ в него только после подтверждения уровня '
                               'знаний. Наставничество - основная образовательная программа по освоению '
                               'навыка заработка на криптовалюте.',
                               reply_markup=keyboard
                               )


@dp.callback_query_handler(text="JOIN_COMMUNITY")
async def join_community_func(query: CallbackQuery) -> None:
    """
    Функция для отправки информации о стоимости подписки.
    :param query:
    :return: None
    """
    await query.message.answer('Доступные подписки:',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
                                   InlineKeyboardButton(text="1 месяц - 100$", callback_data="PAYMENT"),
                                   InlineKeyboardButton(text="2 месяца - 180$", callback_data="PAYMENT"),
                                   InlineKeyboardButton(text="3 месяца - 240$", callback_data="PAYMENT"),
                               ])
                               )


@dp.callback_query_handler(text="PAYMENT")
async def payment_func(query: CallbackQuery) -> None:
    """
    Функция для оплаты
    :param query:
    :return:
    """
    pass


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
    Функция для передачи ссылки на бота с тестом для поднятия уровня
    :param query:
    :return:
    """
    await query.message.answer('Вот ссылка на бота для прохождения теста: @testiruem_stud_bot')


@dp.callback_query_handler(text="CONGRATULATIONS")
async def congratulations_func(query: CallbackQuery):
    """
    Функция для оповещения пользователя, что его уровень был повышен
    :param query:
    :return:
    """
    await query.message.answer('Отлично! Ты справился со вступительным тестом. '
                               'Хорошего криптана видно из далека. Доступ откроется через... 1... 2... 3...',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
                                   InlineKeyboardButton(text="Продолжить", callback_data="LVL_UP")
                               ])
                               )


@dp.callback_query_handler(text="LVL_UP")
async def lvl_up_func(query: CallbackQuery):
    """
    Повышаем уровень пользователя, показываем пользователю новое меню.
    :param query:
    :return:
    """
    # повышаем уровень пользователя в бд
    await query.message.answer('Ура! Теперь доступно полное меню. Ниже ты можешь ознакомиться с ',
                               reply_markup=InlineKeyboardMarkup(row_width=3).add(*[
                                   InlineKeyboardButton(text="О проекте", callback_data="DESCRIPTION"),
                                   InlineKeyboardButton(text="Профиль", callback_data="PROFILE"),
                                   InlineKeyboardButton(text="Подписка", callback_data="SUBSCRIPTION"),
                                   InlineKeyboardButton(text="Магазин", callback_data="MARKET"),
                                   InlineKeyboardButton(text="Реферальная система", callback_data="REFERRAL"),
                               ])
                               )


@dp.callback_query_handler(text="SUBSCRIPTION")
async def check_sub_func(query: CallbackQuery):
    """
    Функция для получения инфонмации о подписке пользователя.
    :param query:
    :return:
    """
    await query.message.answer('Список подписок:\nПодписка: "название подписки в бд"\nСрок доступа: "schedule + бд"',
                               reply_markup=InlineKeyboardMarkup(row_width=3).add(*[
                                   InlineKeyboardButton(text="Главное меню", callback_data="DESCRIPTION"),
                                   InlineKeyboardButton(text="Продлить", callback_data="JOIN_COMMUNITY")
                               ]))


@dp.callback_query_handler(text="REFERRAL")
async def referral_func(query: CallbackQuery):
    """

    :param query:
    :return:
    """
    # инфа по рефералке
    pass


@dp.callback_query_handler(text="PROFILE")
async def check_profile_func(query: CallbackQuery):
    await query.message.answer('Мои данные\nПрофиль тг: @.\nGoogle-аккаунт: \nDiscord:',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(*[
                                   InlineKeyboardButton(text="Доступ в Notion", callback_data="NOTION_LINK"),
                                   InlineKeyboardButton(text="Доступ в Discord", callback_data="DISCORD_LINK"),
                                   InlineKeyboardButton(text="Доступ в чаты/каналы", callback_data="CHAT_LINK"),
                                   InlineKeyboardButton(text="Удалить из чатов/кналов", callback_data="DELETE_CHAT"),
                                   InlineKeyboardButton(text="Отключить google", callback_data="OFF_GOOGLE"),
                                   InlineKeyboardButton(text="Отключить Discord", callback_data="OFF_DISCORD")
                               ])
                               )


@dp.callback_query_handler(text="NOTION_LINK")
async def notion_func(query: CallbackQuery):
    await query.message.answer('Держи ссылку на Notion: "ссылка"')


@dp.callback_query_handler(text="DISCORD_LINK")
async def discord_func(query: CallbackQuery):
    await query.message.answer('Держи ссылку на Discord: "ссылка"')


@dp.callback_query_handler(text="CHAT_LINK")
async def discord_func(query: CallbackQuery):
    await query.message.answer('Ссылки на наши чаты/каналы: "ссылки"')


@dp.callback_query_handler(text="OFF_GOOGLE")
async def off_google_func(query: CallbackQuery):
    # отключение
    pass


@dp.callback_query_handler(text="OFF_DISCORD")
async def off_dicord_func(query: CallbackQuery):
    # отключение
    pass


@dp.callback_query_handler(text="DELETE_CHAT")
async def delete_chat_func(query: CallbackQuery):
    # удаление
    pass


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
