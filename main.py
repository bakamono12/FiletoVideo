import asyncio
import os
import time
from pyrogram import Client, filters, enums
import logging
from pyrogram.errors import FloodWait
from config import session_string

# logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# bot
video_bot = Client("File-To-Video", session_string=session_string, workers=15)


@video_bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "Hi, I'm a bot that can convert video documents into streamable format. "
        "Just forward the message in the group or chat, and I will provide the streamable file.",
        quote=True)


@video_bot.on_message(filters.command("help"))
async def helps(client, message):
    await message.reply_text(
        "Just forward the video document in the group or chat, and I will provide the streamable file.\n"
        "In case of any help, contact @DTMK_C",
        quote=True)


async def update_my_progress(current, total, message=None, download_message=None, is_upload=False):
    percent = (current / total) * 100
    new_message = download_message.text + f"\nDownloading... {percent:.2f}%" if not is_upload \
        else f"Uploading... {percent:.2f}%"
    await video_bot.edit_message_text(chat_id=message.chat.id, message_id=download_message.id,
                                      text=new_message)
    await asyncio.sleep(3)


@video_bot.on_message(filters.video | filters.document)
async def convert_to_streamable(client, message):
    try:
        reply_one = await message.reply_text("Converting the file", quote=True)
        # check if the file is already converted
        s = time.time()
        download_file = await message.download(block=True, progress=update_my_progress,
                                               progress_args=(message, reply_one, False))
        e = time.time()
        logger.info(f"Downloaded the file in {e - s} seconds. ")
        # send the action stating the video upload
        s = time.time()
        await video_bot.send_chat_action(message.chat.id, action=enums.ChatAction.UPLOAD_VIDEO)
        await video_bot.send_video(message.chat.id, video=download_file,
                                   reply_to_message_id=message.id,
                                   progress=update_my_progress,
                                   progress_args=(message, reply_one, True))
        e = time.time()
        logger.info(f"Uploaded the file in {e - s} seconds")
        # delete the video file
        os.remove(download_file)
        await reply_one.delete()
    except FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception as e:
        await message.reply_text("Error occurred: %s" % str(e), quote=True)
        logger.error(e)


# start the bot
video_bot.run()
