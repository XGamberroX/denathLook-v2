from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import config
import sitelook
import logging

# Configuración inicial
config.Config.setup_logging()
logger = logging.getLogger(__name__)

# Inicialización del bot y dispatcher
bot = Bot(token=config.Config.BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Menú inline integrado en el mensaje
def main_menu():
    return InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton("🔍 Analizar Sitio", callback_data='analyze_site'),
        InlineKeyboardButton("💎 Premium", callback_data='premium_info'),
        InlineKeyboardButton("📚 Ayuda", callback_data='help_info'),
        InlineKeyboardButton("📞 Contacto", callback_data='contact_info')
    )

@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    welcome_text = (
        "<b>🖥 WebAnalyzer Bot</b>\n\n"
        "¡Analiza sitios web profesionalmente!\n\n"
        "Usa los botones para interactuar:"
    )
    await message.answer(welcome_text, 
                        reply_markup=main_menu(),
                        parse_mode=types.ParseMode.HTML)

# Manejador de los botones inline
@dp.callback_query_handler(lambda c: c.data in ['analyze_site', 'premium_info', 'help_info', 'contact_info'])
async def process_menu_buttons(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data
    
    if data == 'analyze_site':
        text = "📝 Envía el comando: <code>/st https://tusitio.com</code>"
    elif data == 'premium_info':
        text = "🌟 Ventajas Premium:\n- Prioridad en análisis\n- Límites aumentados"
    elif data == 'help_info':
        text = "ℹ️ Comandos disponibles:\n/st [url] - Análisis completo\n/menu - Muestra este menú"
    elif data == 'contact_info':
        text = "📩 Contacta al soporte: @Asshopx"
    
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, text, parse_mode=types.ParseMode.HTML)

# Registrar handlers
dp.register_message_handler(sitelook.site_handler, commands=['st', 'site'])

if __name__ == '__main__':
    logger.info("Bot iniciado correctamente")
    executor.start_polling(dp, skip_updates=True)