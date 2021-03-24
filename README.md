# normetapi
A Python library for interacting with the [MET Norway Weather API](https://api.met.no/).

## Installation

```bash
pip install normetapi
```

## Examples

```python
from normetapi import location_forecast

# Get forcast for Trondheim:
forecast = location_forecast(63.4107, 10.4538)
print(forecast)
```

```python
from normetapi import nowcast

# Get nowcast for Trondheim:
forecast = nowcast(63.4107, 10.4538, altitude=123)
print(forecast)
```

```python
from normetapi import weathericon

# Get icons:
_, legend = weathericon(output_file='icons.tgz')
print(legend)
```
