#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  GetSongsBot
#  Copyright (C) 2021 The Authors
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


""" init """

# the logging things
import logging
from logging.handlers import RotatingFileHandler
# the secret configuration specific things
from bot.sample_config import Config

# TODO: is there a better way?
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
TG_BOT_SESSION = Config.TG_BOT_SESSION
TG_USER_SESSION = Config.TG_USER_SESSION
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
TG_DUMP_CHAT_S = [
    Config.TG_DUMP_CHAT
]
PLZ_RATE_TEXT = Config.PLZ_RATE_TEXT
START_TEXT = Config.START_TEXT
LEGAL_DISCLAIMER_TEXT = Config.LEGAL_DISCLAIMER_TEXT
TG_SHARE_TEXT = Config.TG_SHARE_TEXT
SIQ_CC_TEXT = Config.SIQ_CC_TEXT
SIQ_TEXT = Config.SIQ_TEXT
STB_WURF_TEXT = Config.STB_WURF_TEXT
SPT_NTOIQ_TEXT = Config.SPT_NTOIQ_TEXT
LOG_FILE_ZZGEVC = Config.LOG_FILE_ZZGEVC


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=20480,
            backupCount=1
        ),
        logging.StreamHandler()
    ]
)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)


# a dictionary to store the currently running processes
AKTIFPERINTAH = {}
# hack :\
TG_BOT_ID = int(TG_BOT_TOKEN.split(":")[0])


from bot.bot import Bot  # noqa: E402
BOT = Bot()
