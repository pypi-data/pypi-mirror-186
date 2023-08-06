from datetime import date, datetime, time
from zoneinfo import ZoneInfo

from django.utils import timezone


def _day_start(t: datetime) -> datetime:
    return t.replace(hour=0, minute=0, second=0, microsecond=0)


def _datetime(day: date, tzinfo: ZoneInfo) -> datetime:
    return timezone.make_aware(datetime.combine(day, time.min), timezone=tzinfo)
