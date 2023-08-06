# noqa: D100
from datetime import datetime
from typing import List, Optional

from bambooapi_client.openapi.apis import EventsApi as _EventsApi
from bambooapi_client.openapi.exceptions import NotFoundException
from bambooapi_client.openapi.models import (
    EventCreateResponse,
    EventInDB,
    EventListItem,
    EventStatusEnum,
    EventTypeEnum,
    OutOfBoundsEventCreate,
    ScheduledUnavailabilityEventCreate,
    TelemetryStartEventCreate,
    TelemetryStopEventCreate,
)


class EventsApi(object):
    """Implementation for '/v1/events' endpoints."""

    def __init__(self, bambooapi_client):
        """Initialize defaults."""
        self._bambooapi_client = bambooapi_client
        self._api_instance = _EventsApi(bambooapi_client.api_client)

    def list_events(
        self,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        site_id: Optional[int] = None,
        event_type: Optional[List[EventTypeEnum]] = None,
        event_status: Optional[List[EventStatusEnum]] = None,
    ) -> List[EventListItem]:
        """List events."""
        kwargs = dict(
            start_time=start_time,
            end_time=end_time,
            site_id=site_id,
            event_type=event_type,
            event_status=event_status,
        )
        set_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return self._api_instance.list_events(**set_kwargs)

    def get_event(self, event_id: int) -> Optional[EventInDB]:
        """Get event by id."""
        try:
            return self._api_instance.read_event(event_id)
        except NotFoundException:
            return None

    def create_out_of_bounds(
        self,
        event_in: OutOfBoundsEventCreate,
    ) -> EventCreateResponse:
        """Create an OutOfBounds event."""
        return self._api_instance.create_out_of_bounds(event_in)

    def create_telemetry_start(
        self,
        event_in: TelemetryStartEventCreate,
    ) -> EventCreateResponse:
        """Create a TelemetryStart event."""
        return self._api_instance.create_telemetry_start(event_in)

    def create_telemetry_stop(
        self,
        event_in: TelemetryStopEventCreate,
    ) -> EventCreateResponse:
        """Create a TelemetryStop event."""
        return self._api_instance.create_telemetry_stop(event_in)

    def create_scheduled_unavailability(
        self,
        event_in: ScheduledUnavailabilityEventCreate,
    ) -> EventCreateResponse:
        """Create an ScheduledUnavailability event."""
        return self._api_instance.create_schdeuled_unavailability(event_in)

    def cancel_scheduled_unavailability(self, event_id: int) -> EventListItem:
        """Cancel an ScheduledUnavailability event."""
        return self._api_instance.cancel_scheduled_unavailability(event_id)
