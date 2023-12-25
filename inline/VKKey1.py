from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackVK1 = CallbackData("create_post", "actionVK1")

confirmation_keyboardVK1 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackVK1.new(actionVK1="postVK1")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackVK1.new(actionVK1="cancelVK1")),
    ]]
)

