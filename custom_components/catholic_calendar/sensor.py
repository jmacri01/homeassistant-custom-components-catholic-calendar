"""CatholicCalendar sensor."""
from __future__ import annotations
import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity

from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType, StateType

from homeassistant.util import dt as dt_util
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.const import CONF_NAME

from .calendar_generator import CalendarGenerator
import datetime
from datetime import timedelta
from .liturgical_grade import LiturgicalGrade

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
            CatholicCalendarSensor(
                name=config[CONF_NAME],
            ),
        ],
        update_before_add=True,
    )


class CatholicCalendarSensor(SensorEntity):
    """Representation of a CatholicCalendar sensor."""

    _attr_force_update = True

    def __init__(
        self: CatholicCalendarSensor,
        name: str,
    ) -> None:
        """Initialize the CatholicCalendar sensor."""
        self._attr_name = name
        self._attr_icon = "mdi:calendar"
        self._festivities: dict[datetime.datetime, list[dict[str, str]]] = {}
        self._todays_festivities: list[dict[str, str]] = []
        self._attr_extra_state_attributes = {"festivities": self._todays_festivities}
        self._years_loaded = []
        _LOGGER.debug("CatholicCalendarSensor initialized - %s", self)

    def __repr__(self: CatholicCalendarSensor) -> str:
        """Return the representation."""
        return 'CatholicCalendarSensor(name="{self.name}")'

    def update(self: CatholicCalendarSensor) -> None:
        """Generate dates."""
        today = dt_util.now().date()

        # load this year and the next if not already loaded
        for year in [today.year, (today + datetime.timedelta(weeks=52)).year]:
            if year not in self._years_loaded:
                self.__generate_festivities(year)
        todays_festivities = []

        if datetime.datetime(today.year, today.month, today.day) in self._festivities:
            todays_festivities.extend(
                self._festivities[datetime.datetime(today.year, today.month, today.day)]
            )

        self._todays_festivities.clear()
        for festivity in sorted(
            todays_festivities, key=lambda x: x["liturgical_grade"] or 0, reverse=True
        ):
            festivity["liturgical_grade"] = LiturgicalGrade.descr(
                festivity["liturgical_grade"]
            )
            self._todays_festivities.append(festivity)

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        return dt_util.now().date()

    def __generate_festivities(self, year):
        _LOGGER.debug("Generating dates for year %s", year)
        calendar_generator = CalendarGenerator(year)
        festivities = calendar_generator.generate_festivities()
        self._years_loaded.append(year)
        for key in festivities:
            if key not in self._festivities:
                self._festivities.update({key: []})
            self._festivities[key].extend(festivities[key])
