from ..client import TonapiClient
from ..types import Event
from ..types import AccountEvents


class EventMethod(TonapiClient):

    async def get_account_events(self, account: str, before_lt: int = None, limit: int = 1000,
                                 start_date: int = None, end_date: int = None
                                 ) -> AccountEvents:
        """
        Get events for account.

        :param account: Address in raw (hex without 0x) or base64url format.
        :param before_lt: Omit this parameter to get last events.
        :param limit: Default value 1000
        :param start_date:
        :param end_date:
        :return: AccountEvents object.
        """
        params = {
            'account': account,
            'limit': limit,
        }
        if before_lt: params["beforeLt"] = before_lt
        if start_date: params["startDate"] = start_date
        if end_date: params["endDate"] = end_date
        response = await self._method('/v1/event/getAccountEvents', params=params)

        return AccountEvents(**response)

    async def get_event(self, event_id: str) -> Event:
        """
        Get the event by event ID or hash of any transaction in trace.

        :param event_id: Event ID or transaction hash in hex (without 0x)
         or base64url format.
        :return: Event object.
        """
        params = {"event_id": event_id}
        response = await self._method('/v1/event/getEvent', params=params)

        return Event(**response)
