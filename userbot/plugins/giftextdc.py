from userbot import bot 
from userbot import bot as borg
global hawkmoth
hawkmoth="I0Rvbm90IEthbmcgTUFERSBCWSBAVEhFX0JMX0FDS19IQVQgTU9ESUZJRUQgQlkgU2gxdmFtICNUZWFtIERDIA=="
from userbot.utils import admin_cmd
from PIL import Image, ImageDraw, ImageFont
import os
from userbot import CMD_HELP

@borg.on(admin_cmd(pattern="giftext ?(.*)"))
async def lol(event):
    await event.delete()
    if not os.path.isdir("./imglol"):
        os.makedirs("./imglol")
    rasta = './imglol'
    reply = await event.get_reply_message()
    me= await borg.download_media(reply.media, rasta)
    lol = event.text
    hui, font,size,color,align,loop,duration= lol[9:].split('|')
    #hui,size,color,align= lol[9:].split('|')
    loltext = hui



    x,y=align.split(";")

    size=int(size)


    def adi(text):
        img = Image.open(me)
        #fnt = f'userbot/helpers/styles/{font}'
        fonts = ImageFont.truetype(r"Fonts/{}".format(font),size)
        draw = ImageDraw.Draw(img)
        draw.text(((int(x), int(y))), text,fill=(color),font=fonts )

        return img

    # Create the frames
    frames = []

    def ruil(text):
        global c
        for i in range(len(text)+1):
            new_frame = adi(text[:i])
            frames.append(new_frame)
        c = 0

    all_text = f"{loltext}"
    ruil(all_text)


    # Save into a GIF file that loops forever
    frames[0].save('catnoiar.gif', format='GIF',
                   append_images=frames[1:], save_all=True, duration=int(duration), loop=int(loop))
    ukanger = "catnoiar.gif" 
    await borg.send_file(event.chat_id, ukanger)
global miracul



#     made by @Royal_boy_45 
# Shivansh Rajput
