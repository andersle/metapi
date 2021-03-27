# normetapi
A Python library for interacting with the [MET Norway Weather API](https://api.met.no/).

## Installation

```bash
pip install normetapi
```

## Examples

### Getting a forcast for a specified location:

```python
from normetapi import location_forecast

# Get forcast for Trondheim:
forecast = location_forecast(63.4107, 10.4538)
print(forecast)
```

The forcast will be returned as a dict. See the description
of [locationforcast](https://api.met.no/weatherapi/locationforecast/2.0/documentation)
in the [MET Norway Weather API description](https://api.met.no/).

### Getting the immediate forecast for a specified location:

```python
from normetapi import nowcast

# Get nowcast for Trondheim:
forecast = nowcast(63.4107, 10.4538, altitude=123)
print(forecast)
```

The forcast will be returned as a dict. See the description
of [nowcast](https://api.met.no/weatherapi/nowcast/2.0/documentation)
in the [MET Norway Weather API description](https://api.met.no/).

### Getting weather icons:

```python
from normetapi import weathericon

# Get icons:
_, legend = weathericon(output_file='icons.tgz')
print(legend)
```

This will download weather icons as a gzipped tar archive
and return legends as a dictionary. See the
description of [weathericon](https://api.met.no/weatherapi/weathericon/2.0/documentation)
in the [MET Norway Weather API description](https://api.met.no/).
