import unittest
import datamethods
import json


class TestData(unittest.TestCase):

    def testmethod(self):
        testdata='{"base_date": "2005/05/20", "calc_freq": "Daily, EOD", "currency": "USD", "description": "MerQube Deep Buffer indices provide an outcome in which the index participates equally in the downside of the SPDR S&P 500 ETF (SPY) up to a loss of 5% and protects against any further losses up until a \u201cFloor\u201d of 30%. In order to provide such downside protection, the index provides upside participation in the returns of the SPDR S&P 500 ETF (SPY) up until a \u201cCap\u201d, where the amount of upside participation is determined by current options prices. The outcome is obtained by holding the index for a period of one year starting on the corresponding month specified in the name.", "family": "Defined Outcome Buffer Indices", "id": "666cb931-2fed-4bdb-a3c8-afb81b39bc99", "identifiers": [{"display_name": "Bloomberg Ticker", "metric": "price_return", "provider": "Bloomberg", "ticker": "MQUSDB05"}, {"display_name": "Reuters RIC", "metric": "price_return", "provider": "Reuters", "ticker": ".MQUSDB05"}, {"display_name": "Morningstar Code", "metric": "price_return", "provider": "Morningstar", "ticker": "MQUSDB05"}], "launch_date": "2020/04/24", "name": "MQUSDB05", "namespace": "default", "portfolio_display": {"fields": [{"display_name": "Root", "field_name": "root"}, {"display_name": "Strike", "field_name": "strike"}, {"display_name": "Expiry", "field_name": "expiry"}, {"display_name": "Option Type", "field_name": "option_type"}, {"display_name": "Number of Shares", "field_name": "shares"}, {"display_name": "Strike Percentage", "field_name": "strike_percentage"}]}, "rebal_freq": "Annual", "related": [{"default_display": true, "id": "LY6WH5-S", "metric": "close", "name": "SPY", "type": "security"}, {"default_display": false, "id": "f4a3ca1c-e86f-49ab-a7c2-2a0a6b579b51", "metric": "", "name": "MQUSDB01", "type": "index"}, {"default_display": false, "id": "d754641e-815e-4283-be40-5cd3d8731269", "metric": "", "name": "MQUSDB02", "type": "index"}, {"default_display": false, "id": "c0c2aef8-c79d-4c7d-85c7-38170bf6384e", "metric": "", "name": "MQUSDB03", "type": "index"}, {"default_display": false, "id": "55752f18-10aa-48de-9d52-18ac5e48c537", "metric": "", "name": "MQUSDB04", "type": "index"}, {"default_display": false, "id": "666cb931-2fed-4bdb-a3c8-afb81b39bc99", "metric": "", "name": "MQUSDB05", "type": "index"}, {"default_display": false, "id": "349198f3-0725-44d1-bc5e-511118cc941b", "metric": "", "name": "MQUSDB06", "type": "index"}, {"default_display": false, "id": "ad7e4c24-2365-48e9-b8db-3fa894668a99", "metric": "", "name": "MQUSDB07", "type": "index"}, {"default_display": false, "id": "c75069d9-b034-41e1-9a03-e8e22a90c6d9", "metric": "", "name": "MQUSDB08", "type": "index"}, {"default_display": false, "id": "c2ed3e84-9f11-429c-b308-7a56efdd7d5c", "metric": "", "name": "MQUSDB09", "type": "index"}, {"default_display": false, "id": "c4a24768-92bf-4dc8-90d9-cb2311a75946", "metric": "", "name": "MQUSDB10", "type": "index"}, {"default_display": false, "id": "2298d1db-f0eb-44ff-8cb6-23d5bdb10857", "metric": "", "name": "MQUSDB11", "type": "index"}, {"default_display": false, "id": "db167f04-4753-4fb4-8a21-e48b1aa397fe", "metric": "", "name": "MQUSDB12", "type": "index"}], "run_configuration": {"job_enabled": true, "num_days_to_load": 0, "schedule": {"retries": 25, "retry_interval_min": 10, "schedule_start": "2021-04-12 17:30:00"}, "tzinfo": "US/Eastern"}, "spec": {"index_class": "merq.indices.deep_buffer_index.DeepBufferIndex", "index_class_args": {"buffer_end": 0.7, "buffer_start": 0.95, "fee": 0.0, "id": "MQUSDB05", "month": 5, "root": "SPY"}}, "stage": "prod", "status": {"created_at": "", "created_by": "", "last_modified": "2021-07-20T23:03:25.202599"}, "table": "MQUSDB05", "tags": "defined_outcome", "title": "MerQube US Large Cap May Deep Buffer Index", "weighting_method": "Other"}'
        t = datamethods.proddata(json.loads(testdata))
        output={'name': 'MQUSDB05', 'title': 'MerQube US Large Cap May Deep Buffer Index', 'last_date': '2021-07-29T00:00:00',
         'last_level': 2446.6298643072923}

        self.assertEqual(t, output)