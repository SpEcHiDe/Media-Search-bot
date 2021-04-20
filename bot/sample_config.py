#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  GetSongsBot
#  Copyright (C) 2021 The Authors

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.

#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import sys
from dotenv import load_dotenv

# apparently, no error appears even if the path does not exists
try:
    load_dotenv(sys.argv[1])
except IndexError:
    load_dotenv("config.env")


class Config:
    LOGGER = True
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", None)
    # Get these values from my.telegram.org
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
    TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # search chat id
    TG_DUMP_CHAT = int(os.environ.get("TG_DUMP_CHAT", "-100"))
    # path to store log files
    LOG_FILE_ZZGEVC = os.environ.get("LOG_FILE_ZZGEVC", "Media-Search-Bot.log")
    # strings
    PLZ_RATE_TEXT = os.environ.get("PLZ_RATE_TEXT")
    START_TEXT = os.environ.get("START_TEXT")
    LEGAL_DISCLAIMER_TEXT = os.environ.get("LEGAL_DISCLAIMER_TEXT")
    TG_SHARE_TEXT = os.environ.get("TG_SHARE_TEXT")
    SIQ_CC_TEXT = os.environ.get("SIQ_CC_TEXT")
    SIQ_TEXT = os.environ.get("SIQ_TEXT")
    STB_WURF_TEXT = os.environ.get("STB_WURF_TEXT")
    SPT_NTOIQ_TEXT = os.environ.get("SPT_NTOIQ_TEXT")


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
