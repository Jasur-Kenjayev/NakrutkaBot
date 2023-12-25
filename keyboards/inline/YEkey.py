from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackYE = CallbackData("create_post", "actionYE")

confirmation_keyboardYE = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackYE.new(actionYE="postYE")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackYE.new(actionYE="cancelYE")),
    ]]
)

