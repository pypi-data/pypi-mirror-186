# noqa: D100
from datetime import datetime
from typing import Dict, List, Optional

from pandas import DataFrame

from bambooapi_client.client.helpers import convert_time_index_to_utc
from bambooapi_client.openapi.apis import PortfoliosApi as _PortfoliosApi
from bambooapi_client.openapi.models import (
    EnergyMarketOperations,
    FlexibilityMarketOperations,
    MarketOperationsEnum,
    PortfolioMarket,
    PortfolioSite,
)


class PortfoliosApi(object):
    """Implementation for '/v1/portfolios endpoints."""

    def __init__(self, bambooapi_client):
        self._bambooapi_client = bambooapi_client
        self._api_instance = _PortfoliosApi(bambooapi_client.api_client)

    def list_portfolios_markets(
        self,
        portfolio_id: int,
    ) -> List[PortfolioMarket]:
        """List all markets of a portfolio."""
        return self._api_instance.list_portfolios_markets(portfolio_id)

    def list_portfolios_sites(self, portfolio_id: int) -> List[PortfolioSite]:
        """List all sites of a portfolio."""
        return self._api_instance.list_portfolios_sites(portfolio_id)

    def read_portfolio_energy_market_operations(
        self,
        portfolio_id: int,
        market_id: int,
        start_time: datetime,
        end_time: datetime,
        operations: List[MarketOperationsEnum],
    ) -> Dict[str, DataFrame]:
        """Get energy market operations of a portfolio and market."""
        response = self._api_instance.read_portfolio_energy_market_operations(
            portfolio_id=portfolio_id,
            market_id=market_id,
            start_time=start_time,
            end_time=end_time,
            operations=operations,
        )
        operations_dfs = {}
        for op_name in map(str, operations):
            if response.get(op_name):
                df = DataFrame.from_records(
                    [row.to_dict() for row in response[op_name]],
                    index='time',
                )
                convert_time_index_to_utc(df)
                operations_dfs[op_name] = df
        return operations_dfs

    def update_portfolio_energy_market_operations(
        self,
        portfolio_id: int,
        market_id: int,
        bids: Optional[DataFrame] = None,
        clearings: Optional[DataFrame] = None,
        profits: Optional[DataFrame] = None,
    ):
        """Update portfolio operations."""
        operations_dict = {
            'bids': bids,
            'clearings': clearings,
            'profits': profits,
        }
        # Remove Nones, convert to records
        operations_dict = {
            k: v.reset_index().to_dict(orient='records')
            for k, v in operations_dict.items()
            if v is not None
        }
        operations = EnergyMarketOperations(**operations_dict)
        self._api_instance.update_portfolio_energy_market_operations(
            portfolio_id=portfolio_id,
            market_id=market_id,
            energy_market_operations=operations,
        )

    def read_portfolio_flexibility_market_operations(
        self,
        portfolio_id: int,
        market_id: int,
        start_time: datetime,
        end_time: datetime,
        operations: List[MarketOperationsEnum],
    ) -> Dict[str, DataFrame]:
        """Get flexibility market operations of a portfolio and market."""
        response = self._api_instance.read_portfolio_flexibility_market_operations(  # noqa: E501
            portfolio_id=portfolio_id,
            market_id=market_id,
            start_time=start_time,
            end_time=end_time,
            operations=operations,
        )
        operations_dfs = {}
        for op_name in map(str, operations):
            if response.get(op_name):
                df = DataFrame.from_records(
                    [row.to_dict() for row in response[op_name]],
                    index='time',
                )
                convert_time_index_to_utc(df)
                operations_dfs[op_name] = df
        return operations_dfs

    def update_portfolio_flexibility_market_operations(
        self,
        portfolio_id: int,
        market_id: int,
        bids: Optional[DataFrame] = None,
        clearings: Optional[DataFrame] = None,
        activations: Optional[DataFrame] = None,
        responses: Optional[DataFrame] = None,
        profits: Optional[DataFrame] = None,
    ):
        """Update portfolio operations."""
        operations_dict = {
            'bids': bids,
            'clearings': clearings,
            'activations': activations,
            'responses': responses,
            'profits': profits,
        }
        # Remove Nones, convert to records
        operations_dict = {
            k: v.reset_index().to_dict(orient='records')
            for k, v in operations_dict.items()
            if v is not None
        }
        operations = FlexibilityMarketOperations(**operations_dict)
        self._api_instance.update_portfolio_flexibility_market_operations(
            portfolio_id=portfolio_id,
            market_id=market_id,
            flexibility_market_operations=operations,
        )
