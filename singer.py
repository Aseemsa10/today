from telethon.sync import TelegramClient
from telethon import events, Button
import json
import configparser
import subprocess
import telethon
import os,sys
import re
from data import *
from database import *
from configs import *


config = configparser.ConfigParser() 
config.read("info.ini")

api_id       = config['owner']['id'];
api_hash = config['owner']['hash'];
client        = telethon.TelegramClient('signerAccounts', api_id, api_hash);

sessions	      = os.listdir('sessions');
random.shuffle(sessions);
THE_SESSIONS = os.listdir('sessions');
cSessions	   = len(THE_SESSIONS);

token = config['API_KEYs']['signer'];
botID  =  int(token.split(':')[0]);

client.start(bot_token=token);
client.connect();

textStart                  = "**أهلا بك في بوت تسليم الحسابات 😊.\n• سوف تستلم نقاطك على الفور بعد  التحقق من الرقم، 😏.\n\n#تنبيه ⚠️:  لا ننصحك أبداً بتسجيل حسابك الشخصي ، كل ما نريده منك فقط حسابات وهمية\nبعد التحقق من الحساب تستطيع تحويل النقاط من هنا الى بوت الخدمات 😍❤️.\n لبدء عملية الاضافة أرسل /add .\n ارسل /balance لمعرفة حسابك.**";
sendYourNumber = """قم بإرسال رقم الهاتف مع الصفر الدولي بشكل متصل كالتالي\n+96777777777""";
numberIsFalse       = "عذرا الرقم ليس صحيحا";
numberIsBanned   = "عذرا الرقم محظور";
thereisnumbernow = "تجري الآن عملية تسجيل رقم ، قم بإلغائها عبر /del ثم عد لتسجيل الدخول بحساب جديد";
donedeletion             = "تم الحذف ، يمكنك الآن تسجيل الدخول بحساب جديد عبر /add";
notfoundfordelete     = "البيانات بالتأكيد فارغة!";
thereisnumberfound = "هذا الرقم مضاف مسبقا ، يرجى إرسال رقم جديد!";
pleaseimportplus      = "يرجى كتابة الرقم بالكامل إضافة إلى تضمين علامة + كالتالي \n +96777777777";
pleasewait                  = "يرجى الإنتظار...";
justnumbers               = "يرجى ارسال ارقام فقط!";
checking_code           = "يتم التحقق من الكود.... يرجى الإنتظار..";
checking_auth            = "يتم التحقق من كود التحقق بخطوتين..... يرجى الإنتظار..";
AA = "يتم التحقق يرجى الانتظار....♻️";

@client.on(events.NewMessage())

async def main(event):
	chattt = await event.get_chat();
	if chattt.__class__.__name__ != 'User':
		return
	try:
		b = event.message.peer_id.channel_id
		b = f"-100{b}"
	except:
		pass

	text                 = event.raw_text;
	message_id  = event.message.id;
	from_id          = str(event.sender_id);
	chat_id           = event.chat_id;
	
	if from_id == botID:
		return
	if text == '/start':
		await event.reply(textStart);
	elif text == '/add':
		if get(from_id,"status") is not False:
			await event.reply(thereisnumbernow);
		else:
			set(from_id,"status","add");
			await event.reply(sendYourNumber);
	elif text == '/balance':
		x = get_points_num(from_id)
		xx = get_numbers(from_id)
		await event.reply("**- عدد نقاطك : {}\n- عدد حساباتك : {} .**".format(x, xx))
		return
		
	elif text == '/del':
		if get(from_id,"status") == '' or get(from_id,"status") is False:
			await event.reply(notfoundfordelete);
		else :
			delete(from_id);
			await event.reply(donedeletion);
	elif text and get(from_id,"status") == 'add':
		regExNu   = re.findall("^\+[0-9]{9,16}$",text);
		if regExNu:
			NUMBER   = regExNu[0];
			await event.reply(pleasewait);
			subprocess.Popen(["python3", "auto.py", "add", NUMBER, str(from_id)])
		else:
			await event.reply(pleaseimportplus);
			return
	elif text and get(from_id,"status") == 'verfiry':
		regExCode  = re.findall("^[0-9]{5}$",text);
		if regExCode:
			CODE       = regExCode[0];
			await event.reply(checking_code);
			set(from_id,"code",f"{CODE}");
		else :
			await event.reply(justnumbers);
			return
			
	elif text and get(from_id,"status") == 'auth':
		regExAuth  = re.findall("^.{1,35}$",text);
		if regExAuth:
			AUTH       = regExAuth[0];
			await event.reply(checking_code);
			set(from_id,"code",f"{AUTH}");
		else :
			return
	elif text and get(from_id,"status") == 'authorize':
		await event.reply(AA)
		set(from_id,"status", "check")
		return

	
	

client.run_until_disconnected();

