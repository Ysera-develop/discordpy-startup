from discord.ext import commands
import os
import traceback

CHANNEL_ID = 672412611765338124

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
channel = client.get_channel(CHANNEL_ID)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def e8s(ctx):
    await cannel.send("./e8s.txt")


bot.run(token)
