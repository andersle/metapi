# Copyright (c) 2021, Anders Lervik.
# Distributed under the MIT License. See LICENSE for more info.
"""A module for interfacing the MET Norway Weather API."""
import json
import requests


API_URL = 'https://api.met.no/weatherapi'


STATUS = {
    200: 'OK',
    203: 'Non-Authorative Information - deprecated product version',
    304: 'Not Modified',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'No data from the product handler',
    422: 'Unprocessable Entity',
    429: 'Too Many Requests',
    499: 'Client Closed Request',
    500: 'Internal Server Error',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Time-out',
}


def _check_status(response):
    """Check the status of a requests response."""
    status = response.status_code
    if status in STATUS:
        return status == 200, status, STATUS[status]
    return False, status, response.content


def get_request(url, decode=None):
    """Get some data using the API and the provided url."""
    headers = {
        'User-Agent': 'https://github.com/andersle/normetapi',
    }
    response = requests.get(url, headers=headers)
    request_ok, status, msg = _check_status(response)
    data = None
    if request_ok:
        data = response.content
        if decode is not None:
            data = data.decode('utf-8')
    else:
        print('Could not get data:')
        print(f'Status: {status}')
        print(f'MSG: {msg}')
    return data


def location_forecast(lat, lon, altitude=None, style='compact'):
    """Get a location forecast for the given lat, lon location.

    Parameters
    ----------
    lat : float
        The latitude to get the forecast for.
    lon : float
        The longitude to get the forecast for.
    altitude : int, optional
        The height above sea level to get the forecast for.
    style : string, optional
        Selects the type of forcast we will get. Two options are
        supported:

        * complete: JSON forecast with all values.

        * compact: A shorter version with only the most used
          parameters.


    Returns
    -------
    data : dict
        The raw data containing the forecast.

    See Also
    --------
    https://api.met.no/weatherapi/locationforecast/2.0/documentation

    """
    if style not in ('compact', 'complete'):
        raise ValueError('"style" must be "compact" or "complete".')
    url = f'{API_URL}/locationforecast/2.0/{style}?lat={lat}&lon={lon}'
    if altitude is not None:
        url += f'&altitude={altitude}'
    data = json.loads(get_request(url, decode='utf-8'))
    return data


def weathericon(output_file=None, legends=True):
    """Download archive of weather icons.

    Parameters
    ----------
    output_file : string, optional
        A file name which we will write the icon archive to.
    legends : boolean, optional
        Determines if we also attempt to download legends.

    Returns
    -------
    data : string
        The raw data (gzipped TAR).
    legend : dict
        Legends, if requested.

    See Also
    --------
    https://api.met.no/weatherapi/weathericon/2.0/documentation

    """
    url = f'{API_URL}/weathericon/2.0/data'

    data = get_request(url)
    if output_file is not None:
        with open(output_file, 'wb') as output:
            output.write(data)
    legend = {}
    if legends:
        url = f'{API_URL}/weathericon/2.0/legends'
        legend = json.loads(get_request(url))
    return data, legend
