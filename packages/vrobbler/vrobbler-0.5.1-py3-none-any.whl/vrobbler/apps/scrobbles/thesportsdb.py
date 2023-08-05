import logging
from typing import Optional

import requests
from django.conf import settings
from django.utils import timezone
from sports.models import SportEvent

from pysportsdb import TheSportsDbClient

logger = logging.getLogger(__name__)

API_KEY = getattr(settings, "THESPORTSDB_API_KEY", "2")
thesportsdb_client = TheSportsDbClient(api_key=API_KEY)


def lookup_event_from_thesportsdb(event_id: str) -> dict:

    event = thesportsdb_client.lookup_event(event_id)

    run_time_seconds = int(event.get('runtimes')[0]) * 60
    # Ticks otherwise known as miliseconds
    run_time_ticks = run_time_seconds * 1000 * 1000

    event_type = SportEvent.Type.GAME

    try:
        plot = event.get('plot')[0]
    except TypeError:
        plot = ""
    except IndexError:
        plot = ""

    # Build a rough approximation of a Jellyfin data response
    data_dict = {
        "ItemType": item_type,
        "Name": event.get('title'),
        "Overview": plot,
        "Tagline": event.get('tagline'),
        "Year": event.get('year'),
        "Provider_thesportsdb": event_id,
        "RunTime": run_time_seconds,
        "RunTimeTicks": run_time_ticks,
        "SeriesName": event.get('series title'),
        "EpisodeNumber": event.get('episode'),
        "SeasonNumber": event.get('season'),
        "PlaybackPositionTicks": 1,
        "PlaybackPosition": 1,
        "UtcTimestamp": timezone.now().strftime('%Y-%m-%d %H:%M:%S.%f%z'),
        "IsPaused": False,
        "PlayedToCompletion": False,
    }

    return data_dict
