from requests import post
from json import loads, dumps
from random import choice
from Crypto.Util.Padding import pad, unpad
import base64
from Crypto.Cipher import AES
from re import findall
from colorama import Fore

web = {'app_name': 'Main', 'app_version': '4.0.8', 'platform': 'Web', 'package': 'web.rubika.ir', 'lang_code': 'fa'}
android = {'app_name': 'Main', 'app_version': '2.9.8', 'platform': 'Android', 'package': 'app.rbmain.a', 'lang_code': 'fa'}

class encryption:
    def __init__(self, auth):
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.iv = bytearray.fromhex('00000000000000000000000000000000')

    def replaceCharAt(self, e, t, i):
        return e[0:t] + i + e[t + len(i):]

    def secret(self, e):
        t = e[0:8]
        i = e[8:16]
        n = e[16:24] + t + e[24:32] + i
        s = 0
        while s < len(n):
            e = n[s]
            if e >= '0' and e <= '9':
                t = chr((ord(e[0]) - ord('0') + 5) % 10 + ord('0'))
                n = self.replaceCharAt(n, s, t)
            else:
                t = chr((ord(e[0]) - ord('a') + 9) % 26 + ord('a'))
                n = self.replaceCharAt(n, s, t)
            s += 1
        return n

    def encrypt(self, text):
        raw = pad(text.encode('UTF-8'), AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = aes.encrypt(raw)
        result = base64.b64encode(enc).decode('UTF-8')
        return result

    def decrypt(self, text):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = aes.decrypt(base64.urlsafe_b64decode(text.encode('UTF-8')))
        result = unpad(dec, AES.block_size).decode('UTF-8')
        return result

class tools(object,):
	def __init__(self,):
		pass

	def textAnalysis(self, text,):
		Results = []
		realText : str = text.replace('**', '').replace('__', '').replace('``', '')

		bolds = findall(r'\*\*(.*?)\*\*' , text)
		italics = findall(r'\_\_(.*?)\_\_' , text)
		monos = findall(r'\`\`(.*?)\`\`' , text)

		bResult = [realText.index(i) for i in bolds]
		iResult = [realText.index(i) for i in italics]
		mResult = [realText.index(i) for i in monos]

		for bIndex , bWord in zip(bResult , bolds):
			Results.append({
				'from_index' : bIndex,
				'length' : len(bWord),
				'type' : 'Bold'
		})

		for iIndex , iWord in zip(iResult , italics):
			Results.append({
				'from_index' : iIndex,
				'length' : len(iWord),
				'type' : 'Italic'
		})

		for mIndex , mWord in zip(mResult , monos):
			Results.append({
				'from_index' : mIndex,
				'length' : len(mWord),
				'type' : 'Mono'
		})

		return (Results, realText)

class accesses:
	class admin:
		pin               = "PinMessages"
		newAdmin          = "SetAdmin"
		editInfo          = "ChangeInfo"
		banMember         = "BanMember"
		changeLink        = "SetJoinLink"
		editMembersAccess = "SetMemberAccess"
		deleteMessages    = "DeleteGlobalAllMessages"

	class user:
		viewMembers = "ViewMembers"
		viewAdmins  = "ViewAdmins"
		sendMessage = "SendMessages"
		addMember   = "AddMember"

class maker(object,):
    def __init__(self, auth,):
        self.auth = auth
        self.enc = encryption(auth,)

    def method(self, method_name, method_data, custom_client = None, method_type = None,):
        if method_type == None:
            t = False
            while t == False:
                try:
                    r = loads(self.enc.decrypt(post(json={"api_version":"5","auth":self.auth,"data_enc":self.enc.encrypt(dumps({"method":method_name,"input":method_data,"client":android if custom_client == 4 else web}))},url=f"https://messengerg2c{choice(range(1 , 100))}.iranlms.ir").json()["data_enc"]))
                    t = True
                except: t = False
            return r

        if method_type == 1:
            t = False
            while t == False:
                try:
                    r = post(json={"api_version":"5","auth":self.auth,"data_enc":self.enc.encrypt(dumps({"method":method_name,"input":method_data,"client":android if custom_client == 4 else web}))},url=f"https://messengerg2c{choice(range(1 , 100))}.iranlms.ir")
                    t = True
                except: t = False
            return r

        if method_type == 2:
            t = False
            while t == False:
                try:
                    r = loads(self.enc.decrypt(loads(post(json={"api_version":"5","auth":self.auth,"data_enc":self.enc.encrypt(dumps({"method":method_name,"input":method_data,"client":android if custom_client == 4 else web}))},url=f"https://messengerg2c{choice(range(1 , 100))}.iranlms.ir").text)['data_enc']))
                    t = True
                except: t = False
            return r

        elif method_type == 4:
            t = False
            while t == False:
                try:
                    r = loads(self.enc.decrypt(post(json={"api_version":"4","auth":self.auth,"client":android if custom_client == 4 else web,"data_enc":self.enc.encrypt(dumps(method_data)),"method":method_name},url=f"https://messengerg2c{choice(range(1 , 100))}.iranlms.ir").json()["data_enc"]))
                    t = True
                except: t = False
            return r

    def getThumbInline(image_bytes:bytes):
        import io, base64, PIL.Image
        im = PIL.Image.open(io.BytesIO(image_bytes))
        width, height = im.size
        if height > width:
            new_height = 40
            new_width  = round(new_height * width / height)
        else:
            new_width  = 40
            new_height = round(new_width * height / width)
        im = im.resize((new_width, new_height), PIL.Image.ANTIALIAS)
        changed_image = io.BytesIO()
        im.save(changed_image, format='PNG')
        changed_image = changed_image.getvalue()
        return base64.b64encode(changed_image)

    def getImageSize(image_bytes:bytes):
        import io, PIL.Image
        im = PIL.Image.open(io.BytesIO(image_bytes))
        width, height = im.size
        return [width , height]

class welcome:
    def welcome_tx():
    	Yellow       = "\033[33m"
    	BackgroundWhite        = "\033[107m"
    	BackgroundLightCyan    = "\033[106m"
    	BackgroundGreen        = "\033[42m"
    	Black        = "\033[30m"
    	Default      = "\033[39m"
    	BackgroundLightGray    = "\033[47m"
    	BackgroundRed          = "\033[41m"
    	Color_Off="\033[0m" 
    	print(BackgroundLightCyan+Black+"    𝗥𝗨𝗕:𝗠𝗮𝗠𝗮𝗗_𝗮𝗗𝘇" +"  "+ BackgroundGreen+Black+" "*8 +Default+"𝗟 𝗶 𝗕 𝗥 𝗔 𝗥 𝗬"+Black+ " " *5+BackgroundLightCyan+" Ⓒ︎ 𝐦 𝐨 𝐡 𝐚 𝐦 𝐚 𝐝"+" "*2)
    	print(BackgroundLightCyan+Black+"    version:1.0.0" +"  "+ BackgroundGreen+Black+" "*7+"[ 𝗦 𝗧 𝗘 𝗥 𝗜 𝗞 ]"+ " " *4+BackgroundLightCyan+" 🅒︎ 𝐦 𝐚 𝐥 𝐞 𝐤 𝐢[●]"+" "+BackgroundLightGray+Color_Off)
    	
    	print('\n')