from dotenv import load_dotenv
import asyncio
import discord
import os
import yt_dlp

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
bot_prefix = os.getenv("BOT_PREFIX")
ydl_opts = {
    # TODO add functionality for playlist
    # at least extract the first song of the playlist
    'extract_flat': False,
    'forceurl': True,
    'playlist_items': '1:1',
    'fragment_retries': 10,
    'ignoreerrors': 'only_download',
    'noprogress': True,
    'postprocessors': [{'key': 'FFmpegConcat',
                        'only_multi_video': True,
                        'when': 'playlist'}],
    'quiet': True,
    'default_search': 'auto',
    'retries': 10,
    'simulate': True,
    'warn_when_outdated': True
}
FFMPEG_OPTIONS = {
    "before_options": (
        "-reconnect 1 "
        "-reconnect_streamed 1 "
        "-reconnect_delay_max 30"
    ),
    "options": "-vn"
}


# TODO restrucure the class to set queue, current_song, is_playing, voice_client,
#      as propierties
class dymb(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def search_song(self, argument):
        url = argument
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url)

    # TODO add queue, and clean the function
    async def play_song(self, message, song):
        if song == "":
            await message.channel.send("No song especified\nUsage:!pico play song-name")
            return

        # join the discord channel
        voice_client = await message.author.voice.channel.connect()

        def after_song(error):
            if error:
                print(error)
            asyncio.run_coroutine_threadsafe(
                voice_client.disconnect(),
                self.loop
            )

        await message.channel.send(f"Adding '{song}' to the song queue!")
        url = await self.search_song(song)

        # TODO implement queue
        # TODO verify that this works with every query
        if 'formats' in url:
            for _format in url['formats']:
                if _format['resolution'] == 'audio only':
                    url = _format['url']
                    print(url)

        if 'entries' in url:
            for entry in url['entries']:
                for _format in entry['requested_formats']:
                    if _format['resolution'] == 'audio only':
                        url = _format['url']
                        print(url)

        voice_client.play(discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS), after=after_song)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(bot_prefix):
            # get the command in the form
            # ["command", "all the other arguments"]
            user_input = message.content.removeprefix(bot_prefix).strip().split(" ", 1)
            command = user_input[0]
            argument = user_input[1] if len(user_input) > 1 else ""

            print(f"Recieved command: {command}")
            print(f"Recieved argument: {argument}")
            match command:
                case "play":
                    await self.play_song(message, argument)
                case "skip":
                    await message.channel.send("skip to be implemented")
                case "list", "queue":
                    await message.channel.send("pause to be implemented")
                case _:
                    await message.channel.send(f"command: '{command}' unknown")
                    await message.channel.send("commands avaible: play, skip, pause")


def main():
    print("Hello from dymb!")
    intents = discord.Intents.default()
    intents.message_content = True

    client = dymb(intents=intents)
    client.run(discord_token)


if __name__ == "__main__":
    main()
