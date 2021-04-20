#  MIT License
#
#  Copyright (c) 2019-2021 Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person
#  obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software
#  without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be
#  included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
#  THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# First we need the asyncio library
import asyncio
import importlib
from bot import (
    LOGGER,
    BOT
)
from bot.plugins import ALL_MODULES


async def main():
    await BOT.start()
    IMPORTED = {}
    for module_name in ALL_MODULES:
        imported_module = importlib.import_module("bot.plugins." + module_name)
        if not hasattr(imported_module, "__mod_name__"):
            imported_module.__mod_name__ = imported_module.__name__
        if not imported_module.__mod_name__.lower() in IMPORTED:
            IMPORTED[imported_module.__mod_name__.lower()] = imported_module
        else:
            raise Exception(
                "Can't have two modules with the same name! Please change one"
            )
    LOGGER(__name__).info("Successfully loaded modules: " + str(ALL_MODULES))
    #
    await BOT.run_until_disconnected()


if __name__ == '__main__':
    LOGGER(__name__).info("Successfully loaded modules: " + str(ALL_MODULES))
    # Then we need a loop to work with
    loop = asyncio.get_event_loop()
    # Then, we need to run the loop with a task
    loop.run_until_complete(main())
