"""Client file"""

from importlib import metadata
import aiohttp
import aiofiles
import io
import json
import asyncio
import random
import advlink
from .errors import two_hundred_error as error
from typing import AsyncIterator, Any, Protocol, overload, Literal
from typing_extensions import Self
from os import PathLike
from aiofiles.threadpool.text import AsyncTextIOWrapper

BLANK: int = 0x2f3136
MAX_NUMBER: int = 82


class FileLike(Protocol): ...

class EmbedLike(Protocol): ...

class Client:
	"""
	The :class:`Client` class for this package.

	Parameters
	-----------

	session: :class:`aiohttp.ClientSession`
		The main session used to obtain seal images (`auto_decompress=False`). You can input this or the package can create one.

	session2: :class:`aiohttp.ClientSession`
		The secondary session that is currently not used for anything. You can input this or the package can create one.

	loop: :class:`asyncio.AbstractEventLoop`
		The loop used for both sessions. You can input this or the package can create one.

	Attributes
	-----------
	blank: :class:`int`
		An :class:`int` that in discord dark mode, is the same as an `Embed`. Will be removed in favor of :constant:`randseal.BLANK` soon.

	Properties
	-----------

	advlink: :class:`advlink.URL`
		An :class:`advlink.URL` containing a seal image url.

	url: :class:`str`
		A simple :class:`str` containing a seal image url.
	
	number: :class:`str`
		A number between 1 and `MAX_NUMBER`, used for getting a seal image by the package.
	"""
	def __init__(self, *, session: aiohttp.ClientSession | None = None, session2: aiohttp.ClientSession | None = None, loop: asyncio.AbstractEventLoop | None = None):
		self.loop = asyncio.get_event_loop() or loop
		self.session = aiohttp.ClientSession(
			auto_decompress=False, loop=self.loop) or session
		self.session2 = aiohttp.ClientSession(loop=self.loop) or session2

	async def File(self, cls: FileLike):
		"""
		Returns a `File` of a seal (new in version 2.0.0, renamed in version 2.4.1)
		"""
		async with self.session.get(self.url) as r:
			if r.status == 200:
				hi = io.BytesIO(await r.read())
				return cls(fp=hi, filename=self.number + ".jpg")
			else:
				raise error

	def Embed(self, cls: EmbedLike):
		"""
		Returns an `Embed` of a seal which can be edited or used in a message (reworked in version 3.0.0)

		Parameters
		-----------

		cls: :class:`EmbedLike`
			A py-cord `File` or a discord.py `File`
		"""
		return cls(colour=BLANK).set_image(url=self.url)


	blank = BLANK

	@overload
	@classmethod
	async def jsonload(cls, fp:
					AsyncTextIOWrapper,
					**kwds,
					) -> dict[str, Any]: ...

	@overload
	@classmethod
	async def jsonload(cls, fp:
					PathLike,
					**kwds,
					) -> dict[str, Any]: ...

	@classmethod
	async def jsonload(cls, fp:
					AsyncTextIOWrapper | PathLike,
					**kwds,
					):
		"""
		Asynchronous `json.load()` using the `aiofiles` package (New in 1.3.0)
		"""
		if isinstance(fp, AsyncTextIOWrapper):
			return json.loads(s=await fp.read(), **kwds)
		else:
			async with aiofiles.open(fp) as f:
				return json.loads(s=await f.read(), **kwds)

	@overload
	@classmethod
	async def jsondump(
		cls,
		obj: dict[str, Any] | Any,
		fp: AsyncTextIOWrapper,
		**kwds
	) -> tuple[str, int]: ...

	@overload
	@classmethod
	async def jsondump(
		cls,
		obj: dict[str, Any] | Any,
		fp: PathLike,
		**kwds
	) -> tuple[str, int]: ...

	@classmethod
	async def jsondump(
			cls,
			obj: dict[str, Any] | Any,
			fp: AsyncTextIOWrapper | PathLike,
			**kwds
	):
		"""
		Asynchronous `json.dump()` using the `aiofiles` package (New in 1.3.0)
		"""
		if isinstance(fp, AsyncTextIOWrapper):
			e = json.dumps(obj, **kwds)
			a = await fp.write(e)
			return (e, a)
		else:
			async with aiofiles.open(fp) as f:
				e = json.dumps(obj, **kwds)
				a = await f.write(e)
				return (e, a)

	def __hash__(self):
		return hash(self)

	def __eq__(self, __o: object):
		return hash(self) == hash(__o)

	def __ne__(self, __o: object):
		return not self.__eq__(__o)

	@property
	def advlink(self):
		"""
		An :class:`advlink.Link` containing a seal image url
		"""
		return advlink.Link(f"https://raw.githubusercontent.com/mariohero24/randsealimgs/main/{self.number}.jpg", session=self.session, session2=self.session2)

	@property
	def url(self):
		"""
		A seal image url
		"""
		return f"https://raw.githubusercontent.com/mariohero24/randsealimgs/main/{self.number}.jpg"


	@property
	def number(self):
		"""
		A seal number
		"""
		return f"{random.randrange(0, MAX_NUMBER)}"

	def __str__(self):
		return f"https://raw.githubusercontent.com/mariohero24/randsealimgs/main/{self.number}.jpg"

	def __int__(self):
		return int(self.number)
		
	@overload
	def urls(self, *, limit: int = MAX_NUMBER, url: Literal[True] = ...) -> AsyncIterator[str]: ...

	@overload
	def urls(self, *, limit: int = MAX_NUMBER, url: Literal[False] = ...) -> AsyncIterator[bytes]: ...

	def urls(self, *, limit: int = MAX_NUMBER, url: bool=True):
		"""
		Returns an :class:`AsyncIterator` for every seal image.

		Parameters
		-----------

		url: :class:`bool`
			If set to ``False``, :class:`bytes` are returned instead of :class:`str`. Defaults to ``True``.
		
		limit: :class:`int`
			How many seal images to return. Defaults to `MAX_NUMBER`.

		Examples
		-----------
		```py
		# Using for loop
		async for url in urls():
			print(url)

		# Flattening into a list. Very slow.
		urlist = await urls().flatten()
		print(urlist)
		```
		"""
		from .iters import imgsITER
		return imgsITER(url=url, session=self.session, limit=limit)

__version__ = metadata.version("randseal")
"""The version of the package"""

# python -m twine upload --repository pypi dist/*