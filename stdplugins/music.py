"""Emoji

Available Commands:

.music"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "music":

        await event.edit(input_str)

        animation_chars = [
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**",    
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[leo_brown_lee Music Player](tg://user?id=980096541)\n\n⠀⠀⠀⠀**Now Playing:MALAYALAM SONG 1**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n**⠀Next Song:** __ മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ.__\n\n⠀⠀⠀⠀**⠀Device: SAMSUNG SM-B310E**"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])

