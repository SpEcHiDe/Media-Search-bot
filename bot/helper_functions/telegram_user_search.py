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


from telethon import Button, events, TelegramClient
from bot import TG_DUMP_CHAT_S
from bot.helper_functions.human_bytes import humanbytes


async def search_tg(
    _u: TelegramClient,
    _b: TelegramClient,
    event: events.InlineQuery.Event,
    sqr: str,
    astr: int,
    lmtn: int
):
    TG_DB_CHAT = TG_DUMP_CHAT_S[0]
    mtls = await _u.get_messages(
        entity=TG_DB_CHAT,
        limit=lmtn,
        offset_id=astr,
        search=sqr
    )
    t_r = mtls.total
    search_results = []
    __tmp_id_s = []
    for mt_ls in mtls:
        if mt_ls.id in __tmp_id_s:
            continue
        sltm = await _b.get_messages(
            entity=TG_DB_CHAT,
            ids=mt_ls.id
        )
        if sltm and sltm.reply_to_msg_id:
            sltm = await sltm.get_reply_message()
        if (
            sltm and
            sltm.document
        ):
            search_results.append(
                get_apprt_bldr(event, sqr, sltm)
            )
            __tmp_id_s.append(sltm.id)
    return search_results, mtls, t_r


def get_apprt_bldr(event, sqr, sltm):
    builder = event.builder
    caption = sltm.text
    description = sltm.raw_text
    hfs = humanbytes(sltm.file.size)
    if (
        caption and
        "#ID_" in caption
    ):
        caption = None
        description = None
    elif caption:
        caption = sltm.text
        description = sltm.raw_text
    title = (
        sltm.file.name or
        " "
    )
    description = (
        description or
        " "
    )
    description = f"{hfs} |{description}"
    return builder.document(
        file=sltm.media,
        title=title,
        description=description,
        text=caption,
        buttons=[Button.switch_inline(
            text="Search Again",
            query=sqr,
            same_peer=True
        )]
    )
