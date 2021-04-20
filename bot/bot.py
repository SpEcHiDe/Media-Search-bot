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


""" MtProto Bot """

from telethon import TelegramClient, __version__
from bot import (
    API_HASH,
    APP_ID,
    TG_BOT_TOKEN,
    TG_BOT_SESSION,
    LOGGER
)
from bot.user import User


class Bot(TelegramClient):
    """ modded client for GetSongsBot """
    USER = None

    def __init__(self):
        super().__init__(
            TG_BOT_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            base_logger=LOGGER(__name__)
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start(bot_token=TG_BOT_TOKEN)
        usr_bot_me = await self.get_me()
        # set HTML as the default parse_mode
        # ref: https://t.me/c/1311056733/88748
        self.parse_mode = "html"
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Telethon v{__version__} started."
        )
        self.USER = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
