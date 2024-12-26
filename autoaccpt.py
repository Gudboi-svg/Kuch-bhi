import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from aiohttp import web

# Manually setting the bot token and API credentials
environ = os.environ
environ["BOT_TOKEN"] = "7678544492:AAFUq20f4cqEQgz7pjyKoalNiFW2v9TOA3E"
environ["API_ID"] = "25707779"  # Replace with your actual API ID
environ["API_HASH"] = "929888fadc26c0670e78e16fe0a3aa6a"  # Replace with your actual API hash

# Define the bot class
class AutoApproveBot(Client):
    def __init__(self):
        super().__init__(
            "Auto Approved Bot",
            bot_token=environ["BOT_TOKEN"],
            api_id=int(environ["API_ID"]),
            api_hash=environ["API_HASH"]
        )
    
    async def start_server(self):
        """Start a dummy web server for Koyeb deployment"""
        app = web.Application()
        app.add_routes([web.get("/", self.handle)])  # Handle requests at root ("/")
        runner = web.AppRunner(app)
        await runner.setup()
        port = int(os.getenv("PORT", 8080))  # Use PORT env variable, default to 8080
        site = web.TCPSite(runner, "0.0.0.0", port)
        await site.start()
        print(f"Web server running on port {port}")

    async def handle(self, request):
        """Simple handler for web server requests"""
        return web.Response(text="AutoApproveBot is running!")

    async def start(self):
        # Start the bot in a separate task
        bot_task = asyncio.create_task(super().start())
        web_server_task = asyncio.create_task(self.start_server())

        # Wait for both tasks to finish
        await asyncio.gather(bot_task, web_server_task)

    async def stop(self, *args):
        await super().stop()
        print("AutoApproveBot has stopped")

# Define the command handler for '/start' to greet the user and show buttons
@AutoApproveBot.on_message(filters.private & filters.command(["start"]))
async def start(client, message: Message):
    button = [
        [InlineKeyboardButton("Add Me In Chat ➕", url="http://t.me/Araccbot?startgroup=botstart"),
         InlineKeyboardButton("Add Me In Channel ➕", url="http://t.me/Araccbot?startchannel=botstart")],
        [InlineKeyboardButton("🗿 Owner", url="t.me/bakanuehe")]
    ]
    
    # Send the welcome message with buttons
    await client.send_message(
        chat_id=message.chat.id,
        text=f"**Hello {message.from_user.first_name}, I am the Auto Approver Join Request Bot.**\n\n"
             f"**Just Add Me To Your Group / Channel**",
        reply_markup=InlineKeyboardMarkup(button),
        disable_web_page_preview=True
    )

# Handle new join requests and automatically approve them
@AutoApproveBot.on_chat_join_request(filters.group | filters.channel)
async def auto_approve(client, message: ChatJoinRequest):
    chat = message.chat
    user = message.from_user
    print(f"{user.first_name} joined 🤝")  # Logs user who joined
    
    # Approve the join request
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    
    # Send the welcome message to the user via private chat (DM)
    greeting_text = f"**Hello {user.first_name}, welcome to the group!\n\nThank you for joining. We suggest you to also check out our other channels for more exciting content!**"
    
    # Buttons for channel invites (replace with actual invite links)
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

if __name__ == "__main__":
    bot = AutoApproveBot()
    bot.run()  # Start the bot and web server
