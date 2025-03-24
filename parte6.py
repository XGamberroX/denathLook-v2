#--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
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
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    else : await ConnectDB.run_query(f"UPDATE pruebas SET ID='{message.from_user.id}' , UltimoCheck={hora_actual} WHERE ID='{message.from_user.id}'")

    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    import os
    import CMDimg
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    archive_jpg = f"Alter「𝑨𝑳𝑮 ﻬ︎」_{random.randint(1,999999)}.jpg"
    text_to_audio = await CMDimg.CMDimg(VerMessage, "http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/", archive_jpg)
    if not (text_to_audio):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>Random Text</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        one = InlineKeyboardButton('𝐀𝐜𝐜𝐞𝐬𝐬 𝐓𝐡𝐞 𝐋𝐢𝐧𝐤 🔗', url=text_to_audio[1])
        dos = InlineKeyboardButton('𝐂𝐥𝐞𝐚𝐧 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 🗑️', callback_data="Finish")
        repmarkup = InlineKeyboardMarkup(row_width=2).add(one,dos)

        async def translate(leng_code, string_to_translate, default_value):
            try:
                from Translate import Translate
                language = leng_code
                lenguage_code = language[0:2].lower()
                return await Translate(lenguage_code, string_to_translate)
            except:
                return default_value

        sr_tr = await translate(message.from_user.language_code, 'Search Results for', 'Search Results for')
        sr_tr2 = await translate(message.from_user.language_code, 'Title', 'Title')
        await bot.send_photo(
            photo=open(archive_jpg, 'rb'),
            chat_id=message.chat.id,
            caption=f"<b>{sr_tr2}:</b> {text_to_audio[0]}\n<b>{sr_tr}:</b> {VerMessage}",
            reply_to_message_id=message.message_id,
            reply_markup=repmarkup)
        os.remove(archive_jpg)
    except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>BadRequest. Check Again!</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    except (aiogram.utils.exceptions.BadRequest):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>Image_process_failed. Check Again!</b>", reply_to_message_id=message.message_id)
            os.remove(archive_jpg)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) :
            return
    except (FileNotFoundError):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>FileNotFoundError. Check Again!</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
           
@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["voz"])
async def CMDsk(message: types.Message):
    NameGateway = 'Tool 🔥 Voice'
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
        cadena_validada = re.sub('[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ]+', ' ', cadena)
        palabras = cadena_validada.split()
        return len(palabras) > 0
    if not await verificar_palabras(message.text[5:]):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>Random Text</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    VerMessage = re.sub('[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ]+', ' ', message.text[5:])
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    inicio = time.time()
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
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
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
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
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    else : await ConnectDB.run_query(f"UPDATE pruebas SET ID='{message.from_user.id}' , UltimoCheck={hora_actual} WHERE ID='{message.from_user.id}'")

    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    import io
    from gtts import gTTS
    import os

    async def text_to_audio(text: str) -> io.BytesIO:
        tts = gTTS(text=text, lang='es')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp

    async def save_audio(audio_data: bytes, audio) -> None:
        with open(audio, 'wb') as f:
            f.write(audio_data)

    async def main(text: str, audio) -> None:
        audio_data = await text_to_audio(text)
        audio_data = audio_data.read()
        await save_audio(audio_data, audio)

        return True
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='upload_voice')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    archive_mp3 = f"Alter「𝑨𝑳𝑮 ﻬ︎」_{random.randint(1,999)}.mp3"
    text_to_audio = await main(VerMessage, archive_mp3)
    if not (text_to_audio):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>Random Text</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        with open(archive_mp3, 'rb') as f:
            await bot.send_audio(message.chat.id, f, caption=VerMessage)
            os.remove(archive_mp3)
    except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
        await asyncio.sleep(e.value)
        return
    
@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["screen"])
async def CMDsk(message: types.Message):
    AccessSTAFF = await AccessAdmin(message.from_user.id)
    if not AccessSTAFF: return
    NameGateway = 'Tool 🔥 SCREENSHOT'
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

    VerMessage = re.sub(r"[\s\n]", "", message.text[7:])
    VerMessage = VerMessage if VerMessage.startswith('https://') else f"https://{VerMessage}"
    async def is_valid_url(url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
    is_valid_url = await is_valid_url(VerMessage)
    if not (is_valid_url):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>https://www.xxxxxx.com/</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
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
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if message.sender_chat:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nYou are forbidden from this bot. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    if message.forward_from:
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nThe use of forwarded messages is prohibited. ⚠️\n- - - - - - - - - - - - - - - - - - - - -</b>", reply_to_message_id=message.message_id)
            return 
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
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
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    else : await ConnectDB.run_query(f"UPDATE pruebas SET ID='{message.from_user.id}' , UltimoCheck={hora_actual} WHERE ID='{message.from_user.id}'")

    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    import asyncio
    from pyppeteer import launch
    from pyppeteer.errors import PageError
    import os
    async def RequestScreenShot(url, ruta):
        logging.getLogger('pyppeteer').setLevel(logging.WARNING)
        try:
            browser = await launch()
            page = await browser.newPage()
            await page.goto(url=url)
            await page.waitFor('body', {'timeout': 5000})
            await page.screenshot({'path': ruta})
            return True
        except PageError:
            return
        finally:
            await browser.close()
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='upload_photo')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    UrlGen = f"ScreenShot{random.randint(1,12)}-{random.randint(1,31)}-{random.randint(1800,2022)}.png"
    if VerMessage.startswith('https://'): url = VerMessage
    else: url = f"https://{VerMessage}"
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    RequestScreenShot = await RequestScreenShot(url=url, ruta=UrlGen)
    if not (RequestScreenShot):
        try :
            await bot.send_message(chat_id=message.chat.id, text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n{NameGateway}\n- - - - - - - - - - - - - - - - - - - - -\nFormat: <code>https://www.xxxxxx.com/</code>\n- - - - - - - - - - - - - - - - - - - - -\n</b>", reply_to_message_id=message.message_id)
            return
        except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
            await asyncio.sleep(e.value)
            return
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    if message.from_user.username == None : username = f"<a href='tg://user?id={message.from_user.id}'>No Username</a>"
    else : username = f'@{message.from_user.username}'
    #--------------------------------- ALTER CHECKER ---------------------------------#
    #--------------------------------- ALTER CHECKER ---------------------------------#
    try :
        one = InlineKeyboardButton('𝐂𝐥𝐞𝐚𝐧 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 🗑️', callback_data="Finish")
        repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
        await bot.send_photo(
            photo=open(UrlGen, 'rb'),
            chat_id=message.chat.id,
            caption=f"<b>↯ Link ↯ {VerMessage}\n↯ Screenshot by ↯ {username}</b>",
            reply_to_message_id=message.message_id,
            reply_markup=repmarkup)
        os.remove(UrlGen)
    except (TimeoutError, exceptions.RetryAfter, aiogram.utils.exceptions.MessageToEditNotFound, aiogram.utils.exceptions.BadRequest) as e:
        await asyncio.sleep(e.value)
        return

@dp.message_handler(commands_prefix=["!", ".", "$", "/", ",","-","#"], commands=["info" ,"myacc", "me","acc"])
async def CMDMyacc(message: types.Message):
    try :
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)

    await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
    if message.reply_to_message != None:
        #print(message.reply_to_message.chat.type, message.reply_to_message.from_user.id, message.reply_to_message.chat.id)
        await CheckPRM(message.reply_to_message.chat.type, message.reply_to_message.from_user.id, message.reply_to_message.chat.id)
        try:
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.reply_to_message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
        except IndexError :
            UserSince = datetime.datetime.now().strftime("%d-%m-%Y")
            await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{message.reply_to_message.from_user.id}', '{UserSince}')")
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.reply_to_message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))

        first_name = message.reply_to_message.from_user.first_name
        last_name = message.reply_to_message.from_user.last_name

        if message.reply_to_message.from_user.username == None : username = f"<a href='tg://user?id={message.reply_to_message.from_user.id}'>No Username</a>"
        else : username = f'@{message.reply_to_message.from_user.username}'
    else :
        #print(message.chat.type, message.from_user.id, message.chat.id)
        await CheckPRM(message.chat.type, message.from_user.id, message.chat.id)
        try:
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
        except IndexError :
            UserSince = datetime.datetime.now().strftime("%d-%m-%Y")
            await ConnectDB.run_query(f"INSERT INTO pruebas (ID, UserSince) VALUES ('{message.from_user.id}', '{UserSince}')")
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
    
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name

        if message.from_user.username == None : username = f"<a href='tg://user?id={message.from_user.id}'>No Username</a>"
        else : username = f'@{message.from_user.username}'

    if first_name == None: first_name = '-'
    if last_name == None: last_name = '-'

    UserID = result['ID']
    Status = result['Status']
    TimeAntiSpam = result['TimeAntiSpam']
    Creditos  = result['Creditos']
    Warnings = result['Warnings']
    UserBanned = result['UserBanned']
    Name = f"{first_name} {last_name}"

    try :
        one = InlineKeyboardButton('𝐌𝐲𝐀𝐜𝐜𝐨𝐮𝐧𝐭', callback_data="myaccount")
        repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
        await bot.send_message(
            chat_id=message.chat.id, 
            text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ UserID: <code>{UserID}</code>\n↯ Name: <code>{Name}</code>\n↯ Status: <code>{Status}</code>\n↯ Credits: <code>{Creditos} credit(s)</code>\n↯ AntiSpam: <code>{TimeAntiSpam}s</code>\n↯ UserName: {username}\n↯ Warnings: <code>{Warnings}</code> | ↯ Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>",
            reply_to_message_id=message.message_id,
            reply_markup=repmarkup)
    except TimeoutError or exceptions.RetryAfter as e:
        await asyncio.sleep(e.value)
        return
    except aiogram.utils.exceptions.CantParseEntities:
        try :
            await bot.send_message(
                chat_id=message.chat.id, 
                text=f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ UserID: <code>{UserID}</code>\n↯ Status: <code>{Status}</code>\n↯ Credits: <code>{Creditos} credit(s)</code>\n↯ AntiSpam: <code>{TimeAntiSpam}s</code>\n↯ UserName: {username}\n↯ Warnings: <code>{Warnings}</code> | ↯ Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_to_message_id=message.message_id,
                reply_markup=repmarkup)
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.MessageToEditNotFound:
            #await asyncio.sleep(e.value)
            return
        except aiogram.utils.exceptions.BadRequest:
            #await asyncio.sleep(e.value)
            return

@dp.callback_query_handler()
async def challenge_callback(callback_query: CallbackQuery) :
    query_data = str(callback_query.data)
    query_id = callback_query.id
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    msg_id = callback_query.message.message_id
    user_name = callback_query.from_user.first_name
    try :
        replyuserid = callback_query.message.reply_to_message.from_user.id
    except AttributeError:
        print("ERROR REPLY USER ID")
        return
        
    if  query_data == 'myaccount' :
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        if callback_query.message.reply_to_message.reply_to_message != None :
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{callback_query.message.reply_to_message.reply_to_message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
            if not callback_query.message.reply_to_message.reply_to_message.from_user.username : username = f"<a href='tg://user?id={callback_query.message.reply_to_message.reply_to_message.from_user.id}'>No Username</a>"
            else : username = f'@{callback_query.message.reply_to_message.reply_to_message.from_user.username}'
            callbackusid = callback_query.message.reply_to_message.reply_to_message.from_user.id

        else :
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{callback_query.message.reply_to_message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))

            if not callback_query.message.reply_to_message.from_user.username : username = f"<a href='tg://user?id={callback_query.message.reply_to_message.from_user.id}'>No Username</a>"
            else : username = f'@{callback_query.message.reply_to_message.from_user.username}'
            callbackusid = callback_query.message.reply_to_message.from_user.id

        CheckPremium = await ConnectDB.run_query(f"SELECT * FROM userpremium WHERE ID='{callbackusid}'")

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
            myaccountmsg = f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ UserID: <code>{UserID}</code>\n↯ Status: <code>{Status}</code>\n↯ NextBilling: <code>{NextBilling}</code> | ↯ Expired in: <code>{remaining_days}</code>\n↯ Credits: <code>{Creditos} credit(s)</code>\n↯ UserName: <b>{username}</b>\n- - - - - - - - - - - - - - - - - - - - -</b>"
        else :
            UserID = result['ID']
            Status = result['Status']
            Creditos  = result['Creditos']
            UserSince = result['UserSince']
            myaccountmsg = f"<b>- - - - - - - - - - - - - - - - - - - - -\n↯ UserID: <code>{UserID}</code>\n↯ Status: <code>{Status}</code>\n↯ Credits: <code>{Creditos} credit(s)</code>\n↯ UserName: <b>{username}</b>\n↯ UserSince: <code>{UserSince}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>"

        try :
            one = InlineKeyboardButton('[ ↩️ ] 𝐑𝐞𝐭𝐮𝐫𝐧', callback_data="Information")
            two = InlineKeyboardButton('𝗙𝗶𝗻𝗶𝘀𝗵', callback_data="Finish")
            repmarkup = InlineKeyboardMarkup(row_width=2).add(one,two)
            await bot.edit_message_text(
                chat_id=chat_id, 
                message_id=msg_id,
                text=myaccountmsg,
                reply_markup=repmarkup)
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
        except aiogram.utils.exceptions.MessageNotModified:
           return

    elif query_data == 'Information' :
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        if callback_query.message.reply_to_message.reply_to_message  != None :
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{callback_query.message.reply_to_message.reply_to_message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
            first_name = callback_query.message.reply_to_message.reply_to_message.from_user.first_name
            last_name = callback_query.message.reply_to_message.reply_to_message.from_user.last_name
            if not first_name: first_name = '-'
            if not last_name: last_name = '-'
            if not callback_query.message.reply_to_message.reply_to_message.from_user.username: username = f"<a href='tg://user?id={callback_query.message.reply_to_message.reply_to_message.from_user.id}'>No Username</a>"
            else : username = f'@{callback_query.message.reply_to_message.reply_to_message.from_user.username}'
        else :
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{callback_query.message.reply_to_message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
            first_name = callback_query.message.reply_to_message.from_user.first_name
            last_name = callback_query.message.reply_to_message.from_user.last_name

            if not first_name: first_name = '-'
            if not last_name: last_name = '-'
            if not callback_query.message.reply_to_message.from_user.username: username = f"<a href='tg://user?id={callback_query.message.reply_to_message.from_user.id}'>No Username</a>"
            else : username = f'@{callback_query.message.reply_to_message.from_user.username}'

        UserID = result['ID']
        Status = result['Status']
        TimeAntiSpam = result['TimeAntiSpam']
        Creditos  = result['Creditos']
        Warnings = result['Warnings']
        UserBanned = result['UserBanned']
        Name = f"{first_name} {last_name}"

        try :
            one = InlineKeyboardButton('𝐌𝐲𝐀𝐜𝐜𝐨𝐮𝐧𝐭', callback_data="myaccount")
            repmarkup = InlineKeyboardMarkup(row_width=1).add(one)
            await bot.edit_message_text(
                chat_id=chat_id, 
                message_id=msg_id,
                text=f'<b>- - - - - - - - - - - - - - - - - - - - -\n↯ UserID: <code>{UserID}</code>\n↯ Name: <code>{Name}</code>\n↯ Status: <code>{Status}</code>\n↯ Credits: <code>{Creditos} credit(s)</code>\n↯ AntiSpam: <code>{TimeAntiSpam}s</code>\n↯ UserName: {username}\n↯ Warnings: <code>{Warnings}</code> | ↯ Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>',
                reply_markup=repmarkup)
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
        except aiogram.utils.exceptions.CantParseEntities:
            try :
                await bot.edit_message_text(
                    chat_id=chat_id, 
                    message_id=msg_id,
                    text=f'<b>- - - - - - - - - - - - - - - - - - - - -\n↯ UserID: <code>{UserID}</code>\n↯ Status: <code>{Status}</code>\n↯ Credits: <code>{Creditos} credit(s)</code>\n↯ AntiSpam: <code>{TimeAntiSpam}s</code>\n↯ UserName: {username}\n↯ Warnings: <code>{Warnings}</code> | ↯ Banned: <code>{UserBanned}</code>\n- - - - - - - - - - - - - - - - - - - - -</b>',
                    reply_markup=repmarkup)
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)
                return
    elif query_data == "Home":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        one = InlineKeyboardButton('⚾ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 ⚾', callback_data="Gateways")
        two = InlineKeyboardButton('🛠️ 𝐓𝐨𝐨𝐥𝐬 🛠️', callback_data="Tools")
        three = InlineKeyboardButton('🧩 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐂𝐫𝐲𝐩𝐭𝐨 🧩', callback_data="Crypto")
        four = InlineKeyboardButton('🍔 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ! 🍔', url="https://t.me/alterchk")
        five = InlineKeyboardButton('𝐅𝐢𝐧𝐢𝐬𝐡 !', callback_data="Finish")
        repmarkup = InlineKeyboardMarkup(row_width=5).add(one, two, three).add(four,five)
        try :
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b><i>Hello, To know my commands press any of the buttons!</i></b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif query_data == "Gateways":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        uno = InlineKeyboardButton('𝐀𝐔𝐓𝐇 𝐆.', callback_data="Auth")
        dos = InlineKeyboardButton('𝐂𝐇𝐀𝐑𝐆𝐄𝐃 𝐆.', callback_data="Charged")
        tres = InlineKeyboardButton('𝐂𝐂𝐍 𝐆.', callback_data="CCN")
        cuatro = InlineKeyboardButton('𝐕𝐁𝐕 𝐆.', callback_data="3D CHK")
        cinco = InlineKeyboardButton('𝐇𝐨𝐦𝐞', callback_data="Home")
        seis = InlineKeyboardButton('𝐌𝐀𝐒𝐒 𝐆.', callback_data="MASS")
        siete = InlineKeyboardButton('𝐅𝐢𝐧𝐢𝐬𝐡', callback_data="Finish")

        try :
            repmarkup = InlineKeyboardMarkup(row_width=7).add(uno,dos,tres,cuatro).add(cinco,seis,siete)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b><i>Hello, To know my commands press any of the buttons!</i></b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif query_data == "Finish":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        try :
            await bot.delete_message(chat_id=chat_id, message_id=msg_id)
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)
        except exceptions.MessageCantBeDeleted :
            print("ERROR IN DELETED")
    elif query_data == "Auth":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='br'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_br = Gateway['Status']
        fecha_br = Gateway['DateOFF']
        comment_br = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='ph'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_st = Gateway['Status']
        fecha_st = Gateway['DateOFF']
        comment_st = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='pfw'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_pfw = Gateway['Status']
        fecha_pfw = Gateway['DateOFF']
        comment_pfw = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='any'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_any = Gateway['Status']
        fecha_any = Gateway['DateOFF']
        comment_any = Gateway['Mensaje']

        uno = InlineKeyboardButton('𝐍𝐞𝐱𝐭 𝐏𝐚𝐠𝐞 [ ➡️ ]', callback_data="NextPage2Auth")
        dos = InlineKeyboardButton('[ 🔙 ] 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬', callback_data="Gateways")
        try :
            repmarkup = InlineKeyboardMarkup(row_width=2).add(uno,dos)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b>Page Number: 1\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Zarek [ Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_br} ]\nFormat: <code>$br cc|mon|year|cvv</code>\nComment: </b>{comment_br}\n<b>Update Since: </b>{fecha_br}\n<b>- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Phoenix [ Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_st} ]\nFormat: <code>$ph cc|mon|year|cvv</code>\nComment: </b>{comment_st}\n<b>Update Since: </b>{fecha_st}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>\n<b>Gateway 🔥 Poseidon [ Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_pfw} ]\nFormat: <code>$pfw cc|mon|year|cvv</code>\nComment: </b>{comment_pfw}\n<b>Update Since: </b>{fecha_pfw}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>\n<b>Gateway 🔥 Adyen [ Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_any} ]\nFormat: <code>$any cc|mon|year|cvv</code>\nComment: </b>{comment_any}\n<b>Update Since: </b>{fecha_any}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif query_data == "NextPage2Auth":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='nashe'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_nashe = Gateway['Status']
        fecha_nashe = Gateway['DateOFF']
        comment_nashe = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='bra'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_bra = Gateway['Status']
        fecha_bra = Gateway['DateOFF']
        comment_bra = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='ci'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_ci = Gateway['Status']
        fecha_ci = Gateway['DateOFF']
        comment_ci = Gateway['Mensaje']
        
        uno = InlineKeyboardButton('[ ↩️ ] 𝐏𝐫𝐞𝐯𝐢𝐨𝐮𝐬 𝐩𝐚𝐠𝐞', callback_data="Auth")
        dos = InlineKeyboardButton('[ 🔙 ] 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬', callback_data="Gateways")
        tres = InlineKeyboardButton('[ ➡️ ] 𝐍𝐞𝐱𝐭 𝐩𝐚𝐠𝐞', callback_data="NextPage3Auth")
        try :
            repmarkup = InlineKeyboardMarkup(row_width=3).add(uno,dos,tres)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b>Page Number: 2\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Nashe [ Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_nashe} ]\nFormat: <code>$nashe cc|mon|year|cvv</code>\nComment: </b>{comment_nashe}\n<b>Update Since: </b>{fecha_nashe}<b>\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Baruch [ Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_bra} ]\nFormat: <code>$bra cc|mon|year|cvv</code>\nComment: </b>{comment_bra}\n<b>Update Since: </b>{fecha_bra}<b>\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Ciclope [ Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_ci} ]\nFormat: <code>$ci cc|mon|year|cvv</code>\nComment: </b>{comment_ci}\n<b>Update Since: </b>{fecha_ci}<b>\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif query_data == "NextPage3Auth":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='ric'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_ric = Gateway['Status']
        fecha_ric = Gateway['DateOFF']
        comment_ric = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='au'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_au = Gateway['Status']
        fecha_au = Gateway['DateOFF']
        comment_au = Gateway['Mensaje']
        uno = InlineKeyboardButton('[ ↩️ ] 𝐏𝐫𝐞𝐯𝐢𝐨𝐮𝐬 𝐩𝐚𝐠𝐞', callback_data="NextPage2Auth")
        dos = InlineKeyboardButton('[ 🔙 ] 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬', callback_data="Gateways")
        try :
            repmarkup = InlineKeyboardMarkup(row_width=2).add(uno,dos)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b>Page Number: 3\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Rygel [ Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_ric} ]\nFormat: <code>$ric cc|mon|year|cvv</code>\nComment: </b>{comment_ric}\n<b>Update Since: </b>{fecha_ric}<b>\n- - - - - - - - - - - - - - - - - - - - -</b>\n<b>Gateway 🔥 Auribe [ Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_au} ]\nFormat: <code>$au cc|mon|year|cvv</code>\nComment: </b>{comment_au}\n<b>Update Since: </b>{fecha_au}<b>\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif query_data == "Charged":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='sb'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_sb = Gateway['Status']
        fecha_sb = Gateway['DateOFF']
        comment_sb = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='saf'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_saf = Gateway['Status']
        fecha_saf = Gateway['DateOFF']
        comment_saf = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='ki'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_ki = Gateway['Status']
        fecha_ki = Gateway['DateOFF']
        comment_ki = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='ab'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_ab = Gateway['Status']
        fecha_ab = Gateway['DateOFF']
        comment_ab = Gateway['Mensaje']

        uno = InlineKeyboardButton('𝐍𝐞𝐱𝐭 𝐏𝐚𝐠𝐞 [ ➡️ ]', callback_data="NextPage2Charged")
        dos = InlineKeyboardButton('[ 🔙 ] 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬', callback_data="Gateways")
        try :
            repmarkup = InlineKeyboardMarkup(row_width=2).add(uno,dos)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b>Page Number: 1\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Anubis [ 15$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_ab} ]\nFormat: <code>$ab cc|mon|year|cvv</code>\nComment: </b>{comment_ab}\n<b>Update Since: </b>{fecha_ab}\n<b>- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Syna [ 15$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_sb} ]\nFormat: <code>$sb cc|mon|year|cvv</code>\nComment: </b>{comment_sb}\n<b>Update Since: </b>{fecha_sb}\n<b>- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Safire [ 8$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_saf} ]\nFormat: <code>$saf cc|mon|year|cvv</code>\nComment: </b>{comment_saf}\n<b>Update Since: </b>{fecha_saf}\n<b>- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Kyu [ 1$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_ki} ]\nFormat: <code>$ki cc|mon|year|cvv</code>\nComment: </b>{comment_ki}\n<b>Update Since: </b>{fecha_ki}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif query_data == "NextPage2Charged":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='rr'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_rr = Gateway['Status']
        fecha_rr = Gateway['DateOFF']
        comment_rr = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='pp'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_pp = Gateway['Status']
        fecha_pp = Gateway['DateOFF']
        comment_pp = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='chk'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_chk = Gateway['Status']
        fecha_chk = Gateway['DateOFF']
        comment_chk = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='kill'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_kill = Gateway['Status']
        fecha_kill = Gateway['DateOFF']
        comment_kill = Gateway['Mensaje']

        uno = InlineKeyboardButton('[ ↩️ ] 𝐏𝐫𝐞𝐯𝐢𝐨𝐮𝐬 𝐩𝐚𝐠𝐞', callback_data="Charged")
        dos = InlineKeyboardButton('[ 🔙 ] 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬', callback_data="Gateways")
        tres = InlineKeyboardButton('[ ➡️ ] 𝐍𝐞𝐱𝐭 𝐩𝐚𝐠𝐞', callback_data="NextPage3Charged")
        try :
            repmarkup = InlineKeyboardMarkup(row_width=3).add(uno,dos,tres)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b>Page Number: 2\nGateway 🔥 Ryuk [ 12$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_rr} ]\nFormat: <code>$rr cc|mon|year|cvv</code>\nComment: </b>{comment_rr}\n<b>Update Since: </b>{fecha_rr}<b>\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Paypal [ 0.01$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_pp} ]\nFormat: <code>$pp cc|mon|year|cvv</code>\nComment: </b>{comment_pp}\n<b>Update Since: </b>{fecha_pp}<b>\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Luxy [ 5$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_chk} ]\nFormat: <code>$chk cc|mon|year|cvv</code>\nComment: </b>{comment_chk}\n<b>Update Since: </b>{fecha_chk}<b>\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Kalaka [ 20$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_kill} ]\nFormat: <code>$kill cc|mon|year|cvv</code>\nComment: </b>{comment_kill}\n<b>Update Since: </b>{fecha_kill}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)


    elif query_data == "NextPage3Charged":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='cys'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_cys = Gateway['Status']
        fecha_cys = Gateway['DateOFF']
        comment_cys = Gateway['Mensaje']

        uno = InlineKeyboardButton('[ ↩️ ] 𝐏𝐫𝐞𝐯𝐢𝐨𝐮𝐬 𝐩𝐚𝐠𝐞', callback_data="NextPage2Charged")
        dos = InlineKeyboardButton('[ 🔙 ] 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬', callback_data="Gateways")
        try :
            repmarkup = InlineKeyboardMarkup(row_width=2).add(uno,dos)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b>Page Number: 3\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Calypso [ 21$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_cys} ]\nFormat: <code>$cys cc|mon|year|cvv</code>\nComment: </b>{comment_cys}\n<b>Update Since: </b>{fecha_cys}<b>\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif query_data == "3D CHK":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='vbv'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_vbv = Gateway['Status']
        fecha_vbv = Gateway['DateOFF']
        comment_vbv = Gateway['Mensaje']

        uno = InlineKeyboardButton('𝐀𝐔𝐓𝐇 𝐆.', callback_data="Auth")
        dos = InlineKeyboardButton('𝐂𝐇𝐀𝐑𝐆𝐄𝐃 𝐆.', callback_data="Charged")
        tres = InlineKeyboardButton('[ 🔙 ] 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬', callback_data="Gateways")
        try :
            repmarkup = InlineKeyboardMarkup(row_width=3).add(uno,dos,tres)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b>- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Braintree [ VBV ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_vbv} ]\nFormat: <code>$vbv cc|mon|year|cvv</code>\nComment: </b>{comment_vbv}\n<b>Update Since: </b>{fecha_vbv}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif query_data == "CCN":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='sy'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_sy = Gateway['Status']
        fecha_sy = Gateway['DateOFF']
        comment_sy = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='pez'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_pez = Gateway['Status']
        fecha_pez = Gateway['DateOFF']
        comment_pez = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='od'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_od = Gateway['Status']
        fecha_od = Gateway['DateOFF']
        comment_od = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='ti'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_ti = Gateway['Status']
        fecha_ti = Gateway['DateOFF']
        comment_ti = Gateway['Mensaje']

        uno = InlineKeyboardButton('𝐀𝐔𝐓𝐇 𝐆.', callback_data="Auth")
        dos = InlineKeyboardButton('𝐂𝐇𝐀𝐑𝐆𝐄𝐃 𝐆.', callback_data="Charged")
        tres = InlineKeyboardButton('[ 🔙 ] 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬', callback_data="Gateways")
        try :
            repmarkup = InlineKeyboardMarkup(row_width=3).add(uno,dos,tres)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b>Page Number: 1\nGateway 🔥 Syberus [ CCN - 5$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_sy} ]\nFormat: <code>$sy cc|mon|year|cvv</code>\nComment: </b>{comment_sy}\n<b>Update Since: </b>{fecha_sy}<b>\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Pezcary [ CCN - Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_pez} ]\nFormat: <code>$pez cc|mon|year|cvv</code>\nComment: </b>{comment_pez}\n<b>Update Since: </b>{fecha_pez}<b>\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Olimpo [ CCN - Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_od} ]\nFormat: <code>$od cc|mon|year|cvv</code>\nComment: </b>{comment_od}\n<b>Update Since: </b>{fecha_od}<b>\n- - - - - - - - - - - - - - - - - - - - -</b>\n<b>Gateway 🔥 Tilin [ CCN - 10$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_ti} ]\nFormat: <code>$ti cc|mon|year|cvv</code>\nComment: </b>{comment_ti}\n<b>Update Since: </b>{fecha_ti}<b>\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif query_data == "MASS":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='masstr'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_masstr = Gateway['Status']
        fecha_masstr = Gateway['DateOFF']
        comment_masstr = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='masscn'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_masscn = Gateway['Status']
        fecha_masscn = Gateway['DateOFF']
        comment_masscn = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='massop'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_massop = Gateway['Status']
        fecha_massop = Gateway['DateOFF']
        comment_massop = Gateway['Mensaje']

        uno = InlineKeyboardButton('𝐀𝐔𝐓𝐇 𝐆.', callback_data="Auth")
        dos = InlineKeyboardButton('𝐂𝐇𝐀𝐑𝐆𝐄𝐃 𝐆.', callback_data="Charged")
        tres = InlineKeyboardButton('[ 🔙 ] 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬', callback_data="Gateways")
        
        try :
            repmarkup = InlineKeyboardMarkup(row_width=3).add(uno,dos,tres)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b>Page Number: 1\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Mass Stripe [ CCN - 5$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_masstr} ]\nFormat: <code>$masstr cc|mon|year|cvv</code>\nComment: </b>{comment_masstr}\n<b>Update Since: </b>{fecha_masstr}<b>\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Mass Unknown [ CCN - 1$ ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_masscn} ]\nFormat: <code>$masscn cc|mon|year|cvv</code>\nComment: </b>{comment_masscn}\n<b>Update Since: </b>{fecha_masscn}<b>\n- - - - - - - - - - - - - - - - - - - - -\nGateway 🔥 Mass Unknown [ CCN Auth ]\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_massop} ]\nFormat: <code>$massop cc|mon|year|cvv</code>\nComment: </b>{comment_massop}\n<b>Update Since: </b>{fecha_massop}<b>\n- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif query_data == "Tools":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='bin'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_bin = Gateway['Status']
        fecha_bin = Gateway['DateOFF']
        comment_bin  = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='gen'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_gen = Gateway['Status']
        fecha_gen = Gateway['DateOFF']
        comment_gen = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='sk'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_sk = Gateway['Status']
        fecha_sk = Gateway['DateOFF']
        comment_sk = Gateway['Mensaje']

        GatewaysSearch =  await ConnectDB.run_query(f"SELECT * FROM Gateways WHERE Name='dd'")
        Gateway = json.loads(json.dumps(GatewaysSearch[0]))
        status_dd = Gateway['Status']
        fecha_dd = Gateway['DateOFF']
        comment_dd = Gateway['Mensaje']

        uno = InlineKeyboardButton('[ 🔙 ] 𝐇𝐨𝐦𝐞', callback_data="Home")
        try :
            repmarkup = InlineKeyboardMarkup(row_width=1).add(uno)
            await bot.edit_message_caption(
                chat_id=chat_id, 
                message_id=msg_id,
                caption=f"<b>- - - - - - - - - - - - - - - - - - - - -\nTool 🔥 SK CHECK\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_sk} ]\nFormat: <code>$sk sk_live_</code>\nComment: </b>{comment_sk}\n<b>Update Since: </b>{fecha_sk}\n<b>- - - - - - - - - - - - - - - - - - - - -\nTool 🔥 CCGEN\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_gen} ]\nFormat: <code>$gen cc|mon|year|cvv</code>\nComment: </b>{comment_gen}\n<b>Update Since: </b>{fecha_gen}\n<b>- - - - - - - - - - - - - - - - - - - - -\nTool 🔥 BIN LOOKUP\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_bin} ]\nFormat: <code>$bin xxxxxx</code>\nComment: </b>{comment_bin}\n<b>Update Since: </b>{fecha_bin}\n<b>- - - - - - - - - - - - - - - - - - - - -\nTool 🔥 RANDOM ADDRESS\n- - - - - - - - - - - - - - - - - - - - -\nSTATUS [ {status_dd} ]\nFormat: <code>$dd US, CA, UK</code>\nComment: </b>{comment_dd}\n<b>Update Since: </b>{fecha_dd}\n<b>- - - - - - - - - - - - - - - - - - - - -</b>",
                reply_markup=repmarkup)
            return
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

    elif  query_data == 'GenerateAgain' :
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        if callback_query.message.reply_to_message.reply_to_message: VerMessage = re.sub("\n", " ", callback_query.message.reply_to_message.reply_to_message.text)
        else : VerMessage = re.sub("\n", " ", callback_query.message.reply_to_message.text[5:])

        try :
            VerMessage = re.sub("[^0-9a-zA-Z]", " ", VerMessage)
            matchcc = re.findall(r"\b[0-9a-zA-Z]{6,16}\b", VerMessage)
            for i in matchcc :
                i = matchcc
            l = i
            for x in range(len(l)) :
                list_= l[x]
                if  list_[0:6].isnumeric() :
                    CCnum=list_
        except : CCnum = 'xxxxxx'
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
        except : mes = 'xx'
        try:
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
        except : ano = 'xxxx'
        try:
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
        except : cvv = 'rnd'
        VerMessage = f'{CCnum}|{mes}|{ano}|{cvv}'

        try :
            result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{VerMessage[0:6]}'")
            result = json.loads(json.dumps(result[0]))
            type = result['type']
            level = result['level']
            brand = result['brand']
            bank = result['bank']
            emoji = result['Emoji']
        except : return "ERROR"

        try:
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{callback_query.message.reply_to_message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
        except IndexError : return "ERROR SEARCHING USER ID"

        if VerMessage:
            from GEN import GeneatedCC

            finalr = str(await GeneatedCC(VerMessage)).split('-')
            listcc = finalr[0]
            extrapcc = finalr[1]

            result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{callback_query.message.reply_to_message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
            UserStatus =  result['Status']

            if callback_query.message.reply_to_message.from_user.username == None :
                UserName = f"<a href='tg://user?id={callback_query.message.reply_to_message.from_user.id}'>{callback_query.message.reply_to_message.from_user.first_name}</a>";
            else :
                UserName = f'@{callback_query.message.reply_to_message.from_user.username}'

            await CheckPRM(callback_query.message.reply_to_message.chat.type, callback_query.message.reply_to_message.from_user.id, callback_query.message.reply_to_message.chat.id)

            fin = '0.100'

            try :
                one = InlineKeyboardButton('𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐀𝐠𝐚𝐢𝐧', callback_data="GenerateAgain")
                dos = InlineKeyboardButton('𝐅𝐨𝐫𝐦𝐚𝐭𝐞 𝐌𝐚𝐬𝐬', callback_data="FormateMass")
                tres = InlineKeyboardButton('𝐂𝐥𝐞𝐚𝐧 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 🗑️', callback_data="Finish")
                repmarkup = InlineKeyboardMarkup(row_width=3).add(one,dos).add(tres)
                await bot.edit_message_text(
                    chat_id=chat_id, 
                    message_id=msg_id,
                    text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nInfo - ↯ <code>{brand} - {type} - {level} | {bank} [{emoji}]</code>\n- - - - - - - - - - - - - - - - - - - - -\nBin - ↯ <code>{VerMessage[0:6]}</code> | Time - ↯ <code>{fin[0:5]}s</code>\nInput - ↯ <code>{extrapcc}|{mes}|{ano}|{cvv}</code>\n- - - - - - - - - - - - - - - - - - - - -\n{listcc}- - - - - - - - - - - - - - - - - - - - -\nChecked by - ↯ {UserName} [{UserStatus}]</b>",
                    reply_markup=repmarkup)
                #return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)

    elif  query_data == 'FormateMass' :
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        if callback_query.message.reply_to_message.reply_to_message: VerMessage = re.sub("\n", " ", callback_query.message.reply_to_message.reply_to_message.text)
        else : VerMessage = re.sub("\n", " ", callback_query.message.reply_to_message.text[5:])

        try :
            VerMessage = re.sub("[^0-9a-zA-Z]", " ", VerMessage)
            matchcc = re.findall(r"\b[0-9a-zA-Z]{6,16}\b", VerMessage)
            for i in matchcc :
                i = matchcc
            l = i
            for x in range(len(l)) :
                list_= l[x]
                if  list_[0:6].isnumeric() :
                    CCnum=list_
        except : CCnum = 'xxxxxx'
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
        except : mes = 'xx'
        try:
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
        except : ano = 'xxxx'
        try:
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
        except : cvv = 'rnd'
        VerMessage = f'{CCnum}|{mes}|{ano}|{cvv}'

        try :
            result = await ConnectDB.run_query(f"SELECT * FROM bins WHERE bin='{VerMessage[0:6]}'")
            result = json.loads(json.dumps(result[0]))
            type = result['type']
            level = result['level']
            brand = result['brand']
            bank = result['bank']
            emoji = result['Emoji']
        except : return "ERROR"

        try:
            result = await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{callback_query.message.reply_to_message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
        except IndexError : return "ERROR SEARCHING USER ID"

        if VerMessage:
            from GEN import GeneatedCC

            finalr = str(await GeneatedCC(VerMessage)).split('-')
            listcc = finalr[0]
            extrapcc = finalr[1]

            result =  await ConnectDB.run_query(f"SELECT * FROM pruebas WHERE ID='{callback_query.message.reply_to_message.from_user.id}'")
            result = json.loads(json.dumps(result[0]))
            UserStatus =  result['Status']

            if callback_query.message.reply_to_message.from_user.username == None :
                UserName = f"<a href='tg://user?id={callback_query.message.reply_to_message.from_user.id}'>{callback_query.message.reply_to_message.from_user.first_name}</a>";
            else :
                UserName = f'@{callback_query.message.reply_to_message.from_user.username}'

            await CheckPRM(callback_query.message.reply_to_message.chat.type, callback_query.message.reply_to_message.from_user.id, callback_query.message.reply_to_message.chat.id)

            fin = '0.100'

            try :
                one = InlineKeyboardButton('𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐀𝐠𝐚𝐢𝐧 [𝐌𝐚𝐬𝐬]', callback_data="FormateMass")
                dos = InlineKeyboardButton('𝐅𝐨𝐫𝐦𝐚𝐭𝐞 𝐍𝐨𝐫𝐦𝐚𝐥', callback_data="GenerateAgain")
                tres = InlineKeyboardButton('𝐂𝐥𝐞𝐚𝐧 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 🗑️', callback_data="Finish")
                repmarkup = InlineKeyboardMarkup(row_width=3).add(one,dos).add(tres)
                await bot.edit_message_text(
                    chat_id=chat_id, 
                    message_id=msg_id,
                    text=f"<b>- - - - - - - - - - - - - - - - - - - - -\nInfo - ↯ <code>{brand} - {type} - {level} | {bank} [{emoji}]</code>\n- - - - - - - - - - - - - - - - - - - - -\nBin - ↯ <code>{VerMessage[0:6]}</code> | Time - ↯ <code>{fin[0:5]}s</code>\nInput - ↯ <code>{extrapcc}|{mes}|{ano}|{cvv}</code>\n- - - - - - - - - - - - - - - - - - - - -\n<code>{listcc}</code>- - - - - - - - - - - - - - - - - - - - -\nChecked by - ↯ {UserName} [{UserStatus}]</b>",
                    reply_markup=repmarkup)
                #return
            except TimeoutError or exceptions.RetryAfter as e:
                await asyncio.sleep(e.value)

    elif query_data == "Finish":
        if replyuserid != user_id :
            await callback_query.answer("Oops, Access Denied, you are not the one using this command. ⚠️", show_alert=True)
            return
        try :
            await bot.delete_message(chat_id=chat_id, message_id=msg_id)
        except TimeoutError or exceptions.RetryAfter as e:
            await asyncio.sleep(e.value)

if __name__ == '__main__':
    executor.start_polling(dp)
