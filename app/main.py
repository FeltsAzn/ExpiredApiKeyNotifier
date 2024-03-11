import asyncio

from internal import ExpiredApiKeyNotifierApplication


async def run() -> None:
    app = ExpiredApiKeyNotifierApplication()
    await app.run()


if __name__ == '__main__':
    asyncio.run(run())
