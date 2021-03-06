from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    meigen = {
        0: "ごめんなさいね～",
        1: "赤ちゃんだからね",
        2: "はいはいそうだね",
        3: "67さんの負け～",
        4: "人狼かっ!?",
    }
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    if message.content == '/maryo':
        await message.channel.send("test")
        await message.channel.send(f"{random.randrange(5)}"])

@client.event
async def on_voice_state_update(member, before, after):
    alert_channel = client.get_channel(785246159978364938)
    if before.channel is None: 
        msg = f'{member.name} が入室しました。'
        await alert_channel.send(msg)
    # elif after.channel is None: 
    #     msg = f'{member.name} が退室しました。'
    #     await alert_channel.send(msg)


bot.run(token)
