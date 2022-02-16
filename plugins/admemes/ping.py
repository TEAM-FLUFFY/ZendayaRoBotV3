"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ല മുത്തേ ഞാൻ എപ്പോഴും ജീവനോടെ ഒണ്ട് എന്റ മൊതലി <a href=https://t.me/TEAM_KERALA>ᖴᑌᑕK Oᖴᖴ🇨🇷[𝗢𝗙𝗙𝗟𝗜𝗡𝗘]</a></b> ഇതെഹം ആണ് എന്ന നിർമിച്ചെടുത്തത്.. I Like My Owner..🔥" 
HELP = "എന്തിനാ നിനക്ക് ഇപ്പൊ help🤔......"
REPO = "ʀᴇᴘᴏ ɪs ᴘʀɪᴠᴀᴛᴇ https://github.com/TEAM-FLUFFY/ZendayaRoBotV3 ɪᴛʜɪʟ ɴᴇᴋᴋɪ ᴛɪᴍᴇ ᴡᴀsᴛᴇ ᴄʜᴇʏʏᴀɴᴅᴀ"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("▣▣▣")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
