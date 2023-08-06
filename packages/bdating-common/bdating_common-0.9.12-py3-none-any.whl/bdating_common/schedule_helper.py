"""
Scheduler DB entry Helper for Bdating.
"""
from elasticsearch import Elasticsearch, NotFoundError
import os
import logging
from bdating_common.es_helper import es_search_result_to_dict
from bdating_common.api_common import settings
from bdating_common.event_helper import report_event
settings.es_index = f"{settings.app_namespace}-bdating"
es = Elasticsearch(settings.es_endpoint)

whoami = os.getenv('WHO_AM_I', 'bdating-common-library')
logger = logging.getLogger(whoami)
logger.setLevel(os.getenv("LOG_LEVEL", 'INFO'))


def find_scheduled_items(now: int, max_size: int = 1000):
    """
    Find all qualified alarms to send, and then process them
    1. Find all records start time < now, then process them and generate events.
    1. Find all records no_later_than < now then delete them.

    """
    query_condition = {
        "query": {
            "bool": {
                "must": [
                    {
                        "term": {
                            "type": "schedule"
                        }
                    },
                    {
                        "term": {
                            "status": "active"
                        }
                    },
                    {
                        "range": {
                            "start_time": {
                                "lte": now
                            }
                        }
                    },
                    # {
                    #     "range": {
                    #         "no_later_than": {
                    #             "gte": now
                    #         }
                    #     }
                    # }
                ]
            }
        },
        "sort": [
            {"start_time": "asc"}
        ],
        "size": max_size
    }

    return es_search_result_to_dict(es.search(index=settings.es_index, body=query_condition), with_id=True)


def create_schedule(schedule_type: str, matching_id: str, start_time: int, no_later_than: int = None, **args):
    """
    Args: the definition of args are following the schedule_type
    """
    if not no_later_than:
        no_later_than = start_time+300  # must finish within 5 mins as default setting
    record = {
        "type": "schedule",
                "schedule_type": schedule_type,  # notify, verify_payment, etc.
                # booking id/transaction id, or any other uniq id that can decide the related schedules
                "matching_id": matching_id,
                "status": "active",  # place holder. Always active.
                "start_time": start_time,  # started to execute after this time
                # if now is already after this time, then cancel this.
                "no_later_than": no_later_than,
                "body": args
    }

    es.index(index=settings.es_index, document=record)
    logger.debug(f"Report event: schedules for id {matching_id} are created.")
    report_event(
        _type='schedule',
        action='created',
        body={
            "matching_condition": record
        },
        success=True,
        source_id=whoami,
    )


def cancel_schedule(schedule_or_matching_id: object):
    try:
        if isinstance(schedule_or_matching_id, dict):  # expect to be scheudle
            record_id = schedule_or_matching_id.get('_id')
            logger.debug(f"Cancel schedule by its record_id {record_id}.")
            es.delete(
                index=settings.es_index,
                id=record_id
            )
        else:
            matching_id = schedule_or_matching_id
            logger.debug(f"Cancel schedule by its original id {matching_id}.")
            es.delete_by_query(
                index=settings.es_index,
                query={
                    "match": {
                        "matching_id": matching_id
                    }
                })
    except Exception as e:
        if not isinstance(e, NotFoundError):
            logger.warning(
                f"Exception when deleting related records for {schedule_or_matching_id}. Excepti")
    #logger.info(f"Schedules mathcing {schedule_or_matching_id} are deleted.")

    #logger.debug(
    #    f"Report event: schedules related to {schedule_or_matching_id} are canceled.")
    report_event(
        _type='schedule',
        action='canceled',
        body={
            'matching_condition': schedule_or_matching_id
        },
        success=True,
        source_id=whoami,
    )
