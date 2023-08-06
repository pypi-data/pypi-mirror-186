"""
Elastic Helper for Bdating.
"""
from fastapi import HTTPException
from elasticsearch import AsyncElasticsearch
import json


class BdatingES(AsyncElasticsearch):
    def __init__(self, settings):
        super().__init__(settings.es_endpoint)
        self.settings = settings

    async def get(self, *args, **kw):
        kw.setdefault('index', self.settings.es_index)
        result = await super().get(*args, **kw)
        return es_get_result_to_dict(result)

    async def update(self, *args, **kw):
        kw.setdefault('index', self.settings.es_index)
        result = await super().update(*args, **kw)
        return result

    async def search(self, *args, **kw):
        kw.setdefault('index', self.settings.es_index)
        result = await super().search(*args, **kw)
        return es_search_result_to_dict(result)

    async def msearch(self, body:list[object], *args, **kw):
        result = await super().msearch(body=body, *args, **kw)
        r=[es_search_result_to_dict(i) for i in result['responses']]

        result = {'results': [], 'total_size': 0, 'size': 0}
        for i in r:
          result['results'].append(i['results'])
          result['total_size'] += i['total_size']
          result['size'] += i['size']
        return result

    async def delete(self, *args, **kw):
        kw.setdefault('index', self.settings.es_index)
        result = await super().delete(*args, **kw)
        return result

    async def delete_by_query(self, *args, **kw):
        kw.setdefault('index', self.settings.es_index)
        result = await super().delete_by_query(*args, **kw)
        return result

    async def create(self, *args, **kw):
        kw.setdefault('index', self.settings.es_index)
        result = await super().create(*args, **kw)
        return result
    
    async def index(self, *args, **kw):
        kw.setdefault('index', self.settings.es_index)
        result = await super().index(*args, **kw)
        return result

def es_get_result_to_dict(es_result: dict, with_id: bool = False) -> dict:
    """
    A typical es result
    {
    "_index": "local-bdating",
    "_id": "a0abCd:provider",
    "_version": 1,
    "_seq_no": 0,
    "_primary_term": 1,
    "found": true,
    "_source": {
      "type": "provider",
      "uid":"23fdad",
      "address": "10809 Mercedes Loaf Apt. 552\nNancyborough, ID 01277",
      "location": [
        -38.1355732927354,
        145.21265948643753
      ],
      "name": "Julie Simmons",
      "bio": "Number next prepare possible generation among arm."
    }
  }
    """
    result = es_result.get('_source', {})
    if with_id:
        result['_id'] = es_result.get('_id')
    return result


def es_search_result_to_dict(es_result: dict, with_id: bool = False) -> dict:
    '''
    A typical es result
    {
  "took" : 6,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 10,
      "relation" : "eq"
    },
    "max_score" : 0.020639554,
    "hits" : [
      {
        "_index" : "local-bdating",
        "_id" : "a0abCd:slot",
        "_score" : 0.020639554,
        "_source" : {
          "type" : "slot",
          "uid" : "a0abCd",

          "address" : """Unit 9190 Box 6681


DPO AP 42608""",
          "location" : {
            "lat" : -37.977931083798815,
            "lon" : 145.07269918572806
          },
          "name" : "Zachary Powers",
          "bio" : "Type seat some agent.",
          "rate_aud" : 150,
          "slot_id" : 2022062623
        }
      },
      ...
    ]
  }
}

  }
    '''
    result = {
        'results': []
    }
    
    for r in es_result.get('hits', {})['hits']:
        record = r.get('_source')
        if with_id:
            record['_id'] = r.get('_id')
        result['results'].append(record)

    if es_result.get('hits', {}).get('total', {}).get('value') is not None:
        result['total_size'] = es_result.get(
            'hits', {}).get('total', {}).get('value')
    result['size'] = len(result['results'])
    return result


def validate_slot_id(slot_id: int):
    if slot_id % 100 > 47:
        raise HTTPException(
            status_code=400, detail="slot id hour part must be between 0-47")
    if slot_id // 100 % 100 < 1 or slot_id // 100 % 100 > 31:
        raise HTTPException(
            status_code=400, detail="slot id day part must be between 1-31")
    if slot_id // 10000 % 100 < 1 or slot_id // 10000 % 100 > 12:
        raise HTTPException(
            status_code=400, detail="slot id month part must be between 1-12")
    if slot_id // 1000000 < 2020 or slot_id // 1000000 > 4000:
        raise HTTPException(
            status_code=400, detail="slot id year part must be resonable")
