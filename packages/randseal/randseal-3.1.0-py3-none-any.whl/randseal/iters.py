import asyncio, aiohttp
from typing import Literal, overload

class imgsITER:
	def __init__(self, *, session: aiohttp.ClientSession, url: bool, limit: int):
		self.number = 0
		self.session = session
		self.url = url
		self.limit = limit

	def __aiter__(self):
		return self

	async def __anext__(self):
		if self.number >= self.limit:
			raise StopAsyncIteration
		self.number += 1
		async with self.session.get(f"https://raw.githubusercontent.com/mariohero24/randsealimgs/main/{self.number}.jpg") as r:
			if r.status == 200:
				if self.url:
					return f"https://raw.githubusercontent.com/mariohero24/randsealimgs/main/{self.number}.jpg"
				else:
					byte = await r.read()
					return byte

	@overload
	async def flatten(self, tupl: Literal[False] = ...) -> list: ...

	@overload
	async def flatten(self, tupl: Literal[True] = ...) -> tuple: ...

	async def flatten(self, tupl: bool=False) -> tuple | list:
		l = []
		for e in range(self.limit):
			a = await self.__anext__()
			l.append(a)
		else:
			if not tupl:
				return l
			else:
				tup = tuple(l)
				return tup
			