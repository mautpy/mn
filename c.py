from pyrogram import Client, filters

# Bot credentials
API_ID = "22625636"
API_HASH = "f71778a6e1e102f33ccc4aee3b5cc697"
BOT_TOKEN = "7857289090:AAEc7CEeHMAMvhKycSBhEUJKlPjL_hEg50s"

# List of video URLs
video_urls = [
    "https://t.me/how_2_use/15",
    "https://t.me/how_2_use/13",
]

# Initialize the bot
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Command to send videos
@app.on_message(filters.command("sendvideo"))
async def send_videos(client, message):
    chat_id = message.chat.id  # Get the user's chat ID
    
    for video_url in video_urls:
        await client.send_video(chat_id, video=video_url)

# Run the bot
app.run()
