# dytb (Discord Youtube Music Bot)

This is an experimental discord bot that plays music from Youtube and Youtube Music!

it is capable of searching and playing songs by the name and url.

This version is still experimental, so errors are to be expected. 

## Currently avaible commands

* play 

## Commands to be implemented

* skip (skips a song)
* pause (pauses the song)
* queue (list the queue)

## Features to be implemented

* Queue


This is version 0.0.2

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


