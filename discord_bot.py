import discord
import os

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()


async def new_star(username):
    activity_channel = client.get_channel(659538118403293194)
    message = discord.Embed(
        title=":star: Github Star :star:",
        type="rich",
        colour=0xffcc00,
        url="https://swaglyrics.dev/"
    )
    message.add_field(name="Hats off to you ", value=f"@{username}", inline=True)
    await activity_channel.send(embed=message)


@client.event
async def on_ready():
    print(f"We are logged in and ready to shine as {client.user}")
    await new_star("@github person")
    activity = discord.Game("with Git")
    await client.change_presence(activity=activity)


client.run(DISCORD_TOKEN)
