import logging
from typing import Tuple
from datetime import datetime
log = logging.getLogger(__name__)
MIN_SLOT_IN_DAY = 0
MAX_SLOT_IN_DAY = 47



def parse_slot(slot_id: int) -> Tuple[datetime, int]:

    try:
        slot = slot_id % 100
        if slot < MIN_SLOT_IN_DAY or slot > MAX_SLOT_IN_DAY:
            return None, None
        return datetime(slot_id // 1000000, slot_id // 10000 % 100, slot_id // 100 % 100), slot
    except ValueError:
        return None, None


def convert_slot_to_epoch(slot_id: int) -> int:
    date_time, _ = parse_slot(slot_id=slot_id)
    return int(date_time.timestamp()) + slot_id % 100 * 30 * 60



if __name__ == "__main__":
    print(convert_slot_to_epoch(2022010123))