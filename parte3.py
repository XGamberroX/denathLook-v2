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
        from CMDbr import ZarekCHK
        CheckRecive = await ZarekCHK(CcVerify, CheckedP[1])
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




@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["bra"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Baruch [ Auth ]'
    TwoNameGateway = 'Gateway ↯ Baruch [ Auth ]'
    ThreeGateway = 'Gateway 🔥 Baruch [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('bra')
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
        from CMDbra import BraintreeWoo
        CheckRecive = await BraintreeWoo(CcVerify, CheckedP[1])
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



@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["kill"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Kalaka [ 20$ ]'
    TwoNameGateway = 'Gateway ↯ Kalaka [ 20$ ]'
    ThreeGateway = 'Gateway 🔥 Kalaka [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('kill')
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
        from CMDkill import CMDkill
        CheckRecive = await CMDkill(CcVerify, CheckedP[1])
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


@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["ab"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Anubis [ 15$ ]'
    TwoNameGateway = 'Gateway ↯ Anubis [ 15$ ]'
    ThreeGateway = 'Gateway 🔥 Anubis [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('ab')
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
        from CMDab import CMDab
        CheckRecive = await CMDab(CcVerify, CheckedP[1])
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["au"])
async def CMDsb(message: types.Message):
    NameGateway = 'Gateway 🔥 Auribe [ Auth ]'
    TwoNameGateway = 'Gateway ↯ Auribe [ Auth ]'
    ThreeGateway = 'Gateway 🔥 Auribe [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('au')
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
    try :
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
    except TypeError :
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
        from CMDau import StripeAuth
        CheckRecive = await StripeAuth(CcVerify, CheckedP[1])
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

async def get_stripeauth(session, cc, cvv, month, year):
    from CMDmasstr import GateMasstr
    cc = f'{cc}|{month}|{year}|{cvv}'
    ResponseMass = await GateMasstr(session, cc)
    return f"<b>CC ↯ [<code>{cc}</code>]\nStatus ↯ {ResponseMass[0]} | Time ↯ {ResponseMass[2][0:4]}s\nMessage ↯ {ResponseMass[1]}</b>"

async def get_stripeauth_2(session, cc, cvv, month, year):
    from CMDmascn import GateMasstr
    cc = f'{cc}|{month}|{year}|{cvv}'
    ResponseMass = await GateMasstr(session, cc)
    return f"<b>CC ↯ [<code>{cc}</code>]\nStatus ↯ {ResponseMass[0]} | Time ↯ {ResponseMass[2][0:4]}s\nMessage ↯ {ResponseMass[1]}</b>"

async def get_stripeauth_3(session, cc, cvv, month, year):
    from CMDmassop import GateMasstr
    cc = f'{cc}|{month}|{year}|{cvv}'
    ResponseMass = await GateMasstr(session, cc)
    return f"<b>CC ↯ [<code>{cc}</code>]\nStatus ↯ {ResponseMass[0]} | Time ↯ {ResponseMass[2][0:4]}s\nMessage ↯ {ResponseMass[1]}</b>"

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["masscn"])
async def CMDmasstr(message: types.Message):
    NameGateway = 'Gateway 🔥 Unknown [ CCN 1$ ]'
    TwoNameGateway = 'Unknown'
    ThreeGateway = 'Gateway 🔥 Unknown CCN [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('masscn')
    if WaitStatus[0] in ['OFFLINE ❌', 'OFFLINE1 ❌']:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter) as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
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
    if await VerifyBanned(str(message.from_user.id)) == 'Yes':
        try:
            await bot.send_message(
                chat_id=message.chat.id,
                text="<b>You are banned from this bot.</b>",
                reply_to_message_id=message.message_id
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except (aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest):
            return
    VerMessage = message.text
    if message.reply_to_message:
        VerMessage = message.reply_to_message.text
    if len(re.findall(r'\d', VerMessage)) >= 15:
        pass

    if not any(char.isdigit() for char in VerMessage):
        try:
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>",
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
    CcVerify = await CCheckMASS(re.sub("[^\d\n]", " ", VerMessage))
    if len(CcVerify) > 10:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThis command only supports 10 ccs!\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    if not CcVerify:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    for cc in CcVerify:
        try:
            result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{cc[0:6]}'")
            result = json.loads(json.dumps(result[0]))
            type = result['type']
            level = result['level']
            brand = result['brand']
            bank = result['bank']
            country = result['country']
            emoji = result['Emoji']
        except IndexError:
            try:
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBin Not Found!\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
            except aiogram.utils.exceptions.MessageToEditNotFound:
                # await asyncio.sleep(e.value)
                return
            except aiogram.utils.exceptions.BadRequest:
                # await asyncio.sleep(e.value)
                return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        if ((brand == 'VISA') or (brand == 'MASTERCARD') or (brand == 'DISCOVER') or (brand == 'AMERICAN EXPRESS')) == False :
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{cc}</code>\nInfo ↯ <code>{brand} {emoji}</code>\nComment ↯ <code>This bot only accepts American, Visa, Mastercard and Discover.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
        rbin = await ConnectDB.run_query(f"SELECT * FROM binbanned WHERE Bin='{cc[0:6]}'")
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        if rbin:
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ Bin banned for this bot. ↯\n- - - - - - - - - - - - - - - - - - - - -\nBin ↯ <code>{cc[0:6]} ({emoji})</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    now = datetime.datetime.now()
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    try :
        fin = f'{time.time()-inicio}'
        message_send = await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ CHECKING MASS 🔴 ] ↯\n- - - - - - - - - - - - - - - - - - - - -\n↯ Start Time: <code>{current_datetime}</code>\n↯ Gateway: {TwoNameGateway} | ↯ CCS Detected: <code>{len(CcVerify)}</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
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
        async def main(lista):
            import certifi
            import ssl
            ssl_context = ssl.create_default_context(cafile=certifi.where())
            conn = aiohttp.TCPConnector(ssl=ssl_context)
            async with aiohttp.ClientSession(connector=conn) as session:
                    mylist = lista.split('\n')
                    tasks = []
                    for x in range(len(mylist)):
                        splitter = mylist[x].split('|')
                        ccnum    = splitter[0]
                        mes      = splitter[1]
                        ano      = splitter[2]
                        cvv      = splitter[3]
                        tasks.append(asyncio.ensure_future(get_stripeauth_2(session=session, cc=ccnum, month=mes, year=ano, cvv=cvv)))
                    original_pokemon = await asyncio.gather(*tasks)
                    return original_pokemon
        finalr = await main('\n'.join(CcVerify))
        finalr = ("\n- - - - - - - - - - - - - - - - - - - - -\n".join(finalr))
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        try :
            total_count = finalr.count("LIVE ✅") + finalr.count("DEAD ❌")
            result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
            Credits = result['Creditos']
            new_credits = int(Credits) - int(total_count)
            await ConnectDB.run_query(f"UPDATE pruebas SET Creditos='{new_credits}' WHERE ID='{message.from_user.id}'")
            await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n{finalr}</b>")
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["masstr"])
async def CMDmasstr(message: types.Message):
    NameGateway = 'Gateway 🔥 Stripe [ CCN 5$ ]'
    TwoNameGateway = 'Stripe'
    ThreeGateway = 'Gateway 🔥 Stripe CCN [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('masstr')
    if WaitStatus[0] in ['OFFLINE ❌', 'OFFLINE1 ❌']:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter) as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
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
    if await VerifyBanned(str(message.from_user.id)) == 'Yes':
        try:
            await bot.send_message(
                chat_id=message.chat.id,
                text="<b>You are banned from this bot.</b>",
                reply_to_message_id=message.message_id
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except (aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest):
            return
    VerMessage = message.text
    if message.reply_to_message:
        VerMessage = message.reply_to_message.text
    if len(re.findall(r'\d', VerMessage)) >= 15:
        pass

    if not any(char.isdigit() for char in VerMessage):
        try:
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>",
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
    CcVerify = await CCheckMASS(re.sub("[^\d\n]", " ", VerMessage))
    if len(CcVerify) > 10:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThis command only supports 10 ccs!\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    if not CcVerify:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    for cc in CcVerify:
        try:
            result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{cc[0:6]}'")
            result = json.loads(json.dumps(result[0]))
            type = result['type']
            level = result['level']
            brand = result['brand']
            bank = result['bank']
            country = result['country']
            emoji = result['Emoji']
        except IndexError:
            try:
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBin Not Found!\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
            except aiogram.utils.exceptions.MessageToEditNotFound:
                # await asyncio.sleep(e.value)
                return
            except aiogram.utils.exceptions.BadRequest:
                # await asyncio.sleep(e.value)
                return
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        if ((brand == 'VISA') or (brand == 'MASTERCARD') or (brand == 'DISCOVER') or (brand == 'AMERICAN EXPRESS')) == False :
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nCC ↯ <code>{cc}</code>\nInfo ↯ <code>{brand} {emoji}</code>\nComment ↯ <code>This bot only accepts American, Visa, Mastercard and Discover.</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
        rbin = await ConnectDB.run_query(f"SELECT * FROM binbanned WHERE Bin='{cc[0:6]}'")
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        if rbin:
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ Bin banned for this bot. ↯\n- - - - - - - - - - - - - - - - - - - - -\nBin ↯ <code>{cc[0:6]} ({emoji})</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    now = datetime.datetime.now()
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    try :
        fin = f'{time.time()-inicio}'
        message_send = await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ [ CHECKING MASS 🔴 ] ↯\n- - - - - - - - - - - - - - - - - - - - -\n↯ Start Time: <code>{current_datetime}</code>\n↯ Gateway: {TwoNameGateway} | ↯ CCS Detected: <code>{len(CcVerify)}</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
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
        async def main(lista):
            import certifi
            import ssl
            ssl_context = ssl.create_default_context(cafile=certifi.where())
            conn = aiohttp.TCPConnector(ssl=ssl_context)
            async with aiohttp.ClientSession(connector=conn) as session:
                    mylist = lista.split('\n')
                    tasks = []
                    for x in range(len(mylist)):
                        splitter = mylist[x].split('|')
                        ccnum    = splitter[0]
                        mes      = splitter[1]
                        ano      = splitter[2]
                        cvv      = splitter[3]
                        tasks.append(asyncio.ensure_future(get_stripeauth(session=session, cc=ccnum, month=mes, year=ano, cvv=cvv)))
                    original_pokemon = await asyncio.gather(*tasks)
                    return original_pokemon
        finalr = await main('\n'.join(CcVerify))
        finalr = ("\n- - - - - - - - - - - - - - - - - - - - -\n".join(finalr))
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        try :
            total_count = finalr.count("LIVE ✅") + finalr.count("DEAD ❌")
            result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
            Credits = result['Creditos']
            new_credits = int(Credits) - int(total_count)
            await ConnectDB.run_query(f"UPDATE pruebas SET Creditos='{new_credits}' WHERE ID='{message.from_user.id}'")
            await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n{finalr}</b>")
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


@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["massop"])
async def CMDmasstr(message: types.Message):
    NameGateway = 'Gateway 🔥 Unknown [ CCN Auth ]'
    TwoNameGateway = 'Unkown'
    ThreeGateway = 'Gateway 🔥 Unknown CCN [↯]'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('massop')
    if WaitStatus[0] in ['OFFLINE ❌', 'OFFLINE1 ❌']:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter) as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
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
    if await VerifyBanned(str(message.from_user.id)) == 'Yes':
        try:
            await bot.send_message(
                chat_id=message.chat.id,
                text="<b>You are banned from this bot.</b>",
                reply_to_message_id=message.message_id
            )
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except (aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest):
            return
    VerMessage = message.text
    if message.reply_to_message:
        VerMessage = message.reply_to_message.text
    if len(re.findall(r'\d', VerMessage)) >= 15:
        pass

    if not any(char.isdigit() for char in VerMessage):
        try:
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>",
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
    CcVerify = await CCheckMASS(re.sub("[^\d\n]", " ", VerMessage))
    if len(CcVerify) > 10:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThis command only supports 10 ccs!\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    if not CcVerify:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            return
        except aiogram.utils.exceptions.BadRequest:
            return