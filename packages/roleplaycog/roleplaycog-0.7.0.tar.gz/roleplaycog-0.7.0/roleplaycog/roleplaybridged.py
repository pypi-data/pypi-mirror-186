import discord, json, os
from aiohttp import ClientSession
from discord.ext import commands, bridge
from importlib.metadata import version

__version__ = version("roleplaycog")

description = None
from randseal import Client
client = Client()

class cog(commands.Cog):
	def __init__(self, bot: bridge.Bot):
		self.bot = bot
		if not os.path.exists("database/roleplaydata/characters/"):
			os.makedirs("database/roleplaydata/characters")


	@bridge.bridge_command(description="Shows information about the roleplay extension")
	async def roleplayinfo(self, ctx: bridge.BridgeContext):
		embed = discord.Embed(colour=client.blank, title=f"roleplaycog v{__version__}", description="Welcome to roleplaycog! Lets go through the commands and their usages. (Tip: You can have multi word character names by encasing their name in \", \', or \"\"\".")
		embed.add_field(name="create", value="Creates/edits a character using the given information.", inline=False)
		embed.add_field(name="send", value="Creates a webhook, and sends a message, using it as your character.", inline=False)
		embed.add_field(name="delete", value="Delete a character by name.", inline=False)
		embed.add_field(name="characters", value="Displays an embed containing a list of all your characters.", inline=False)
		embed.add_field(name="show", value="Shows some information about a character.", inline=False)
		if ctx.guild.owner_id == ctx.author.id:
			embed.add_field(name="setlogs", value="Sets a roleplay logging channnel so people don't use their characters to do bad stuff.")
		await ctx.respond(embed=embed, ephemeral=True)


	@bridge.bridge_command(name="create", description="Creates/edits a character")
	async def roleplaycreatechar(self, ctx: bridge.BridgeContext, image_url, name, *, description="No description"):
		if not os.path.exists(f"database/roleplaydata/characters/{ctx.author.id}.json"):
			with open(f"database/roleplaydata/characters/{ctx.author.id}.json", "w") as fuwu:
				json.dump({}, fuwu)
		with open(f"database/roleplaydata/characters/{ctx.author.id}.json") as fr:
			data = json.load(fr)
			with open(f"database/roleplaydata/characters/{ctx.author.id}.json", "w") as fw:
				data.update({f"{name}": {
					"name": name, "image": image_url, "description": description
				}})
				json.dump(data, fw, indent=4)
		webhook = await ctx.channel.create_webhook(name=data[f'{name}']['name'])
		await webhook.send("Hello.", avatar_url=data[f'{name}']['image'], allowed_mentions=discord.AllowedMentions.none())
		await ctx.respond("Done", ephemeral=True)
		await webhook.delete()


	@bridge.bridge_command(name="send", description="Sends a message as your character")
	async def roleplaysendaschar(self, ctx: bridge.BridgeContext, character, *, message):
		if not os.path.exists(f"database/roleplaydata/characters/{ctx.author.id}.json"):
			with open(f"database/roleplaydata/characters/{ctx.author.id}.json", "w") as fuwu:
				json.dump({}, fuwu)
		try:
			with open(f"database/roleplaydata/characters/{ctx.author.id}.json") as f1:
				data = json.load(f1)
				char = await ctx.channel.create_webhook(name=data[f'{character}']['name'])
				await char.send(message, avatar_url=data[f'{character}']['image'])
				await ctx.respond("Sent", ephemeral=True)
				await char.delete()
				if os.path.exists(f"database/roleplaydata/logs.json"):
					with open(f"database/roleplaydata/logs.json") as f2:
						data2 = json.load(f2)
						async with ClientSession() as session:
							webhook = discord.Webhook.from_url(data2[f'{ctx.guild_id}'], session=session)
							embed = discord.Embed(colour=client.blank, title="New roleplay message")
							embed.add_field(name="User", value=str(ctx.author))
							embed.add_field(name="Character", value=character)
							embed.add_field(name="Message", value=message)
							embed.set_thumbnail(url=data[f'{character}']['image'])
							await webhook.send(embed=embed, username=self.bot.user.name, avatar_url=self.bot.user.avatar.url)
		except:
			pass

	
	@bridge.bridge_command(name="delete", description="Deletes a character")
	async def roleplaydeletechar(self, ctx: bridge.BridgeContext, *, character):
		if not os.path.exists(f"database/roleplaydata/characters/{ctx.author.id}.json"):
			with open(f"database/roleplaydata/characters/{ctx.author.id}.json", "w") as fuwu:
				json.dump({}, fuwu)
		try:
			with open(f"database/roleplaydata/characters/{ctx.author.id}.json") as fr:
				data = json.load(fr)
				with open(f"database/roleplaydata/characters/{ctx.author.id}.json", "w") as fw:
					data.update({f"{character}": None})
					await ctx.respond("Done")
					json.dump(data, fw, indent=4)
		except FileNotFoundError:
			await ctx.respond("No such character found")


	@bridge.bridge_command(name="characters", description="Lists all the characters you have")
	async def roleplaydisplaycharacters(self, ctx: bridge.BridgeContext):
		if not os.path.exists(f"database/roleplaydata/characters/{ctx.author.id}.json"):
			with open(f"database/roleplaydata/characters/{ctx.author.id}.json", "w") as fuwu:
				json.dump({}, fuwu)
		embed = discord.Embed(colour=client.blank)
		with open(f"database/roleplaydata/characters/{ctx.author.id}.json") as f:
			data = json.load(f)
			for item in list(data.keys()):
				try:
					embed.add_field(name=data[f'{item}']['name'], value=data[f'{item}']['description'])
				except:
					continue
		await ctx.respond(embed=embed)


	@bridge.bridge_command(name="show", description="Shows a character")
	async def roleplayshowcharacter(self, ctx: bridge.BridgeContext, *, character):
		if not os.path.exists(f"database/roleplaydata/characters/{ctx.author.id}.json"):
			with open(f"database/roleplaydata/characters/{ctx.author.id}.json", "w") as fuwu:
				json.dump({}, fuwu)
		with open(f"database/roleplaydata/characters/{ctx.author.id}.json") as f:
			data = json.load(f)
			embed = discord.Embed(title=data[f'{character}']['name'], colour=client.blank, description=data[f'{character}']['description'])
			embed.set_thumbnail(url=data[f'{character}']['image'])
		await ctx.respond(embed=embed)


	@bridge.bridge_command(name="setlogs", description="Set the logging channel for roleplaying")
	@commands.has_guild_permissions(administrator=True)
	async def roleplaysetlogs(self, ctx: bridge.BridgeContext, channel: discord.TextChannel):
		if not os.path.exists(f"database/roleplaydata/logs.json"):
			with open(f"database/roleplaydata/logs.json", "w") as f:
				json.dump({}, f)
		with open(f"database/roleplaydata/logs.json") as fr:
			data = json.load(fr)
			with open(f"database/roleplaydata/logs.json", "w") as fw:
				webhook = await channel.create_webhook(name=f"{self.bot.user.name} roleplay logs")
				data.update({
					f"{ctx.guild_id}": webhook.url
				})
				json.dump(data, fw)
		await ctx.respond("Set")

def setup(bot: bridge.Bot):
	bot.add_cog(cog(bot))

# python3 -m twine upload --repository pypi dist/* 