import asyncio
import aiohttp


class Suite:
    def __init__(self, threads=8):
        self.__semaphore = asyncio.Semaphore(threads)
        self.__futures = []
        self.__loop = asyncio.get_event_loop()
        self.__session = aiohttp.ClientSession(loop=self.__loop)

    def run(self):
        results = self.__loop.run_until_complete(self.runner())
        self.__loop.close()
        return results

    async def runner(self):
        async with self.__session:
            return await asyncio.gather(*self.__futures)

    def register(self, func):
        self.__futures.append(func(self.__session, self.__semaphore))

    @property
    def session(self):
        return self.__session
