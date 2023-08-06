# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['weather_provider_api',
 'weather_provider_api.core',
 'weather_provider_api.core.errors',
 'weather_provider_api.core.initializers',
 'weather_provider_api.routers',
 'weather_provider_api.routers.weather',
 'weather_provider_api.routers.weather.base_models',
 'weather_provider_api.routers.weather.repository',
 'weather_provider_api.routers.weather.sources',
 'weather_provider_api.routers.weather.sources.cds',
 'weather_provider_api.routers.weather.sources.cds.client',
 'weather_provider_api.routers.weather.sources.cds.models',
 'weather_provider_api.routers.weather.sources.knmi',
 'weather_provider_api.routers.weather.sources.knmi.client',
 'weather_provider_api.routers.weather.sources.knmi.models',
 'weather_provider_api.routers.weather.sources.weather_alert',
 'weather_provider_api.routers.weather.utils',
 'weather_provider_api.scripts',
 'weather_provider_api.versions']

package_data = \
{'': ['*']}

install_requires = \
['accept-types>=0.4.1,<0.5.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'cfgrib>=0.9.10.3,<0.10.0.0',
 'eccodes>=1.5.0,<2.0.0',
 'ecmwflibs>=0.5.0,<0.6.0',
 'fastapi>=0.88.0,<0.89.0',
 'geopy>=2.3.0,<3.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'lxml>=4.9.1,<5.0.0',
 'netcdf4>=1.6.2,<2.0.0',
 'numpy>=1.23.5,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'starlette-prometheus>=0.9.0,<0.10.0',
 'structlog>=22.3.0,<23.0.0',
 'tomli>=2.0.1,<3.0.0',
 'uvicorn>=0.20.0,<0.21.0',
 'xarray>=2022.12.0,<2023.0.0']

entry_points = \
{'console_scripts': ['wpla_clear_arome = '
                     'weather_provider_api.scripts.erase_arome_repository:main',
                     'wpla_clear_era5land = '
                     'weather_provider_api.scripts.erase_era5land_repository:main',
                     'wpla_clear_era5sl = '
                     'weather_provider_api.scripts.erase_era5sl_repository:main',
                     'wpla_run_api = weather_provider_api.main:main',
                     'wpla_update_arome = '
                     'weather_provider_api.scripts.update_arome_repository:main',
                     'wpla_update_era5land = '
                     'weather_provider_api.scripts.update_era5land_repository:main',
                     'wpla_update_era5sl = '
                     'weather_provider_api.scripts.update_era5sl_repository:main']}

setup_kwargs = {
    'name': 'weather-provider-api',
    'version': '2.32.113',
    'description': 'Weather Provider Libraries and API',
    'long_description': "<!--\nSPDX-FileCopyrightText: 2019-2022 Alliander N.V.\nSPDX-License-Identifier: MPL-2.0\n-->\n[![License: MIT](https://img.shields.io/badge/License-MPL2.0-informational.svg)](https://github.com/alliander-opensource/weather-provider-api/blob/master/LICENSE)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-api&metric=alert_status)](https://sonarcloud.io/dashboard?id=alliander-opensource_Weather-Provider-API)\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-api&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=alliander-opensource_Weather-Provider-API)\n[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-api&metric=security_rating)](https://sonarcloud.io/dashboard?id=alliander-opensource_Weather-Provider-API)\n[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-api&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=alliander-opensource_Weather-Provider-API)\n[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-api&metric=bugs)](https://sonarcloud.io/dashboard?id=alliander-opensource_Weather-Provider-API)\n<!--[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=alliander-opensource_weather-provider-api&metric=coverage)](https://sonarcloud.io/dashboard?id=alliander-opensource_Weather-Provider-API)-->\n\n# Weather Provider Library and API\n\nThis API is intended to help you fetch weather data from different data sources in an efficient and uniform way.\nBy just supplying a list of locations and a time window you can get data for a specific source immediately.\n\nThis project can currently be found on the following location:\nhttps://github.com/alliander-opensource/Weather-Provider-API\n\nFor more information also check out this webinar:\n\n[![Webinar Weather Provider API](https://img.youtube.com/vi/pjE0DZmSphQ/0.jpg)](https://www.youtube.com/watch?v=pjE0DZmSphQ)\n\n\nThe project uses a number of data sources for the acquisition of weather data. Currently being supported by this API \nare the following weather data sources:\n\n**DATA SOURCE #1: KNMI Historical data per day / hour**\n\nConsists of the data from 35 weather stations for temperature, sun, cloud, air pressure, wind and precipitation.\n\nA full description of available weather variables is available for the data per day:\nhttp://projects.knmi.nl/klimatologie/daggegevens/selectie.cgi\n\nA full description for the data per hour consists only of a subset of the previous list:\nhttp://projects.knmi.nl/klimatologie/uurgegevens/selectie.cgi\n\n**DATA SOURCE #2: KNMI prediction data (14 day prediction, per block of 6 hours)**\n\nPrediction data for weather stations:\nDe Bilt, Den Helder(De Kooy), Groningen(Eelde), Leeuwarden, Maastricht(Beek), Schiphol, Twente en Vlissingen\n\nAvailable weather variables are temperature, wind, precipitation, cape for summer, and snow for winter.\n\nAn interactive graph can be found at:<BR>\nhttps://www.knmi.nl/nederland-nu/weer/waarschuwingen-en-verwachtingen/weer-en-klimaatpluim\n\n**DATA SOURCE #3: KNMI prediction data (48 hour, per hour prediction)**\n\nPrediction data is updated every 6 hours (00, 06, 12 and 18 UTC+00) based on the HARMONIE AROME model of KNMI.\n\nGeographical resolution is 0.037 grades west-east and 0.023 grades north-south.\n\nA full description of available weather variables is available at:\nhttps://www.knmidata.nl/data-services/knmi-producten-overzicht/atmosfeer-modeldata/data-product-1\n\n**DATA SOURCE #4: KNMI current weather data()**\n>> Actuele waarnemingen\n\n**DATA SOURCE #5: CDS (Climate Data Store) hourly data from 1979 to present**\n\nERA5 is the fifth generation ECMWF (European Centre for Medium Range Weather Forecast)\natmospheric reanalysis of the global climate.\nERA5 data released so far covers the period from 1979 to 2-3 months before the present.\nERA5 provides worldwide data for temperature and pressure, wind (at 100 meter height),\nradiation and heat, clouds, evaporation and runoff, precipitation and rain, snow, soil, etc.\nThe spatial resolution of the data set is approximately 80 km.\n\nA full description of available weather variables is available at:\nhttps://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview\n\nNOTE: The Weather Provider Library and API currently only stores only a selection of the available variables\nin its archives.\n\n## Input parameters to use the API\n\n### General input parameters\n\n- coords: nested 3-layer list representing a list of polygon.\nIn case of points, they are treated as one-point polygon\n- start: start time of output data, for prediction data this is not needed\n- end: end time of output data, for prediction data this is not needed\n- data_time: history or prediction data\n- data_source: KNMI, Climate Data Store(CDS, not available yet), DarkSky (not available yet)\n- data_timestep: day, hour, or day_part (6 hour)\n- weather_factors: list of weather factors,\n            default is all available weather factors\n- output_unit: org (original), human_readable or SI (International System of Units),\n            default is the original names and units in data sources.\n### Case specific input parameters\n#### Choosing (a group of) weather variables for historical data from KNMI\nFor historical data from KNMI the value for ``` weather_factors ``` in input can be a list of desired variables in random order,\nindicated by their acronyms separated by ':',\nfor example ``` TG: TN: EV24 ```.\n\nThe following acronyms are defined to indicate groups of variables:\n* **WIND = DDVEC:FG:FHX:FHX:FX** - *wind*\n* **TEMP = TG:TN:TX:T10N** - *temperature*\n* **SUNR = SQ:SP:Q** - *sunshine duration and global radiation*\n* **PRCP = DR:RH:EV24** - *precipitation and evaporation*\n* **PRES = PG:PGX** - *pressure at sea level*\n* **VICL = VVN:VVX:NG** - *visibility and clouds*\n* **MSTR = UG:UX:UN** - *humidity*\n* **ALL** - *all variables (default)*\n\n#### Choosing the name and unit for output\nThe output data from the four data sources of KNMI may have different names and units for the same weather variable,\nwhich may not easy to use in analytics.\n\nThis API provides an option to chose a standard name/unit for the mostly used weather variables, see table below.\nThe value of  ``` output_unit ``` in input can be set to:\n* ``` org ```: to keep the originally used names and units\n* ``` SI ```: to convert the variable-names into SI/human readable name,\nand convert the units into SI units\n* ``` human ```: to convert the variable-names into SI/human readable name,\nand convert the units into human-readable units.\n\n\n| Hist day name | Hist day unit | Hist hour name | Hist hour unit | Forecast 14d name | Forecast 14d unit | Forecast 48h name | Forecast 48h unit | SI/Human readable name |    SI unit    | Human readable unit |\n| :-----------: |:-------------:| :-------------:| :------------: |:-----------------:| :----------------:| :---------------- |:-----------------:| :---------------------:| :-----------: |:-------------------:|\n| FG            | 0.1 m/s       | FH             | 0.1 m/s        | wind_speed        | km/uur            |                   |                   | wind_speed             | m/s           | m/s                 |\n| FHX           | 0.1 m/s       | FX             | 0.1 m/s        |                   |                   |                   |                   | wind_speed_max         | m/s           | m/s                 |\n| TG            | 0.1 celsius   | T              | 0.1 celsius    | temperature       | celsius           | 2T                | K                 | temperature            | K             | celsius             |\n| Q             | J/cm2         | Q              | J/cm2          |                   |                   | GRAD              | J m**-2           | global_radiation       | J/m2          | J/m2                |\n| RH            | 0.1 mm        | RH             | 0.1 mm         | precipitation     | mm                |                   |                   | precipitation          | m             | mm                  |\n| PG            | 0.1 hPa       | P              | 0.1 hPa        |                   |                   | LSP               | Pa                | air_pressure           | Pa            | Pa                  |\n| NG            | [1,2…9]      | N              | [1,2…9]       |                   |                   |                   |                   | cloud_cover            | [1,2…9]      | [1,2…9]             |\n| UG            | %             | U              | %              |                   |                   |                   |                   | humidity               | %             | %                   |\n\nThe CDS data uses only SI units, and as such there is no distinction between ``` org ``` and ``` si ``` .\n\n## Getting started - using as a package/project\n### Prerequisites\n\nThis package is supported from Python 3.8 or later. See '''requirements.txt''' for a list of dependencies.\nThis package works under at least Linux and Windows environments. (Other Operating Systems not tested)\n\n### Installing\n\n1. Clone the repo\n2. Navigate to root\n3. Install the dependencies using conda/pip or both, depending on your environment\n```\nconda install --file requirements.txt\n```\n```\npip install -r requirements.txt\n```\n4. Ready for use!\n\n### Using as a full project\nThe full API can now be run by executing:\n```main.py```\nWith the exception of ERA5 Single Levels and Harmonie Arome data, every data source can now be accessed\nusing either the created end points or the API docs interface at the running location.\n(127.0.0.1:8080 when running locally)\n\nSpecific calls can now be run by executing the proper command. For examples, check out the **\\bin** folder.\n\n### Using as a wheel\nInstall the wheel into your project environment and import the required classes.\nUsually this will be either a specific Weather Model or the Weather Controller.\n\n## Contributing\n\nPlease read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.\n\n## Contact\nTo contact the project owners directly please e-mail us at [weather.provider@alliander.com](mailto://weather.provider@alliander.com)\n            \n## Authors\n\nThis project was initially created by:\n\n* **Tongyou Gu** - *Original API development*\n* **Jeroen van de Logt** - *Functions in utilities*\n* **Bas Niesink** - *Implementation weather REST API*\n* **Raoul Linnenbank** - *Active API Development, Geo positioning, CDS ERA5, caching, remodeling, Harmonie Arome and optimisation*\n\nCurrently, this project is governed in an open source fashion, this is documented in [PROJECT_GOVERNANCE](PROJECT_GOVERNANCE.md).\n\n## License\n\nThis project is licensed under the Mozilla Public License, version 2.0 - see LICENSE for details\n\n## Licenses third-party code\n\nThis project includes third-party code, which is licensed under their own respective Open-Source licenses. SPDX-License-Identifier headers are used to show which license is applicable. The concerning license files can be found in the LICENSES directory. \n\n## Acknowledgments\n\nThanks to team Inzicht & Analytics and Strategie & Innovatie to\nmake this project possible.\n\nA big thanks as well to Alliander for being the main sponsor for this open source project.  \n\nAnd of course a big thanks to the guys of IT New Business & R&D to provide\nsuch an easy-to-use Python environment in the cloud.\n",
    'author': 'Verbindingsteam',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alliander-opensource/wpla/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
