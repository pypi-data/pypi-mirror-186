"""Removed features"""

import discord, io, random, aiohttp, asyncio
from client import Client


class archiveClient(Client):
	"""A subclass of `Client`. Only features that have been reworked or removed are different."""
	def __init__(self, session: aiohttp.ClientSession | None = None, session2: aiohttp.ClientSession | None = None):
		super().__init__(session, session2)

	def File():
		import requests
		sealrand = f"{random.randrange(0, 82)}"
		r = requests.get(
			f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg", stream=True)
		return discord.File(fp=io.BytesIO(r.content), filename=sealrand + ".jpg")

archiveClient

none = None
false: bool = False
true: bool = True
null = None