from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery,User, Chat, Poll, PollOption
from pyrogram import filters, Client, errors, enums, utils
from pyrogram.raw import functions
from pyrogram.errors import UserNotParticipant 
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.errors import FloodWait, UserPrivacyRestricted, UserRestricted, PeerFlood, UserNotMutualContact, UserChannelsTooMuch
from pyrogram.raw.functions.chatlists import CheckChatlistInvite, JoinChatlistInvite,LeaveChatlist
from pyrogram.raw.types import InputChatlistDialogFilter, InputPeerChat, InputPeerUser, Poll
from database import *
from pyrogram.utils import get_peer_id
from pyrogram.raw.functions.account import GetAuthorizations, ResetAuthorization

from pyrogram.raw.base import input_peer, PollAnswer
from pyrogram.raw.functions.messages import AddChatUser
from pyrogram.raw.base import Poll, PollResults
from pyrogram.raw.base.messages import MessageViews
from button import *
from configs import cfg
#from pyrogram.types import UserStatus
from texts import *
from database import *
from pyrogram.raw import functions, types
from pyrogram.raw.functions.messages import GetMessagesViews
import requests
import datetime
import json, requests, re
import subprocess
import telethon
import os,sys
import zipfile
import configparser
from telethon.sync import TelegramClient
import sys, time, os, random
import json
import configparser
import requests
from database import *
from texts import *
import re
import json

from data import *
from zipfile import ZipFile
import random
from pyrogram.types import BotCommand, Poll, PollOption
from pyrogram.handlers import MessageHandler, CallbackQueryHandler, ChosenInlineResultHandler




token = cfg.BOT_TOKEN;
botID  =  int(token.split(':')[0]);

appa	  = Client(f"sessions/0HMXQ3IPOY",
               api_id="25849984",
               api_hash="0485b0a59bc7138c53eec4b79a66a058");

sss = appa.start()
print(sss)
ddd = appa.get_me()
print(ddd)

app = Client(
    "Bot",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

owner = 6460393623

def zip_folder(folder_path, zip_name):
	with ZipFile(zip_name, 'w') as zipf:
		for root, _, files in os.walk(folder_path):
			for file in files:
				file_path = os.path.join(root, file)
				arc_name = os.path.relpath(file_path, folder_path)
				zipf.write(file_path, arcname=arc_name)

def sendMessage(chat_id, text):
	URL	  = "https://api.telegram.org/bot"+cfg.BOT_TOKEN+"/sendmessage"
	PARAMS = {'chat_id': chat_id, 'text': text}
	RGET       = requests.get(url=URL, params=PARAMS);
	return json.loads(RGET.text)

sessions	      = os.listdir('sessions');
random.shuffle(sessions);
THE_SESSIONS = os.listdir('sessions');
cSessions	   = len(THE_SESSIONS);

#status = get(user_id, 'status', 'database/mover.json')
xview = 10 
maxview = 500
xpoll = 50
maxpoll = 1000
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command(commands="start", prefixes="/"))
async def op(_, m: Message):
    #if not already_db(m.from_user.id):

    try:
        await app.send_chat_action(m.from_user.id, enums.ChatAction.TYPING)
        delete(m.from_user.id, None, 'database/mover.json')
        await app.get_chat_member(cfg.CHID, m.from_user.id)
        ref = 10  # تم تعديل هذا السطر ليكون رقمًا صحيحًا بدلاً من سلسلة نصية
        user_id = m.from_user.id
        if m.chat.type == enums.ChatType.PRIVATE:
            update_join_date(user_id=user_id)
            #join_date = update_join_date["join_date"].strftime("%Y-%m-%d %H:%M:%S")
            if not already_db(user_id):
                add_user(m.from_user.id)
                update_join_date(user_id)
                x = all_users() 
                await app.send_message(chat_id=owner,text="**※ مستخدم جديد ✅※.\n\n※ معلومات المستخدم الجديد  : 👇: \n• الاسم  :  {}\n • الايدي  :  `{}`\n• اليوزر  :  @{}\n\n※ إجمالي المستخدمين  :  {}.**".format(m.from_user.mention, m.from_user.id, m.from_user.username, x))
                command = m.text.split()
                if len(command) == 2:
                    refuser = command[1]
                    increment_referral_count(refuser)
                    add_points(refuser, ref)
                    await app.send_message(chat_id=refuser, text="**- 🎉 تهانينا، تمت إضافة عمولة الاحالة إلى حسابك مقابل  الإشتراك الجديد🥳.**")
                if already_pro(user_id): 
                    type = "Premium" 
                elif not already_pro(user_id): 
                    type = "Free" 
                else: 
                    type = "None"              
                await m.reply_text(text="**🧰 مرحبًا {}!\n🔋 حالة الروبوت: نشط ✅.\n👀 نوع المستخدم: {}\nأخيرًا!  أنا هنا في متناول يدك!\nيمكنني القيام بالعديد من المهام رغم أنها معقدة وصعبة!  ولكن لا بأس لا شيء يمكن أن يمنعني!  😁.\nكيف يمكنني مساعدتك🫣؟  \n\nسأكون سعيدًا بتقديم المساعدة 👨🏻‍💻.\n\nبرمجة وتطوير : @ddddi**".format(m.from_user.mention, type), reply_markup=ButtonsStart)
            else:
                if already_pro(user_id):
                    type = "Premium"
                elif not already_pro(user_id):
                    type = "Free" 
                else: 
                    type = "None"        
                await m.reply_text(text="**🧰 مرحبًا {}!\n🔋 حالة الروبوت: نشط ✅.\n👀 نوع المستخدم: {}\nأخيرًا!  أنا هنا في متناول يدك!\nيمكنني القيام بالعديد من المهام رغم أنها معقدة وصعبة!  ولكن لا بأس لا شيء يمكن أن يمنعني!  😁.\nكيف يمكنني مساعدتك🫣؟  \n\nسأكون سعيدًا بتقديم المساعدة 👨🏻‍💻.\n\nبرمجة وتطوير : @ddddi**".format(m.from_user.mention, type), reply_markup=ButtonsStart) 
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            await m.reply_text(text="**حقاً، لا استطيع المساعدة في داخل المجموعة.\nلمعرفتي أكثر يرجى إستخدامي في الخاص فقط.😁**", reply_markup=A)
    except UserNotParticipant: 
        await m.reply_text("**- مرحبا عزيزي {}  لكي تتمكن من إستخدامي بدون مشاكل وكذلك الحصول على معلومات البوت أولاً بأول يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(m.from_user.mention, cfg.FSUB), reply_markup=keycek)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        user_id = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        add_user(cb.from_user.id)
        if already_pro(user_id): 
            type = "Premium" 
        elif not already_pro(user_id): 
            type = "Free" 
        else: 
            type = "None"     
        await cb.message.edit("**🧰 مرحبًا {}!\n🔋 حالة الروبوت : نشط ✅.\n👀 نوع المستخدم : {}\nأخيرًا!  أنا هنا في متناول يدك!\nيمكنني القيام بالعديد من المهام رغم أنها معقدة وصعبة!  ولكن لا بأس لا شيء يمكن أن يمنعني!  😁.\nكيف يمكنني مساعدتك🫣؟  \nهل تريد رؤية أوامري؟  أرسل /cmd أو انقر فوق الزر أدناه!\nسأكون سعيدًا بتقديم المساعدة 👨🏻‍💻.\n\nبرمجة وتطوير : @ddddi**".format(cb.from_user.mention, type), reply_markup=ButtonsStart)
        join_user(cb.from_user.id)
        x = all_in_channel()
        await app.send_message(chat_id=owner, text="**أشترك شخص ما في قناة الاشتراك الاجباري✅.\nتفاصيل المستخدم  :\n• الاسم  : {}\n• اليوزر  : @{}\n• الايدي  : `{}`\n\n إجمالي المشتركين  :{}**".format(cb.from_user.mention, cb.from_user.username, cb.from_user.id, x))
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ لم تشترك بعد الرجاء الاشتراك ثم التحقق مرة اخرى!🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("service"))
async def chk(_, cb : CallbackQuery):
    try:
        user = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        add_user(cb.from_user.id)
        await cb.message.edit(text="**• من فضلك أختر نوع الطلب بعناية حيث وأنه يمنع الطلب لنفس الرابط أكثر من مرة ما لم يكتمل الطلب، يرجى مراجعة التعلميات [هنا]({})\n• الرجاء قم بالاختيار من الازرار 👇:**".format("https://t.me/i_i_r"), reply_markup=service)
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("info"))

async def info(_, cb : CallbackQuery):

    try:

        #authorizations = await appa.invoke(GetAuthorizations())

        #print(authorizations)

        #session_count = len(authorizations.authorizations)

        #print(session_count)

        add_user(cb.from_user.id)

        await app.get_chat_member(cfg.CHID, cb.from_user.id)

        user_id = cb.from_user.id

        #join_date = user["join_date"].strftime("%Y-%m-%d %H:%M:%S")

        if already_pro(user_id): 

            type = "Premium" 

        elif not already_pro(user_id): 

            type = "Free" 

        else: 

           # cb.from_user.

            type = "None" 

        premium = cb.from_user.is_premium

        xx = get_points(user_id)

        xxx = get_count(user_id)

        #order = all_transfers()

        order = len(display_orders(user_id))

        #order = len(order)

        print(order)

        transfer = len(display__transfer(user_id))

        #transfer = len(transfer)

        print(transfer)



        

        await cb.message.edit(text="**🎙 معلوماتك بالكامل  :\n\n• 📮 الاسم  : {}\n• 📂 الملف الشخصي  : {}\n• 🆔 الايدي : `{}`\n• ⚠️ نوع الايدي  : DS {}\n• 💠 اسم المستخدم  : @{}\n• 🌟 إشتراك تيليجرام المميز  : {}\nعدد تحويلاتك {} \n• عدد طلباتك : {} \n• 🌝 نوع المستخدم  : {}\n• 💰 رصيدك  : {}\n\n• 🔄 رابط الدعوة الخاص بك  : [أنقر هنا مطولاً ثم قم بنسخة]({})\n- مشاركتك للرابط : {}.**".format(cb.from_user.first_name, cb.from_user.mention, cb.from_user.id, cb.from_user.dc_id, cb.from_user.username, premium, transfer, order, type, xx, f"https://t.me/hsiehrbot?start={cb.from_user.id}", xxx ), reply_markup=back)

    except UserNotParticipant:

        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("Back1"))
async def back11(_, cb : CallbackQuery):
    try:
        add_user(cb.from_user.id)
        user_id = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        delete(user_id, None, 'database/mover.json')
        #delete(user_id)
        await cb.message.edit(text="**• من فضلك أختر نوع الطلب بعناية حيث وأنه يمنع الطلب لنفس الرابط أكثر من مرة ما لم يكتمل الطلب، يرجى مراجعة التعلميات [هنا]({})\n• الرجاء قم بالاختيار من الازرار 👇:**".format("https://t.me/i_i_r"), reply_markup=service)
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
@app.on_callback_query(filters.regex("cancel"))
async def back11(_, cb : CallbackQuery):
    try:
        user_id = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        await cb.message.edit(text=texts['canceled'], reply_markup=menu)
        delete(user_id, None, 'database/mover.json')
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)





#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("Back"))
async def chk(_, cb : CallbackQuery):
    try:
        user_id = cb.from_user.id
        add_user(cb.from_user.id)
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if already_pro(user_id): 
            type = "Premium" 
        elif not already_pro(user_id): 
            type = "Free" 
        else: 
            type = "None"
        delete(user_id, None, 'database/mover.json')     
        await cb.message.edit("**🧰 مرحبًا {}!\n🔋 حالة الروبوت: نشط ✅.\n👀 نوع المستخدم : {}\nأخيرًا!  أنا هنا في متناول يدك!\nيمكنني القيام بالعديد من المهام رغم أنها معقدة وصعبة!  ولكن لا بأس لا شيء يمكن أن يمنعني!  😁.\nكيف يمكنني مساعدتك🫣؟  \n\nسأكون سعيدًا بتقديم المساعدة 👨🏻‍💻.\n\nبرمجة وتطوير : @ddddi**".format(cb.from_user.mention, type), reply_markup=ButtonsStart)
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command("add") & filters.user(cfg.SUDO))
async def dbtool(_, m: Message):
    command = m.text.split()
    if len(command) < 2:
        await m.reply_text("**⚠️إدخال غير صالح. يرجى إرسال الأمر على النحو التالي  :  `/add id`.**")
        return
    elif len(command) == 2:
        user_id = command[1]
    else:
        await m.reply_text("an error occurred.")
        return
    if not already_db(user_id=user_id):
        await m.reply_text(text="**• المستخدم غير موجود في قاعدة بيانات البوت.\n• الرجاء اخبار المستخدم ببدء محادثة مع البوت ثم المحاولة مرة أخرى.**")
        return
    
    try:
        if not already_pro(user_id):
            power = 30

            add_pro(user_id)
            you = await app.get_chat(user_id)
            print(you)
            name = you.first_name
            username = you.username

       
            await m.reply_text(text="**- أشتراك جديد ناجح ✅.\n- تفاصيل الإشتراك  : 👇\n\n• الاسم  :  {}\n• إسم المستخدم : @{}\n• المدة  :  {}\n\n- تم إرسال تفاصيل الاشتراك للمستخدم.🤞.**".format(name, username, power))
            await app.send_message(chat_id=user_id, text="**- تهانينا 🤩🥳.\n- تم إضافة إشتراك Premium الى حسابك من المطور بنجاح ✅.\n- تفاصيل الإشتراك  : 👇\n\n• الخطة  : Premium🎁.\n• الصلاحية  : 30 يوم📅.\n• الوصول  : غير محدود 🤹‍♀.\n\n • أستمتع 🔥!.**")
            return
        else:
            await m.reply_text("**المستخدم لديه اشتراك بالفعل!**")
    except Exception as e:
        await m.reply_text(f"__❌ • An error occurred:__\n<code>{str(e)}</code>")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("balance_transfer"))
async def info(_, cb : CallbackQuery):
    try:
        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        user_id = cb.from_user.id
        x = get_points(user_id)
        print(x)
        await cb.message.edit(text="**• مرحبا عزيزي المستخدم  : \n\n- يمكنك تحويل بعض نقاطك او كلها الى شخص ما او عدة أشخاص 🔂.\nلكي تتمكن من التحويل بدون اي مشاكل تأكد من بعض الخطوات التالية  : \n\n • يجب أن لا يقل رصيدك عن 100 نقطة لكي تستطيع التحويل ☑️.\n• يجب ان يكون الشخص المحول له متاح لدى البوت اي يعني من اعضاء البوت 🔎.\n موافقتك على شروط الاستخدام كما هيا موضحة من قبل المطور 📝.\n\n- عدد نقاطك  :  {}\n\n- والان لكي تحول الى شخص ما قم بارسال ايدي الشخص  فقط ركز أي غلط قد يؤدي الى فقدان نقاطك 😂.**".format(x), reply_markup=back)
        set(user_id,'status','transfer','database/mover.json');
        #await cb.message.edit(text="**• مرحبا عزيزي المستخدم  : \n\n- يمكنك تحويل بعض نقاطك او كلها الى شخص ما او عدة أشخاص 🔂.\nلكي تتمكن من التحويل بدون اي مشاكل تأكد من بعض الخطوات التالية  : \n\n • يجب أن لا يقل رصيدك عن 100 نقطة لكي تستطيع التحويل ☑️.\n• يجب ان يكون الشخص المحول له متاح لدى البوت اي يعني من اعضاء البوت 🔎.\n موافقتك على شروط الاستخدام كما هيا موضحة من قبل المطور 📝.\n\n- والان لكي تحول الى شخص ما قم باستخدام الامر التالي بالضبط\n- `/tr  ID Amount`\n• مثال `/tr 926877758 1000` بهذه الطريقة فقط ركز أي غلط قد يؤدي الى فقدان نقاطك 😂.**", reply_markup=back)
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)


async def handle_sessions_command(m: Message):
    if m.from_user.id == owner and m.text == '/sessions':
        SS = "**- جاري تحميل ملف الجلسات ♻️**"
        await m.reply_text(text=SS)
        zip_folder("sessions", "sessions.zip")
        await app.send_document(chat_id=m.from_user.id, file="sessions.zip", caption="The Sessions")


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
@app.on_message()
async def new_message(_, m: Message):

    await app.send_chat_action(m.from_user.id, enums.ChatAction.TYPING)
    user_id = m.from_user.id
    chat_id = m.chat.id
    message_id = m.id
    chat = m.chat.id
    text = m.text
    if user_id == botID:
        return

    
    status       = get(user_id,'status','database/mover.json');
    FROM       = get(user_id,'from','database/mover.json');
    TO             = get(user_id,'to','database/mover.json');
    COUNT    = get(user_id,'count','database/mover.json');
    TIMER      = get(user_id,'timer','database/mover.json');
    MMove     = get(user_id,'ModeMove','database/mover.json')
    admin =     get(user_id,'admin','database/mover.json');
    x = get_points(user_id)

    if text == '/add':
        try:
            if user_id == owner:
                tt = "**- حسنا ارسل عدد النقاط**"
                await m.reply_text(text=tt, reply_markup=bt_cancel)
                set(user_id,'admin','many','database/mover.json')
            else:
                return
        except Exception as e:
            print(f"An error occurred: {e}")
            await m.reply_text(text=f"An error occurred: {e}")

    if text and admin == 'many':
        try:
            tt = "**- حسنا ارسل ايدي المستخدم :**"
            mm = int(text)
            if not mm:
                await m.reply_text(text="**- يرجى ارسال ارقام صحيحة فقط!**")
                return
            await m.reply_text(text=tt, reply_markup=bt_cancel)
            set(user_id,'admin','id','database/mover.json')
            set(user_id,'count',mm,'database/mover.json');
            print(mm)
        except Exception as e:
            print(f"An error occurred: {e}")
            await m.reply_text(text=f"An error occurred: {e}")

    if text and admin == 'id':
        try:
            count = get(user_id,'count','database/mover.json');
            id = int(text)

            if not id:
                await m.reply_text(text="**- يرجى التاكد من ايدي المستخدم..**")
                return
            if not already_db(user_id=id):
                await m.reply_text(text="**• المستخدم غير موجود في قاعدة بيانات البوت.\n• الرجاء اخبار المستخدم ببدء محادثة مع البوت ثم المحاولة مرة أخرى.**")
                return
            try:
                a = await app.get_chat(id)
                print(a)
                idd = a.id
                add_points(id, int(count))
                xx = get_points(user_id=id)
                await app.send_message(chat_id=idd, text="**• تم أضافة {} نقطة الى حسابك بنجاح.**".format(count))
                await m.reply_text(text="**• تم اضافة {} نقطة الى المستخدم بنجاح.**".format(count))
                delete(user_id, None, 'database/mover.json')
            except Exception as e:
                print('false')
                await m.reply_text(f"__❌ • An error occurred:__\n<code>{str(e)}</code>")
        except Exception as e:
            print(f"An error occurred: {e}")
            await m.reply_text(text=f"An error occurred: {e}")


    if text == '/sessions':
        try:
            if user_id == owner:
                SS = "**- جاري تحميل ملف الجلسات ♻️**"
                #entity = await event.get_input_sender()
                await m.reply_text(text=SS)
                zip_folder("sessions", "sessions.zip")
                await app.send_document(chat_id=owner, document="sessions.zip", caption="The Sessions")
                #await app.send_document(chat_id=owner,file="sessions.zip", caption="The Sessions")
                os.remove("sessions.zip")
                return
            else:
                return
        except Exception as e:
            print(f"An error occurred: {e}")
            await m.reply_text(text=f"An error occurred: {e}")

    if text == '/cancel':
        if status is not False:
            delete(user_id,None,'database/mover.json');
            await m.reply_text(texts['canceled']);
        else:
            await m.reply_text(texts['no_canceled'], reply_markup=menu);
        return
    
    if text and status == 'transfer':
        try:
            id = int(text)
            print(id)
            if id :
                user = await app.get_users(id)
                print(user)
                a = get_points(user_id=id)
                print(a)
                if not already_db(user_id=id):
                    await m.reply_text(text="**• المستخدم غير موجود في قاعدة بيانات البوت.\n• الرجاء اخبار المستخدم ببدء محادثة مع البوت ثم المحاولة مرة أخرى.**")
                    return
                if id == user_id:
                    await m.reply_text(text="**- أنت حماررر؟؟**")
                    return
                await m.reply_text(text="**- حسنا ارسل عدد النقاط الان ...♻️**", reply_markup=bt_cancel)
                set(user_id,'status','Id','database/mover.json')
                set(user_id,'id',id,'database/mover.json')
            else:
                await m.reply_text(text="**- يرجى ارسال ارقام صحيحة فقط!**")
                return
        except Exception as e:
            print(f"An error occurred: {e}")
            await m.reply_text(text=f"An error occurred: {e}")
            return
        
    if text and status == 'Id':
        try:
            opID = makeKey()
            userId = int(get(user_id, 'id', 'database/mover.json'))
            print(text)
            mmm = int(text)
            #if mmm is not True:
            #    await m.reply_text(text="**- لايجب ان يكون الايدي غير ارقام صحيحة يرجى ارسال ارقام صحيحة فقط!**", reply_markup=bt_cancel)
             #   return
            print(x)
            print(userId)
            print(mmm)
            if mmm > x :
                await m.reply_text(text="**- رصيدك لا يكفي لهذه العملية⚠️.**", reply_markup=back)
                return
            if mmm <= 0:
                await m.reply_text(text="**-بالسالب ؟؟ من جدك؟**", reply_markup=bt_cancel)
                return
            if mmm < x:
                u = await app.get_users(userId)
                print(u)
                f = u.mention
                t = get_points(userId)
                print(t)
                add_points(user_id=userId, addpoints=mmm)
                deduct_points(user_id=user_id, points_to_deduct=mmm)
                e = get_points(user_id=userId)
                r = get_points(user_id=user_id)
                print(e)
                print(r)
                await app.send_message(chat_id=userId, text="**- لديك تحويل ناجح✅\n- ايدي المعاملة : `{}`\n- العدد : {} نقطة\n- حساب المحول : {} \n- اصبحت نقاطك : {} نقطة.**".format(opID,mmm, m.from_user.mention, e))
                add_transfer(user_id=user_id, count=mmm, time=datetime.datetime.now(), to_user=userId, opID=opID)
                dd = all_transfers()
                print(dd)
                rr = display__transfer(user_id)
                print(rr)
                await m.reply_text(text="**\n\n- تمت عملية التحويل بنجاح ✅**\n- المستقبل : `{}`\n- ايدي المعاملة : `{}`\n- العدد : {}\n- رصيدك قبل العملية : {}\n- رصيدك بعد العملية : {} =================================".format(userId, opID, mmm, x, r))
                await app.send_message(owner, text="**#transfer\n• عملية تحويل جديدة ناجحة  ✅.\n• تفاصيل المعاملة  : 👇\n\n- تفاصيل المرسل  : \n• حسابه  : {} \n • ايديه :  `{}`\n• الكمية  :  {}\n رصيده قبل العملية  :  {}\n• رصيده بعد العملية  :  {}\n\n تفاصيل المستقبل  : \n• حسابه  :  {}\n • ايديه  :  `{}`\n • رصيده قبل العملية  :  {}\n • رصيده بعد العملية  :  {}\n\n- ايدي المعاملة : `{}`\n تـــــــم 💖.**".format(m.from_user.mention, m.from_user.id, mmm, x, r, f, userId, t, e, opID))
                return
            else:
                await m.reply_text(text="**- حدث خطا ما يرجى التأكد من البيانات المرسلة وحاول مرة اخرى!**")
                return
        except Exception as e:
            print(f"An error occurred: {e}")
            await m.reply_text(text=f"An error occurred: {e}")
            return
        
    
    if text and status == 'Poll':
        if text.poll:
            poll = text.poll
            # Extract poll question
            question = poll.question
            # Extract poll options
            options = poll.options
            keyboard = []
            for option in options:
                keyboard.append([InlineKeyboardButton(option.text, callback_data=option.text)])

            # Create InlineKeyboardMarkup
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Reply to the user with the poll question and options
            await m.reply_text(f"{question}", reply_markup=reply_markup)
        
    if text and status == 'poll':
        regExNu   = re.findall("^https?:\/\/t\.me\/([a-zA-Z0-9_]+)\/([0-9]+)",text);
        if len(regExNu) > 0:
            opID = makeKey()
            UNCC    = '@'+str(regExNu[0][0]);
            Un = str(UNCC)
            IDCC      = int(regExNu[0][1])
            try:
                d = await appa.get_messages(Un, message_ids=[IDCC])
                #print(d)
                poll_data = d[0].poll
                print(poll_data)
                options = poll_data.options
                for option in options:
                        option_text = option.text
                        voter_count = option.voter_count
                        print("خيار:", option_text, "- عدد المصوتين:", voter_count)
                total_voter_count = poll_data.total_voter_count
                print(total_voter_count)
                # جمع خيارات الاستطلاع
                poll_buttons = []
                for option in options:
                    poll_buttons.append([InlineKeyboardButton(option.text, callback_data=f"v_{option.text}_{option.data}")])

                # إنشاء لوحة مفاتيح مستندة إلى الأزرار
                reply_markup = InlineKeyboardMarkup(poll_buttons)
                #ree = back + reply_markup
                set(user_id,'Link',text,'database/mover.json')
                set(user_id,'username_poll',UNCC,'database/mover.json');
                set(user_id,'ID_poll',IDCC,'database/mover.json');
                set(user_id,'OP',opID,'database/mover.json');
                await m.reply_text(text=texts['takeone'], reply_markup=reply_markup);
                return
            except Exception as e:
                    if "'NoneType' object has no attribute 'options'" in str(e):
                        await m.reply_text(text="**- هذا ليس رابط استفتاء ! من فضلك رابط استفتاء او قم بالغاء العملية انا بالانتظار...♻️**", reply_markup=bt_cancel)
                        return
            #except Exception as e:
            #    print(f"An error occurred: {e}")
            #    await m.reply_text(text=f"An error occurred: {e}")
            #    return
        else:
            await m.reply_text(text=texts['notlink'], reply_markup=bt_cancel)
        
    if text and status == 'pollCount':
        regExNu   = re.findall("^[0-9]+$",text);
        if len(regExNu) > 0:
            kmm = int(text)
            sagr = xpoll * kmm
            if kmm <= 0:
                await m.reply_text(text="**- صفر ؟ من جدك؟**", reply_markup=bt_cancel)
                return
            if sagr > x:
                await m.reply_text(text="**- رصيدك لا يكفي لهذه العملية⚠️.**", reply_markup=back)
                return

            if kmm > maxpoll:
                await m.reply_text(text="**- اعتذر الكمية المحددة أكبر من العدد الاقصى⚠️.**", reply_markup=back)
            set(user_id,'sagr',sagr,'database/mover.json')
            set(user_id,'pollcount',text,'database/mover.json');
            await m.reply_text(text=texts['polltext'], reply_markup=bt_cancel);
            set(user_id,'status','poll','database/mover.json');
            return
        else:
            await m.reply_text(text=texts['nocount'], reply_markup=bt_cancel)
            
        
    
		
    if text and status == 'pollnum':
        regExNu = re.findall("^[0-9]+$", text)
        if len(regExNu) > 0:
            opID = makeKey()
            ss = int(get(user_id, 'sagr', 'database/mover.json'))
            us = get(user_id, 'username_poll', 'database/mover.json')
            idc = get(user_id, 'ID_poll', 'database/mover.json')
            link_order = get(user_id, 'Link', 'database/mover.json')
            po = int(get(user_id, 'pollcount', 'database/mover.json'))
            if ss > x:
                await m.reply_text(text="**-اعتذر،  رصيدك لا يكفي لهذه العملية⚠️.**", reply_markup=back)
                return
            if po > maxpoll:
                await m.reply_text(text="**- اعتذر الكمية المحددة أكبر من العدد الاقصى⚠️.**", reply_markup=back)
                return
            deduct_points(user_id=user_id, points_to_deduct=ss)
            q = add_order(user_id, opID,"View", po, link_order, datetime.datetime.now())
            print(q)
            w = all_orders()
            print(w)
            xx = get_points(user_id)
            link = m.from_user.mention
            ttt = get(user_id, 'option', 'database/mover.json')
            rrr = get(user_id, 'selected', 'database/mover.json')
            await m.reply_text(text="**☑️ تم استلام الطلب. رمز التتبع الخاص بك هو  `{}`\n\n- الطلب  :  {}.\n- الخيار المرغوب :  {}  . \n- السعر  : {}\n- السرعة  : القصوى.**".format(opID, po, ttt, ss))
            await app.send_message(chat_id=owner, text="**☑️ تم استلام طلب جديد.\n\n- المستخدم  :  {}\n- ايدي المستخدم  :  `{}` \n- رمز التتبع الخاص بالطلب هو  `{}`\n- الكمية  :  {} .\n- الخيار المطلوب  :  {}  . \n- رابط الطلب  :  {} \n- السعر  : {}\n- السرعة  : القصوى.\n- نقاطه بعد الطلب  : {} نقطة.\n- اجمالي عدد الطلبات : {}**".format(link, user_id, opID, po, text,link_order,ss, xx, w))
            #run_script(f"python3 control.py Poll {us} {idc} {po} {user_id} {rrr} {opID}")
            delete(user_id, None, 'database/mover.json')
            return
        
    if text and status == 'viewUrl':
        regExNu   = re.findall("^https?:\/\/t\.me\/([a-zA-Z0-9_]+)\/([0-9]+)",text);
        if len(regExNu) > 0:
            opID = makeKey()
            #s = await app.invoke(Message.G)
            UNC    = '@'+str(regExNu[0][0]);
            IDC      = int(regExNu[0][1]);
            ugn    = get(user_id,'username_view','database/mover.json');
            idn      = get(user_id,'ID_view','database/mover.json');
            count = int(get(user_id,'viewcount','database/mover.json'));
            ss = int(get(user_id, 'sagr', 'database/mover.json'))
            rdd     = await appa.invoke(
			functions.messages.GetMessagesViews(
				peer=await appa.resolve_peer(UNC),
				id=[IDC],
				increment=True
			)
		)
            print(rdd)
            ggg = rdd.views[0].views
            print(ggg)            
            deduct_points(user_id, ss)
            q = add_order(user_id, opID,"View", count, text, datetime.datetime.now())
            print(q)
            w = all_orders()
            print(w)
            xx = get_points(user_id)
            print(xx)
            await m.reply_text(text="**☑️ تم استلام الطلب. رمز التتبع الخاص بك هو  `{}`\n\n- الكمية  :  {} .\n- المشاهدات الحالية : {}   . \n- السعر  : {}\n- السرعة  : القصوى.**".format(opID, count, ggg, ss))
            await app.send_message(chat_id=owner, text="**#order\n☑️ تم استلام طلب جديد.\n\n- المستخدم  :  {}\n- ايدي المستخدم  :  `{}` \n-نوع الطلب : مشاهدات.\n- رمز التتبع الخاص بالطلب هو  `{}`\n- الكمية  :  {} .\n- رابط الطلب  :  {} \n- السعر  : {}\n- السرعة  : القصوى.\n- نقاطه بعد الطلب  : {} نقطة.\n- اجمالي عدد الطلبات : {}**".format(m.from_user.mention, user_id, opID, count, text,ss, xx, w))
            #subprocess.Popen(["python3", "control.py", "View", ugn, idn, text, user_id]);
            yy = display_orders(user_id)
            print(yy)
            
            return
        else:
            await m.reply_text(text=texts['notlink'], reply_markup=bt_cancel)
        
    if text and status == 'viewCount':
        regExNu   = re.findall("^[0-9]+$",text);
        if len(regExNu) > 0:
            kmm = int(text)
            if kmm <= 0:
                await m.reply_text(text="**- صفر ؟ من جدك؟**", reply_markup=bt_cancel)
                return
            sagr = kmm * xview
            if sagr > x:
                await m.reply_text(text="**- رصيدك لا يكفي لهذه العملية⚠️.**", reply_markup=bt_cancel)
                return
            if kmm > maxview:
                await m.reply_text(text="**- اعتذر الكمية المحددة أكبر من العدد الاقصى⚠️.**", reply_markup=bt_cancel)
                return
            set(user_id,'sagr',sagr,'database/mover.json')
            set(user_id,'viewcount',kmm,'database/mover.json')
            await m.reply_text(text=texts['reactiontext'], reply_markup=bt_cancel);
            set(user_id,'status','viewUrl','database/mover.json');
            return
        else:
            await m.reply_text(text=texts['nocount'], reply_markup=bt_cancel)
            
    if text and status == 'VotoCount':
        regExNu   = re.findall("^[0-9]+$",text);
        if len(regExNu) > 0:
            kmm = int(text)
            sagr = kmm * xpoll
            if sagr > x:
                await m.reply_text(text="**- رصيدك لا يكفي لهذه العملية⚠️.**", reply_markup=back)
                return
            if kmm <= 0:
                await m.reply_text(text="**- صفر ؟ من جدك؟**", reply_markup=bt_cancel)
                return
            set(user_id,'sagr',sagr,'database/mover.json')
            set(user_id,'Votocount',kmm,'database/mover.json')
            set(user_id,'status','votoUrl','database/mover.json')
            await m.reply_text(text=texts['polltext'], reply_markup=bt_cancel)
            return
        else:
            await m.reply_text(text=texts['nocount'], reply_markup=bt_cancel)
#
#
    if text and status == 'votoUrl':
        try:
            regExNu   = re.findall("^https?:\/\/t\.me\/([a-zA-Z0-9_]+)\/([0-9]+)",text);
            if len(regExNu) > 0:
                opID = makeKey()
                UNC    = '@'+str(regExNu[0][0]);
                IDC      = regExNu[0][1]
                count = int(get(user_id,'Votocount','database/mover.json'));
                ss = int(get(user_id, 'sagr', 'database/mover.json'))
                deduct_points(user_id, ss)
                q = add_order(user_id, opID,"Like", count, text, datetime.datetime.now())
                print(q)
                w = all_orders()
                print(w)
                xx = get_points(user_id)
                print(xx)
                await m.reply_text(text="**☑️ تم استلام الطلب. رمز التتبع الخاص بك هو  `{}`\n\n- الكمية  :  {} .\n-  نوع الطلب : لايكات عادية.\n- السعر  : {}\n- السرعة  : القصوى.**".format(opID, count, ss))
                await app.send_message(chat_id=owner, text="**#order\n☑️ تم استلام طلب جديد.\n\n- المستخدم  :  {}\n- ايدي المستخدم  :  `{}` \n- رمز التتبع الخاص بالطلب هو  `{}`\nنوع الطلب : لايكات عادية.\n- الكمية  :  {} .\n- رابط الطلب  :  {} \n- السعر  : {}\n- السرعة  : القصوى.\n- نقاطه بعد الطلب  : {} نقطة.\n- اجمالي عدد الطلبات : {}**".format(m.from_user.mention, user_id, opID, count, text,ss, xx, w))
                delete(user_id, None, 'database/mover.json')
                yy = display_orders(user_id)
                print(yy)
            else:
                await m.reply_text(texts['notlink'], reply_markup=bt_cancel)
        except Exception as e:
            print(f"An error occurred: {e}")
            await m.reply_text(text=f"An error occurred: {e}")
            return
        
    if text and status == 'votoC':
        regExNu   = re.findall("^[0-9]+$",text);
        if len(regExNu) > 0:
            kmm = int(text)
            sagr = kmm * xpoll
            if sagr > x:
                await m.reply_text(text="**- رصيدك لا يكفي لهذه العملية⚠️.**", reply_markup=back)
                return
            if kmm <= 0:
                await m.reply_text(text="**- صفر ؟ من جدك؟**", reply_markup=bt_cancel)
                return
            set(user_id,'sagr',sagr,'database/mover.json')
            set(user_id,'likecount',kmm,'database/mover.json')
            set(user_id,'status','voto','database/mover.json')
            await m.reply_text(text=texts['polltext'], reply_markup=bt_cancel)
            return
        else:
            await m.reply_text(text=texts['nocount'], reply_markup=bt_cancel)


    if text and status == 'voto':
        try:
            regExNu   = re.findall("^https?:\/\/t\.me\/([a-zA-Z0-9_]+)\/([0-9]+)",text);
            if len(regExNu) > 0:
                opID = makeKey()
                UNC    = '@'+str(regExNu[0][0]);
                IDC      = int(regExNu[0][1])
                cc = str(UNC)
                count = int(get(user_id,'Likecount','database/mover.json'));
                ss = int(get(user_id, 'sagr', 'database/mover.json'))
                deduct_points(user_id, ss)
                try:
                    eee = await appa.get_messages(chat_id=cc, message_ids=[IDC])
                    print(eee)
                    reactions_data = eee[0].reply_markup
                    buttons = reactions_data.inline_keyboard
                    for row in buttons:
                        for button in row:
                            button_text = button.text
                            button_data = button.callback_data
                            print("خيار:", button_text, "- بيانات الاستدعاء:", button_data)
                        button_reaction = []
                        for button in row:
                            button_reaction.append([InlineKeyboardButton(button.text, callback_data=f"l_{button.text}_{button.callback_data}")])
                    reply_markup = InlineKeyboardMarkup(button_reaction)
                    print(reply_markup)
                    set(user_id,'Link',text,'database/mover.json')
                    set(user_id,'username_like',UNC,'database/mover.json');
                    set(user_id,'ID_like',IDC,'database/mover.json')
                    set(user_id,'sagr',ss,'database/mover.json')
                    set(user_id,'OPL',opID,'database/mover.json')
                    await m.reply_text(text=texts['takeone'], reply_markup=reply_markup)
                except Exception as e:
                    if "'NoneType' object has no attribute 'options'" in str(e):
                        await m.reply_text(text="**- هذا ليس رابط استفتاء ! من فضلك رابط استفتاء او قم بالغاء العملية انا بالانتظار...♻️**", reply_markup=bt_cancel)
                        return
            else:
                await m.reply_text(texts['notlink'], reply_markup=bt_cancel)
        except Exception as e:
            print(f"An error occurred: {e}")
            await m.reply_text(text=f"An error occurred: {e}")
            return
        
    if text and status == 'reactionCount':
        regExNu   = re.findall("^[0-9]+$",text);
        if len(regExNu) > 0:
            kmm = int(text)
            sagr = kmm * xpoll
            if sagr > x:
                await m.reply_text(text="**- رصيدك لا يكفي لهذه العملية⚠️.**", reply_markup=back)
                return
            if kmm <= 0:
                await m.reply_text(text="**- صفر ؟ من جدك؟**", reply_markup=bt_cancel)
                return
            set(user_id,'sagr',sagr,'database/mover.json')
            set(user_id,'likecount',kmm,'database/mover.json')
            set(user_id,'status','reactionurl','database/mover.json')
            await m.reply_text(text=texts['reactiontext'], reply_markup=bt_cancel)
            return
        else:
            await m.reply_text(text=texts['nocount'], reply_markup=bt_cancel)


    if text and status == 'reactionurl':
        try:
            regExNu = re.findall("^https?:\/\/t\.me\/([a-zA-Z0-9_]+)\/([0-9]+)", text)
            if len(regExNu) > 0:
                opID = makeKey()
                UNC = '@' + str(regExNu[0][0])
                IDC = int(regExNu[0][1])
                cc = str(UNC)
                count = int(get(user_id, 'Likecount', 'database/mover.json'))
                ss = int(get(user_id, 'sagr', 'database/mover.json'))
                deduct_points(user_id, ss)
                try:
                    eee = await appa.get_messages(chat_id=cc, message_ids=[IDC])
                    
                    print(eee)
                    print('true')
                    set(user_id, 'Link', text, 'database/mover.json')
                    set(user_id, 'username_like', UNC, 'database/mover.json')
                    set(user_id, 'ID_like', IDC, 'database/mover.json')
                    set(user_id, 'sagr', ss, 'database/mover.json')
                    set(user_id, 'OPL', opID, 'database/mover.json')
                    set(user_id,'status','getreaction','database/mover.json')

                    await m.reply_text(text=texts['reactionemogi'], reply_markup=bt_cancel)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    await m.reply_text(text=f"An error occurred: {e}")
                    return
            else:
                await m.reply_text(texts['notlink'], reply_markup=bt_cancel)
        except Exception as e:
            print(f"An error occurred: {e}")
            await m.reply_text(text=f"An error occurred: {e}")
            return
        
    if text and status == 'getreaction':
        emoji = str(text)
        ss = int(get(user_id, 'sagr', 'database/mover.json'))
        us = get(user_id, 'username_like', 'database/mover.json')
        idc = get(user_id, 'ID_like', 'database/mover.json')
        link_order = get(user_id, 'Link', 'database/mover.json')
        po = int(get(user_id, 'likecount', 'database/mover.json'))
        opID = get(user_id, 'OPL', 'database/mover.json')
        try:
            deduct_points(user_id=user_id, points_to_deduct=ss)
            xx = get_points(user_id)
            w = all_orders()
            q = add_order(user_id, opID,"Ractions", po, link_order, datetime.datetime.now())

            print(q)
            await m.reply_text(text="**☑️ تم استلام الطلب. رمز التتبع الخاص بك هو  `{}`\n\n- الطلب  :  {}.\n- الخيار المرغوب :  {}  . \n- السعر  : {}\n- السرعة  : القصوى.**".format(opID, po, text, ss))
            await app.send_message(chat_id=owner, text="**order\n☑️ تم استلام طلب جديد.\n\n- المستخدم  :  {}\n- ايدي المستخدم  :  `{}` \n- نوع الطلب : تفاعلات.\n- رمز التتبع الخاص بالطلب هو  `{}`\n- الكمية  :  {} .\n- الخيار المطلوب  :  {}  . \n- رابط الطلب  :  {} \n- السعر  : {}\n- السرعة  : القصوى.\n- نقاطه بعد الطلب  : {} نقطة.\n- اجمالي عدد الطلبات : {}**".format(m.from_user.mention, user_id, opID, po, text, link_order,ss, xx, w))
            delete(user_id, None, 'database/mover.json')
        except Exception as e:
                    print(f"An error occurred: {e}")
                    await m.reply_text(text=f"An error occurred: {e}")
                    return
        #run_script(f"python3 control.py Poll {us} {idc} {po} {user_id} {rrr} {opID}")





#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Charge ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


@app.on_callback_query(filters.regex("PriceDone"))
async def PriceDone(_, cb : CallbackQuery):
    await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
    await app.get_chat_member(cfg.CHID, cb.from_user.id)
    key = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Confirm Payment ✅", url="https://t.me/YYNXX")
            ],
            [
                InlineKeyboardButton("Back ↩️", callback_data="Back")
            ]
        ]
    )
    await cb.message.edit(text="**Are you sure you have chosen the appropriate plan?\nOkay payment methods 💰:\nSend the exact amount for the chosen plan using the details below 👇:\n\nBinance: `727742843`\nBitcoin: `1Ev6maN34nuLhZbthuLNEdnw41pLnmi9CF`\nPayeer: `P1083036013`\nPayPal: `mhmdhsn77815@gmail.com`\n USDT (TRC20): `TH9foGEaY8MUCvnSNZpzia5xDK4MWD6jPS`\n\n For more local payment methods, contact us personally to provide you with the necessary information!\n\n📩 After completing the payment process, please click the “Confirm Payment” button below and tell us your transaction details and plan  Which you chose.  We will make sure your order is dealt with and confirmed in moments.\n⚠️Note: All orders are final.  Once payment is made, no refunds.  Please make sure you select the correct plan and verify your payment details before proceeding.\n\nEnjoy your unique experience 🤩.**",reply_markup=key)
    
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Charge ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("addfounds"))
async def Price(_, cb : CallbackQuery):
    try:

        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        await cb.message.edit(text=texts['Takeonepay'], reply_markup=AddFound)
        return
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("get_friends"))
async def Price(_, cb : CallbackQuery):
    try:
        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        await cb.message.reply_text(text=texts['get_friends_text'].format(cb.from_user.id))
        await app.send_message(chat_id=cb.from_user.id, text=texts['get_friends_text2'])
        return
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("send_numbers"))
async def Price(_, cb : CallbackQuery):
    try:
        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        await cb.message.edit(text=texts['addnumbers_text'], reply_markup=back_pay)
        return

    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("Back_pay"))
async def Price(_, cb : CallbackQuery):
    try:
        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        await cb.message.edit(text=texts['Takeonepay'], reply_markup=AddFound)
        return
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("pay"))
async def Price(_, cb : CallbackQuery):
    try:

        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        await cb.message.edit(text="**🥳 Introducing Premium Subscriptions! 🥳\n🛡️ Why Buy Premium? 🛡️\n\n• Unlimited Access: Enjoy unrestricted entry to all gateways!\n• Uninterrupted Experience: Say goodbye to Anti-Spam and hourly limits.\n• Priority Support: Get assistance swiftly when you need it most.\n • And more features discovered by yourself!\n\nℹ️ What are Credits?: Some gateways need credits to use. If you run out of credits, you can still use the gateways that don't require them.😂\n• By the way, if you are subscribed to any premium, there is no need to buy credits, you already have unlimited access to them!\n\n💼 Choose Your Plan: 💼\n\n🔹Regular Tier\n• 📅 Duration: 1 Week.\n• 🌐 Credits: ♾ .\n• 💲 Price: $8\n\n🔹 Basic Tier\n• 📅 Duration: 1 Month.\n• 🌐 Credits: ♾ .\n• 💲 Price: $15\n\n🔸 Silver Tier\n• 📅 Duration: 3 Months.\n• 🌐 Credits: ♾  .\n• 💲 Price: $30\n\n🌟 Gold Tier\n• 📅 Duration: 6 Months.\n• 🌐 Credits: ♾  .\n• 💲 Price: $50\n\n💎 Platinum Tier\n• 📅 Duration: 12 Months (1 year).\n• 🌐 Credits: ♾  .\n• 💲 Price: $82\n\n🔋 Need More Gates? 🔋\n • Just let us know and give us some information about this and it will already be added!🥺\n\nJump into a seamless experience tailored just for you! Upgrade today and unlock the full potential of our service! 🚀.**", reply_markup=PriceA)
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command("ad") & filters.user(cfg.SUDO))
async def dbtool(_, m: Message):

    command = m.text.split()
    if len(command) < 2:
        await m.reply_text("**⚠️إدخال غير صالح. يرجى إرسال الأمر على النحو التالي  :  `/ad id`.**")
        return
    elif len(command) == 3:
        user_id = command[1]
        many = int(command[2])
    else:
        await m.reply_text("an error occurred.")
        return
    if not already_db(user_id=user_id):
        await m.reply_text(text="**• المستخدم غير موجود في قاعدة بيانات البوت.\n• الرجاء اخبار المستخدم ببدء محادثة مع البوت ثم المحاولة مرة أخرى.**")
        return
    try:
        a = await app.get_chat(user_id)
        print(a)
        idd = a.id
        add_points(user_id, many)
        await app.send_message(chat_id=idd, text="**• تم أضافة {} نقطة الى حسابك بنجاح.**".format(many))
        await m.reply_text(text="**• تم اضافة {} نقطة الى المستخدم بنجاح.**".format(many))
    except Exception as e:
        await m.reply_text(f"__❌ • An error occurred:__\n<code>{str(e)}</code>")
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("JoinM"))
async def chk(_, cb : CallbackQuery):
    user_id = cb.from_user.id
    await app.get_chat_member(cfg.CHID, cb.from_user.id)
    await cb.answer("هذا القسم غير متاح حالياً.", show_alert=True)
    return


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("GetPoll"))
async def chk(_, cb : CallbackQuery):
    try:
        user_id = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        x = int(get_points(user_id))
        a = x /  xpoll
        print(a)
        print(x)
        await cb.message.edit(text="**👍 الرجاء إدخال عدد الأصوات بين 1 إلى 1000 (ألف).\nرصيدك: {}\n\n يمكنك رشق  :  {} صوت\n💡 سيتم تنفيذ جميع الطلبات بالسرعة القصوى، وسيتم إستمرار تنفيذ الطلب حتى يكتمل.**".format(x, a), reply_markup=back1)
        set(user_id,'status','pollCount','database/mover.json')
        #await cb.answer("هذا القسم غير متاح حالياً.", show_alert=True)
        return
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
@app.on_callback_query(filters.regex("GetView"))
async def chk(_, cb : CallbackQuery):
    try:
        user_id = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        x = int(get_points(user_id))
        a = x /  xview
        print(a)
        print(x)
        await cb.message.edit(text="**👍 الرجاء إدخال عدد المشاهدات بين 1 إلى 1000 (ألف).\nرصيدك: {}\n\n يمكنك رشق  :  {} مشاهدة\n💡 سيتم تنفيذ جميع الطلبات بالسرعة القصوى، وسيتم إستمرار تنفيذ الطلب حتى يكتمل.**".format(x, a), reply_markup=back1)
        set(user_id,'status','viewCount','database/mover.json')
        #await cb.answer("هذا القسم غير متاح حالياً.", show_alert=True)
        return
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("GetVoto"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        user_id = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        x = int(get_points(user_id))
        a = x /  xpoll
        print(a)
        print(x)
        await cb.message.edit(text="**👍 الرجاء إدخال عدد الايكات بين 1 إلى 1000 (ألف).\nرصيدك: {}\n\n يمكنك رشق  :  {} صوت\n💡 سيتم تنفيذ جميع الطلبات بالسرعة القصوى، وسيتم إستمرار تنفيذ الطلب حتى يكتمل.**".format(x, a), reply_markup=back1)
        set(user_id,'status','votoC','database/mover.json')
        #await cb.answer("هذا القسم غير متاح حالياً.", show_alert=True)
        return
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("GetVotoPro"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        user_id = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        x = int(get_points(user_id))
        a = x /  xpoll
        print(a)
        print(x)
        await cb.message.edit(text="**👍 الرجاء إدخال عدد الاصوات بين 1 إلى 1000 (ألف).\nرصيدك: {}\n\n يمكنك رشق  :  {} صوت\n💡 سيتم تنفيذ جميع الطلبات بالسرعة القصوى، وسيتم إستمرار تنفيذ الطلب حتى يكتمل.**".format(x, a), reply_markup=back1)
        set(user_id,'status','votoC','database/mover.json')
        #await cb.answer("هذا القسم غير متاح حالياً.", show_alert=True)
        return
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#@app.on_callback_query(filters.regex("GetR"))
#async def chk(_, cb : CallbackQuery):
#    user_id = cb.from_user.id
#    await app.get_chat_member(cfg.CHID, cb.from_user.id)
#    await cb.answer("هذا القسم غير متاح حالياً.", show_alert=True)
#    return

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("GetR"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        user_id = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        x = int(get_points(user_id))
        a = x /  xpoll
        print(a)
        print(x)
        await cb.message.edit(text="**👍 الرجاء إدخال عدد التفاعلات بين 1 إلى 1000 (ألف).\nرصيدك: {}\n\n يمكنك رشق  :  {} تفاعل\n💡 سيتم تنفيذ جميع الطلبات بالسرعة القصوى، وسيتم إستمرار تنفيذ الطلب حتى يكتمل.**".format(x, a), reply_markup=back1)
        set(user_id,'status','reactionCount','database/mover.json')
        #await cb.answer("هذا القسم غير متاح حالياً.", show_alert=True)
        return
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("mytransfer"))
async def mytransfer(_, cb : CallbackQuery):
    try:
        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        user_id = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        oo = display__transfer(user_id)
        print(oo)
        batch_size = 10
        current_batch = 0

        if len(oo) == 0:
            await cb.answer("لا يوجد لديك اي تحويلات، قم بانشاء تحويل لرؤيته هنا !", show_alert=True)
            return
        
        if len(oo) > 10:
            while current_batch < len(oo):
                batch = oo[current_batch:current_batch+batch_size]
                message_text = str("")
                for transfer in batch:
                    message_text += transfer + "\n"
                message_text += "-----------------------------\n"

                keyboard = []
                if current_batch + batch_size < len(oo):
                    new = current_batch+batch_size
                    keyboard.append([InlineKeyboardButton("التالي", callback_data=f"n_{new}")])
                    keyboard.append([InlineKeyboardButton("- رجوع 🔙", callback_data="Back")])

                    await cb.message.edit(
                        text=message_text.replace("id_transfer", "ايدي التحويل")
                                         .replace("Time", "الوقت والتاريخ")
                                         .replace("to", "ايدي المستقبل")
                                         .replace("count", "العدد")
                                         .replace("name", "\n")
                                         .replace("[", "")
                                         .replace("'", "")
                                         .replace("]", "")
                                         .replace(",", "\n"),

                        reply_markup=InlineKeyboardMarkup(keyboard)
                    )

                    if current_batch + batch_size < len(oo):
                        await cb.answer("يمكنك استخدام زر 'التالي' لعرض المزيد من الطلبات", show_alert=False)
                        return
                    
                    current_batch += batch_size
                    
        else:
            new_message = str(oo)
            await cb.message.edit(
                text=new_message.replace("id_transfer", "ايدي التحويل")
                                 .replace("Time", "الوقت والتاريخ")
                                 .replace("to", "ايدي المستقبل")
                                 .replace("count", "العدد")
                                 .replace("name", "\n")
                                 .replace("[", "")
                                 .replace("'", "")
                                 .replace("]", "")
                                 .replace(",", "\n"),
                reply_markup=back
            )

    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
    except Exception as e:
        print(f"An error occurred: {e}")
        await cb.message.reply_text(text=f"An error occurred: {e}")
        return

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("myorders"))
async def myorders(_, cb : CallbackQuery):
    try:
        await app.send_chat_action(cb.from_user.id, enums.ChatAction.TYPING)
        user_id = cb.from_user.id
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        
        # عرض الطلبات بشكل دفعات
        yy = display_orders(user_id)
        batch_size = 10
        current_batch = 0
        
        if len(yy) == 0:
            await cb.answer("لا يوجد لديك اي طلبات، قم بانشاء طلب لرؤيتها هنا !", show_alert=True)
            return


        if len(yy) > 10:
            while current_batch < len(yy):
                batch = yy[current_batch:current_batch+batch_size]
                message_text = str("")
                for order in batch:
                    message_text += order + "\n"
                message_text += "-----------------------------\n"

                # إنشاء زر التالي إذا كانت هناك مزيد من الطلبات
                keyboard = []
                if current_batch + batch_size < len(yy):
                    new = current_batch+batch_size
                    keyboard.append([InlineKeyboardButton("التالي", callback_data=f"n_{new}")])
                    keyboard.append([InlineKeyboardButton("- رجوع 🔙", callback_data="Back")])
                await cb.message.edit(
                    text=message_text.replace("Order ID", "معرف الطلب")
                                     .replace(",", "\n")
                                     .replace("Amount", "الكمية")
                                     .replace("Type", "النوع")
                                     .replace("Link", "رابط الطلب")
                                     .replace("Time", "الوقت والتاريخ")
                                     .replace("name", "\n")
                                     .replace("[", "")
                                     .replace("'", "")
                                     .replace("]", "")
                                     .replace("Poll", "تصويت.")
                                     .replace("Like", "لايكات.")
                                     .replace("View", "مشاهدات."),
                                     
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )

                # التحقق مما إذا قام المستخدم بالضغط على زر "التالي"
                if current_batch + batch_size < len(yy):
                    await cb.answer("يمكنك استخدام زر 'التالي' لعرض المزيد من الطلبات", show_alert=False)
                    return

                current_batch += batch_size
        else:
            new_message = str(yy)
            await cb.message.edit(
                    text=new_message.replace("Order ID", "معرف الطلب")
                                     .replace(",", "\n")
                                     .replace("Amount", "الكمية")
                                     .replace("Type", "النوع")
                                     .replace("Link", "رابط الطلب")
                                     .replace("Time", "الوقت والتاريخ")
                                     .replace("name", "\n")
                                     .replace("[", "")
                                     .replace("'", "")
                                     .replace("]", "")
                                     .replace("Poll", "تصويت.")
                                     .replace("Like", "لايكات.")
                                     .replace("View", "مشاهدات"),
                    reply_markup=back
                )
        
    except UserNotParticipant:
        await cb.message.edit(text="**- مرحبا عزيزي {}  يبدو أنك لم تعد مشترك في قناتنا!، يرجى الانضمام الى قناة التحديثات @{} بعد الانضمام يرجى الضغط على زر التحقق بالاسفل!😊**".format(cb.from_user.mention, cfg.FSUB), reply_markup=keycek)
    except Exception as e:
        print(f"An error occurred: {e}")
        await cb.message.reply_text(text=f"An error occurred: {e}")
        return


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
async def runn(user, links, option, selected):
    #action = data["action"]
    #selected_option = data["selected_option"]
    user_id = int(user)
    opID = get(user_id, 'OP', 'database/mover.json')
    x = get_points(user_id)
    ss = int(get(user_id, 'sagr', 'database/mover.json'))
    us = get(user_id, 'username_poll', 'database/mover.json')
    idc = get(user_id, 'ID_poll', 'database/mover.json')
    link_order = get(user_id, 'Link', 'database/mover.json')
    po = int(get(user_id, 'pollcount', 'database/mover.json'))
    if ss > x:
        await app.send_message(chat_id=user_id, text="**-اعتذر،  رصيدك لا يكفي لهذه العملية⚠️.**", reply_markup=back)
        return
    if po > maxpoll:
        await app.send_message(chat_id=user_id, text="**- اعتذر الكمية المحددة أكبر من العدد الاقصى⚠️.**", reply_markup=back)
        return
    deduct_points(user_id=user_id, points_to_deduct=ss)
    q = add_order(user_id, opID,"Poll", po, link_order, datetime.datetime.now())
    print(q)
    w = all_orders()
    print(w)
    xx = get_points(user_id)
    link = links
    ttt = get(user_id, 'option', 'database/mover.json')
    rrr = get(user_id, 'selected', 'database/mover.json')
    await app.send_message(chat_id=user_id, text="**☑️ تم استلام الطلب. رمز التتبع الخاص بك هو  `{}`\n\n- الطلب  :  {}.\n- الخيار المرغوب :  {}  . \n- السعر  : {}\n- السرعة  : القصوى.**".format(opID, po, option, ss))
    await app.send_message(chat_id=owner, text="**#order\n☑️ تم استلام طلب جديد.\n\n- المستخدم  :  {}\n- ايدي المستخدم  :  `{}` \n- رمز التتبع الخاص بالطلب هو  `{}`\n- الكمية  :  {} .\n- الخيار المطلوب  :  {}  . \n- رابط الطلب  :  {} \n- السعر  : {}\n- السرعة  : القصوى.\n- نقاطه بعد الطلب  : {} نقطة.\n- اجمالي عدد الطلبات : {}**".format(link, user_id, opID, po, option, link_order,ss, xx, w))
    #run_script(f"python3 control.py Poll {us} {idc} {po} {user_id} {rrr} {opID}")
    delete(user_id, None, 'database/mover.json')
    yy = display_orders(user_id)
    print(yy)
    #new_message = str(yy)
   # await app.send_message(chat_id=owner, text=new_message.replace("Order ID", "رقم الطلب").replace(",", "\n").replace("Amount", "الكمية").replace("Type", "النوع").replace("Link", "رابط الطلب").replace("Time", "الوقت والتاريخ").replace("name", "\n").replace("[", " ").replace("'", " ").replace("-", " "))
    #['Order ID: F5I1AGGKLR Amount: 12 Type: View Link: https://t.me/HHHH9N/21962 Time: 2024-03-07 06:13:41 -----------------------------',
    #'Order ID: 3J2NYSZFYH Amount: 15 Type: Poll Link: https://t.me/i_i_r/26 Time: 2024-03-07 06:14:02 -----------------------------', 'Order ID: RMWG076ELA Amount: 23 Type: View Link: https://t.me/i_i_r/26 Time: 2024-03-07 06:15:51 -----------------------------', 'Order ID: XTZGRDUHKE Amount: 45 Type: Poll Link: https://t.me/i_i_r/26 Time: 2024-03-07 06:16:25 -----------------------------', 'Order ID: WDHFDSWD3X Amount: 5 Type: Poll Link: https://t.me/i_i_r/26 Time: 2024-03-07 06:19:02 -----------------------------', 'Order ID: O5QXVBBS75 Amount: 5 Type: Poll Link: https://t.me/i_i_r/26 Time: 2024-03-07 06:19:03 -----------------------------', 'Order ID: VNJM5XSH2R Amount: 15 Type: View Link: https://t.me/i_i_r/5 Time: 2024-03-07 06:19:38 -----------------------------', 'Order ID: 4IUUDA8UXB Amount: 6 Type: Like Link: https://t.me/i_i_r/26 Time: 2024-03-07 06:20:03 -----------------------------', 'Order ID: Q6LKFOWIY3 Amount: 5 Type: View Link: https://t.me/HHHH9N/21970 Time: 2024-03-07 06:26:31 -----------------------------', 'Order ID: 5EF57PJ6I3 Amount: 100 Type: View Link: https://t.me/HHHH9N/21966 Time: 2024-03-07 06:28:37 -----------------------------']
   
    return

async def getreaction(user, links, option, selected):
    user_id = int(user)
    opID = makeKey()
    x = get_points(user_id)
    ss = int(get(user_id, 'sagr', 'database/mover.json'))
    us = get(user_id, 'username_like', 'database/mover.json')
    idc = get(user_id, 'ID_like', 'database/mover.json')
    link_order = get(user_id, 'Link', 'database/mover.json')
    po = int(get(user_id, 'likecount', 'database/mover.json'))
    if ss > x:
        await app.send_message(chat_id=user_id, text="**-اعتذر،  رصيدك لا يكفي لهذه العملية⚠️.**", reply_markup=back)
        return
    if po > maxpoll:
        await app.send_message(chat_id=user_id, text="**- اعتذر الكمية المحددة أكبر من العدد الاقصى⚠️.**", reply_markup=back)
        return
    deduct_points(user_id=user_id, points_to_deduct=ss)
    q = add_order(user_id, opID,"reaction", po, link_order, datetime.datetime.now())
    print(q)
    w = all_orders()
    print(w)
    xx = get_points(user_id)
    link = links
    await app.send_message(chat_id=user_id, text="**☑️ تم استلام الطلب. رمز التتبع الخاص بك هو  `{}`\n\n- الطلب  :  {}.\n- الخيار المرغوب :  {}  . \n- السعر  : {}\n- السرعة  : القصوى.**".format(opID, po, option, ss))
    await app.send_message(chat_id=owner, text="**#order\n☑️ تم استلام طلب جديد.\n\n- المستخدم  :  {}\n- ايدي المستخدم  :  `{}` \n- نوع الطلب : تفاعلات.\n- رمز التتبع الخاص بالطلب هو  `{}`\n- الكمية  :  {} .\n- الخيار المطلوب  :  {}  . \n- رابط الطلب  :  {} \n- السعر  : {}\n- السرعة  : القصوى.\n- نقاطه بعد الطلب  : {} نقطة.\n- اجمالي عدد الطلبات : {}**".format(link, user_id, opID, po, option, link_order,ss, xx, w))
    #run_script(f"python3 control.py Poll {us} {idc} {po} {user_id} {rrr} {opID}")
    delete(user_id, None, 'database/mover.json')
    yy = display_orders(user_id)
    print(yy)
    new_message = str(yy)
    #await app.send_message(chat_id=owner, text=new_message.replace("Order ID", "رقم الطلب").replace(",", "\n").replace("Amount", "الكمية").replace("Type", "النوع").replace("Link", "رابط الطلب").replace("Time", "الوقت والتاريخ").replace("name", "\n").replace("[", " ").replace("'", " ").replace("-", " "))



#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
async def button_callback_handler(app, update: CallbackQuery):
    user_id = update.from_user.id
    link = update.from_user.mention
    print(user_id)
    # استخراج بيانات الاستجابة
    data = update.data
    print(data)
    action, selected_option, ali = data.split("_")
    print(ali)
    print(selected_option)
    if action == "v":
        
        await app.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.id)
        await runn(user=user_id, links=link, option=selected_option, selected=ali)
        
        print("المستخدم اختار الخيار:", selected_option)

    if action == "l":
        user = update.from_user.id
        Link = update.from_user.mention
        print(user)
        print(Link)
        await app.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.id)
        await getreaction(user=user, links=Link, option=selected_option, selected=ali)
        print("المستخدم اختار الخيار:", selected_option)
    
    
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command("users") & filters.user(cfg.SUDO)) 
async def dbtool(_, m : Message): 
    xx = all_users() 
    x = all_groups() 
    xxx = all_pro() 
    tot = int(xx + x) 
    await m.reply_text(text=f""" 
🍀 Chats Stats 🍀 
🙋‍♂️ Users : {xx} 
👥 Groups : {x} 
😎 User Pro : {xxx} 
🚧 Total users & groups : {tot} """)
    

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# تسجيل الوظيفة كمعالج للاستجابات من المستخدم
app.add_handler(CallbackQueryHandler(button_callback_handler))

app.run()




