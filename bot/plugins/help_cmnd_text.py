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


from telethon import events, Button
from bot import (
    PLZ_RATE_TEXT,
    START_TEXT,
    LEGAL_DISCLAIMER_TEXT,
    SIQ_CC_TEXT,
    SIQ_TEXT,
    STB_WURF_TEXT,
    TG_SHARE_TEXT,
    TG_BOT_ID
)
from bot import BOT


@BOT.on(
    events.NewMessage
)
async def _(evt: events.NewMessage.Event):
    if evt.via_bot_id and evt.via_bot_id == TG_BOT_ID:
        return

    if not evt.is_private:
        return

    if evt.file:
        return

    if evt.raw_text.startswith("/start "):
        return

    if evt.raw_text.startswith("/start"):
        share_text = TG_SHARE_TEXT
        share_url = (
            "https://t.me"
            f"/share/url?url={share_text}"
        )
        await evt.reply(
            START_TEXT,
            buttons=[
                [
                    Button.switch_inline(
                        text=SIQ_CC_TEXT,
                        query="",
                        same_peer=True
                    ),
                    Button.switch_inline(
                        text=SIQ_TEXT,
                        query="",
                        same_peer=False
                    )
                ],
                [
                    Button.url(
                        text=STB_WURF_TEXT,
                        url=share_url
                    )
                ]
            ]
        )
        return

    if evt.raw_text.startswith("/rate"):
        await evt.reply(
            PLZ_RATE_TEXT,
            link_preview=False
        )
        return

    if evt.raw_text.startswith(
        ("/legal_disclaimer", "/dmca")
    ):
        await evt.reply(
            LEGAL_DISCLAIMER_TEXT,
            link_preview=True
        )
        return
