# randseal
Simple package that can produce a seal image. The image is then output as a `discord.File` or `discord.Embed` for discord.py or py-cord.

### Usage example. Bot can be a commands.Bot in discord.py or a discord.Bot in py-cord.
```py
import randseal
import discord

bot = discord.Bot(intents=discord.Intents.default())
client = randseal.Client()

@bot.command()
async def sealimg(ctx):
  file=await client.asyncFile()
  await ctx.respond(file=file)

@bot.command()
async def sealembed(ctx):
  await ctx.respond(embed=client.Embed())

bot.run("token")
```

This package also contains several utility functions for making discord bots.
