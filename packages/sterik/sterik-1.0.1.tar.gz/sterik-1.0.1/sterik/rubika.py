from sterik.Configs import maker , encryption , tools , welcome
import base64
import datetime
import io
import math
from json import loads , dumps
from random import choice,randint
from pathlib import Path
from PIL import Image
from requests import get, post

__version__ = "1.0.0"
__license__ = "MIT license"
__copyright__ = "Copyright (C) 2022 mohamad maleki>>>sterik\nrubika:@MaMad_aDz"

class Bot:
	def __init__(self,auth = None):
		if not auth == None:
			self.auth = auth
			self.maker = maker(auth)
			welcome.welcome_tx()
		else:print("Please enter the AUTH !")

	def tmpGeneration():
		tmp_session = ""
		choices = [*"abcdefghijklmnopqrstuvwxyz0123456789"]
		for i in range(32): tmp_session += choice(choices)
		return tmp_session

	def sendCode(self, phone_number):
		tmp = Bot.tmpGeneration()
		enc = encryption(tmp)
		return self.maker.method('sendCode',{"phone_number":f"98{phone_number[1:]}","send_type":"SMS"})

	def signIn(self, phone_number,phone_code_hash,phone_code):
		tmp = Bot.tmpGeneration()
		enc = encryption(tmp)
		return self.maker.method('sendCode',{"phone_number":f"98{phone_number[1:]}","phone_code_hash":phone_code_hash,"phone_code":phone_code})
		
	defaultDevice = {"app_version":"MA_2.9.8","device_hash":"CEF34215E3E610825DC1C4BF9864D47A","device_model":"rubika-library","is_multi_account": False,"lang_code":"fa","system_version":"SDK 22","token":"cgpzI3mbTPKddhgKQV9lwS:APA91bE3ZrCdFosZAm5qUaG29xJhCjzw37wE4CdzAwZTawnHZM_hwZYbPPmBedllAHlm60v5N2ms-0OIqJuFd5dWRAqac2Ov-gBzyjMx5FEBJ_7nbBv5z6hl4_XiJ3wRMcVtxCVM9TA-","token_type":"Firebase"}
	def registerDevice(self, auth, device=defaultDevice):
		enc = encryption(auth)
		return self.maker.method('registerDevice',{"auth":auth,"data_enc":enc.encrypt(dumps(device))},custom_client=4,method_type=4)

	def logout(self):
		return self.maker.method('logout',{})

	def getChats(self, start_id=None):
		return self.maker.method('getChats',{"start_id":start_id})

	def sendMessage(self, chat_id, text, message_id=None, metadata=[]):
		inData = {"object_guid":chat_id,"rnd":f"{randint(100000,999999999)}","text":text,"reply_to_message_id":message_id}
		if metadata != [] : inData["metadata"] = {"meta_data_parts":metadata}
		if "**" in text or "``" in text or "__" in text:
			metadatas = tools().textAnalysis(text)
			inData['metadata'] = {'meta_data_parts': metadatas[0]}
			inData['text'] = metadatas[1]
		return self.maker.method('sendMessage',inData)

	def editMessage(self, message_id, chat_id, newText, metadata=[]):
		inData = {"message_id": message_id,"object_guid": chat_id,"text": newText}
		if metadata != [] : inData["metadata"] = {"meta_data_parts":metadata}
		if "**" in newText or "``" in newText or "__" in newText:
			metadatas = tools().textAnalysis(newText)
			inData['metadata'] = {'meta_data_parts': metadatas[0]}
			inData['text'] = metadatas[1]
		return self.maker.method('editMessage',inData)

	def forwardMessages(self, From, message_ids, to):
		return self.maker.method('forwardMessages',{"from_object_guid": From,"message_ids": message_ids,"rnd": f"{randint(100000,999999999)}","to_object_guid": to})

	def deleteMessages(self, chat_id, message_ids):
		return self.maker.method('deleteMessages',{'object_guid' : chat_id,"message_ids":message_ids,"type":"Global"}).get('data')

	def getUserInfo(self, chat_id):
		return self.maker.method('getUserInfo',{"user_guid":chat_id})

	def getLastMessage(self, chat_id):
		if chat_id.startswith("u") or chat_id.startswith("c"): return self.maker.method('getUserInfo',{"user_guid":chat_id}).get('data').get('chat').get('last_message')
		if chat_id.startswith("g"): return self.maker.method('getGroupInfo',{"group_guid": chat_id}).get('data').get('chat').get('last_message')

	def getMessages(self, chat_id, min_id):
		return self.maker.method('getMessagesInterval',{"object_guid":chat_id,"middle_message_id":min_id}).get("data").get("messages")
		
	def getInfoByUsername(self, username):
		return self.maker.method('getObjectByUsername',{"username":username})

	def banGroupMember(self, chat_id, user_id):
		return self.maker.method('banGroupMember',{"group_guid": chat_id,"member_guid": user_id,"action":"Set"},method_type=1)

	def unbanGroupMember(self, chat_id, user_id):
		return self.maker.method('banGroupMember',{"group_guid": chat_id,"member_guid": user_id,"action":"Unset"},custom_client=4,method_type=4)

	def invite(self, chat_id, user_ids):
		return self.maker.method('addGroupMembers',{"group_guid": chat_id,"member_guids": user_ids},method_type=1)
	
	def getGroupAdmins(self, chat_id):
		return self.maker.method('getGroupAdminMembers',{"group_guid":chat_id})

	def getGroupMembers(self, chat_id, start_id=None):
		return self.maker.method('getGroupAllMembers',{"group_guid": chat_id,"start_id": start_id})

	def getGroupLink(self, chat_id):
		return self.maker.method('getGroupLink',{"group_guid":chat_id}).get('data').get('join_link')

	def changeGroupLink(self, chat_id):
		return self.maker.method('setGroupLink',{"group_guid": chat_id},custom_client=4,method_type=4)

	def getMessagesInfo(self, chat_id, message_ids):
		return self.maker.method('getMessagesByID',{"object_guid": chat_id,"message_ids": message_ids}).get("data").get("messages")

	def setMembersAccess(self, chat_id, access_list):
		return self.maker.method('setGroupDefaultAccess',{"access_list": access_list,"group_guid": chat_id},custom_client=4,method_type=4)

	def getGroupInfo(self, chat_id):
		return self.maker.method('getGroupInfo',{"group_guid": chat_id})
		
	def getChatsUpdate(self):
		time_stamp = str(math.floor(datetime.datetime.today().timestamp()) - 200)
		return self.maker.method('getChatsUpdates',{"state":time_stamp,}).get("data").get("chats")

	def getChatUpdate(self, chat_id):
		time_stamp = str(math.floor(datetime.datetime.today().timestamp()) - 200)
		return self.maker.method('getMessagesUpdates',{"object_guid":chat_id,"state":time_stamp}).get("data").get("updated_messages")
	
	def myStickersSet(self):
		time_stamp = str(math.floor(datetime.datetime.today().timestamp()) - 200)
		return self.maker.method('getMyStickerSets',{}).get("data")

	def getChannelMembers(self, channel_guid, text=None, start_id=None):
		return self.maker.method('getChannelAllMembers',{"channel_guid": channel_guid,"search_text": text,"start_id": start_id},custom_client=4,method_type=4)

	def searchInChannelMembers(self, text, channel_guid):
		try:
			p = self.maker.method('getChannelAllMembers',{"channel_guid": channel_guid,"search_text": text},custom_client=4,method_type=4)
			if p['in_chat_members'] != []:
				return p['in_chat_members']
			else:
				return 'no exist'
		except: 
			return 'error'

	def checkJoinChannel(self,member_guid,channel_guid):
		user_data:dict = self.getUserInfo(member_guid)['data']['user']
		del user_data['is_deleted'], user_data['is_verified'], user_data['online_time']
		search_mem = ''
		if 'username' in user_data.keys() and user_data['username'] != '':
			search_mem = user_data['username']
		elif 'last_name' in user_data.keys():
			search_mem = user_data['first_name'] + ' ' + user_data['last_name']
		elif not 'last_name' in user_data.keys() and 'first_name' in user_data.keys():
			search_mem = user_data['first_name']
		else:
			return 'Profile not success'
		ppo = False
		while ppo == False:
			response = self.searchInChannelMembers(search_mem, channel_guid)
			if response == 'error':
				continue
			elif response == 'no exist':
				ppo =True
				if not 'username' in user_data.keys():
					return 'need for username'
				else:
					return 'no exist'
			else:
				ppo = True
				ss = [i['member_guid'] for i in response]
				if member_guid in ss:
					return 'is exist'
				elif not member_guid in ss and not 'username' in user_data.keys():
					return 'need for username'
				else:
					return 'no exist'

	def setGroupAdmin(self, chat_id, user_id , access):
		return self.maker.method('setGroupAdmin',{"group_guid": chat_id,"access_list":access,"action": "SetAdmin","member_guid": user_id})

	def deleteGroupAdmin(self, chat_id, user_id):
		return self.maker.method('setGroupAdmin',{"group_guid": chat_id,"action": "UnsetAdmin","member_guid": user_id})

	def setChannelAdmin(self, chat_id, user_id, access_list=[]):
		return self.maker.method('setChannelAdmin',{"group_guid": chat_id,"access_list": access_list,"action": "SetAdmin","member_guid": user_id},custom_client=4)

	def inviteChannel(self, chat_id, user_ids):
		return self.maker.method('addChannelMembers',{"channel_guid": chat_id,"member_guids": user_ids})

	def sendSticker(self, group_guid):
		return self.maker.method('sendMessage',{"object_guid":group_guid,"rnd":f"{randint(100000,999999999)}","sticker":{"emoji_character": "😔","w_h_ratio": "1.0","sticker_id": "5e0c9c5c03ae0456535bb403","file":{"file_id": "494573877","mime": "png","dc_id": "32","access_hash_rec": "449970287806732600832117650401","file_name": "sticker.png"},},"sticker_set_id": "5e0c9ac6bcfaf77f4f1b647a"})
	
	def getChannelInfo(self, channel_guid):
		return self.maker.method('getChannelInfo',{"channel_guid":channel_guid},custom_client=4,method_type=4)

	def setGroupTimer(self, chat_id, time):
		return self.maker.method('editGroupInfo',{"group_guid": chat_id,"slow_mode": time,"updated_parameters":["slow_mode"]},custom_client=4,method_type=4)

	def seenChats(self, seenList):
		# seenList must be a dict , keys are object guids and values are last message’s id, {"guid":"msg_id"}
		return self.maker.method('seenChats',{"seen_list": seenList})

	def sendChatAction(self, chat_id, action):
    	#every some seconds before sending message this request should send
		return self.maker.method('sendChatActivity',{"activity": action,"object_guid": chat_id})

	def pin(self, chat_id, message_id):
		return self.maker.method('setPinMessage',{"action":"Pin","message_id": message_id,"object_guid": chat_id},custom_client=4,method_type=4)

	def unpin(self, chat_id, message_id):
		return self.maker.method('setPinMessage',{"action":"Unpin","message_id": message_id,"object_guid": chat_id},custom_client=4,method_type=4)

	def chatGroupvisit(self,guid,visiblemsg):
		return self.maker.method('editGroupInfo',{"chat_history_for_new_members": "Visible","group_guid": guid,"updated_parameters": visiblemsg})

	def chatGrouphidden(self,guid,hiddenmsg):
		return self.maker.method('editGroupInfo',{"chat_history_for_new_members": "Hidden","group_guid": guid,"updated_parameters": hiddenmsg})

	def joinGroup(self, link):
		return self.maker.method('joinGroup',{"hash_link": link.split('/')[-1]})
				
	def leaveGroup(self, group_guid):
		return self.maker.method('leaveGroup',{"group_guid": group_guid})

	def joinChannel(self, link):
		return self.maker.method('joinChannelByLink',{"hash_link": link.split("/")[-1]})

	def joinChannelByID(self, chat_id):
		return self.maker.method('joinChannelAction',{"action": "Join","channel_guid": chat_id})

	def LeaveChannel(self, chat_id):
		return self.maker.method('joinChannelAction',{"action": "Leave","channel_guid": chat_id})

	def groupPreviewByJoinLink(self, link):
		return self.maker.method('groupPreviewByJoinLink',{"hash_link": link.split('/')[-1]}).get('data')

	def deleteChatHistory(self, group,msg_id):
		return self.maker.method('deleteChatHistory',{"last_message_id": msg_id,"object_guid": group})

	def editnameGroup(self,groupgu,namegp,biogp):
		return self.maker.method('editGroupInfo',{"description": biogp,"group_guid": groupgu,"title":namegp,"updated_parameters":["title","description"]})

	def editbioGroup(self,groupgu,biogp,namegp):
		return self.maker.method('editGroupInfo',{"description": biogp,"group_guid": groupgu,"title":namegp,"updated_parameters":["title","description"]})

	def block(self, chat_id):
		return self.maker.method('setBlockUser',{"action": "Block","user_guid": chat_id})

	def unblock(self, chat_id):
		return self.maker.method('setBlockUser',{"action": "Unblock","user_guid": chat_id})

	def startVoiceChat(self, chat_id):
		return self.maker.method('createGroupVoiceChat',{"chat_guid":chat_id})

	def editVoiceChat(self, chat_id,voice_chat_id, title):
		return self.maker.method('setGroupVoiceChatSetting',{"chat_guid":chat_id,"voice_chat_id" : voice_chat_id,"title" : title ,"updated_parameters": ["title"]})

	def finishVoiceChat(self, chat_id, voice_chat_id):
		return self.maker.method('setGroupVoiceChatSetting',{"chat_guid":chat_id,"voice_chat_id" : voice_chat_id})

	def uploadAvatar(self,myguid,main,thumbnail=None):
		mainID = str(Bot.uploadFile(self, main)[0]["id"])
		thumbnailID = str(Bot.uploadFile(self, thumbnail or main)[0]["id"])
		return self.maker.method('uploadAvatar',{"object_guid":myguid,"thumbnail_file_id":thumbnailID,"main_file_id":mainID})

	def getAvatars(self,myguid):
		return self.maker.method('getAvatars',{"object_guid":myguid}).get("data").get("avatars")

	def deleteAvatar(self,myguid,avatar_id):
		return self.maker.method('deleteAvatar',{"object_guid":myguid,"avatar_id":avatar_id})

	def sendPoll(self,guid,SOAL,LIST):
		return self.maker.method('createPoll',{"allows_multiple_answers": "false","is_anonymous": "true","object_guid": guid,"options":LIST,"question":SOAL,"rnd":f"{randint(100000,999999999)}","type":"Regular"})

	def votePoll(self, poll_id, option_index):
		return self.maker.method('votePoll',{"poll_id": poll_id,"selection_index": option_index},custom_client=4,method_type=4)

	def getPollStatus(self, poll_id):
		return self.maker.method('getPollStatus',{"poll_id":poll_id})

	def getPollOptionVoters(self, poll_id, option_index, start_id=None):
		return self.maker.method('getPollOptionVoters',{"poll_id":poll_id,"selection_index": option_index,"start_id": start_id}).get('data')

	def getLinkFromAppUrl(self,app_url,):
		return self.maker.method('getLinkFromAppUrl',{"app_url":app_url}).get("data")

	def search(self, text):
		return self.maker.method('searchGlobalObjects',{"search_text": text},custom_client=4,method_type=4)

	def searchText(self,guid,text):
		return self.maker.method('searchChatMessages',{"object_guid": guid,"search_text": text,"type":"Text"}).get("data").get("message_ids")[:5]

	def editProfile(self, **kwargs):
		if "username" in list(kwargs.keys()):
			return self.maker.method('updateUsername',{"username": kwargs.get("username"),"updated_parameters":["username"]},custom_client=4,method_type=4)
			kwargs = kwargs.pop("username")
		if len(list(kwargs.keys())) > 0:
			return self.maker.method('updateProfile',{"first_name": kwargs.get("first_name"),"last_name": kwargs.get("last_name"),"bio": kwargs.get("bio"),"updated_parameters":list(kwargs.keys())},custom_client=4,method_type=4)

	def getThumbInline(self,image_bytes:bytes):
		im = Image.open(io.BytesIO(image_bytes))
		width, height = im.size
		if height > width:
			new_height = 40
			new_width  = round(new_height * width / height)
		else:
			new_width  = 40
			new_height = round(new_width * height / width)
		im = im.resize((new_width, new_height), Image.ANTIALIAS)
		changed_image = io.BytesIO()
		im.save(changed_image, format='PNG')
		changed_image = changed_image.getvalue()
		return base64.b64encode(changed_image)

	def getImageSize(self,image_bytes:bytes):
		im = Image.open(io.BytesIO(image_bytes))
		width, height = im.size
		return width , height

	def hexToRgb(self,value):
		value = value.lstrip('#')
		lv = len(value)
		return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

	def requestSendFile(self, file):
		return self.maker.method('requestSendFile',{"file_name": str(file.split("/")[-1]),"mime": file.split(".")[-1],"size": Path(file).stat().st_size}).get('data')

	def uploadFile(self, file):
		if not "http" in file:
			frequest = Bot.requestSendFile(self, file)
			bytef = open(file,"rb").read()
			hash_send = frequest["access_hash_send"]
			file_id = frequest["id"]
			url = frequest["upload_url"]
			header = {'auth':self.auth,'Host':url.replace("https://","").replace("/UploadFile.ashx",""),'chunk-size':str(Path(file).stat().st_size),'file-id':str(file_id),'access-hash-send':hash_send,"content-type": "application/octet-stream","content-length": str(Path(file).stat().st_size),"accept-encoding": "gzip","user-agent": "okhttp/3.12.1"}
			if len(bytef) <= 131072:
				header["part-number"], header["total-part"] = "1","1"
				while True:
					try:
						j = post(data=bytef,url=url,headers=header).text
						j = loads(j)['data']['access_hash_rec']
						break
					except Exception as e:continue
				return [frequest, j]
			else:
				t = round(len(bytef) / 131072 + 1)
				for i in range(1,t+1):
					if i != t:
						k = i - 1
						k = k * 131072
						while True:
							try:
								header["chunk-size"], header["part-number"], header["total-part"] = "131072", str(i),str(t)
								o = post(data=bytef[k:k + 131072],url=url,headers=header).text
								o = loads(o)['data']
								break
							except Exception as e:continue
					else:
						k = i - 1
						k = k * 131072
						while True:
							try:
								header["chunk-size"], header["part-number"], header["total-part"] = str(len(bytef[k:])), str(i),str(t)
								p = post(data=bytef[k:],url=url,headers=header).text
								p = loads(p)['data']['access_hash_rec']
								break
							except Exception as e:continue
						return [frequest, p]
		else:
			frequest = self.maker.method('requestSendFile',{"file_name": file.split("/")[-1],"mime": file.split(".")[-1],"size": len(get(file).content)}).get('data')
			hash_send = frequest["access_hash_send"]
			file_id = frequest["id"]
			url = frequest["upload_url"]
			bytef = get(file).content
			header = {'auth':self.auth,'Host':url.replace("https://","").replace("/UploadFile.ashx",""),'chunk-size':str(len(get(file).content)),'file-id':str(file_id),'access-hash-send':hash_send,"content-type": "application/octet-stream","content-length": str(len(get(file).content)),"accept-encoding": "gzip","user-agent": "okhttp/3.12.1"}
			if len(bytef) <= 131072:
				header["part-number"], header["total-part"] = "1","1"
				while True:
					try:
						j = post(data=bytef,url=url,headers=header).text
						j = loads(j)['data']['access_hash_rec']
						break
					except Exception as e:continue
				return [frequest, j]
			else:
				t = round(len(bytef) / 131072 + 1)
				for i in range(1,t+1):
					if i != t:
						k = i - 1
						k = k * 131072
						while True:
							try:
								header["chunk-size"], header["part-number"], header["total-part"] = "131072", str(i),str(t)
								o = post(data=bytef[k:k + 131072],url=url,headers=header).text
								o = loads(o)['data']
								break
							except Exception as e:continue
					else:
						k = i - 1
						k = k * 131072
						while True:
							try:
								header["chunk-size"], header["part-number"], header["total-part"] = str(len(bytef[k:])), str(i),str(t)
								p = post(data=bytef[k:],url=url,headers=header).text
								p = loads(p)['data']['access_hash_rec']
								break
							except Exception as e:continue
						return [frequest, p]

	def fileUpload(self, bytef ,hash_send ,file_id ,url):		
		if len(bytef) <= 131072:
			h = {'auth':self.auth,'chunk-size':str(len(bytef)),'file-id':str(file_id),'access-hash-send':hash_send,'total-part':str(1),'part-number':str(1)}
			t = False
			while t == False:
				try:
					j = post(data=bytef,url=url,headers=h).text
					j = loads(j)['data']['access_hash_rec']
					t = True
				except:
					t = False
			return j
		else:
			t = len(bytef) / 131072
			t += 1
			t = math.floor(t)
			for i in range(1,t+1):
				if i != t:
					k = i - 1
					k = k * 131072
					t2 = False
					while t2 == False:
						try:
							o = post(data=bytef[k:k + 131072],url=url,headers={'auth':self.auth,'chunk-size':str(131072),'file-id':file_id,'access-hash-send':hash_send,'total-part':str(t),'part-number':str(i)}).text
							o = loads(o)['data']
							t2 = True
						except:
							t2 = False
					j = k + 131072
					j = round(j / 1024)
					j2 = round(len(bytef) / 1024)
					print(str(j) + 'kb / ' + str(j2) + ' kb')                
				else:
					k = i - 1
					k = k * 131072
					t2 = False
					while t2 == False:
						try:
							p = post(data=bytef[k:],url=url,headers={'auth':self.auth,'chunk-size':str(len(bytef[k:])),'file-id':file_id,'access-hash-send':hash_send,'total-part':str(t),'part-number':str(i)}).text
							p = loads(p)['data']['access_hash_rec']
							t2 = True
						except:
							t2 = False
					j2 = round(len(bytef) / 1024)
					print(str(j2) + 'kb / ' + str(j2) + ' kb') 
					return p

	def requestFile(self, name, size , mime):
		o = ''
		while str(o) != '<Response [200]>':
			o = self.maker.method('requestSendFile',{"file_name":name,"size":size,"mime":mime},method_type=1)
			try:
				k = loads(encryption(self.auth).decrypt(o.json()["data_enc"]))
				if k['status_det'] == 'TOO_REQUESTS':
					return 'many_request'
				elif k['status'] != 'OK' or k['status_det'] != 'OK':
					o = '502'
			except:
				o = '502'
		return k['data']
		#"wss://jsocket1.iranlms.ir:80" ,
		#"wss://jsocket2.iranlms.ir:80" ,
		#"wss://jsocket3.iranlms.ir:80",
		#"wss://jsocket5.iranlms.ir:80"

	def sendFile(self, chat_id, file_id , mime , dc_id, access_hash_rec, file_name, size, text=None, message_id=None):
		if text == None:
			if message_id == None:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"File","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec}})
			else:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","reply_to_message_id":message_id,"file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"File","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec}})
		else:
			if message_id == None:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","text":text,"file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"File","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec}})
			else:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","text":text,"reply_to_message_id":message_id,"file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"File","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec}})

	def sendImage(self, chat_id, file_id , mime , dc_id, access_hash_rec, file_name,  size, thumb_inline , width , height, text=None, message_id=None):
		if text == None:
			if message_id == None:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"Image","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec,'thumb_inline':thumb_inline,'width':width,'height':height}})
			else:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","reply_to_message_id":message_id,"file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"Image","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec,'thumb_inline':thumb_inline,'width':width,'height':height}})
		else:
			if message_id == None:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","text":text,"file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"Image","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec,'thumb_inline':thumb_inline,'width':width,'height':height}})
			else:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","text":text,"reply_to_message_id":message_id,"file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"Image","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec,'thumb_inline':thumb_inline,'width':width,'height':height}})

	def send_Voice(self, chat_id, file_id , mime , dc_id, access_hash_rec, file_name,  size, duration, text=None, message_id=None):
		if text == None:
			if message_id == None:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"Voice","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec,'time':duration,}})
			else:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","reply_to_message_id":message_id,"file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"Voice","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec,'time':duration,}})  
		else:
			if message_id == None:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","text":text,"file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"Voice","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec,'time':duration,}})
			else:
				return self.maker.method('sendMessage',{"object_guid":chat_id,"rnd":f"{randint(100000,900000)}","text":text,"reply_to_message_id":message_id,"file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"Voice","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec,'time':duration,}})

	def sendDocument(self, chat_id, file, caption=None, message_id=None):
		# Bot.sendDocument("guid","./file.txt", caption="anything", message_id="12345678")
		uresponse = Bot.uploadFile(self, file)
		file_id = str(uresponse[0]["id"])
		mime = file.split(".")[-1]
		dc_id = uresponse[0]["dc_id"]
		access_hash_rec = uresponse[1]
		file_name = file.split("/")[-1]
		size = str(len(get(file).content if "http" in file else open(file,"rb").read()))
		self.maker.method('sendMessage',{"object_guid":chat_id,"reply_to_message_id":message_id,"rnd":f"{randint(100000,999999999)}","file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"File","file_name":file_name,"size":size,"mime":mime,"access_hash_rec":access_hash_rec}},method_type=2)

	def sendGIF(self, chat_id, file, width, height, thumbnail="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", caption=None, message_id=None):
		uresponse = Bot.uploadFile(self, file)
		file_id = str(uresponse[0]["id"])
		mime = file.split(".")[-1]
		dc_id = uresponse[0]["dc_id"]
		access_hash_rec = uresponse[1]
		file_name = file.split("/")[-1]
		size = str(len(get(file).content if "http" in file else open(file,"rb").read()))
		return self.maker.method('sendMessage',{"object_guid": chat_id,"is_mute": False,"rnd": randint(100000,999999999),"file_inline": {"access_hash_rec": access_hash_rec,"dc_id": dc_id,"file_id": file_id,"auto_play": False,"file_name": file_name,"width": width,"height": height,"mime": mime,"size": size,"thumb_inline": thumbnail,"type": "Gif"},"text": caption,"reply_to_message_id":message_id},custom_client=4,method_type=4)

	def sendLocation(self, chat_id, location:list, message_id=None):
		return self.maker.method('sendMessage',{"is_mute": False,"object_guid":chat_id,"rnd":f"{randint(100000,999999999)}","location":{"latitude": location[0],"longitude": location[1]},"reply_to_message_id":message_id},custom_client=4,method_type=4)
