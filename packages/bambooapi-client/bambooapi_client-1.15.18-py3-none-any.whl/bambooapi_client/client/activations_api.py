"""Management of site/device activations."""
from datetime import datetime
from typing import List, Optional

from bambooapi_client.openapi.apis import ActivationsApi as _ActivationsApi
from bambooapi_client.openapi.exceptions import NotFoundException
from bambooapi_client.openapi.models import (
    Activation,
    ActivationCreate,
    ActivationStatusEnum,
    ActivationUpdate,
)


class ActivationsApi(object):
    """Implementation for '/v1/activations' endpoints."""

    def __init__(self, bambooapi_client):
        """Initialize defaults."""
        self._bambooapi_client = bambooapi_client
        self._api_instance = _ActivationsApi(bambooapi_client.api_client)

    def create_activation(
        self,
        activation: ActivationCreate,
        reason: str,
    ) -> Activation:
        """Create a new activation."""
        return self._api_instance.create_activation(
            activation,
            reason=reason,
        )

    def get_activation(self, activation_id: int) -> Optional[Activation]:
        """Get activation by id."""
        try:
            return self._api_instance.get_activation_by_id(activation_id)
        except NotFoundException:
            return None

    def list_activations(
        self,
        site_id: Optional[int] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        status_list: Optional[List[ActivationStatusEnum]] = None,
    ) -> List[Activation]:
        """List activations."""
        kwargs = dict(
            site_id=site_id,
            start_time=start_time,
            end_time=end_time,
            status_list=status_list,
        )
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return self._api_instance.list_activations(**kwargs)

    def update_activation(
        self,
        activation_id: int,
        activation: ActivationUpdate,
        reason: str,
    ) -> Activation:
        """Update activation."""
        return self._api_instance.update_activation(
            activation_id,
            activation,
            reason=reason,
        )
