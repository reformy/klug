import discord
from discord.ext.commands import Bot


app_id = '985188238077616148'
pubkey = 'cc4b986d7c0797b2d05d2181949df5c69a35de95a4e0c82089dcacc0157238bb'
token = 'OTg1MTg4MjM4MDc3NjE2MTQ4.GpCZAy.bBAvcMuX1Tp2Z39-HpiL52ymO0WC2eohC-uIt0'


class KlugBot(Bot):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_command_error(self, context, exception):
        print('on_command_error')
        print(context)
        print(exception)


intents = discord.Intents(messages=True)
bot = KlugBot(command_prefix='++', intents=intents)


@bot.command(name='bal', description='Get your balance')
async def balance(ctx, name: str):
    print(f'balance: {name}')


bot.run(token)
