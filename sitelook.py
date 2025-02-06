from aiogram import types
import aiohttp
import asyncio
from config import Config
import logging

logger = logging.getLogger(__name__)

GATEWAYS = {
    'Stripe': ['stripe'],
    'PayPal': ['paypal.com/sdk', 'paypalobjects'],
    'Shopify': ['myshopify.com'],
    'Woocommerce': ['woocommerce'],
    'Braintree': ['braintree'],
    'Authorize.net': ['authorize.net']
}

SECURITY = {
    'Cloudflare': ['CF-RAY'],
    'Akamai': ['akamai'],
    'Sucuri': ['sucuri'],
    'reCaptcha': ['recaptcha']
}

async def fetch_url(session, url):
    try:
        async with session.get(url, timeout=10, ssl=False) as response:
            text = await response.text()
            return text.lower(), response.headers
    except Exception as e:
        raise e

async def site_handler(message: types.Message):
    args = message.text.split()
    if len(args) < 2:
        return await message.answer("❌ Formato incorrecto. Uso: <code>/st https://ejemplo.com</code>", parse_mode=types.ParseMode.HTML)
    
    url = args[1].lower()
    if not url.startswith(('http://', 'https://')):
        url = f'http://{url}'

    try:
        async with aiohttp.ClientSession() as session:
            response_text, headers = await fetch_url(session, url)
            
            # Detectar gateways
            found_gateways = []
            for name, patterns in GATEWAYS.items():
                if any(pattern in response_text for pattern in patterns):
                    found_gateways.append(name)
            
            # Detectar seguridades
            found_security = []
            for name, patterns in SECURITY.items():
                if name == 'reCaptcha':
                    if any(pattern in response_text for pattern in patterns):
                        found_security.append(name)
                else:
                    if any(pattern in headers for pattern in patterns):
                        found_security.append(name)

            # Construir respuesta
            response_msg = [
                "🔍 <b>Resultados del análisis:</b>",
                f"🌐 <b>URL:</b> <code>{url}</code>",
                f"💳 <b>Gateways:</b> {', '.join(found_gateways) if found_gateways else 'No detectados'}",
                f"🛡 <b>Seguridad:</b> {', '.join(found_security) if found_security else 'No detectada'}"
            ]
            
            await message.answer('\n'.join(response_msg), parse_mode=types.ParseMode.HTML)
            logger.info(f"Análisis exitoso para {url}")

    except asyncio.TimeoutError:
        error_msg = "⌛ Tiempo de espera agotado. El sitio no responde."
        await message.answer(error_msg)
        logger.error(f"Timeout para {url}")
    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        await message.answer(error_msg)
        logger.error(f"Error en {url}: {str(e)}", exc_info=True)