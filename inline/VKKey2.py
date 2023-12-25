from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackVK2 = CallbackData("create_post", "actionVK2")

confirmation_keyboardVK2 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackVK2.new(actionVK2="postVK2")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackVK2.new(actionVK2="cancelVK2")),
    ]]
)

