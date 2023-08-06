## Signal Ads Python SDK

## Usage

- Send Single SMS

```python

from signal import SignalAdsApi

signal = SignalAdsApi()

signal.set_api_key('your-api-key')

sender = '5000'
text = 'test'
receptor = '09121234567'

signal.send_single_sms(sender, text, receptor)

```

`Sample Output`

```json

{
  "data": {
    "message_id": "2bb0220b-...",
    "price": 160
  },
  "message": "پیام شما با موفقیت در صف ارسال قرار گرفت",
  "error": {
    "message": null,
    "errors": null
  }
}

```


- Send Multiple SMS With Same Text

```python

from signal import SignalAdsApi

signal = SignalAdsApi()

signal.set_api_key('your-api-key')

sender = '5000'
text = 'test'
receptors = ['09121234567']

signal.send_multiple_sms(sender, text, receptors)

```

`Sample Output`

```json

{
  "data": {
    "message_id": "755455f6-....",
    "price": 160
  },
  "message": "پیام شما با موفقیت در صف ارسال قرار گرفت",
  "error": {
    "message": null,
    "errors": null
  }
}

```

- Send Multiple SMS With Multiple Text

```python

from signal import SignalAdsApi

signal = SignalAdsApi()

signal.set_api_key('your-api-key')

sender = '5000'
pairs = [{'text': 'Hi', 'receptor': '09123456789'}]

signal.send_pair_to_pair_sms(sender, pairs)

```

`Sample Output`

```json

{
  "data": {
    "message_id": "bb6100b3-....",
    "price": 160
  },
  "message": "پیام شما با موفقیت در صف ارسال قرار گرفت",
  "error": {
    "message": null,
    "errors": null
  }
}

```

- Send Sms With Pattern

```python

from signal import SignalAdsApi

signal = SignalAdsApi()

signal.set_api_key('your-api-key')

sender = '5000'
pattern_id = '10'
pattern_params = ['param1', 'param2', 'param3']
receptors = ['09121234567']

signal.send_sms_with_pattern(sender, pattern_id, pattern_params, receptors)

```

`Sample Output`

```json

{
  "data": {
    "message_id": "bb6100b3-....",
    "price": 160
  },
  "message": "پیام شما با موفقیت در صف ارسال قرار گرفت",
  "error": {
    "message": null,
    "errors": null
  }
}

```

- Get account credit

```python

from signal import SignalAdsApi

signal = SignalAdsApi()

signal.set_api_key('your-api-key')

signal.get_account_credit()

```

`Sample Output`

```json

{
  "data": {
    "credit": "333946"
  },
  "message": null,
  "error": {
    "message": null,
    "errors": null
  }
}

```
