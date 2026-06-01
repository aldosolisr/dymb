# dytb (Discord Youtube Music Bot)

This is an experimental discord bot that plays music from Youtube!

It is not functional yet, but it is capable of playing one song, yes just one song but it kind
of works. 

This is version 0.0.1

## How to configure
Create a .env file inside the directory and add the following

```
DISCORD_TOKEN=your_discord_token

# replace !pico for the prefix of your preference
BOT_PREFIX=!pico
```

The discord token is obtained from the [discord developer portal](https://discord.com/developers/home)
webpage, follow the instructions there to create an app.

## Usage

Run it 
```
uv run main.py
```

At the discord channel
```
!pico play youtube_video_url
```

For now this is the only command that is implemented on this version of the 
program, more commands are to be expected.


