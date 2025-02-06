import logging

class Config:
    PREMIUM_USERS = {5927555659,}  # Reemplaza con tus IDs
    ADMIN_ID = 5927555659  # ID del administrador
    OWNER_ID = 5927555659 # ID del propietario
    BOT_TOKEN = "7756492352:AAGN91eRfnWf2WU8h_Ip1NH2wZ7-9NLuBP8"
    
    @staticmethod
    def setup_logging():
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler("bot.log"),
                logging.StreamHandler()
            ]
        )
        logging.getLogger('aiogram').setLevel(logging.WARNING)
