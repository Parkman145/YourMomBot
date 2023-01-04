import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(NzU1NjA0MjAzMjEyMjQzMDI0.X2FtQA.w8QDfDj8XS1Ya1r2XYtV38a08U4)
