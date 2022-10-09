#!/usr/bin/env python
# pip install python-telegram-bot==v13.14

from telegram.ext import Updater, CommandHandler, MessageHandler
from tok import token
import tok
import logging

# --- запускаем логгирование ----
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

token = tok.token
