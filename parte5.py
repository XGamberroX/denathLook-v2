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
        from CMDpfw import CMDPayflowAuth
        Status = await CMDPayflowAuth(CcVerify, CheckedP[1])
        if not message.from_user.username : UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
        else : UserName = f'@{message.from_user.username}'
        fin = f'{time.time()-inicio}'
        #--------------------------------- ALTER CHECKER ---------------------------------#
        #--------------------------------- ALTER CHECKER ---------------------------------#
        if (Status[0] == 'Approved') :
            AVSDATA = Status[2]
            PROCCVV2 = Status[3]
            RESPMSG = Status[1]
            respstatus = '[ APPROVED ✅ ]'
            try :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{respstatus}</b>\nCVV ↯ <b>[{PROCCVV2}]</b> | AVS ↯ <b>[{AVSDATA}]</b>\nMessage - ↯ <b>{RESPMSG}\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        elif (Status[0] == 'Declined') :
            AVSDATA = Status[2]
            PROCCVV2 = Status[3]
            RESPMSG = Status[1]
            respstatus = '[ DECLINED ❌ ]'
            try :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{respstatus}</b>\nCVV ↯ <b>[{PROCCVV2}]</b> | AVS ↯ <b>[{AVSDATA}]</b>\nMessage - ↯ <b>{RESPMSG}\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        if (Status[0] == 'ApprovedSinCVV') :
            RESPMSG = Status[1]
            respstatus = '[ APPROVED ✅ ]'
            try :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{respstatus}</b>\nMessage - ↯ <b>{RESPMSG}\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        elif (Status[0] == 'DeclinedSinCVV') :
            RESPMSG = Status[1]
            respstatus = '[ DECLINED ❌ ]'
            try :
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message_send.message_id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{ThreeGateway}\n- - - - - - - - - - - - - - - - - - - - -\n</b>CC - ↯ <code>{CcVerify}</code>\nStatus - ↯ <b>{respstatus}</b>\nMessage - ↯ <b>{RESPMSG}\n- - - - - - - - - - - - - - - - - - - - -\n</b>Bin - ↯ <b>{brand} | {type} | {level}</b>\nBank - ↯ <b>{bank}</b>\nCountry - ↯ <b>{country} [{emoji}]</b>\n- - - - - - - - - - - - - - - - - - - - -\nProxy - ↯ [ <b>{CheckedP[0]}</b> ]\nTest Time - ↯ <b>{fin[0:4]}s</b>\nChecked by - ↯ <b>{UserName} [{UserStatus}]</b>")
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        elif int(Status.find('An unexpected error occurred')) >= 0 :
            Status = f'[ {Status} ]'
            CheckRecive = f'Please try again.'
        else :
            Status = '[ DECLINED ❌ ]'
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["premium"])
async def CMDpremium(message: types.Message):
    AccessSTAFF = await AccessAdmin(message.from_user.id)
    if not AccessSTAFF: return
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    yourmessageone = message.text[9:]
    async def CaptureData() :
        try :
            Separador = yourmessageone.split("|")
            UserIDUP = Separador[0]
            DaysAdded = Separador[1]
            if UserIDUP.find('-') >= 0 :
                try :
                    result = await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{UserIDUP}'")
                    if len(result) != 0 :
                        if len(UserIDUP) >= 7 :
                            if DaysAdded != '' :
                                if int(DaysAdded) < 1 : return None
                                return "UPDATE", UserIDUP, DaysAdded, 'ChatID'
                    elif len(result) == 0 :
                        if len(UserIDUP) >= 7 :
                            if DaysAdded != '' :
                                if int(DaysAdded) < 1 : return None                                    
                                return "INSERT", UserIDUP, DaysAdded, 'ChatID'
                except IndexError : None
            else :
                try :
                    result = await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{UserIDUP}'")
                    if len(result) != 0 :
                        if len(UserIDUP) >= 7 :
                            if DaysAdded != '' : return "UPDATE", UserIDUP, DaysAdded, 'UserID'
                    elif len(result) == 0 :
                        if len(UserIDUP) >= 7 :
                            if DaysAdded != '' :
                                try :
                                    result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{UserIDUP}'")
                                    result = json.loads(json.dumps(result[0]))
                                except IndexError: return 'User no exist'
                                return "INSERT", UserIDUP, DaysAdded, 'UserID'
                except IndexError : None
        except IndexError : None
    CaptureData = await CaptureData()
    if not CaptureData:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    elif CaptureData == 'User no exist' :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe user is not found in my DB! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        if CaptureData[3] == 'ChatID' :
            from datetime import datetime, timedelta, date
            import pytz

            FormatBilling = date.today() + timedelta(days=int(CaptureData[2]))
            fechasinformato = datetime.now(pytz.timezone('US/Central') )
            NextBilling = fechasinformato + timedelta(days=int(CaptureData[2]))
            NextBilling = NextBilling.strftime("%d-%m-%Y %H:%M:%S")
            
            if CaptureData[0] == 'INSERT':
                try :
                    await ConnectDB.run_query(f"INSERT INTO userpremium (ID, FormatBilling, NextBilling) VALUES ('{CaptureData[1]}','{FormatBilling}','{NextBilling}')")
                    await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ CHAT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ ChatID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Days added ↯ <code>{CaptureData[2]} day(s)</code>\n↯ NextBilling ↯ <code>{NextBilling}</code>\n- - - - - - - - - - - - - - - - - - - - -\nCheck your chat now!\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
                    await bot.send_message(chat_id=-1001857380843, text=f"<b>New Added Premium: <code>{CaptureData[1]}</code>\nDays Added: <code>{CaptureData[2]} day(s)</code>\nAdmin: @{message.from_user.username}</b>")
                    return
                except TimeoutError or exceptions.RetryAfter as e:
                    await asyncio.sleep(e.value)
                    return
            elif CaptureData[0] == 'UPDATE' :
                try :
                    await ConnectDB.run_query(f"UPDATE userpremium SET FormatBilling='{FormatBilling}', NextBilling='{NextBilling}' WHERE ID='{CaptureData[1]}'")
                    await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ CHAT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ ChatID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Days added ↯ <code>{CaptureData[2]} day(s)</code>\n↯ NextBilling ↯ <code>{NextBilling}</code>\n- - - - - - - - - - - - - - - - - - - - -\nCheck your chat now!\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
                    await bot.send_message(chat_id=-1001857380843, text=f"<b>New Added Premium: <code>{CaptureData[1]}</code>\nDays Added: <code>{CaptureData[2]} day(s)</code>\nAdmin: @{message.from_user.username}</b>")
                    return
                except TimeoutError or exceptions.RetryAfter as e:
                    await asyncio.sleep(e.value)
                    return
        elif CaptureData[3] == 'UserID' :
            from datetime import datetime, timedelta, date
            import pytz

            FormatBilling = date.today() + timedelta(days=int(CaptureData[2]))

            fechasinformato = datetime.now(pytz.timezone('US/Central'))
            NextBilling = fechasinformato + timedelta(days=int(CaptureData[2]))
            NextBilling = NextBilling.strftime("%d-%m-%Y %H:%M:%S")

            if CaptureData[0] == 'INSERT':
                await ConnectDB.run_query(f"INSERT INTO userpremium (ID, FormatBilling, NextBilling) VALUES ('{CaptureData[1]}','{FormatBilling}','{NextBilling}')")
                await ConnectDB.run_query(f"UPDATE pruebas SET Status='Premium' , TimeAntiSpam='35' WHERE ID='{CaptureData[1]}'")

                result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{CaptureData[1]}'")
                result = json.loads(json.dumps(result[0]))
                UserStatus   =  result['Status']
                Credits      =  result['Creditos']
                TimeAntiSpam =  result['TimeAntiSpam']
                Warnings     =  result['Warnings']
                UserBanned   =  result['UserBanned']

                try :
                    await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ ACCOUNT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ UserID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Status ↯ <code>{UserStatus}</code> | Days added: <code>{CaptureData[2]} day(s)</code>\n↯ Credits ↯ <code>{Credits}</code>\n↯ AntiSpam ↯ <code>{TimeAntiSpam}s</code>\n↯ Warnings ↯ <code>{Warnings}</code> | Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -\nCheck the private chat with me\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
                    await bot.send_message(chat_id=-1001857380843, text=f"<b>New Added Premium: <code>{CaptureData[1]}</code>\nDays Added: <code>{CaptureData[2]} day(s)</code>\nAdmin: @{message.from_user.username}</b>")
                except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)

                import datetime
                ahora = datetime.datetime.now(pytz.timezone('UTC'))
                expireminutes = ahora + datetime.timedelta(minutes=120)
                try :
                    link = await bot.create_chat_invite_link(chat_id=-1001857380843, member_limit=1, expire_date=expireminutes)
                    one = InlineKeyboardButton('𝘼𝙡𝙩𝙚𝙧𝘾𝙃𝙆 𝙈𝙚𝙢𝙗𝙚𝙧𝙨 𝙋𝙧𝙚𝙢𝙞𝙪𝙢', url=link.invite_link)

                    try :
                        language = message.from_user.language_code
                        lenguage_code = language[0:2].lower()
                    except TypeError:
                        translate = 'Please, join the Alter user group. ⬇'
                    else :
                        translate = await Translate(lenguage_code,'Please, join the Alter user group. ⬇')

                    remaining_days = (datetime.datetime.strptime(str(FormatBilling),'%Y-%m-%d') - datetime.datetime.today()).days
                    if (int(remaining_days) == 0) or (int(remaining_days) == -1): remaining_days = 'Today'
                    elif (int(remaining_days) == 1) : remaining_days = '1 day'
                    else : remaining_days = f'{int(remaining_days) + 1} days'

                    repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
                    await bot.send_message(chat_id=CaptureData[1], text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ ACCOUNT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ UserID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Status ↯ <code>{UserStatus}</code>\n↯ NextBilling ↯ <code>{NextBilling}</code> | ↯ Expired in ↯ <code>{remaining_days}</code>\n↯ Credits ↯ <code>{Credits}</code>\n↯ AntiSpam ↯ <code>{TimeAntiSpam}s</code>\n↯ Warnings ↯ <code>{Warnings}</code> | Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -\n{translate}\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_markup=repmarkup)

                except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
                except ErrorsAiogram.utils.exceptions.ChatNotFound: print("ERROR AL ENVIAR EL LINK")

            elif CaptureData[0] == 'UPDATE' :
                await ConnectDB.run_query(f"UPDATE userpremium SET FormatBilling='{FormatBilling}', NextBilling='{NextBilling}' WHERE ID='{CaptureData[1]}'")
                await ConnectDB.run_query(f"UPDATE pruebas SET Status='Premium' , TimeAntiSpam='35' WHERE ID='{CaptureData[1]}'")

                result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{CaptureData[1]}'")
                result = json.loads(json.dumps(result[0]))
                UserStatus   =  result['Status']
                Credits      =  result['Creditos']
                TimeAntiSpam =  result['TimeAntiSpam']
                Warnings     =  result['Warnings']
                UserBanned   =  result['UserBanned']
                try :
                    await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ ACCOUNT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ </b>UserID<b> ↯ [ <code>{CaptureData[1]}</code> ]\n↯ </b>Status<b> ↯ <code>{UserStatus}</code> | </b>Days added:<b> <code>{CaptureData[2]} day(s)</code>\n↯ </b>Credits<b> ↯ <code>{Credits}</code>\n↯ </b>AntiSpam<b> ↯ <code>{TimeAntiSpam}s</code>\n↯ </b>Warnings<b> ↯ <code>{Warnings}</code> | </b>UserBanned:<b> <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -\nCheck the private chat with me\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
                    await bot.send_message(chat_id=-1001857380843, text=f"<b>New Added Premium: <code>{CaptureData[1]}</code>\nDays Added: <code>{CaptureData[2]} day(s)</code>\nAdmin: @{message.from_user.username}</b>")
                except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)          
                
                import datetime
                ahora = datetime.datetime.now(pytz.timezone('UTC'))
                expireminutes = ahora + datetime.timedelta(minutes=120)
                try :
                    one = InlineKeyboardButton('𝘼𝙡𝙩𝙚𝙧𝘾𝙃𝙆 𝙇𝙞𝙣𝙠𝙨', url="https://t.me/alterchk/40")
                    try :
                        language = message.from_user.language_code
                        lenguage_code = language[0:2].lower()
                    except TypeError:
                        translate = 'If you have not yet joined the Alter user group, please request one from an administrator. ⬇'
                    else :
                        translate = await Translate(lenguage_code,'If you have not yet joined the Alter user group, please request one from an administrator. ⬇')

                    remaining_days = (datetime.datetime.strptime(str(FormatBilling),'%Y-%m-%d') - datetime.datetime.today()).days
                    if (int(remaining_days) == 0) or (int(remaining_days) == -1): remaining_days = 'Today'
                    elif (int(remaining_days) == 1) : remaining_days = '1 day'
                    else : remaining_days = f'{int(remaining_days) + 1} days'

                    repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
                    await bot.send_message(chat_id=CaptureData[1], text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ ACCOUNT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ UserID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Status ↯ <code>{UserStatus}</code>\n↯ NextBilling ↯ <code>{NextBilling}</code> | ↯ Expired in ↯ <code>{remaining_days}</code>\n↯ Credits ↯ <code>{Credits}</code>\n↯ AntiSpam ↯ <code>{TimeAntiSpam}s</code>\n↯ Warnings ↯ <code>{Warnings}</code> | Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -\n{translate}\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_markup=repmarkup)

                except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
                except ErrorsAiogram.utils.exceptions.ChatNotFound: print("ERROR AL ENVIAR EL LINK")
         

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["key"])
async def CMDkey(message: types.Message):
    AccessSTAFF = await AccessOwner(message.from_user.id)
    if not AccessSTAFF: return
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)

    async def CreateKey() :
        import string_utils
        permitted_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        redeem = f'AlterCHK-{string_utils.shuffle(permitted_chars)[0:25]}-Bot'
        yourmessage = message.text[5:]
        try :
            Separador = yourmessage.split("|")
            Days = Separador[0]
            Credits = Separador[1]
            UserPermitteds = Separador[2]
            if not Days.isnumeric(): return None
            elif not Credits.isnumeric(): return None
            elif not UserPermitteds.isnumeric(): return None
            if int(UserPermitteds) <= 0 : return None
            if int(Days) <= 0 : return None
        except IndexError : return None
        return redeem, Days, Credits, UserPermitteds

    if re.sub("[^0-9]", "", message.text) == '':
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    KeyDates = await CreateKey()
    if not KeyDates:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        try :
            if int(KeyDates[1]) == 1 : Days = '1 day'
            else : Days = f'{KeyDates[1]} days'
            await ConnectDB.run_query(f"INSERT INTO keysalter (KeyAlter, Days, Credits, UsersAlloweds) VALUES ('{KeyDates[0]}','{KeyDates[1]}','{KeyDates[2]}', '{KeyDates[3]}')")
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nKEY SUCCESSF. CREATED\n- - - - - - - - - - - - - - - - - - - - -\n↯ 🔥 Key Created 🔥 ↯\n( <code>{KeyDates[0]}</code> )\n↯ ⌚️ Information ⌚️ ↯\n(<code>{Days}</code> <code>{KeyDates[2]} credits</code>)\n- - - - - - - - - - - - - - - - - - - - -\n↯ 🏮 Access Gateways 🏮 ↯\n<code>- Normal ↯ Gateways\n- Private ↯ Gateways</code>\n - - - - - - - - - - - - - - - - - - - -\nCan redeem it ↯ {KeyDates[3]} user(s)\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)

        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["timeup"])
async def CMDMyacc(message: types.Message):
    AccessSTAFF = await AccessAdmin(message.from_user.id)
    if not AccessSTAFF: return
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    yourmessageone = message.text[8:]
    async def CaptureData() :
        try :
            Separador = yourmessageone.split("|")
            UserIDUP = Separador[0]
            TimeUp = Separador[1]
            try :
                result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{UserIDUP}'")
                if len(result) != 0 : return UserIDUP, TimeUp
                else : return None   
            except IndexError : None
        except IndexError : None

    CaptureData = await CaptureData()
    if not CaptureData:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        try :
            await ConnectDB.run_query(f"UPDATE pruebas SET TimeAntiSpam='{CaptureData[1]}' WHERE ID='{CaptureData[0]}'")
            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ COMPLETE UPDATE ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\nUserID: <code>{CaptureData[0]}</code>\nNewAntiSpam: <code>{CaptureData[1]} second(s)</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id, reply_markup=repmarkup)
            await bot.send_message(chat_id=-1001857380843, text=f"<b>New AntiSpam: <code>{CaptureData[1]}s</code>\nUserID: <code>{CaptureData[0]}</code>\nAdmin: @{message.from_user.username}</b>")
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

 
@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["addcr"])
async def CMDMyacc(message: types.Message):
    AccessSTAFF = await AccessOwner(message.from_user.id)
    if not AccessSTAFF: return
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    yourmessageone = message.text[7:]
    async def CaptureData() :
        try :
            Separador = yourmessageone.split("|")
            UserIDUP = Separador[0]
            Credits = Separador[1]
            if Credits.isdigit(): pass
            else: return None
            try :
                result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{UserIDUP}'")
                result = json.loads(json.dumps(result[0]))
                UserStatus   =  result['Status']
                if len(result) != 0 : return UserIDUP, Credits, UserStatus
                else : return None   
            except IndexError : None
        except IndexError : None

    CaptureData = await CaptureData()
    if not CaptureData:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        try :
            await ConnectDB.run_query(f"UPDATE pruebas SET Creditos='{CaptureData[1]}' WHERE ID='{CaptureData[0]}'")

            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ COMPLETE UPDATE ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\nUserID: <code>{CaptureData[0]}</code>\nStatus: <code>{CaptureData[2]}</code>\nCredits: <code>{CaptureData[1]}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id, reply_markup=repmarkup)
            await bot.send_message(chat_id=-1001857380843, text=f"<b>New Credits: <code>{CaptureData[1]}</code>\nUserID: <code>{CaptureData[0]}</code>\nAdmin: @{message.from_user.username}</b>")
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
        
@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["alban"])
async def CMDalban(message: types.Message):
    AccessSTAFF = await AccessAdmin(message.from_user.id)
    if not AccessSTAFF: return
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    async def CaptureData() :
        try :
            Separador = message.text
            UserIDUP = re.sub("[^0-9]", "", Separador)
            try :
                result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{UserIDUP}'")
                if len(result) != 0 : return UserIDUP
                else : return None   
            except IndexError : None
        except IndexError : None

    CaptureData = await CaptureData()
    if not CaptureData:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        try :
            await ConnectDB.run_query(f"UPDATE pruebas SET UserBanned='Yes' WHERE ID='{CaptureData}'")
            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ COMPLETE BANNED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\nUserID: <code>{CaptureData}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id, reply_markup=repmarkup)
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["alunban"])
async def CMDalunban(message: types.Message):
    AccessSTAFF = await AccessAdmin(message.from_user.id)
    if not AccessSTAFF: return
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    async def CaptureData() :
        try :
            Separador = message.text
            UserIDUP = re.sub("[^0-9]", "", Separador)
            try :
                result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{UserIDUP}'")
                if len(result) != 0 : return UserIDUP
                else : return None   
            except IndexError : None
        except IndexError : None

    CaptureData = await CaptureData()
    if not CaptureData:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        try :
            await ConnectDB.run_query(f"UPDATE pruebas SET UserBanned='No' WHERE ID='{CaptureData}'")
            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ COMPLETE UNBANNED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\nUserID: <code>{CaptureData}</code>\nBanned: <code>No</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id, reply_markup=repmarkup)
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["alreset"])
async def CMDalreset(message: types.Message):
    AccessSTAFF = await AccessAdmin(message.from_user.id)
    if not AccessSTAFF: return
    async def CaptureData() :
        try :
            Separador = message.text
            UserIDUP = re.sub("[^0-9-]", "", Separador)
            try :
                result = await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{UserIDUP}'")
                if len(result) != 0 : return UserIDUP
                else : return None   
            except IndexError : None
        except IndexError : None

    CaptureData = await CaptureData()
    if not CaptureData:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        await ConnectDB.run_query(f"DELETE FROM userpremium WHERE ID='{CaptureData}'")
        await ConnectDB.run_query(f"UPDATE pruebas SET TimeAntiSpam='90', Creditos='0', TimeAntiSpam='90', Status='Free User', UserBanned='No' WHERE ID='{CaptureData}'")
        one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
        repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
        if (CaptureData.find('-') >= 0) :
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ COMPLETE RESET ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\nChatID: <code>{CaptureData}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id, reply_markup=repmarkup)
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        else :
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ COMPLETE RESET ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\nUserID: <code>{CaptureData}</code>\nStatus: <code>Free User</code>\nCredits: <code>0 credit(s)</code>\nAntiSpam: <code>90s</code>\nWarnings: <code>0</code> | Banned: <code>No</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id, reply_markup=repmarkup)
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["alname"])
async def CMDalname(message: types.Message):
    AccessSTAFF = await AccessAdmin(message.from_user.id)
    if not AccessSTAFF: return
    yourmessageone = message.text[8:]
    async def CaptureData() :
        try :
            Separador = yourmessageone.split("|")
            UserIDUP = Separador[0]
            NewStatus = Separador[1]
            try :
                result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{UserIDUP}'")
                if len(result) != 0 : return UserIDUP, NewStatus
                else : return None   
            except IndexError : None
        except IndexError : None

    CaptureData = await CaptureData()
    if not CaptureData:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        try :
            await ConnectDB.run_query(f"UPDATE pruebas SET Status='{CaptureData[1]}' WHERE ID='{CaptureData[0]}'")
            one = InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk')
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ COMPLETE UPDATE ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\nUserID: <code>{CaptureData[0]}</code>\nNewStatus: <code>{CaptureData[1]}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id, reply_markup=repmarkup)
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["account"])
async def CMDalname(message: types.Message):
    AccessSTAFF = await AccessAdmin(message.from_user.id)
    if not AccessSTAFF: return
    async def CaptureData() :
        try :
            Separador = message.text
            UserIDUP = re.sub("[^0-9-]", "", Separador)
            try :
                result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{UserIDUP}'")
                if len(result) != 0 : return UserIDUP
                else : return None   
            except IndexError : None
        except IndexError : None

    CaptureData = await CaptureData()
    if not CaptureData:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        CheckPremium = await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{CaptureData}'")
        try:
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{CaptureData}'")
            result = json.loads(json.dumps(result[0]))
        except IndexError:
                fechasinformato = datetime.now()
                UserSince = fechasinformato.strftime("%d-%m-%Y")
                await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{CaptureData}', '{UserSince}')")
                result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{CaptureData}'")
                result = json.loads(json.dumps(result[0]))
        if len(CheckPremium) != 0 :
            resultprm = json.loads(json.dumps(CheckPremium[0]))
            NextBilling =  resultprm['NextBilling']
            FormatBilling =  resultprm['FormatBilling']
            UserID = result['ID']
            Status = result['Status']
            Creditos  = result['Creditos']

            birthdate = datetime.datetime.strptime(FormatBilling,'%Y-%m-%d')
            currentDate = datetime.datetime.today()

            remaining_days = (birthdate - currentDate).days
            #print(f"{birthdate} - {currentDate} = {remaining_days}")
            if (int(remaining_days) == 0) or (int(remaining_days) == -1): remaining_days = 'Today'
            elif (int(remaining_days) == 1) : remaining_days = '1 day'
            else :
                remaining_days = int(remaining_days) + 1
                remaining_days = f'{remaining_days} days'
            myaccountmsg = f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ UserID: <code>{UserID}</code>\n↯ Status: <code>{Status}</code>\n↯ NextBilling: <code>{NextBilling}</code> | ↯ Expired in: <code>{remaining_days}</code>\n↯ Credits: <code>{Creditos} credit(s)</code>\n- - - - - - - - - - - - - - - - - - - - -</b>"
        else :
            UserID = result['ID']
            Status = result['Status']
            Creditos  = result['Creditos']
            UserSince = result['UserSince']
            myaccountmsg = f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ UserID: <code>{UserID}</code>\n↯ Status: <code>{Status}</code>\n↯ Credits: <code>{Creditos} credit(s)</code>\n↯ UserSince: <code>{UserSince}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>"
        try :
            await bot.send_message(chat_id=message.chat.id, text=myaccountmsg, reply_to_message_id=message.message_id)
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["id"])
async def CMDalname(message: types.Message):
    try :
        await bot.send_message(chat_id=message.chat.id, text=f"<code>{message.chat.id}</code>", reply_to_message_id=message.message_id)
        return
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
        return

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["reedem", "claim", "redeem"])
async def CMDreedem(message: types.Message):
    from datetime import datetime, timedelta, date
    import pytz
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError:
            fechasinformato = datetime.now()
            UserSince = fechasinformato.strftime("%d-%m-%Y")
            await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{message.from_user.id}', '{UserSince}')")
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))

    VerMessage = re.sub("[^0-9a-zA-Z-]", "", message.text[7:])
    if not VerMessage:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>↯ [ INVALID KEY ] ↯</b>", reply_to_message_id=message.message_id)
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
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
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
    if VerMessage:
        try:
            result =  await ConnectDB.run_query(f"SELECT * FROM keysalter WHERE KeyAlter='{VerMessage}'")
            result = json.loads(json.dumps(result[0]))
            Used = result['Used']
            UsersAlloweds = result['UsersAlloweds']
            Days = result['Days']
            Credits_key = result['Credits']
        except IndexError :
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>↯ [ This is not a valid key. ] ↯</b>", reply_to_message_id=message.message_id)
                return 
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        async def CaptureData() :
            try :
                UserIDUP = message.from_user.id
                DaysAdded = Days
                try :
                    Credits_user = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
                    Credits_user = json.loads(json.dumps(Credits_user[0]))['Creditos']
                    Credits = int(Credits_key) + int(Credits_user)
                    
                    result = await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{UserIDUP}'")
                    if len(result) != 0 :
                        if int(len(str(UserIDUP))) >= 8 :
                            if DaysAdded: return "UPDATE", UserIDUP, DaysAdded, Credits
                    elif len(result) == 0 :
                        if int(len(str(UserIDUP))) >= 8 :
                            if DaysAdded: return "INSERT", UserIDUP, DaysAdded, Credits
                except IndexError : None
            except IndexError : None
        CaptureData = await CaptureData()
        if not CaptureData:
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
        result =  await ConnectDB.run_query(f"SELECT * FROM keysalter WHERE KeyAlter='{VerMessage}'")
        Used = json.loads(json.dumps(result[0]))['Used']
        NewUsed = 1 + int(Used)
        await ConnectDB.run_query(f"UPDATE keysalter SET Used='{NewUsed}' WHERE KeyAlter='{VerMessage}'")

        if int(UsersAlloweds) > int(Used):

            FormatBilling = date.today() + timedelta(days=int(CaptureData[2]))
            Fechasinformato = datetime.now(pytz.timezone('US/Central'))
            NextBilling = Fechasinformato + timedelta(days=int(CaptureData[2]))
            NextBilling = NextBilling.strftime("%d-%m-%Y %H:%M:%S")

            if CaptureData[0] == 'INSERT':
                from datetime import datetime, timedelta, date
                import pytz
                await ConnectDB.run_query(f"INSERT INTO userpremium (ID, FormatBilling, NextBilling) VALUES ('{CaptureData[1]}','{FormatBilling}','{NextBilling}')")
                await ConnectDB.run_query(f"UPDATE pruebas SET Status='Premium' , TimeAntiSpam='35', Creditos='{CaptureData[3]}' WHERE ID='{CaptureData[1]}'")

                result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{CaptureData[1]}'")
                result = json.loads(json.dumps(result[0]))
                UserStatus   =  result['Status']
                Credits      =  result['Creditos']
                TimeAntiSpam =  result['TimeAntiSpam']
                Warnings     =  result['Warnings']
                UserBanned   =  result['UserBanned']

                one = InlineKeyboardButton('𝘼𝙡𝙩𝙚𝙧𝘾𝙃𝙆 𝙋𝙧𝙞𝙘𝙚𝙨', url="https://t.me/alterchkreferencias/13")
                two = InlineKeyboardButton('𝘼𝙡𝙩𝙚𝙧𝘾𝙃𝙆 𝙋𝙖𝙮𝙢𝙚𝙣𝙩𝙨/𝙎𝙚𝙡𝙡𝙚𝙧𝙨', url="https://t.me/alterchkreferencias/12")
                try :
                    language = message.from_user.language_code
                    lenguage_code = language[0:2].lower()
                except TypeError:
                    translate = 'You can purchase a subscription of alterchkbot by clicking on the button below. ⬇'
                else :
                    translate = await Translate(lenguage_code,'You can purchase a subscription of alterchkbot by clicking on the button below. ⬇')

                remaining_days = (datetime.strptime(str(FormatBilling),'%Y-%m-%d') - datetime.today()).days
                if (int(remaining_days) == 0) or (int(remaining_days) == -1): remaining_days = 'Today'
                elif (int(remaining_days) == 1) : remaining_days = '1 day'
                else : remaining_days = f'{int(remaining_days) + 1} days'

                repmarkup = InlineKeyboardMarkup(row_width=2).add(one).add(two)

                if message.chat.id == CaptureData[1] :
                    try :
                        await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ ACCOUNT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ UserID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Status ↯ <code>{UserStatus}</code>\n↯ NextBilling ↯ <code>{NextBilling}</code> | ↯ Expired in ↯ <code>{remaining_days}</code>\n↯ Credits ↯ <code>{Credits}</code>\n↯ AntiSpam ↯ <code>{TimeAntiSpam}s</code>\n↯ Warnings ↯ <code>{Warnings}</code> | Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -\n{translate}\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_markup=repmarkup, reply_to_message_id=message.message_id)
                        await bot.send_message(chat_id=-1001857380843, text=f"<b>New Added Reedem(UserID): <code>{CaptureData[1]}</code>\nDays Added: <code>{CaptureData[2]} day(s)</code></b>")
                    except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
                else :
                    try :
                        await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ ACCOUNT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ UserID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Status ↯ <code>{UserStatus}</code>\n↯ NextBilling ↯ <code>{NextBilling}</code> | ↯ Expired in ↯ <code>{remaining_days}</code>\n↯ Credits ↯ <code>{Credits}</code>\n↯ AntiSpam ↯ <code>{TimeAntiSpam}s</code>\n↯ Warnings ↯ <code>{Warnings}</code> | Banned: <code>{UserBanned}</code></b>", reply_to_message_id=message.message_id)
                        await bot.send_message(chat_id=-1001857380843, text=f"<b>New Added Reedem(UserID): <code>{CaptureData[1]}</code>\nDays Added: <code>{CaptureData[2]} day(s)</code></b>")

                        await bot.send_message(chat_id=CaptureData[1], text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ ACCOUNT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ UserID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Status ↯ <code>{UserStatus}</code>\n↯ Credits ↯ <code>{Credits}</code>\n↯ Warnings ↯ <code>{Warnings}</code> | Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -\n{translate}\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_markup=repmarkup)
                    except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
                    except ErrorsAiogram.utils.exceptions.ChatNotFound: print("ERROR AL ENVIAR EL LINK")

            elif CaptureData[0] == 'UPDATE' :
                from datetime import datetime, timedelta, date
                import pytz
                await ConnectDB.run_query(f"UPDATE userpremium SET FormatBilling='{FormatBilling}', NextBilling='{NextBilling}' WHERE ID='{CaptureData[1]}'")
                await ConnectDB.run_query(f"UPDATE pruebas SET Status='Premium' , TimeAntiSpam='35', Creditos='{CaptureData[3]}' WHERE ID='{CaptureData[1]}'")

                result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{CaptureData[1]}'")
                result = json.loads(json.dumps(result[0]))
                UserStatus   =  result['Status']
                Credits      =  result['Creditos']
                TimeAntiSpam =  result['TimeAntiSpam']
                Warnings     =  result['Warnings']
                UserBanned   =  result['UserBanned']

                one = InlineKeyboardButton('𝘼𝙡𝙩𝙚𝙧𝘾𝙃𝙆 𝙋𝙧𝙞𝙘𝙚𝙨', url="https://t.me/alterchkreferencias/13")
                two = InlineKeyboardButton('𝘼𝙡𝙩𝙚𝙧𝘾𝙃𝙆 𝙋𝙖𝙮𝙢𝙚𝙣𝙩𝙨/𝙎𝙚𝙡𝙡𝙚𝙧𝙨', url="https://t.me/alterchkreferencias/12")
                try :
                    language = message.from_user.language_code
                    lenguage_code = language[0:2].lower()
                except TypeError:
                    translate = 'You can purchase a subscription of alterchkbot by clicking on the button below. ⬇'
                else :
                    translate = await Translate(lenguage_code,'You can purchase a subscription of alterchkbot by clicking on the button below. ⬇')

                remaining_days = (datetime.strptime(str(FormatBilling),'%Y-%m-%d') - datetime.today()).days
                if (int(remaining_days) == 0) or (int(remaining_days) == -1): remaining_days = 'Today'
                elif (int(remaining_days) == 1) : remaining_days = '1 day'
                else : remaining_days = f'{int(remaining_days) + 1} days'

                repmarkup = InlineKeyboardMarkup(row_width=2).add(one).add(two)

                if message.chat.id == CaptureData[1] :
                    try :
                        await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ ACCOUNT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ UserID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Status ↯ <code>{UserStatus}</code>\n↯ NextBilling ↯ <code>{NextBilling}</code> | ↯ Expired in ↯ <code>{remaining_days}</code>\n↯ Credits ↯ <code>{Credits}</code>\n↯ AntiSpam ↯ <code>{TimeAntiSpam}s</code>\n↯ Warnings ↯ <code>{Warnings}</code> | Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -\n{translate}\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_markup=repmarkup, reply_to_message_id=message.message_id)
                        await bot.send_message(chat_id=-1001857380843, text=f"<b>New Added Reedem(UserID): <code>{CaptureData[1]}</code>\nDays Added: <code>{CaptureData[2]} day(s)</code></b>")
                    except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
                else :
                    try :
                        await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ ACCOUNT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ UserID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Status ↯ <code>{UserStatus}</code>\n↯ NextBilling ↯ <code>{NextBilling}</code> | ↯ Expired in ↯ <code>{remaining_days}</code>\n↯ Credits ↯ <code>{Credits}</code>\n↯ AntiSpam ↯ <code>{TimeAntiSpam}s</code>\n↯ Warnings ↯ <code>{Warnings}</code> | Banned: <code>{UserBanned}</code></b>", reply_to_message_id=message.message_id)
                        await bot.send_message(chat_id=-1001857380843, text=f"<b>New Added Reedem(UserID): <code>{CaptureData[1]}</code>\nDays Added: <code>{CaptureData[2]} day(s)</code></b>")

                        await bot.send_message(chat_id=CaptureData[1], text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n🔥 ↯ ACCOUNT UPDATED ↯ 🔥\n- - - - - - - - - - - - - - - - - - - - -\n↯ UserID ↯ [ <code>{CaptureData[1]}</code> ]\n↯ Status ↯ <code>{UserStatus}</code>\n↯ Credits ↯ <code>{Credits}</code>\n↯ Warnings ↯ <code>{Warnings}</code> | Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -\n{translate}\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_markup=repmarkup)
                    except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)
                    except ErrorsAiogram.utils.exceptions.ChatNotFound: print("ERROR AL ENVIAR EL LINK")
        else :
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>↯ [ THIS KEY HAS EXPIRED ] ↯</b>", reply_to_message_id=message.message_id)
            except TimeoutError or exceptions.RetryAfter as e: await asyncio.sleep(e.value)

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["gatestatus"])
async def CMDgatestatus(message: types.Message):
    AccessSTAFF = await AccessModerator(message.from_user.id)
    if not AccessSTAFF: return
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    yourmessageone = message.text[12:]
    async def CaptureData() :
        try :
            Separador = yourmessageone.split("|")
            Gate = Separador[0]
            NewStatus = Separador[1]
            try :
                MessageMain = Separador[2]
            except IndexError : MessageMain = None
            try :
                result = await Validator(str(Gate))
                if result != '' :
                    ListaCC = ['OFF','ON']
                    CheckingList = NewStatus in ListaCC
                    if CheckingList == True :
                        if MessageMain: MessageMaintenance = MessageMain
                        else : MessageMaintenance = 'No comment added'
                        return Gate, NewStatus, MessageMaintenance, result
            except KeyError : None
        except IndexError : None
    CaptureData = await CaptureData()
    if not CaptureData:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncomplete ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        from datetime import datetime
        import pytz 

        now = datetime.now(pytz.timezone('US/Central'))
        fecha_actual = now.strftime(f"%d-%m-%Y %H:%M:%S %p")
        if CaptureData[1] == 'ON' :
            Status = 'ONLINE ✅'
            LinesStatus = '✅ SUCCESSF. ACTIVED ✅'
        elif CaptureData[1] == 'OFF' :
            Status = 'OFFLINE ❌'
            LinesStatus = '🚫 SUCCESSF. DEACTIVED 🚫'

        await ConnectDB.run_query(f"UPDATE Gateways SET Status='{Status}', Mensaje='{CaptureData[2]}', DateOFF='{fecha_actual}' WHERE Name='{CaptureData[0]}'")
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{LinesStatus}\n- - - - - - - - - - - - - - - - - - - - -\n↯ ⚠️ Gate [ {CaptureData[0]} ] has entered the [ {CaptureData[1]} ] state.\n↯ 🔰 Comment added: </b>{CaptureData[2]}\n<b>↯ 📮 Date added:</b> {fecha_actual}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["bin"])
async def CMDreedem(message: types.Message):
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('bin')
    if (WaitStatus[0] == 'OFFLINE ❌') or (WaitStatus[0] == 'OFFLINE1 ❌') :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBIN LOOKUP\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    if int(len(re.sub("[^0-9]", "", message.text)))>=6:
        VerMessage = message.text
    elif message.reply_to_message: VerMessage = message.reply_to_message.text
    else : VerMessage = message.text

    try: 
        if not re.sub("[^0-9]", "", VerMessage) :
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBIN LOOKUP\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>xxxxxx</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
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
    except TypeError:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nBIN LOOKUP\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>xxxxxx</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
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
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
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
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
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
    matchcc = re.sub("[^0-9]", "", VerMessage)
    if 3 <= int(matchcc[0:1]) <= 6 : CcVerify = matchcc
    else : CcVerify = None
    if not CcVerify:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>xxxxxx</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
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
    result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{CcVerify[0:6]}'")
    if len(result) != 0 :
        result = json.loads(json.dumps(result[0]))
        type = result['type']
        level = result['level']
        brand = result['brand']
        bank = result['bank']
        country = result['country']
        emoji = result['Emoji']
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ BIN LOOKUP [✅] ↯\n- - - - - - - - - - - - - - - - - - - - -\nBin - ↯ [ <code>{CcVerify[0:6]}</code> ]\nInfo - ↯ [ <code>{brand}</code> | <code>{type}</code> | <code>{level}</code> ]\nBank - ↯ [ <code>{bank}</code> ]\nCountry - ↯ [ <code>{country} {emoji}</code> ]\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    else :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ INVALID BIN. ⚠️ ↯\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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


@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["dd"])
async def CMDreedem(message: types.Message):
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('dd')
    if (WaitStatus[0] == 'OFFLINE ❌') or (WaitStatus[0] == 'OFFLINE1 ❌') :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nRandom 🔥 Address\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>$dd US, CA, UK</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    VerMessage = message.text[4:]
    if not re.sub("[^a-zA-Z]", "", VerMessage) :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nRandom 🔥 Address\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>$dd US, CA, UK</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
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
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
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
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
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
    VerMessage = VerMessage.upper()
    if VerMessage == 'US' : 
        addgen = VerMessage
    elif VerMessage == 'CA' : 
        addgen = VerMessage
    elif VerMessage == 'UK' : 
        addgen = VerMessage
    else :
        addgen = None
    if not addgen:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nIncorrect ↯ Invalid Info! ⚠️\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>$dd US, CA, UK</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
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
    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
    result = json.loads(json.dumps(result[0]))
    UserStatus =  result['Status']

    if not message.from_user.username: UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>";
    else : UserName = f'@{message.from_user.username}'
    
    if VerMessage == 'US' :
        import random_address
        genaddr = random_address.real_random_address()
        #genaddr = json.loads(genaddr)
        address = genaddr['address1']
        try :
            City = genaddr['city']
        except KeyError :
            City = '-'
        try :
            State = genaddr['state']
        except KeyError :
            State = '-'
        Zip_Code = genaddr['postalCode']
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nRandom 🔥 Address [↯]\n- - - - - - - - - - - - - - - - - - - - -\nAddress - ↯ <code>{address}</code>\nCity - ↯ <code>{City}</code>\nState - ↯ <code>{State}</code>\nZip Code - ↯ <code>{Zip_Code}</code>\n- - - - - - - - - - - - - - - - - - - - -\nChecked by - ↯ {UserName} [{UserStatus}]</b>", reply_to_message_id=message.message_id)
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
    elif VerMessage == 'CA' :
        async with aiohttp.ClientSession() as session:
            try:     
                session.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Accept': '*/*',
                    'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    'Referer': 'https://www.meiguodizhi.com/ca-address?hl=en',
                    'content-type': 'application/json',
                    'Origin': 'https://www.meiguodizhi.com',
                    'Connection': 'keep-alive',
                    })
                data = {
                    "city":"",
                    "path":"/ca-address",
                    "method":"refresh"
                }
                async with session.post('https://www.meiguodizhi.com/api/v1/dz', json=data, timeout=15, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/")) as resp:       
                    response = await resp.json()
                    address = response['address']['Address']
                    City = response['address']['City']
                    State = response['address']['State']
                    Zip_Code = response['address']['Zip_Code']
            except UnboundLocalError :
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'  
            except TypeError :
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            except aiohttp.client_exceptions.ContentTypeError :
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
    elif VerMessage == 'UK' :
        async with aiohttp.ClientSession() as session:
            try:     
                session.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Connection': 'keep-alive',
                    'Referer': 'https://postal-code.co.uk/postcode/London',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': '__utma=249660167.1101903003.1659372958.1659379338.1659395029.3; __utmz=249660167.1659372958.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); euconsent-v2=CPdBusAPdBusAAKAqAENCaCsAP_AAH_AABpYI6td_X__bW9j-_5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwXx2E7NF36pq4KmR4Eu1LBIQNlHMHUDUmwaokVrzHsak2cpyNKJ7JEknMZO2dYGF9Pn1tjuYKY7_5_9_bx2D-t_9_-39T378Xf3_dp_2_-_vCfV599jfn9fV_789KP9_79v-_8__________3_4I7AEmGrcQBdmWODNoGEUKIEYVhIVQKACCgGFogsAHBwU7KwCXWELABAKEIwIgQ4gowYBAAIJAEhEAEgRYIBEARAIAAQAIgEIAGJgEFgBYGAQAAgGhYoBQACBIQZEBEcpgQFQJBQS2ViCUFehphAHWeAFBojYqABEkgIpAQEhYOAYIkBLxZIGmKN8gBGCFAKJUAA.fngAAAAAAAAA; addtl_consent=1~39.4.3.9.6.9.13.6.4.15.9.5.2.7.4.1.7.1.3.2.10.3.5.4.21.4.6.9.7.10.2.9.2.18.7.6.14.5.20.6.5.1.3.1.11.29.4.14.4.5.3.10.6.2.9.6.6.4.5.4.4.29.4.5.3.1.6.2.2.17.1.17.10.9.1.8.6.2.8.3.4.142.4.8.42.15.1.14.3.1.8.10.25.3.7.25.5.18.9.7.41.2.4.18.21.3.4.2.7.6.5.2.14.18.7.3.2.2.8.20.8.8.6.3.10.4.20.2.13.4.6.4.11.1.3.22.16.2.6.8.2.4.11.6.5.33.11.8.1.10.28.12.1.3.21.2.7.6.1.9.30.17.4.9.15.8.7.3.6.6.7.2.4.1.7.12.13.22.13.2.12.2.10.5.15.2.4.9.4.5.4.7.13.5.15.4.13.4.14.8.2.15.2.5.5.1.2.2.1.2.14.7.4.8.2.9.10.18.12.13.2.18.1.1.3.1.1.9.25.4.1.19.8.4.5.3.5.4.8.4.2.2.2.14.2.13.4.2.6.9.6.3.4.3.5.2.3.6.10.11.6.3.16.3.11.3.1.2.3.9.19.11.15.3.10.7.6.4.3.4.6.3.3.3.3.1.1.1.6.11.3.1.1.11.6.1.10.5.2.6.3.2.2.4.3.2.2.7.15.7.12.2.1.3.3.4.5.4.3.2.2.4.1.3.1.1.1.2.9.1.6.9.1.5.2.1.7.2.8.11.1.3.1.1.2.1.3.2.6.1.12.5.3.1.3.1.1.2.2.7.7.1.4.1.2.6.1.2.1.1.3.1.1.4.1.1.2.1.8.1.7.4.3.2.1.3.5.3.9.6.1.15.10.28.1.2.2.12.3.4.1.6.3.4.7.1.3.1.1.3.1.5.3.1.3.2.2.1.1.4.2.1.2.1.2.2.2.4.2.1.2.2.2.4.1.1.1.2.2.1.1.1.1.2.1.1.1.2.2.1.1.2.1.2.1.7.1.2.1.1.1.2.1.1.1.1.2.1.1.3.2.1.1.8.1.1.1.5.2.1.6.5.1.1.1.1.1.2.2.3.1.1.4.1.1.2.2.1.1.4.3.1.2.2.1.2.1.2.3.1.1.2.4.1.1.1.5.1.3.6.3.1.5.2.3.4.1.2.3.1.4.2.1.2.2.2.1.1.1.1.1.1.11.1.3.1.1.2.2.5.2.3.3.5.1.1.1.4.2.1.1.2.5.1.9.4.1.1.3.1.7.1.4.5.1.7.2.1.1.1.2.1.1.1.4.2.1.12.1.1.3.1.2.2.3.1.2.1.1.1.2.1.1.2.1.1.1.1.2.1.3.1.5.1.2.4.3.8.2.2.9.7.2.3.2.1.4.6.1.1.6.1.1; __qca=P0-1739271107-1659372958351; __gads=ID=c90bf303920e980a-2202d30a47d40006:T=1659372959:RT=1659372959:S=ALNI_MZjFG8u8FMGs6rL3RdQ_VrgxVAq9Q; __gpi=UID=0000078db231ca84:T=1659372959:RT=1659395029:S=ALNI_MbfHAQJ3lgUoVuw3Yfr6uzb-HstpQ; 682de13fa716953be10fec7bc55c8510=3ebcffcf5de0f7b93e4ad9015594857d; __utmc=249660167; __utmb=249660167.1.10.1659395029; __utmt=1',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    })
                params = {
                    'lat': f'51.{random.randint(100000,999999)}60604846',
                    'lng': f'-0.13157844543457034',
                }
                async with session.post('https://postal-code.co.uk/ajax/reverse.php', params=params, timeout=15, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/")) as resp:       
                    response = await resp.text()
                    response = json.loads(response)
                    address = response[0]
                    zipcode = response[2]
            except UnboundLocalError :
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'  
            except TypeError :
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            except aiohttp.client_exceptions.ContentTypeError :
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            try :
                await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nRandom 🔥 Address [↯]\n- - - - - - - - - - - - - - - - - - - - -\nAddress - ↯ <code>{address}</code>\nZip Code - ↯ <code>{zipcode}</code>\n- - - - - - - - - - - - - - - - - - - - -\nChecked by - ↯ {UserName} [{UserStatus}]</b>", reply_to_message_id=message.message_id)
                return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
    try :
        await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nRandom 🔥 Address [↯]\n- - - - - - - - - - - - - - - - - - - - -\nAddress - ↯ <code>{address}</code>\nCity - ↯ <code>{City}</code>\nState - ↯ <code>{State}</code>\nZip Code - ↯ <code>{Zip_Code}</code>\n- - - - - - - - - - - - - - - - - - - - -\nChecked by - ↯ {UserName} [{UserStatus}]</b>", reply_to_message_id=message.message_id)
        return
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
        return

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["gen"])
async def CMDgen(message: types.Message):
    NameGateway = 'Tool 🔥 CCGEN'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('gen')
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
            
    if message.reply_to_message:
        try :
            VerMessage = re.sub("\n", " ", message.reply_to_message.text)
        except TypeError:
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>cc|mon|year|cvv</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
    else :
        VerMessage = re.sub("\n", " ", message.text[5:])
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if re.sub("[^0-9]", "", VerMessage) == '':
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
    inicio = time.time()
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
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
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
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
    try:
        VerMessage = ''.join(['x' if c.isalpha() else c for c in VerMessage])
        VerMessage = re.sub("[^0-9a-zA-Z]", " ", VerMessage)
        matchcc = re.findall(r"\b[0-9a-zA-Z]{6,16}\b", VerMessage)
        l = []
        for cc in matchcc:
            if cc[0:6].isnumeric():
                l.append(cc)
        CCnum = l[0] if l else 'xxxxxx'
    except UnboundLocalError:
        CCnum = 'xxxxxx'
        
    try :
        mes = re.sub("[^0-9]", " ", VerMessage)
        BinCheck = int(CCnum[0:1])
        if 3 <= int(BinCheck) <= 6 :
            if 4 <= int(BinCheck) <= 6 :
                matchmes = re.findall(r"\b(0[1-9]|1[0-2])\b", mes)
                mes = matchmes[0]
            elif int(BinCheck) == 3 :
                matchmes = re.findall(r"\b(0[1-9]|1[0-2])\b", mes)
                mes = matchmes[0]
    except :
            mes = 'xx'
    try :
        ano = re.sub("[^0-9]", " ", VerMessage)
        BinCheck = int(CCnum[0:1])
        if 3 <= int(BinCheck) <= 6 :
            if 4 <= int(BinCheck) <= 6 :
                matchano = re.findall(r"\b(3[0-1]|2[2-9]|202[2-9]|203[0-1])\b", ano)
                ano = matchano[0]
                if len(ano) == 2 :
                    ano = f'20{ano}'
            elif int(BinCheck) == 3 :
                matchano = re.findall(r"\b(3[0-1]|2[2-9]|202[2-9]|203[0-1])\b", ano)
                ano = matchano[0]
                if len(ano) == 2 :
                    ano = f'20{ano}'
    except :
        ano = 'xxxx'
    try :
        cvv = re.sub("[^0-9a-zA-Z]", " ", VerMessage)
        BinCheck = int(CCnum[0:1])
        if 3 <= int(BinCheck) <= 6 :
            if 4 <= int(BinCheck) <= 6 :
                matchcvv = re.findall(r"\b[0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z]\b", cvv.lower())
                cvv = matchcvv[0]
                cvv = re.sub("[^0-9x]", "x", cvv)
                cvv = cvv.ljust(3, 'x')
                cvv = cvv[0:3]
            elif int(BinCheck) == 3 :
                matchcvv = re.findall(r"\b[0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z]\b", cvv.lower())
                cvv = matchcvv[0]
                cvv = re.sub("[^0-9x]", "x", cvv)
                cvv = cvv.ljust(4, 'x')
                cvv = cvv[0:4]
    except :
        cvv = 'rnd'
    try :
        VerMessage = f'{CCnum}|{mes}|{ano}|{cvv}'
    except UnboundLocalError as e:
        print(e)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{VerMessage[0:6]}'")
        result = json.loads(json.dumps(result[0]))
        type = result['type']
        level = result['level']
        brand = result['brand']
        bank = result['bank']
        emoji = result['Emoji']
    except :
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
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if ((brand == 'VISA') or (brand == 'MASTERCARD') or (brand == 'DISCOVER') or (brand == 'AMERICAN EXPRESS')) == False :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nCC ↯ [ <code>{VerMessage[0:6]}</code> ] {brand} [ {emoji} ]\n- - - - - - - - - - - - - - - - - - - - -\n↯ This bot only accepts American, Visa, Mastercard and Discover. ⚠️ ↯\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
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
    if VerMessage:
        from GEN import GeneatedCC
        finalr = str(await GeneatedCC(VerMessage)).split('-')
        listcc = finalr[0]
        extrapcc = finalr[1]

        await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
        result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
        UserStatus =  result['Status']

        if not message.from_user.username: UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>";
        else : UserName = f'@{message.from_user.username}'
        fin = f'{time.time()-inicio}'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        one = InlineKeyboardButton('𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐀𝐠𝐚𝐢𝐧', callback_data="GenerateAgain")
        dos = InlineKeyboardButton('𝐅𝐨𝐫𝐦𝐚𝐭𝐞 𝐌𝐚𝐬𝐬', callback_data="FormateMass")
        tres = InlineKeyboardButton('𝐂𝐥𝐞𝐚𝐧 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 🗑️', callback_data="Finish")
        repmarkup = InlineKeyboardMarkup(row_width=3).add(one,dos).add(tres)
        await bot.send_message(
            chat_id=message.chat.id, 
            text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nInfo - ↯ <code>{brand} - {type} - {level} | {bank} [{emoji}]</code>\n- - - - - - - - - - - - - - - - - - - - -\nBin - ↯ <code>{VerMessage[0:6]}</code> | Time - ↯ <code>{fin[0:5]}s</code>\nInput - ↯ <code>{extrapcc}|{mes}|{ano}|{cvv}</code>\n- - - - - - - - - - - - - - - - - - - - -\n{listcc}- - - - - - - - - - - - - - - - - - - - -\nChecked by - ↯ {UserName} [{UserStatus}]</b>",
            reply_to_message_id=message.message_id,
            reply_markup=repmarkup)
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
        return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",", "#"], commands=["cmds","start"])
async def CMDcmds(message: types.Message):
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='upload_video')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    try:
        result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
        result = json.loads(json.dumps(result[0]))
    except IndexError or TypeError:
            UserSince = datetime.datetime.now().strftime("%d-%m-%Y")
            await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{message.from_user.id}', '{UserSince}')")
            
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))

    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    try :
        one = InlineKeyboardButton('⚾ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 ⚾', callback_data="Gateways")
        two = InlineKeyboardButton('🛠️ 𝐓𝐨𝐨𝐥𝐬 🛠️', callback_data="Tools")
        three = InlineKeyboardButton('🧩 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐂𝐫𝐲𝐩𝐭𝐨 🧩', callback_data="Crypto")
        four = InlineKeyboardButton('𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url="https://t.me/alterchk")
        five = InlineKeyboardButton('𝐅𝐢𝐧𝐢𝐬𝐡', callback_data="Finish")
        repmarkup = InlineKeyboardMarkup(row_width=5).add(one, two, three).add(four,five)
        await bot.send_animation(
            animation='https://thumbs.gfycat.com/FickleShadowyBengaltiger-mobile.mp4',
            chat_id=message.chat.id,
            caption=f"<b><i>Hello, To know my commands press any of the buttons!</i></b>",
            reply_to_message_id=message.message_id,
            reply_markup=repmarkup)
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
        return
    except aiogram.utils.exceptions.BadRequest:
        return
@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["img"])
async def CMDsk(message: types.Message):
    NameGateway = 'Tool 🔥 Random Image'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    WaitStatus = await VerifyStatus('pfw')
    if (WaitStatus[0] == 'OFFLINE ❌') or (WaitStatus[0] == 'OFFLINE1 ❌') :
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {WaitStatus[0]} ]\nFormat: <code>cc|mon|year|cvv</code>\nComment: </b>{WaitStatus[2]}\n<b>Update Since: </b>{WaitStatus[1]}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return

    try :
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
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return

    async def verificar_palabras(cadena: str) -> bool:
        cadena_validada = re.sub('[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ0-9]+', ' ', message.text[5:])
        palabras = cadena_validada.split()
        return len(palabras) > 0
    if not await verificar_palabras(message.text[5:]):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>Random Text</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    VerMessage = re.sub('[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ0-9]+', ' ', message.text[5:])
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    inicio = time.time()
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='upload_photo')
    except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
        await asyncio.sleep(e.value)
        return
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

            repmarkup = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('𝐀𝐥𝐭𝐞𝐫𝐂𝐇𝐊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/alterchk'))
            await bot.send_message(
                chat_id=message.chat.id, 
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{translate} ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_to_message_id=message.message_id,
                reply_markup=repmarkup
            )
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return