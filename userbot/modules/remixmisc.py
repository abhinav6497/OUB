#imported from github.com/ravana69/PornHub to userbot by @heyworld 
#please don't nuke my credits 😓
import requests
import bs4 
import os
import asyncio
import time
import html
from justwatch import JustWatch
from telethon import *
from userbot.events import register 
from userbot import CMD_HELP, bot, TEMP_DOWNLOAD_DIRECTORY, DEFAULT_BIO, ALIVE_NAME
from telethon import events
from telethon.tl import functions, types
from urllib.parse import quote
from datetime import datetime
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChatBannedRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.tl.types import DocumentAttributeVideo
from telethon.errors.rpcerrorlist import YouBlockedUserError


import logging

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
weebyfont = ['卂', '乃', '匚', '刀', '乇', '下', '厶', '卄', '工', '丁', '长', '乚', '从', '𠘨', '口', '尸', '㔿', '尺', '丂', '丅', '凵',
             'リ', '山', '乂', '丫', '乙']



logger = logging.getLogger(__name__)

thumb_image_path = TEMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


if 1 == 1:
    name = "Profile Photos"
    client = bot



@register(outgoing=True, pattern="^.app(?: |$)(.*)")
async def apk(e):
    try:
        app_name = e.pattern_match.group(1)
        remove_space = app_name.split(' ')
        final_name = '+'.join(remove_space)
        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps")
        lnk = str(page.status_code)
        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')
        results = soup.findAll("div","ZmHEEd")
        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text
        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text
        app_dev_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']
        app_rating = results[0].findNext('div', 'Vpfmgd').findNext('div', 'pf5lIe').find('div')['aria-label']
        app_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']
        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']
        app_details = "<a href='"+app_icon+"'>📲&#8203;</a>"
        app_details += " <b>"+app_name+"</b>"
        app_details += "\n\n<code>Developer :</code> <a href='"+app_dev_link+"'>"+app_dev+"</a>"
        app_details += "\n<code>Rating :</code> "+app_rating.replace("Rated ", "⭐ ").replace(" out of ", "/").replace(" stars", "", 1).replace(" stars", "⭐ ").replace("five", "5")
        app_details += "\n<code>Features :</code> <a href='"+app_link+"'>View in Play Store</a>"
        app_details += "\n\n===> [Abhinav Shinde](t.me/AbhinavShinde) <==="
        await e.edit(app_details, link_preview = True, parse_mode = 'HTML')
    except IndexError:
        await e.edit("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await e.edit("Exception Occured:- "+str(err))


        
@register(outgoing=True, pattern="^.undlt(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    c = await event.get_chat()
    if c.admin_rights or c.creator:
        a = await bot.get_admin_log(event.chat_id,limit=1, search="", edit=False, delete=True)
        for i in a:
          await event.reply(i.original.action.message)
    else:
        await event.edit("You need administrative permissions in order to do this command")
        await asyncio.sleep(3)
        await event.delete()
        
@register(outgoing=True, pattern="^.calc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input = event.pattern_match.group(1) #get input
    exp = "Given expression is " + input #report back input
    #lazy workaround to add support for two digits
    final_input = tuple(input)
    term1part1 = final_input[0]
    term1part2 = final_input[1]
    term1 = str(term1part1) + str(term1part2)
    final_term1 = (int(term1))
    operator = str(final_input[2])
    term2part1 = final_input[3]
    term2part2 = final_input[4]
    term2 = str(term2part1) + str(term2part2)
    final_term2 = (int(term2))
    #actual calculations go here
    if input == "help":
        await event.edit("Syntax .calc <term1><operator><term2>\nFor eg .calc 02*02 or 99*99 (the zeros are important) (two terms and two digits max)")
    elif operator == "*":
        await event.edit("Solution -->\n" + exp + "\n" + str(final_term1 * final_term2))
    elif operator == "-":
        await event.edit("Solution -->\n" + exp + "\n" + str(final_term1 - final_term2))
    elif operator == "+":
        await event.edit("Solution -->\n" + exp + "\n" + str(final_term1 + final_term2))
    elif operator == "/":
        await event.edit("Solution -->\n" + exp + "\n" + str(final_term1 / final_term2))
    elif operator == "%":
        await event.edit("Solution -->\n" + exp + "\n" + str(final_term1 % final_term2))
    else:
        await event.edit("use .calc help")
        
@register(outgoing=True, pattern="^.xcd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xkcd_id = None
    if input_str:
        if input_str.isdigit():
            xkcd_id = input_str
        else:
            xkcd_search_url = "https://relevantxkcd.appspot.com/process?"
            queryresult = requests.get(
                xkcd_search_url,
                params={
                    "action":"xkcd",
                    "query":quote(input_str)
                }
            ).text
            xkcd_id = queryresult.split(" ")[2].lstrip("\n")
    if xkcd_id is None:
        xkcd_url = "https://xkcd.com/info.0.json"
    else:
        xkcd_url = "https://xkcd.com/{}/info.0.json".format(xkcd_id)
    r = requests.get(xkcd_url)
    if r.ok:
        data = r.json()
        year = data.get("year")
        month = data["month"].zfill(2)
        day = data["day"].zfill(2)
        xkcd_link = "https://xkcd.com/{}".format(data.get("num"))
        safe_title = data.get("safe_title")
        transcript = data.get("transcript")
        alt = data.get("alt")
        img = data.get("img")
        title = data.get("title")
        output_str = """[\u2060]({})**{}**
[XKCD ]({})
Title: {}
Alt: {}
Day: {}
Month: {}
Year: {}""".format(img, input_str, xkcd_link, safe_title, alt, day, month, year)
        await event.edit(output_str, link_preview=True)
    else:
        await event.edit("xkcd n.{} not found!".format(xkcd_id))
        
        
@register(outgoing=True, pattern="^.remove(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
        return False
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not (chat.admin_rights or chat.creator):
            await event.edit("`You aren't an admin here!`")
            return False
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    await event.edit("Searching Participant Lists.")
    async for i in bot.iter_participants(event.chat_id):
        p = p + 1
        #
        # Note that it's "reversed". You must set to ``True`` the permissions
        # you want to REMOVE, and leave as ``None`` those you want to KEEP.
        rights = ChatBannedRights(
            until_date=None,
            view_messages=True
        )
        if isinstance(i.status, UserStatusEmpty):
            y = y + 1
            if "y" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit("I need admin priveleges to perform this action!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusLastMonth):
            m = m + 1
            if "m" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit("I need admin priveleges to perform this action!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusLastWeek):
            w = w + 1
            if "w" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit("I need admin priveleges to perform this action!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusOffline):
            o = o + 1
            if "o" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit("I need admin priveleges to perform this action!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusOnline):
            q = q + 1
            if "q" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit("I need admin priveleges to perform this action!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusRecently):
            r = r + 1
            if "r" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit("I need admin priveleges to perform this action!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if i.bot:
            b = b + 1
            if "b" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit("I need admin priveleges to perform this action!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        elif i.deleted:
            d = d + 1
            if "d" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit("I need admin priveleges to perform this action!")
                    e.append(str(e))
                else:
                    c = c + 1
        elif i.status is None:
            n = n + 1
    if input_str:
        required_string = """Kicked {} / {} users
Deleted Accounts: {}
UserStatusEmpty: {}
UserStatusLastMonth: {}
UserStatusLastWeek: {}
UserStatusOffline: {}
UserStatusOnline: {}
UserStatusRecently: {}
Bots: {}
None: {}"""
        await event.edit(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await asyncio.sleep(5)
    await event.edit("""Total= {} users
Number Of Deleted Accounts= {}
Status: Empty= {}
      : Last Month= {}
      : Last Week= {}
      : Offline= {}
      : Online= {}
      : Recently= {}
Number Of Bots= {}
Unidentified= {}""".format(p, d, y, m, w, o, q, r, b, n))


async def ban_user(chat_id, i, rights):
    try:
        await bot(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)
    
    
@register(outgoing=True, pattern="^.rnupload(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    await event.edit("`Rename & Upload in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big`")
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        end = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        to_download_directory = TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await bot.download_media(
            reply_message,
            downloaded_file_name,
            )
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            c_time = time.time()
            await bot.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
                )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await event.edit("Downloaded in {} seconds. Uploaded in {} seconds.".format(ms_one, ms_two))
        else:
            await event.edit("File Not Found {}".format(input_str))
    else:
        await event.edit("Syntax // .rnupload filename.extension as reply to a Telegram media")

    
       
@register(outgoing=True, pattern="^.grab(?: |$)(.*)")
async def potocmd(event):
        """Gets the profile photos of replied users, channels or chats"""
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await bot.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await event.edit("`ID number you entered is invalid`")
                    return
            except:
                 await event.edit("`lol wtf`")
                 return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await bot.send_file(event.chat_id, send_photos)
            else:
                await event.edit("`No photo found of that Nigga , now u Die`")
                return


@register(outgoing=True, pattern="^.res(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to a Link.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Reply to a Link```")
       return
    chat = "@CheckRestrictionsBot"
    sender = reply_message.sender
    await event.edit("```Processing```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=894227130))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("`RIP Check Your Blacklist Boss`")
              return
          if response.text.startswith(""):
             await event.edit("Am I Dumb Or Am I Dumb?")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
            
            
@register(outgoing=True, pattern="^.clone(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await event.edit(str(error_i_a))
        return False
    user_id = replied_user.user.id
    profile_pic = await event.client.download_profile_photo(user_id, TEMP_DOWNLOAD_DIRECTORY)
    # some people have weird HTML in their names
    first_name = html.escape(replied_user.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their names
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.user.last_name
    # last_name is not Manadatory in @Telegram
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
      last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    # inspired by https://telegram.dog/afsaI181
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = html.escape(replied_user.about)
    await bot(functions.account.UpdateProfileRequest(
        first_name=first_name
    ))
    await bot(functions.account.UpdateProfileRequest(
        last_name=last_name
    ))
    await bot(functions.account.UpdateProfileRequest(
        about=user_bio
    ))
    n = 1
    pfile = await bot.upload_file(profile_pic)  # pylint:disable=E060      
    await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
        pfile
    ))
    #message_id_to_reply = event.message.reply_to_msg_id
    #if not message_id_to_reply:
    #    message_id_to_reply = event.message.id
    #await bot.send_message(
    #  event.chat_id,
    #  "Hey ? Whats Up !",
    #  reply_to=message_id_to_reply,
    #  )
    await event.delete()
    await bot.send_message(
      event.chat_id,
      "**cloned like pero.**",
      reply_to=reply_message
      )

async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.from_id or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.from_id
                )
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
            

def get_stream_data(query):
    stream_data = {}

    # Compatibility for Current Userge Users
    try:
        country = Config.WATCH_COUNTRY
    except Exception:
        country = "IN"

    # Cooking Data
    just_watch = JustWatch(country = country)
    results = just_watch.search_for_item(query = query)
    movie = results['items'][0]
    stream_data['title'] = movie['title']
    stream_data['movie_thumb'] = "https://images.justwatch.com"+movie['poster'].replace("{profile}","")+"s592"
    stream_data['release_year'] = movie['original_release_year']
    try:
        print(movie['cinema_release_date'])
        stream_data['release_date'] = movie['cinema_release_date']
    except KeyError:
        try:
            stream_data['release_date'] = movie['localized_release_date']
        except KeyError:
            stream_data['release_date'] = None

    stream_data['type'] = movie['object_type']

    available_streams = {}
    for provider in movie['offers']:
        provider_ = get_provider(provider['urls']['standard_web'])
        available_streams[provider_] = provider['urls']['standard_web']
    
    stream_data['providers'] = available_streams

    scoring = {}
    for scorer in movie['scoring']:
        if scorer['provider_type']=="tmdb:score":
            scoring['tmdb'] = scorer['value']

        if scorer['provider_type']=="imdb:score":
            scoring['imdb'] = scorer['value']
    stream_data['score'] = scoring
    return stream_data

#Helper Functions
def pretty(name):
    if name=="play":
        name = "Google Play Movies" 
    return name[0].upper()+name[1:]

def get_provider(url):
    url = url.replace("https://www.","")
    url = url.replace("https://","")
    url = url.replace("http://www.","")
    url = url.replace("http://","")
    url = url.split(".")[0]
    return url

@register(outgoing=True, pattern="^.watch(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    await event.edit("Finding Sites...")
    streams = get_stream_data(query)
    title = streams['title']
    thumb_link = streams['movie_thumb']
    release_year = streams['release_year']
    release_date = streams['release_date']
    scores = streams['score']
    try:
        imdb_score = scores['imdb']
    except KeyError:
        imdb_score = None
    
    try:
        tmdb_score = scores['tmdb']
    except KeyError:
        tmdb_score = None
        
    stream_providers = streams['providers']
    if release_date is None:
        release_date = release_year

    output_ = f"**Movie:**\n`{title}`\n**Release Date:**\n`{release_date}`"
    if imdb_score:
        output_ = output_ + f"\n**IMDB: **{imdb_score}"
    if tmdb_score:
        output_ = output_ + f"\n**TMDB: **{tmdb_score}"

    output_ = output_ + "\n\n**Available on:**\n"
    for provider,link in stream_providers.items():
        if 'sonyliv' in link:
            link = link.replace(" ","%20")
        output_ += f"[{pretty(provider)}]({link})\n"
    
    await bot.send_file(event.chat_id, caption=output_, file=thumb_link,force_document=False,allow_cache=False, silent=True)
    await event.delete()

#credits:
#Ported from Saitama Bot. 
#By :- @PhycoNinja13b
#Modified by :- @kirito6969,@deleteduser420
@register(outgoing=True, pattern="^.weeb(?: |$)(.*)")
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = ' '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)
   

boldfont = ['𝗮', '𝗯', '𝗰', '𝗱', '𝗲', '𝗳', '𝗴', '𝗵', '𝗶', '𝗷', '𝗸', '𝗹', '𝗺', '𝗻', '𝗼', '𝗽', '𝗾', '𝗿', '𝘀', '𝘁', '𝘂',
              '𝘃', '𝘄', '𝘅', '𝘆', '𝘇']
   
@register(outgoing=True, pattern="^.bold(?: |$)(.*)")
async def thicc(bolded):

    args = bolded.pattern_match.group(1)
    if not args:
        get = await bolded.get_reply_message()
        args = get.text   
    if not args:
        await bolded.edit("`What I am Supposed to bold for U Dumb`")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            boldcharacter = boldfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boldcharacter)
    await bolded.edit(string)
    
    
medievalbold = ['𝖆', '𝖇', '𝖈', '𝖉', '𝖊', '𝖋', '𝖌', '𝖍', '𝖎', '𝖏', '𝖐', '𝖑', '𝖒', '𝖓', '𝖔', '𝖕', '𝖖', '𝖗', '𝖘', '𝖙', '𝖚',
                '𝖛', '𝖜', '𝖝', '𝖞', '𝖟']
   
@register(outgoing=True, pattern="^.medibold(?: |$)(.*)")
async def mediv(medievalx):

    args = medievalx.pattern_match.group(1)
    if not args:
        get = await medievalx.get_reply_message()
        args = get.text   
    if not args:
        await medievalx.edit("`What I am Supposed to medieval bold for U Dumb`")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            medievalcharacter = medievalbold[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, medievalcharacter)
    await medievalx.edit(string)
    
    
doublestruckt = ['𝕒', '𝕓', '𝕔', '𝕕', '𝕖', '𝕗', '𝕘', '𝕙', '𝕚', '𝕛', '𝕜', '𝕝', '𝕞', '𝕟', '𝕠', '𝕡', '𝕢', '𝕣', '𝕤', '𝕥', '𝕦',
                '𝕧', '𝕨', '𝕩', '𝕪', '𝕫']
   
@register(outgoing=True, pattern="^.doublestruck(?: |$)(.*)")
async def doublex(doublestrucktx):

    args = doublestrucktx.pattern_match.group(1)
    if not args:
        get = await doublestrucktx.get_reply_message()
        args = get.text   
    if not args:
        await doublestrucktx.edit("`What I am Supposed to double struck for U Dumb`")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            strucktcharacter = doublestruckt[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, strucktcharacter)
    await doublestrucktx.edit(string)
    
    
cursiveboldx = ['𝓪', '𝓫', '𝓬', '𝓭', '𝓮', '𝓯', '𝓰', '𝓱', '𝓲', '𝓳', '𝓴', '𝓵', '𝓶', '𝓷', '𝓸', '𝓹', '𝓺', '𝓻', '𝓼', '𝓽', '𝓾',
                '𝓿', '𝔀', '𝔁', '𝔂', '𝔃']  
   
@register(outgoing=True, pattern="^.curbold(?: |$)(.*)")
async def cursive2(cursivebolded):

    args = cursivebolded.pattern_match.group(1)
    if not args:
        get = await cursivebolded.get_reply_message()
        args = get.text   
    if not args:
        await cursivebolded.edit("`What I am Supposed to cursive bold for U Dumb`")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursiveboldcharacter = cursiveboldx[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, cursiveboldcharacter)
    await cursivebolded.edit(string)
    
    
medival2 = ['𝔞', '𝔟', '𝔠', '𝔡', '𝔢', '𝔣', '𝔤', '𝔥', '𝔦', '𝔧', '𝔨', '𝔩', '𝔪', '𝔫', '𝔬', '𝔭', '𝔮', '𝔯', '𝔰', '𝔱', '𝔲',
            '𝔳', '𝔴', '𝔵', '𝔶', '𝔷']
   
@register(outgoing=True, pattern="^.medi(?: |$)(.*)")
async def medival22(medivallite):

    args = medivallite.pattern_match.group(1)
    if not args:
        get = await medivallite.get_reply_message()
        args = get.text   
    if not args:
        await medivallite.edit("`What I am Supposed to medival for U Dumb`")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            medivalxxcharacter = medival2[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, medivalxxcharacter)
    await medivallite.edit(string)
    
    
    
cursive = ['𝒶', '𝒷', '𝒸', '𝒹', '𝑒', '𝒻', '𝑔', '𝒽', '𝒾', '𝒿', '𝓀', '𝓁', '𝓂', '𝓃', '𝑜', '𝓅', '𝓆', '𝓇', '𝓈', '𝓉', '𝓊',
           '𝓋', '𝓌', '𝓍', '𝓎', '𝓏']
   
@register(outgoing=True, pattern="^.cur(?: |$)(.*)")
async def xcursive(cursivelite):

    args = cursivelite.pattern_match.group(1)
    if not args:
        get = await cursivelite.get_reply_message()
        args = get.text   
    if not args:
        await cursivelite.edit("`What I am Supposed to cursive for U Dumb`")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursivecharacter = cursive[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, cursivecharacter)
    await cursivelite.edit(string)

    
@register(outgoing=True, pattern="^.rclone(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    name = f"{ALIVE_NAME}"
    bio = f"{DEFAULT_BIO}"
    n = 1
    await bot(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit= n)))
    await bot(functions.account.UpdateProfileRequest(about=bio))
    await bot(functions.account.UpdateProfileRequest(first_name=name))
    await event.edit("succesfully reverted to your account back")
            
CMD_HELP.update({
    "remixmisc":
    "`.app`\
\nUsage: type .app name and get app details.\
\n\n`.undlt`\
\nUsage: undo deleted message but u need admin permission.\
\n\n`.calc`\
\nUsage:.calc <term1><operator><term2>\nFor eg .calc 02*02 or 99*99 (the zeros are important) (two terms and two digits max).\
\n\n`.remove`\
\nUsage:.remove d or y or m or w or o or q or r.\n(d=deletedaccount y=userstatsempty m=userstatsmonth w=userstatsweek o=userstatsoffline q=userstatsonline r=userstatsrecently).\
\n\n`.xcd`\
\nUsage: type xcd <query>.ps:i have no damm idea how it works 🤷\
\n\n`.grab` <count>\
\nUsage:replay .grab or .grab <count> to grab profile picture.\
\n\n`.rnupload` filename.extenstion\
\nUsage:reply to a sticker and type .rnupload xyz.jpg\
\n\n`.clone` @username and '.rclone' for reverting\
\nUsage: clone you whole freking account except username so stay safe\
\n\n`.res`\
\nUsage: type account,channel,group or bot username and reply with .res and check restriction\
\n\n`.watch` <movie/tv> show\
\nUsage:know details about particular movie/show.\
\n\n`.weeb` <text>\
\nUsage:weebify a text\
\n\nIt contains (`.bold <text>`,`.cur <text>`,`.curbold <text>`,`.medi <text>`,`.medibold <text>`,`.doublestruck <text>`)\
\nUsage:makes your text <bold,cursive,cursivebold,medival,medivalbold,gayishbold>\
\n\n`.randompp`\
\nUsage:Automatically changes your profile picture after one hour. To stop this use .restart.\
\n\n`.gps` <location name>.\
\nUsage:Sends you the given location name.\
\n\n`.ls` <directory>.\
\nUsage:Get list file inside directory.\
\n\n<`.modi` or `.trump` or `.cmm` or `.kanna`> <text>\
\n\nUsage: just for fun.\
\n\n`.hc` **sign**\
\nExample:`.hc scorpio`\
\nUsage:Gets your horoscope.\
\n\n`.tweet` <username>.<tweet>\
\nUsage:Create tweet with custom username.\
\n\nmention: Mention users with a custom name.\
\nUsage:`Hi @ender1324[bluid boi]`\
\nResult:Hi [bluid boi](tg://resolve?domain=ender1324)."
})
