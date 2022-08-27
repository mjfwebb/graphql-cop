"""Collect trace mode details."""
from lib.utils import graph_query, curlify


def trace_mode(url, proxy, headers):
  """Get the trace mode."""
  res = {
    'result':False,
    'title':'Trace Mode',
    'description':'Tracing is Enabled',
    'impact':'Information Leakage',
    'severity':'INFO',
    'curl_verify':''
  }

  q = 'query cop { __typename }'
  gql_response = graph_query(url, proxies=proxy, headers=headers, payload=q)
  res['curl_verify'] = curlify(gql_response)

  try:
    if gql_response.json()['errors'][0]['extensions']['tracing']:
      res['result'] = True
    elif 'stacktrace' in str(gql_response.json()).lower():
      res['result'] = True
  except:
    pass

  return res
