class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ {},
Mʏ Nᴀᴍᴇ Is <a href=https://t.me/{}>{}</a>, I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs, Jᴜsᴛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Eɴᴊᴏʏ 😍</b>."""
    HELP_TXT = """<b>Hᴇʏ {}
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs..</b>"""
    ABOUT_TXT = """<b>✯ Mʏ Nᴀᴍᴇ : <a href='https://t.me/Oru_adaar_Robot'>Nᴀɴᴄʏ ~ 🎀.</a>
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/Hacker_Jr'>HᴀᴄKᴇʀ Jʀ ~ 🕊.</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʀᴏɢʀᴀᴍ.</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/'>Pʏᴛʜᴏɴ 3.</a>
✯ Dᴀᴛᴀ Bᴀsᴇ: <a href='https://cloud.mongodb.com/'>Mᴏɴɢᴏ Dʙ.</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://okteto.com/'>Oᴋᴛᴇᴛᴏ.</a>
✯ Bᴜʟʟᴅ Sᴛᴀᴛᴜs: <code>ᴠ2.8.1 [ Bᴇᴛᴀ ].</code></b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""

    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    FILE_MSG = """
<b>Hai 👋 {} </b>😍

<b>📫 Your File is Ready</b>

<b>📂 Fɪʟᴇ Nᴀᴍᴇ</b> : <code>{}</code>
                                   
<b>⚙️ Fɪʟᴇ Sɪᴢᴇ</b> : <b>{}</b>
"""
    CHANNEL_CAP = """<b>Hai 👋 {}</b> 😍

<code>{}</code>

⚠️ <b>This file will be deleted from here within 10 minute as it has copyright ... !!!</b>

<b>കോപ്പിറൈറ്റ് ഉള്ളതുകൊണ്ട് ഫയൽ 10 മിനിറ്റിനുള്ളിൽ ഇവിടെനിന്നും ഡിലീറ്റ് ആകുന്നതാണ് അതുകൊണ്ട് ഇവിടെ നിന്നും മറ്റെവിടെക്കെങ്കിലും മാറ്റിയതിന് ശേഷം ഡൗൺലോഡ് ചെയ്യുക!</b>

<b>© Powered by @Team_KL</b>"""
