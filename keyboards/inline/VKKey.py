from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackVK = CallbackData("create_post", "actionVK")

confirmation_keyboardVK = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackVK.new(actionVK="postVK")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackVK.new(actionVK="cancelVK")),
    ]]
)

