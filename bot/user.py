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


""" MtProto User """

import re
from telethon import TelegramClient, __version__
from telethon.sessions import StringSession
from bot import (
    API_HASH,
    APP_ID,
    TG_USER_SESSION,
    LOGGER
)


class User(TelegramClient):
    """ modded client for GetSongsUser """

    def __init__(self):
        session_name = TG_USER_SESSION
        if session_name == ":memory:" or len(session_name) > 17:
            session_name = re.sub(r"[\n\s]+]", "", session_name)
            session_name = StringSession(session_name)
        super().__init__(
            session_name,
            api_hash=API_HASH,
            api_id=APP_ID,
            base_logger=LOGGER(__name__)
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        # set HTML as the default parse_mode
        # ref: https://t.me/c/1311056733/88748
        self.parse_mode = "html"
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on TeleThon v{__version__} started."
        )
        return self

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("User stopped. Bye.")
