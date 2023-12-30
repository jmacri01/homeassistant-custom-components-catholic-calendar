"""CatholicCalendar calendar"""
from __future__ import annotations
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
import logging
from homeassistant.const import CONF_NAME
from homeassistant.components.calendar import (
    PLATFORM_SCHEMA,
    CalendarEntity,
    CalendarEvent,
)
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType, StateType
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .calendar_generator import CalendarGenerator
from homeassistant.core import HomeAssistant
import datetime
from datetime import timedelta, timezone
from homeassistant.util import dt as dt_util

_LOGGER: logging.Logger = logging.getLogger(__name__)

__version__ = "1.0.0"

COMPONENT_REPO = (
    "https://github.com/jmacri01/homeassistant-custom-components-catholic-calendar"
)

REQUIREMENTS = []

DEFAULT_THUMBNAIL = "https://www.home-assistant.io/images/favicon-192x192-full.png"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {vol.Required(CONF_NAME): cv.string},
)

_LOGGER: logging.Logger = logging.getLogger(__name__)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_devices: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the CatholicCalendar sensor."""
    async_add_devices(
        [
            CatholicCalendar(
                name=config[CONF_NAME],
            ),
        ],
        update_before_add=True,
    )


class CatholicCalendar(CalendarEntity):
    """Representation of a CatholicCalendar calendar."""

    _attr_force_update = True

    def __init__(
        self: CatholicCalendar,
        name: str,
    ) -> None:
        """Initialize the CatholicCalendar calendar."""
        self._attr_name = name
        self._years_loaded: list[int] = []
        self._festivities: dict[datetime.datetime, list[dict[str, str]]] = {}
        _LOGGER.debug("CatholicCalendar initialized - %s", self)

    def __repr__(self: CatholicCalendar) -> str:
        """Return the representation."""
        return "CatholicCalendar"

    @property
    def event(self) -> CalendarEvent | None:
        """Return the next upcoming event."""
        curr_date = dt_util.now().date()
        if curr_date.year not in self._years_loaded:
            self.__generate_festivities(curr_date.year)

        events = self.__get_calendar_events(curr_date)
        if len(events) == 0:
            return None
        return events[0]

    async def async_get_events(
        self,
        hass: HomeAssistant,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
    ) -> list[CalendarEvent]:
        """Return calendar events within a datetime range."""
        for year in range(start_date.year, end_date.year + 1):
            if year not in self._years_loaded:
                self.__generate_festivities(year)
        calendar_events = []

        curr_date = start_date
        while curr_date <= end_date:
            _LOGGER.debug("getting calender event for date: %s", curr_date)
            calendar_events.extend(self.__get_calendar_events(curr_date))
            curr_date += datetime.timedelta(days=1)

        _LOGGER.debug("retrieved calendar_events: %s", calendar_events)
        return calendar_events

    def __get_calendar_events(self, date) -> list[CalendarEvent]:
        calendar_events = []
        if datetime.datetime(date.year, date.month, date.day) in self._festivities:
            for festivity in self._festivities[
                datetime.datetime(date.year, date.month, date.day)
            ]:
                calendar_events.append(
                    CalendarEvent(start=date, end=date, summary=festivity["name"])
                )
        return calendar_events

    def __generate_festivities(self, year):
        calendar_generator = CalendarGenerator(year)
        festivities = calendar_generator.generate_festivities()
        self._years_loaded.append(year)
        for key in festivities.keys():
            if key not in self._festivities:
                self._festivities.update({key: []})
            self._festivities[key].extend(festivities[key])
