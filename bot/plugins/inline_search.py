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


from telethon import events
from telethon.errors import (
    QueryIdInvalidError
)
from bot import BOT, SPT_NTOIQ_TEXT
from bot.helper_functions.telegram_user_search import (
    search_tg
)


@BOT.on(
    events.InlineQuery
)
async def handler(event: events.InlineQuery.Event):
    start_at = int(event.query.offset or 0)
    limit = 9
    new_offset = str(start_at + limit)
    search_query = event.query.query
    search_results = []
    switch_pm_text_s = ""
    cache_time = 54321
    if search_query.strip() != "":
        search_results, usr_srch_reslts, rtbt = await search_tg(
            event.client.USER,
            event.client,
            event,
            search_query,
            start_at,
            limit
        )
        if len(usr_srch_reslts) > 0:
            new_offset = str(usr_srch_reslts[-1].id)
        len_srch_ress = len(search_results)
        switch_pm_text_s = (
            f"Found {len_srch_ress} / {rtbt} "
            f"results for {search_query}"
        )
    else:
        switch_pm_text_s = SPT_NTOIQ_TEXT
    if len(search_results) <= 0:
        new_offset = None
    try:
        await event.answer(
            results=search_results,
            cache_time=cache_time,
            gallery=False,
            next_offset=new_offset,
            private=False,
            switch_pm=switch_pm_text_s,
            switch_pm_param="inline",
        )
    except QueryIdInvalidError:
        await event.answer(
            results=[],
            cache_time=cache_time,
            gallery=False,
            next_offset=None,
            private=False,
            switch_pm=(
                "search servers are busy, "
                "please try again after sometime"
            ),
            switch_pm_param="toolongxtion",
        )

