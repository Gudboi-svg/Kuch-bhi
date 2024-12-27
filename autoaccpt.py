from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from aiohttp import web
import asyncio

# Manually setting the bot token and API credentials
environ["BOT_TOKEN"] = "7678544492:AAFUq20f4cqEQgz7pjyKoalNiFW2v9TOA3E"
environ["API_ID"] = "25707779"  # Replace with your actual API ID
environ["API_HASH"] = "929888fadc26c0670e78e16fe0a3aa6a"  # Replace with your actual API hash

# Define a variable for the base URL of your Koyeb app
BASE_URL = "gradual-larisa-animebotforpractice-f4065a4e.koyeb.app"

# Create a new client instance
pr0fess0r_99 = Client(
    "Auto Approved Bot",
    bot_token=environ["BOT_TOKEN"],
    api_id=int(environ["API_ID"]),
    api_hash=environ["API_HASH"]
)

# Start command to greet the user and show buttons
@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    button = [
        [InlineKeyboardButton("Add Me In Chat ➕", url=f"http://t.me/Araccbot?startgroup=botstart"),
         InlineKeyboardButton("Add Me In Channel ➕", url=f"http://t.me/Araccbot?startchannel=botstart")],
        [InlineKeyboardButton("🗿 Owner", url="t.me/bakanuehe")]
    ]
    
    # Send the welcome message with bold text and buttons
    await client.send_message(
        chat_id=message.chat.id,
        text=f"**Hello {message.from_user.first_name}, I am the Auto Approver Join Request Bot.**\n\n"
             f"**Just Add Me To Your Group / Channel**",
        reply_markup=InlineKeyboardMarkup(button),
        disable_web_page_preview=True
    )

# Handle new join requests and automatically approve
@pr0fess0r_99.on_chat_join_request(filters.group | filters.channel)
async def auto_approve(client: pr0fess0r_99, message: ChatJoinRequest):
    chat = message.chat
    user = message.from_user
    print(f"{user.first_name} joined 🤝")  # Logs user who joined

    # Approving join request
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)

    # Send the welcome message to the user via private chat (DM)
    greeting_text = f"**Hello {user.first_name},\n\nThank you for joining. We suggest you also check out our other channels for more exciting content!**"

    # Buttons for channel invites (add your actual invite links here)
    buttons = [
        [InlineKeyboardButton("BackUp Channel", url="https://t.me/backuphentai"),
         InlineKeyboardButton("PVT METHODS", url="https://t.me/+mp84LUoFPvAxM2E1")]
    ]
    
    # Send the customized greeting message with buttons to the user's private chat (DM)
    await client.send_message(
        chat_id=user.id,
        text=greeting_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )

# A basic aiohttp web server setup
async def start_aiohttp():
    app = web.Application()

    # Define a simple health check route for the server to be up
    async def health_check(request):
        return web.Response(text="Server is up and running!")

    app.router.add_get('/health', health_check)

    # Start the aiohttp server on port 8080 (as Koyeb expects it)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)  # Listen on port 8080
    await site.start()

    print(f"Aiohttp server running on port 8080 for {BASE_URL}")

    # Run the bot alongside aiohttp
    await pr0fess0r_99.start()

    # Keep the server running
    while True:
        await asyncio.sleep(3600)  # Sleep to keep the server running

# Run both aiohttp server and the bot
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_aiohttp())  # Start the aiohttp server
    loop.run_forever()  # Keep the bot running forever
