"""Sites are physical locations where flexibility devices are deployed."""
import typing as tp
from datetime import datetime
from typing import Dict, List, Optional, Union

import pandas as pd

from bambooapi_client.openapi.apis import SitesApi as _SitesApi
from bambooapi_client.openapi.exceptions import NotFoundException
from bambooapi_client.openapi.models import (
    AvailabilityScheduleItem,
    BaselineModel,
    FlexibilityModel,
    ForecastTypeOption,
    Horizon,
    PeriodRange,
    Site,
    SiteAvailabilityEnum,
    SiteDataPoint,
    SiteListItem,
    SiteMeasurements,
    SiteReliabilityIndex,
    SiteTreatmentPlantCosts,
    ThermalZone,
    ThermalZoneSetpoints,
)

from .helpers import convert_time_index_to_utc, to_datapoints


class SitesApi(object):
    """Implementation for '/v1/sites' endpoints."""

    def __init__(self, bambooapi_client):
        """Initialize defaults."""
        self._bambooapi_client = bambooapi_client
        self._api_instance = _SitesApi(bambooapi_client.api_client)

    def list_sites(self) -> tp.List[SiteListItem]:
        """List sites."""
        return self._api_instance.list_sites()

    def get_site(self, site_id: int) -> tp.Optional[Site]:
        """Get site by id."""
        try:
            return self._api_instance.read_site(site_id)
        except NotFoundException:
            return None

    def get_site_id(self, site_name: str) -> tp.Optional[int]:
        """Get site id by name."""
        try:
            return self._api_instance.get_site_id_by_name(site_name)
        except NotFoundException:
            return None

    def is_available(self, site_id: int) -> bool:
        """Read site availability."""
        availability = self._api_instance.read_site_availability(
            site_id=site_id,
        )
        return availability == SiteAvailabilityEnum('available')

    def set_availability(self, site_id: int, available: bool) -> None:
        """Set site availability."""
        if available:
            site_availability = SiteAvailabilityEnum('available')
        else:
            site_availability = SiteAvailabilityEnum('unavailable')
        availability = self._api_instance.update_site_availability(
            site_id=site_id,
            body=site_availability,
        )
        return availability

    def read_site_contract_schedule(
        self,
        site_id: int,
        start_time: datetime,
        end_time: datetime,
    ) -> pd.DataFrame:
        """Read site contract schedule."""
        schedule = self._api_instance.read_site_contract_schedule(
            site_id=site_id,
            start_time=start_time,
            end_time=end_time
        )
        schedule_dicts = [
            contract_schedule_item.to_dict()
            for contract_schedule_item in schedule
        ]
        if schedule_dicts:
            df = pd.DataFrame.from_records(schedule_dicts, index='time')
            convert_time_index_to_utc(df)
            return df
        else:
            return pd.DataFrame()

    def read_availability_schedule(
        self,
        site_id: int,
        start_time: datetime,
        end_time: datetime,
        frequency: Optional[str] = None,
    ) -> pd.DataFrame:
        """Read site availability schedule."""
        kwargs = dict(frequency=frequency) if frequency else {}
        schedule = self._api_instance.read_site_availability_schedule(
            site_id=site_id,
            start_time=start_time,
            end_time=end_time,
            **kwargs,
        )
        if schedule:
            # Convert to dict
            schedule = [m.to_dict() for m in schedule]
            # Convert to dataframe
            df = pd.DataFrame.from_records(schedule, index='time')
            convert_time_index_to_utc(df)
            return df
        else:
            return pd.DataFrame()

    def list_devices(
        self,
        site_id: int,
        device_type: str = 'thermal_loads',
    ) -> tp.List[tp.Any]:
        """List devices of a specified type for a given site."""
        return self._api_instance.list_devices(
            site_id,
            device_type=device_type,
        )

    def get_device(self, site_id: int, device_name: str) -> tp.Optional[dict]:
        """Get single device by name for a given site."""
        try:
            device = self._api_instance.read_device(site_id, device_name)
        except NotFoundException:
            return None
        if isinstance(device, dict):
            return device
        else:
            return device.to_dict()

    def list_thermal_zones(self, site_id: int) -> tp.List[ThermalZone]:
        """List zones for a given site."""
        return self._api_instance.list_thermal_zones(site_id)

    def get_thermal_zone(
        self,
        site_id: int,
        zone_name: str,
    ) -> tp.Optional[ThermalZone]:
        """Get single zone by name for a given site."""
        try:
            return self._api_instance.read_thermal_zone(site_id, zone_name)
        except NotFoundException:
            return None

    def read_device_baseline_model(
        self,
        site_id: int,
        device_name: str,
        horizon: str = Horizon('day-ahead').to_str(),
    ) -> tp.Optional[BaselineModel]:
        """Read baseline model for a given site and device."""
        try:
            return self._api_instance.read_baseline_model(
                site_id,
                device_name,
                horizon=horizon,
            )
        except NotFoundException:
            return None

    def update_device_baseline_model(
        self,
        site_id: int,
        device_name: str,
        baseline_model: tp.Union[BaselineModel, dict],
        horizon: str = Horizon('day-ahead').to_str(),
    ) -> BaselineModel:
        """Update baseline model for a given site and device."""
        return self._api_instance.update_baseline_model(
            site_id,
            device_name,
            baseline_model,
            horizon=horizon,
        )

    def read_measurements(
        self,
        site_id,
        device_types: List[str],
        start_time: datetime,
        end_time: datetime,
        frequency: Optional[str] = None,
    ) -> List[Dict[str, Union[int, str, pd.DataFrame]]]:
        """Read devices measurements for selected device types."""
        kwargs = dict(frequency=frequency) if frequency else {}
        _measurements = self._api_instance.read_measurements(
            site_id,
            device_types=device_types,
            start_time=start_time,
            end_time=end_time,
            **kwargs,
        )
        device_measurements_list = [m.to_dict() for m in _measurements]
        for item in device_measurements_list:
            measurements = item.get('measurements')
            if measurements:
                df = pd.DataFrame.from_records(measurements, index='time')
                convert_time_index_to_utc(df)
                item['measurements'] = df
            else:
                item['measurements'] = pd.DataFrame()
        return device_measurements_list

    def update_measurements(
        self,
        site_id: int,
        site_measurements: List[SiteMeasurements],
    ) -> None:
        """Update site measurements."""
        self._api_instance.put_insert_site_measurements(
            site_id,
            site_measurements,
        )

    def update_measurements_private(
        self,
        site_id: int,
        site_measurements: List[SiteMeasurements],
    ) -> None:
        """Put measurements directly into database.

        **For private use only.**
        """
        self._api_instance.put_insert_site_measurements_private(
            site_id,
            site_measurements,
        )

    def read_device_measurements(
        self,
        site_id: int,
        device_name: str,
        start_time: datetime,
        end_time: datetime,
        frequency: tp.Optional[str] = None,
    ) -> tp.Optional[pd.DataFrame]:
        """Read site device measurements."""
        kwargs = dict(
            period=PeriodRange('CustomRange').to_str(),
            start_time=start_time.isoformat(),
            end_time=end_time.isoformat(),
        )
        if frequency:
            kwargs.update(frequency=frequency)
        _meas = self._api_instance.read_device_measurements(
            site_id,
            device_name,
            **kwargs,
        )
        # Convert SiteDataPoint objects to dict before converting to DF
        if _meas:
            _meas = [m.to_dict() for m in _meas]
            # Convert to DF
            df = pd.DataFrame.from_records(_meas, index='time')
            convert_time_index_to_utc(df)
            return df
        else:
            return pd.DataFrame()

    def update_device_measurements(
        self,
        site_id: int,
        device_name: str,
        data_frame: pd.DataFrame,
    ) -> None:
        """Update site device measurements (deprecated)."""
        _dps = to_datapoints(data_frame)
        self._api_instance.put_insert_device_measurements(
            site_id,
            device_name,
            _dps,
        )

    def update_device_measurements_private(
        self,
        site_id: int,
        device_name: str,
        data_frame: pd.DataFrame,
    ) -> None:
        """Put device measurements directly into database (deprecated).

        **For private use only.**
        """
        _dps = to_datapoints(data_frame)
        self._api_instance.put_insert_device_measurements_private(
            site_id,
            device_name,
            _dps,
        )

    def read_device_baseline_forecasts(
        self,
        site_id: int,
        device_name: str,
        start_time: datetime,
        end_time: datetime,
        horizon: str = ForecastTypeOption('best_available').to_str(),
        frequency: tp.Optional[str] = None,
    ) -> pd.DataFrame:
        """Read site device forecasts."""
        kwargs = dict(
            horizon=horizon,
            period=PeriodRange('CustomRange').to_str(),
            start_time=start_time.isoformat(),
            end_time=end_time.isoformat(),
        )
        if frequency:
            kwargs.update(frequency=frequency)

        _meas = self._api_instance.read_device_baseline_forecasts(
            site_id,
            device_name,
            **kwargs,
        )
        # Convert DataPoint objects to dict before converting to DF
        if _meas:
            _meas = [m.to_dict() for m in _meas]
            # Convert to DF
            df = pd.DataFrame.from_records(_meas, index='time')
            convert_time_index_to_utc(df)
            return df
        else:
            return pd.DataFrame()

    def update_device_baseline_forecasts(
        self,
        site_id: int,
        device_name: str,
        data_frame: pd.DataFrame,
        horizon: str = Horizon('day-ahead').to_str(),
    ) -> tp.List[SiteDataPoint]:
        """Update site device baseline forecasts."""
        _dps = data_frame.reset_index().to_dict(orient='records')
        return self._api_instance.insert_device_baseline_forecasts(
            site_id,
            device_name,
            _dps,
            horizon=horizon,
        )

    def get_reliability_index(
        self,
        site_id: int,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
    ) -> Optional[SiteReliabilityIndex]:
        """Get the last reliability index in the given period."""
        try:
            kwargs = {}
            if start_time is not None:
                kwargs.update(start_time=start_time)
            if end_time is not None:
                kwargs.update(end_time=end_time)
            return self._api_instance.read_site_reliability_index(
                site_id=site_id,
                **kwargs,
            )
        except NotFoundException as e:
            if 'Reliability index not found' in str(e):
                return None
            raise

    def insert_reliability_index(
        self,
        site_id: int,
        time: datetime,
        value: float,
    ) -> None:
        """Insert site reliability index."""
        reliability_index = SiteReliabilityIndex(time=time, value=value)
        return self._api_instance.insert_site_reliability_index(
            site_id=site_id,
            site_reliability_index=reliability_index,
        )

    def read_thermal_zone_flexibility_model(
        self,
        site_id: int,
        zone_name: str,
        horizon: str = Horizon('day-ahead').to_str(),
    ) -> tp.Optional[FlexibilityModel]:
        """Read thermal flexibility model for a given site and zone."""
        try:
            return self._api_instance.read_flexibility_model(
                site_id,
                zone_name,
                horizon=horizon,
            )
        except NotFoundException:
            return None

    def update_thermal_zone_flexibility_model(
        self,
        site_id: int,
        zone_name: str,
        flexibility_model: tp.Union[FlexibilityModel, dict],
        horizon: str = Horizon('day-ahead').to_str(),
    ) -> FlexibilityModel:
        """Update thermal flexibility model for a given site and zone."""
        return self._api_instance.update_flexibility_model(
            site_id,
            zone_name,
            flexibility_model,
            horizon=horizon,
        )

    def update_device_flexibility_forecast(
        self,
        site_id: int,
        device_name: str,
        data_frame: pd.DataFrame,
        ramping: str,
        horizon: str = Horizon('day-ahead').to_str(),
    ) -> tp.List[SiteDataPoint]:
        """Update device flexibility forecast."""
        _dps = data_frame.reset_index().to_dict(orient='records')
        return self._api_instance.insert_device_flexibility_forecasts(
            site_id=site_id,
            device_name=device_name,
            site_data_point=_dps,
            horizon=horizon,
            ramping=ramping,
        )

    def read_device_flexibility_forecast(
        self,
        site_id: int,
        device_name: str,
        ramping: str,
        start_time: datetime,
        end_time: datetime,
        horizon: str = ForecastTypeOption('best_available').to_str(),
        frequency: tp.Optional[str] = None,
    ) -> pd.DataFrame:
        """Read site device flexibility."""
        kwargs = dict(
            period=PeriodRange('CustomRange').to_str(),
            start_time=start_time,
            end_time=end_time,
        )
        if frequency:
            kwargs.update(frequency=frequency)

        _meas = self._api_instance.read_device_flexibility_forecasts(
            site_id=site_id,
            device_name=device_name,
            ramping=ramping,
            horizon=horizon,
            **kwargs,
        )
        if _meas:
            _meas = [m.to_dict() for m in _meas]
            df = pd.DataFrame.from_records(_meas, index='time')
            convert_time_index_to_utc(df)
            return df
        else:
            return pd.DataFrame()

    def update_thermal_zone_flexibility_forecast(
        self,
        site_id: int,
        zone_name: str,
        data_frame: pd.DataFrame,
        ramping: str,
        horizon: str = Horizon('day-ahead').to_str(),
    ) -> tp.List[SiteDataPoint]:
        """Update site thermal zone flexibility forecast."""
        _dps = data_frame.reset_index().to_dict(orient='records')
        return self._api_instance.insert_thermal_zone_flexibility_forecasts(
            site_id=site_id,
            zone_name=zone_name,
            site_data_point=_dps,
            ramping=ramping,
            horizon=horizon,
        )

    def read_thermal_zone_flexibility_forecast(
        self,
        site_id: int,
        zone_name: str,
        ramping: str,
        start_time: tp.Optional[str] = None,
        end_time: tp.Optional[str] = None,
        horizon: str = ForecastTypeOption('best_available').to_str(),
        frequency: tp.Optional[str] = None,
    ) -> pd.DataFrame:
        """Read site thermal zone flexibility forecast."""
        kwargs = dict(
            period=PeriodRange('CustomRange').to_str(),
            start_time=start_time,
            end_time=end_time,
        )
        if frequency:
            kwargs.update(frequency=frequency)

        _meas = self._api_instance.read_thermal_zone_flexibility_forecasts(
            site_id=site_id,
            zone_name=zone_name,
            ramping=ramping,
            horizon=horizon,
            **kwargs,
        )
        if _meas:
            _meas = [m.to_dict() for m in _meas]
            df = pd.DataFrame.from_records(_meas, index='time')
            convert_time_index_to_utc(df)
            return df
        else:
            return pd.DataFrame()

    def read_thermal_zone_setpoints(
        self,
        site_id: int,
        zone_name: str,
    ) -> ThermalZoneSetpoints:
        """Read site thermal zone setpoints."""
        return self._api_instance.read_thermal_zone_setpoints(
            site_id=site_id,
            zone_name=zone_name,
        )

    def update_thermal_zone_setpoints(
        self,
        site_id: int,
        zone_name: str,
        thermal_zone_setpoints: ThermalZoneSetpoints,
    ) -> ThermalZoneSetpoints:
        """Update site thermal zone setpoint."""
        return self._api_instance.update_thermal_zone_setpoints(
            site_id=site_id,
            zone_name=zone_name,
            thermal_zone_setpoints=thermal_zone_setpoints,
        )

    def read_treatment_plant_average_costs(
        self,
        site_id: int,
        plant_name: str,
        start_time: datetime,
        end_time: datetime,
        spot_market_id: Optional[int] = None,
        frequency: Optional[str] = None,
    ) -> SiteTreatmentPlantCosts:
        """Get site and retailer average costs for plant management."""
        kwargs = dict(
            site_id=site_id,
            plant_name=plant_name,
            start_time=start_time,
            end_time=end_time,
        )
        if spot_market_id is not None:
            kwargs.update(spot_market_id=spot_market_id)
        if frequency:
            kwargs.update(frequency=frequency)
        return self._api_instance.get_treatment_plant_cost(**kwargs)
