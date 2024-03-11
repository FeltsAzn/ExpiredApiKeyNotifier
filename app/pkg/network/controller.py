from .wb_connector import WildBerriesNetworkConnector


class WildBerriesController:
    _connector = WildBerriesNetworkConnector()

    async def validate_api_key(self, api_key: str) -> bool | None:
        response = await self._connector.run_validating(api_key)
        return response
