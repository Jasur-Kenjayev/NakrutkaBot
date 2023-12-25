from aiogram.dispatcher.filters.state import StatesGroup, State


class BalansS(StatesGroup):
    mball = State()
    oball = State()
    baConfirm = State()
