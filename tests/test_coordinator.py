"""Availability behavior for failed Ariston cloud refreshes."""

from datetime import timedelta
from unittest.mock import AsyncMock

from ariston.ariston_api import ConnectionException
from homeassistant.helpers.update_coordinator import CoordinatorEntity
import pytest

from custom_components.ariston.coordinator import DeviceDataUpdateCoordinator


@pytest.mark.parametrize(
    "error",
    [
        ConnectionException(429),
        ConnectionException("GALEVO property response is incomplete"),
    ],
)
async def test_failed_refresh_retains_data_and_recovers_at_configured_interval(
    hass, ariston_device, error
):
    """A retained snapshot stays unavailable until the next successful refresh."""
    previous = {"heating_mode": "winter"}
    current = {"heating_mode": "summer"}
    update = AsyncMock(side_effect=[previous, error, current])
    coordinator = DeviceDataUpdateCoordinator(hass, ariston_device, 60, "state", update)
    entity = CoordinatorEntity(coordinator)

    await coordinator.async_refresh()
    assert entity.available
    assert coordinator.data is previous

    await coordinator.async_refresh()
    assert not entity.available
    assert not coordinator.last_update_success
    assert coordinator.data is previous
    assert coordinator.update_interval == timedelta(seconds=60)

    await coordinator.async_refresh()
    assert entity.available
    assert coordinator.data is current
    assert update.await_count == 3
