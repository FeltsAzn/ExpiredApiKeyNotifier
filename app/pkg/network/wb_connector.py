import asyncio
from datetime import datetime

from aiohttp import ClientSession
from fake_useragent import UserAgent

from pkg.network.tools import retry, get_proxy


class WildBerriesNetworkConnector:
    url = "https://statistics-api.wildberries.ru/api/v1/supplier/stocks?dateFrom={current_date}"

    def __init__(self) -> None:
        self._semaphore = asyncio.Semaphore(5)
        self._user_agent = UserAgent()

    async def run_validating(self, api_key: str) -> bool | None:
        async with ClientSession() as session:
            current_date = datetime.now()
            url = self.url.format(current_date=current_date.strftime("%Y-%m-%d"))
            response = await self._get_website_response(url, api_key, session)
        return response

    @retry(3)
    async def _get_website_response(
            self,
            url: str,
            api_key: str,
            session: ClientSession
    ) -> bool:
        proxy = get_proxy()
        headers = {
            "Authorization": api_key,
            "Content-type": "application/json",
            "User-Agent": self._user_agent.random
        }
        async with self._semaphore:
            async with session.get(url=url, proxy=proxy, headers=headers) as response:
                status_code = response.status
                if status_code == 200:
                    return True
                elif status_code == 401:
                    return False
                else:
                    raise ConnectionError(f"Status code: {status_code}, proxy={proxy}")
