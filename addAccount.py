from pyrogram import Client
from pyrogram.raw import functions, types
import sys, time
import asyncio
import json
from pyrogram.raw.functions.account import GetAuthorizations, ResetAuthorization
from  pyrogram.raw.types.account import Authorizations
import configparser
from pyrogram.errors import FloodWait, UserPrivacyRestricted, UserRestricted, PeerFlood, UserNotMutualContact, UserChannelsTooMuch
from database import *
import datetime


opreat      = sys.argv[1];
opreats    = ['join','left','check','send','getusers','adduser','getUsers','joining','CX','MovePro','View','getMessage','addLikes','joinPrivate','kakaroot','getSessionsAuth', 'logoutis'];


if opreat not in opreats:
	exit();

ses    = sys.argv[2].split('.')[0];



config = configparser.ConfigParser()
config.read("jello.ini")

api_id       = config['owner']['id'];
api_hash = config['owner']['hash'];

async def Controll():
	if opreat != 'joinPrivate' :
		try:
			app	  = Client(f"sessions/{ses}",api_id=api_id, api_hash=api_hash);
			connect  = await app.connect();
			if opreat == 'check':
				try:
					await app.get_me();
					print('true');
				except:
					print('false');

			await app.get_me();
		except Exception as Errors:
			RESPONSE      = str(Errors).replace('Telegram says: ', '').split(' - ')[0];

			if RESPONSE in ['[401 AUTH_KEY_UNREGISTERED]', '[401 USER_DEACTIVATED]', '[401 USER_DEACTIVATED_BAN]', '[401 SESSION_REVOKED]']:
				try:
					print('deleted');
					os.remove(f"sessions/{ses}.session");
				except:
					pass
	else :
		try:
			
			app	  = Client(f"private/{ses}",api_id=api_id, api_hash=api_hash);
			connect  = await app.connect();
		except Exception as Errors:
			RESPONSE      = str(Errors).replace('Telegram says: ', '').split(' - ')[0];

			if RESPONSE in ['[401 AUTH_KEY_UNREGISTERED]', '[401 USER_DEACTIVATED]', '[401 USER_DEACTIVATED_BAN]', '[401 SESSION_REVOKED]']:
				try:
					print('deleted');
					os.remove(f"private/{ses}.session");
				except:
					pass

		if opreat == 'check':
			print(RESPONSE);
		print('false',Errors);
		connect   = False;
		#print(ses);
		return
	if not connect:
		print('NO_CONNECTED');
		return

	try:
		await app.invoke(functions.account.UpdateStatus(
			offline=False
		));
	except:
		pass
	
	if opreat == 'kakaroot':
		chat_id      = int(sys.argv[3]);
		timeINT     = int(sys.argv[4]);
		
		textC          = '';
		try :
			
			aKaka   = app.get_chat_history(chat_id=chat_id,limit=1);
			print('True');
			
			jCheck    = False;
			async for kakai in aKaka:
				timeA    = datetime.now();
				timeB    = datetime.timestamp(timeA);
				timeC    = time.mktime(time.strptime(str(kakai.date),"%Y-%m-%d %H:%M:%S"));
				timeD    = int(timeB) - int(timeC);
				if timeINT > int(timeC):
					continue;
				if timeD >= 86400:
					continue;
				else :
					jCheck  = True;
				
				textC     = kakai.text
				if textC == '' :
					textC      = 'DATA_IS_OLD';
				
				kakaroot  = getkakaroot(textC);
				if kakaroot != 'None':
					
					print(f"Kaka Jello Root :{kakaroot}.Now");
				else :
					print('NO_Root');
			if jCheck is False:
				print('DATA_IS_OLD');
		except Exception as Errors:
			print('False');
			print(Errors);
	
	if opreat == 'getSessionsAuth' :
		Kaid , Arrad = "", []
		authorizations = (await app.send(GetAuthorizations()))["authorizations"]
		for auth in authorizations:
			if auth.current:
				continue
			logined_time = datetime.utcfromtimestamp(auth.date_created).strftime(
				"%d-%m-%Y %H-%M-%S KSA"
			)
			Arrad.append(
				[
					{'text':f"{escape(auth.device_model)} , {logined_time}",'callback_data':f"logoutis#{ses}#{auth.hash}"}
				]
			)
		Kaid = json.dumps({"inline_keyboard":Arrad})
		print(f"#butt#{Kaid}#butt#")
			# auth.hash auth.ip
			# escape(auth.device_model)
	if opreat == 'logoutis' :
		hash = sys.argv[3]
		try :
			await app.send(ResetAuthorization(hash=hash))
			print("Fook ! hg")
		except :
			print("Look ! hg")
	
	if opreat == 'joining':
		username     = sys.argv[3];
		try:
			join_to_username    = await app.join_chat(username);
			joining_id                    = join_to_username.id;
			print(['true',joining_id]);
		except Exception as prim:
			print(['false',prim]);
		pass

asyncio.get_event_loop().run_until_complete(Controll());