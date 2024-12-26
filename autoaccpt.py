from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

# Manually setting the bot token and API credentials
environ["BOT_TOKEN"] = "7740922993:AAFPzuwZDAfUuyMEgQFg0iMnGfCD9cmwiPs"
environ["API_ID"] = "25707779"  # Replace with your actual API ID
environ["API_HASH"] = "929888fadc26c0670e78e16fe0a3aa6a"  # Replace with your actual API hash

pr0fess0r_99 = Client(
    "Auto Approved Bot",
    bot_token=environ["BOT_TOKEN"],
    api_id=int(environ["API_ID"]),
    api_hash=environ["API_HASH"]
)

# Start command to greet the user and show buttons
@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me()  # Get bot information (includes bot username)
    
    button = [
        [InlineKeyboardButton("Add Me In Chat ➕", url="http://t.me/Araccbot?startgroup=botstart"),
         InlineKeyboardButton("Add Me In Channel ➕", url="http://t.me/Araccbot?startchannel=botstart")],
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
    # Customized text as per your requirement
    greeting_text = f"**Hello {user.first_name},\n\nThank you for joining. We suggest you to also check out our other channels for more exciting content!"

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

# Start the bot asynchronously
async def main():
    print("Auto Approved Bot running...")
    await pr0fess0r_99.start()

# Run the bot asynchronously
import asyncio
asyncio.run(main())
