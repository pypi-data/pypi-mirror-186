import requests
import pandas as pd
from urllib.parse import urlencode, quote

timestamp = 1667304000
chain = 'Ethereum'
bridge_id = 5

# dd = dict(excludeTotalDataChart='true',
#           excludeTotalDataChartBreakdown='true',
#           dataType=data_type)
# param = urlencode(dd, quote_via=quote)

base_url = "https://bridges.llama.fi"
url = base_url + f'/bridgedaystats/{timestamp}/{chain}?id={bridge_id}'
resp = requests.Session()\
    .request('GET', url, timeout=30).json()
resp

df = pd.DataFrame(resp)
df['date'] = pd.to_datetime(df['date'], unit='s', utc=True)
df = df.set_index('date')
df.loc['2022-09-01':'2022-09-04', :]