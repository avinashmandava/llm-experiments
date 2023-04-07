from external_apis import datadog
import numpy as np

def get_formatted_metrics(technology):
  # You can add addtional technologies here, just list the metrics you wnat to use and add an if statement.
  if technology == 'PostgreSQL':
    metrics_list = ['postgresql.rows_returned', 'postgresql.rows_updated']
  else:
    raise ValueError(f'No metrics found for {technology}')
  metric_data = {}
  for metric in metrics_list:
    try:
      data = datadog.get_time_series('avg', metric)['data']['attributes']['values'][0]
      current = data[-1]
      mean = np.mean(data)
      std = np.std(data)
      z = (current-mean)/std
      metric_data[metric] = {
        'mean': mean,
        'std': std,
        'current_value': current,
        'z_score': z
      }
    except:
      continue

  return metric_data


