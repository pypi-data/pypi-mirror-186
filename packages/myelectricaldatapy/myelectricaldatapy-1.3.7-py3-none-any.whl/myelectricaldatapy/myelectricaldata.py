"""Class for Enedis Gateway (http://www.myelectricaldata.fr)."""
from __future__ import annotations

import logging
import re
from datetime import date
from datetime import datetime as dt
from typing import Any, Optional, Tuple

import pandas as pd

from .auth import TIMEOUT, EnedisAuth

_LOGGER = logging.getLogger(__name__)


class EnedisAnalytics:
    """Data analaytics."""

    def __init__(self, data: dict[str, Any]) -> None:
        """Initialize Dataframe."""
        self.df = pd.DataFrame(data)

    def get_data_analytcis(
        self,
        convertKwh: bool = False,
        convertUTC: bool = False,
        start_date: str | None = None,
        intervals: list[Tuple[dt, dt]] | None = None,
        groupby: str | None = None,
        freq: str = "H",
        summary: bool = False,
        cumsum: float = 0,
    ) -> Any:
        """Convert datas to analyze."""
        if start_date and not self.df.empty:
            self.df = self.df[(self.df["date"] > start_date)]

        if self.df.empty:
            return self.df.to_dict(orient="records")

        if convertKwh:
            self.df["interval_length"] = self.df["interval_length"].transform(
                self._weighted_interval
            )
            self.df["value"] = (
                pd.to_numeric(self.df["value"]) / 1000 * self.df["interval_length"]
            )
        if convertUTC:
            self.df["date"] = pd.to_datetime(
                self.df["date"], utc=True, format="%Y-%m-%d %H:%M:%S"
            )

        if intervals:
            self.df = self._get_data_interval(intervals, groupby, freq, summary, cumsum)

        return self.df.to_dict(orient="records")

    def _weighted_interval(self, interval: str) -> float | int:
        """Compute weighted."""
        if interval and len(rslt := re.findall("PT([0-9]{2})M", interval)) == 1:
            return int(rslt[0]) / 60
        return 1

    def _get_data_interval(
        self,
        intervalls: list[Tuple[dt, dt]],
        groupby: str | None = None,
        freq: str = "H",
        summary: bool = False,
        cumsum: float = 0,
    ) -> pd.DataFrame:
        """Group date from range time.

        Returns a tuple
        First dict contains the data in the interval
        and the second dict contains the data outside
        """
        in_df = pd.DataFrame()
        for intervall in intervalls:
            df2 = self.df[
                (self.df.date.dt.time >= intervall[0].time())
                & (self.df.date.dt.time < intervall[1].time())
            ]
            in_df = pd.concat([in_df, df2], ignore_index=True)

        # out_df = self.df[~self.df.isin(in_df)].dropna()

        if groupby:
            in_df = (
                in_df.groupby(pd.Grouper(key="date", freq="H"))["value"]
                .sum()
                .reset_index()
            )
            in_df = in_df[in_df.value != 0]

            # out_df = (
            #     out_df.groupby(pd.Grouper(key="date", freq="H"))["value"]
            #     .sum()
            #     .reset_index()
            # )

        if summary:
            in_df["sum_value"] = in_df.value.cumsum() + cumsum
            # out_df["sum_value"] = out_df.value.cumsum() + cumsum

        # return in_df, out_df
        return in_df

    def set_price(
        self,
        data: dict[str, Any],
        price: float,
        summary: bool = False,
    ) -> Any:
        """Set prince."""
        df = pd.DataFrame(data)
        if df.empty:
            return df.to_dict(orient="records")
        df["price"] = df["value"] * price
        if summary:
            df["sum_price"] = df["price"].cumsum()
        return df.to_dict("records")

    def get_last_value(self, data: dict[str, Any], orderby: str, value: str) -> Any:
        """Return last value after order by."""
        df = pd.DataFrame(data)
        if not df.empty:
            df = df.sort_values(by=orderby)
            return df[value].iloc[-1]


class EnedisByPDL:
    """Get data of pdl."""

    def __init__(
        self,
        token: str,
        pdl: str,
        session: Optional[Any] = None,
        timeout: int = TIMEOUT,
        production: bool = False,
        tempo: bool = False,
        ecowatt: bool = False,
    ) -> None:
        """Initialize."""
        self.auth = EnedisAuth(token, session, timeout)
        self.pdl = pdl
        self.b_production = production
        self.b_tempo = tempo
        self.b_ecowatt = ecowatt
        self.offpeaks: list[str] = []
        self.dt_offpeak: list[dt] = []
        self.power_datas: dict[str, Any] = {}
        self.last_refresh_date: date | None = None
        self.contract: dict[str, Any] = {}
        self.tempo_day: str | None = None
        self.ecowatt: dict[str, Any] = {}
        self.valid_access: dict[str, Any] = {}
        self.models: list[Tuple[str, dt, dt]] = []

    async def async_fetch_datas(
        self, service: str, start: dt | None = None, end: dt | None = None
    ) -> Any:
        """Retrieve date from service.

        service:    contracts, identity, contact, addresses,
                    daily_consumption_max_power,
                    daily_consumption, daily_production,
                    consumption_load_curve, production_load_curve
        """
        path_range = ""
        if start and end:
            start_date = start.strftime("%Y-%m-%d")
            end_date = end.strftime("%Y-%m-%d")
            path_range = f"/start/{start_date}/end/{end_date}"
        path = f"{service}/{self.pdl}{path_range}"
        return await self.auth.request(path=path)

    async def async_valid_access(self) -> Any:
        """Return valid access."""
        return await self.async_fetch_datas("valid_access")

    async def async_get_contract(self) -> Any:
        """Return contract information."""
        contract = {}
        contracts = await self.async_fetch_datas("contracts")
        usage_points = contracts.get("customer", {}).get("usage_points", "")
        for usage_point in usage_points:
            if usage_point.get("usage_point", {}).get("usage_point_id") == self.pdl:
                contract = usage_point.get("contracts", {})
                if offpeak_hours := contract.get("offpeak_hours"):
                    self.offpeaks = re.findall("(?:(\\w+)-(\\w+))+", offpeak_hours)
                    self.dt_offpeak = [
                        (  # type: ignore
                            dt.strptime(offpeak[0], "%HH%M"),
                            dt.strptime(offpeak[1], "%HH%M"),
                        )
                        for offpeak in self.offpeaks
                    ]
        return contract

    async def async_get_contracts(self) -> Any:
        """Return all contracts information."""
        return await self.async_fetch_datas("contracts")

    async def async_get_address(self) -> Any:
        """Return adress information."""
        address = {}
        addresses = await self.async_fetch_datas("addresses")
        usage_points = addresses.get("customer", {}).get("usage_points", "")
        for usage_point in usage_points:
            if usage_point.get("usage_point", {}).get("usage_point_id") == self.pdl:
                address = usage_point.get("usage_point")
        return address

    async def async_get_addresses(self) -> Any:
        """Return all adresses information."""
        return await self.async_fetch_datas("adresses")

    async def async_get_tempoday(self) -> Any:
        """Return Tempo Day."""
        day = dt.now().strftime("%Y-%m-%d")
        return await self.auth.request(path=f"rte/tempo/{day}/{day}")

    async def async_get_ecowatt(self) -> Any:
        """Return Ecowatt information."""
        day = dt.now().strftime("%Y-%m-%d")
        return await self.auth.request(path=f"rte/ecowatt/{day}/{day}")

    async def async_has_offpeak(self) -> bool:
        """Has offpeak hours."""
        if not self.offpeaks:
            await self.async_get_contract()
        return len(self.offpeaks) > 0

    async def async_check_offpeak(self, start: dt) -> bool:
        """Return offpeak status."""
        if await self.async_has_offpeak() is True:
            start_time = start.time()
            for range_time in self.offpeaks:
                starting = dt.strptime(range_time[0], "%HH%M").time()
                ending = dt.strptime(range_time[1], "%HH%M").time()
                if ending <= start_time > starting:
                    return True
        return False

    async def async_get_identity(self) -> Any:
        """Get identity."""
        return await self.async_fetch_datas("identity")

    async def async_get_daily_consumption(self, start: dt, end: dt) -> Any:
        """Get daily consumption."""
        return await self.async_fetch_datas("daily_consumption", start, end)

    async def async_get_daily_production(self, start: dt, end: dt) -> Any:
        """Get daily production."""
        return await self.async_fetch_datas("daily_production", start, end)

    async def async_get_details_consumption(self, start: dt, end: dt) -> Any:
        """Get consumption details. (max: 7 days)."""
        return await self.async_fetch_datas("consumption_load_curve", start, end)

    async def async_get_details_production(self, start: dt, end: dt) -> Any:
        """Get production details. (max: 7 days)."""
        return await self.async_fetch_datas("production_load_curve", start, end)

    async def async_get_max_power(self, start: dt, end: dt) -> Any:
        """Get consumption max power."""
        return await self.async_fetch_datas("daily_consumption_max_power", start, end)

    async def async_close(self) -> None:
        """Close session."""
        await self.auth.async_close()

    async def async_load(self, models: list[Tuple[str, dt, dt]] | None = None) -> None:
        """Retrieves production and consumption data.

        models , list contain tuple
        tuple : service (string) , start (datetime) , end (datetime)
        """
        if models is None:
            models = self.models
        else:
            self.models = models
        self.valid_access = await self.async_valid_access()
        self.power_datas = {}
        for model in models:
            service = model[0]
            start = model[1]
            end = model[2]
            datas = await self.async_fetch_datas(service, start, end)
            self.power_datas.update(
                {service: datas.get("meter_reading", {}).get("interval_reading")}
            )

        if self.last_refresh_date is None or dt.now().date() > self.last_refresh_date:
            await self.async_get_contract()
            if self.b_tempo:
                self.tempo_day = await self.async_get_tempoday()
            if self.b_ecowatt:
                self.ecowatt = await self.async_get_ecowatt()

        self.last_refresh_date = dt.now().date()

    async def async_refresh(self) -> None:
        """Refresh datas."""
        await self.async_load()
