# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wetterdienst',
 'wetterdienst.core',
 'wetterdienst.core.scalar',
 'wetterdienst.metadata',
 'wetterdienst.provider',
 'wetterdienst.provider.dwd',
 'wetterdienst.provider.dwd.metadata',
 'wetterdienst.provider.dwd.mosmix',
 'wetterdienst.provider.dwd.mosmix.metadata',
 'wetterdienst.provider.dwd.observation',
 'wetterdienst.provider.dwd.observation.metadata',
 'wetterdienst.provider.dwd.observation.util',
 'wetterdienst.provider.dwd.radar',
 'wetterdienst.provider.dwd.radar.metadata',
 'wetterdienst.provider.eaufrance',
 'wetterdienst.provider.eaufrance.hubeau',
 'wetterdienst.provider.eccc',
 'wetterdienst.provider.eccc.observation',
 'wetterdienst.provider.eccc.observation.metadata',
 'wetterdienst.provider.environment_agency',
 'wetterdienst.provider.environment_agency.hydrology',
 'wetterdienst.provider.eumetnet',
 'wetterdienst.provider.eumetnet.opera',
 'wetterdienst.provider.geosphere',
 'wetterdienst.provider.geosphere.observation',
 'wetterdienst.provider.noaa',
 'wetterdienst.provider.noaa.ghcn',
 'wetterdienst.provider.nws',
 'wetterdienst.provider.nws.observation',
 'wetterdienst.provider.wsv',
 'wetterdienst.provider.wsv.pegel',
 'wetterdienst.ui',
 'wetterdienst.ui.explorer',
 'wetterdienst.ui.explorer.layout',
 'wetterdienst.util']

package_data = \
{'': ['*'], 'wetterdienst.ui.explorer': ['assets/*']}

install_requires = \
['Pint>=0.17,<0.18',
 'PyPDF2>=1.26,<2.0',
 'aenum>=3.0,<4.0',
 'aiohttp>=3.8.1,<4.0.0',
 'beautifulsoup4>=4.9,<5.0',
 'cachetools>=5.2,<6.0',
 'click-params>=0.4,<0.5',
 'click>=8.0,<9.0',
 'cloup>=1.0,<2.0',
 'dateparser>=1.0,<2.0',
 'deprecation>=2.1,<3.0',
 'diskcache>=5.4.0,<6.0.0',
 'environs>=9.4.0,<10.0.0',
 'fsspec>=2022.02,<2023.0',
 'lxml>=4.9.1,<5.0.0',
 'measurement>=3.2,<4.0',
 'numpy>=1.22,<2.0',
 'pandas>=1.3,<2.0',
 'platformdirs>=2,<3',
 'python-dateutil>=2.8,<3.0',
 'rapidfuzz>=2.1,<3.0',
 'requests>=2.20,<3.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'tabulate>=0.8,<0.9',
 'timezonefinder>=6.1,<7.0',
 'tqdm>=4.47,<5.0']

extras_require = \
{'duckdb': ['duckdb>=0.6.0,<0.7.0'],
 'explorer': ['dash>=2,<3',
              'dash-bootstrap-components>=1,<2',
              'dash-leaflet>=0.1.23,<0.2.0',
              'geojson>=2.5.0,<3.0.0',
              'plotly>=5.11,<6.0'],
 'export': ['openpyxl>=3.0,<4.0',
            'sqlalchemy>=1.4,<2.0',
            'xarray>=2022.11,<2023.0'],
 'export:python_version < "3.11"': ['pyarrow>=10.0,<11.0', 'zarr>=2.13,<3.0'],
 'influxdb': ['influxdb>=5.3,<6.0', 'influxdb-client>=1.18,<2.0'],
 'interpolation': ['scipy>=1.9,<2.0', 'shapely>=1.8,<2.0', 'utm>=0.7,<0.8'],
 'ipython': ['matplotlib>=3.3,<4.0'],
 'mpl': ['matplotlib>=3.3,<4.0'],
 'mysql': ['mysqlclient>=2.0,<3.0'],
 'postgresql': ['psycopg2-binary>=2.8,<3.0'],
 'radar:python_version < "3.11"': ['h5py[radar]>=3.1,<4.0'],
 'radarplus': ['wradlib>=1.13,<2.0'],
 'restapi': ['fastapi>=0.65,<0.66', 'uvicorn>=0.14,<0.15'],
 'sql': ['duckdb>=0.6.0,<0.7.0']}

entry_points = \
{'console_scripts': ['wddump = wetterdienst.provider.dwd.radar.cli:wddump',
                     'wetterdienst = wetterdienst.ui.cli:cli']}

setup_kwargs = {
    'name': 'wetterdienst',
    'version': '0.52.0',
    'description': 'Open weather data for humans',
    'long_description': 'Wetterdienst - Open weather data for humans\n###########################################\n\n.. |pic1| image:: https://raw.githubusercontent.com/earthobservations/wetterdienst/main/docs/img/german_weather_stations.png\n    :alt: German weather stations managed by Deutscher Wetterdienst\n    :width: 32 %\n\n.. |pic2| image:: https://raw.githubusercontent.com/earthobservations/wetterdienst/main/docs/img/temperature_ts.png\n    :alt: temperature timeseries of Hohenpeissenberg/Germany\n    :width: 32 %\n\n.. |pic3| image:: https://raw.githubusercontent.com/earthobservations/wetterdienst/main/docs/img/hohenpeissenberg_warming_stripes.png\n    :alt: warming stripes of Hohenpeissenberg/Germany\n    :width: 32 %\n\n|pic1| |pic2| |pic3|\n\n**What our customers say:**\n\n"Our house is on fire. I am here to say, our house is on fire. I saw it with my own eyes using **wetterdienst**\nto get the data." - Greta Thunberg\n\n“You must be the change you wish to see in the world. And when it comes to climate I use **wetterdienst**.” - Mahatma Gandhi\n\n"Three things are (almost) infinite: the universe, human stupidity and the temperature time series of\nHohenpeissenberg, Germany I got with the help of **wetterdienst**; and I\'m not sure about the universe." - Albert Einstein\n\n"We are the first generation to feel the effect of climate change and the last generation who can do something about\nit. I used **wetterdienst** to analyze the climate in my area and I can tell it\'s getting hot in here." - Barack Obama\n\n.. image:: https://github.com/earthobservations/wetterdienst/workflows/Tests/badge.svg\n   :target: https://github.com/earthobservations/wetterdienst/actions?workflow=Tests\n   :alt: CI: Overall outcome\n.. image:: https://codecov.io/gh/earthobservations/wetterdienst/branch/main/graph/badge.svg\n   :target: https://codecov.io/gh/earthobservations/wetterdienst\n   :alt: CI: Code coverage\n.. image:: https://img.shields.io/pypi/v/wetterdienst.svg\n   :target: https://pypi.org/project/wetterdienst/\n   :alt: PyPI version\n.. image:: https://img.shields.io/conda/vn/conda-forge/wetterdienst.svg\n   :target: https://anaconda.org/conda-forge/wetterdienst\n   :alt: Conda version\n\n.. image:: https://img.shields.io/pypi/status/wetterdienst.svg\n   :target: https://pypi.python.org/pypi/wetterdienst/\n   :alt: Project status (alpha, beta, stable)\n.. image:: https://static.pepy.tech/personalized-badge/wetterdienst?period=month&units=international_system&left_color=grey&right_color=blue&left_text=PyPI%20downloads/month\n   :target: https://pepy.tech/project/wetterdienst\n   :alt: PyPI downloads\n.. image:: https://img.shields.io/conda/dn/conda-forge/wetterdienst.svg?label=Conda%20downloads\n   :target: https://anaconda.org/conda-forge/wetterdienst\n   :alt: Conda downloads\n.. image:: https://img.shields.io/github/license/earthobservations/wetterdienst\n   :target: https://github.com/earthobservations/wetterdienst/blob/main/LICENSE\n   :alt: Project license\n.. image:: https://img.shields.io/pypi/pyversions/wetterdienst.svg\n   :target: https://pypi.python.org/pypi/wetterdienst/\n   :alt: Python version compatibility\n\n.. image:: https://readthedocs.org/projects/wetterdienst/badge/?version=latest\n   :target: https://wetterdienst.readthedocs.io/en/latest/?badge=latest\n   :alt: Documentation status\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n   :alt: Documentation: Black\n\n.. image:: https://zenodo.org/badge/160953150.svg\n   :target: https://zenodo.org/badge/latestdoi/160953150\n   :alt: Citation reference\n\n\n.. overview_start_marker\n\nIntroduction\n############\n\nOverview\n********\n\nWelcome to Wetterdienst, your friendly weather service library for Python.\n\nWe are a group of like-minded people trying to make access to weather data in\nPython feel like a warm summer breeze, similar to other projects like\nrdwd_ for the R language, which originally drew our interest in this project.\nOur long-term goal is to provide access to multiple weather services as well as other\nrelated agencies such as river measurements. With ``wetterdienst`` we try to use modern\nPython technologies all over the place. The library is based on pandas_ across the board,\nuses Poetry_ for package administration and GitHub Actions for all things CI.\nOur users are an important part of the development as we are not currently using the\ndata we are providing and only implement what we think would be the best. Therefore\ncontributions and feedback whether it be data related or library related are very\nwelcome! Just hand in a PR or Issue if you think we should include a new feature or data\nsource.\n\n.. _rdwd: https://github.com/brry/rdwd\n.. _pandas: https://pandas.pydata.org/\n.. _Poetry: https://python-poetry.org/\n\nData\n****\n\nFor an overview of the data we have currently made available and under which\nlicense it is published take a look at the data_ section. Detailed information\non datasets and parameters is given at the coverage_ subsection. Licenses and\nusage requirements may differ for each provider so check this out before including\nthe data in your project to be sure that you fulfill copyright requirements!\n\n.. _data: https://wetterdienst.readthedocs.io/en/latest/data/index.html\n.. _coverage: https://wetterdienst.readthedocs.io/en/improve-documentation/data/coverage.html\n\nHere is a short glimpse on the data that is included:\n\n.. coverage_start_marker\n\nDWD (Deutscher Wetterdienst / German Weather Service / Germany)\n    - Historical Weather Observations\n        - Historical (last ~300 years), recent (500 days to yesterday), now (yesterday up to last hour)\n        - Every minute to yearly resolution\n        - Time series of stations in Germany\n    - Mosmix - statistical optimized scalar forecasts extracted from weather models\n        - Point forecast\n        - 5400 stations worldwide\n        - Both MOSMIX-L and MOSMIX-S is supported\n        - Up to 115 parameters\n    - Radar\n        - 16 locations in Germany\n        - All of Composite, Radolan, Radvor, Sites and Radolan_CDC\n        - Radolan: calibrated radar precipitation\n        - Radvor: radar precipitation forecast\n\nECCC (Environnement et Changement Climatique Canada / Environment and Climate Change Canada / Canada)\n    - Historical Weather Observations\n        - Historical (last ~180 years)\n        - Hourly, daily, monthly, (annual) resolution\n        - Time series of stations in Canada\n\nNOAA (National Oceanic And Atmospheric Administration / National Oceanic And Atmospheric Administration / United States Of America)\n    - Global Historical Climatology Network\n        - Historical, daily weather observations from around the globe\n        - more then 100k stations\n        - data for weather services which don\'t publish data themselves\n\nWSV (Wasserstraßen- und Schifffahrtsverwaltung des Bundes / Federal Waterways and Shipping Administration)\n    - Pegelonline\n        - data of river network of Germany\n        - coverage of last 30 days\n        - parameters like stage, runoff and more related to rivers\n\nEA (Environment Agency)\n    - Hydrology\n        - data of river network of UK\n        - parameters flow and ground water stage\n\nNWS (NOAA National Weather Service)\n    - Observation\n        - recent observations (last week) of US weather stations\n        - currently the list of stations is not completely right as we use a diverging source!\nEaufrance\n    - Hubeau\n        - data of river network of France (continental)\n        - parameters flow and stage of rivers of last 30 days\n\nZAMG (Central Institution for Meteorology and Geodynamics Austria)\n    - Observation\n        - historical meteorological data of Austrian stations\n\nTo get better insight on which data we have currently made available and under which\nlicense those are published take a look at the data_ section.\n\n.. coverage_end_marker\n\nFeatures\n********\n\n- API(s) for stations (metadata) and values\n- Get station(s) nearby a selected location\n- Define your request by arguments such as `parameter`, `period`, `resolution`,\n  `start date`, `end date`\n- Command line interface\n- Web-API via FastAPI\n- Run SQL queries on the results\n- Export results to databases and other data sinks\n- Public Docker image\n- Interpolation and Summary of station values\n\nSetup\n*****\n\nNative\n======\n\nVia PyPi (standard):\n\n.. code-block:: bash\n\n    pip install wetterdienst\n\nVia Github (most recent):\n\n.. code-block:: bash\n\n    pip install git+https://github.com/earthobservations/wetterdienst\n\nThere are some extras available for ``wetterdienst``. Use them like:\n\n.. code-block:: bash\n\n    pip install wetterdienst[http,sql]\n\n- docs: Install the Sphinx documentation generator.\n- ipython: Install iPython stack.\n- export: Install openpyxl for Excel export and pyarrow for writing files in Feather- and Parquet-format.\n- http: Install HTTP API prerequisites.\n- sql: Install DuckDB for querying data using SQL.\n- duckdb: Install support for DuckDB.\n- influxdb: Install support for InfluxDB.\n- cratedb: Install support for CrateDB.\n- mysql: Install support for MySQL.\n- postgresql: Install support for PostgreSQL.\n- interpolation: Install support for station interpolation.\n\nIn order to check the installation, invoke:\n\n.. code-block:: bash\n\n    wetterdienst --help\n\n.. _run-in-docker:\n\nDocker\n======\n\nDocker images for each stable release will get pushed to GitHub Container Registry.\n\nThere are images in two variants, ``wetterdienst-standard`` and ``wetterdienst-full``.\n\n``wetterdienst-standard`` will contain a minimum set of 3rd-party packages,\nwhile ``wetterdienst-full`` will try to serve a full environment by also\nincluding packages like GDAL and wradlib.\n\nPull the Docker image:\n\n.. code-block:: bash\n\n    docker pull ghcr.io/earthobservations/wetterdienst-standard\n\nLibrary\n-------\n\nUse the latest stable version of ``wetterdienst``:\n\n.. code-block:: bash\n\n    $ docker run -ti ghcr.io/earthobservations/wetterdienst-standard\n    Python 3.8.5 (default, Sep 10 2020, 16:58:22)\n    [GCC 8.3.0] on linux\n\n.. code-block:: python\n\n    import wetterdienst\n    wetterdienst.__version__\n\nCommand line script\n-------------------\n\nThe ``wetterdienst`` command is also available:\n\n.. code-block:: bash\n\n    # Make an alias to use it conveniently from your shell.\n    alias wetterdienst=\'docker run -ti ghcr.io/earthobservations/wetterdienst-standard wetterdienst\'\n\n    wetterdienst --help\n    wetterdienst version\n    wetterdienst info\n\nExample\n*******\n\n**Task: Get historical climate summary for two German stations between 1990 and 2020**\n\nLibrary\n=======\n\n.. code-block:: python\n\n    >>> import pandas as pd\n    >>> pd.options.display.max_columns = 8\n    >>> from wetterdienst import Settings\n    >>> from wetterdienst.provider.dwd.observation import DwdObservationRequest\n    >>> Settings.tidy = True  # default, tidy data\n    >>> Settings.humanize = True  # default, humanized parameters\n    >>> Settings.si_units = True  # default, convert values to SI units\n    >>> request = DwdObservationRequest(\n    ...    parameter=["climate_summary"],\n    ...    resolution="daily",\n    ...    start_date="1990-01-01",  # if not given timezone defaulted to UTC\n    ...    end_date="2020-01-01",  # if not given timezone defaulted to UTC\n    ... ).filter_by_station_id(station_id=(1048, 4411))\n    >>> request.df.head()  # station list\n        station_id                 from_date                   to_date  height  \\\n    ...      01048 1934-01-01 00:00:00+00:00 ... 00:00:00+00:00   228.0\n    ...      04411 1979-12-01 00:00:00+00:00 ... 00:00:00+00:00   155.0\n    <BLANKLINE>\n         latitude  longitude                    name    state\n    ...   51.1278    13.7543       Dresden-Klotzsche  Sachsen\n    ...   49.9195     8.9671  Schaafheim-Schlierbach   Hessen\n\n    >>> request.values.all().df.head()  # values\n      station_id          dataset      parameter                      date  value  \\\n    0      01048  climate_summary  wind_gust_max 1990-01-01 00:00:00+00:00    NaN\n    1      01048  climate_summary  wind_gust_max 1990-01-02 00:00:00+00:00    NaN\n    2      01048  climate_summary  wind_gust_max 1990-01-03 00:00:00+00:00    5.0\n    3      01048  climate_summary  wind_gust_max 1990-01-04 00:00:00+00:00    9.0\n    4      01048  climate_summary  wind_gust_max 1990-01-05 00:00:00+00:00    7.0\n    <BLANKLINE>\n       quality\n    0      NaN\n    1      NaN\n    2     10.0\n    3     10.0\n    4     10.0\n\nClient\n======\n\n.. code-block:: bash\n\n    # Get list of all stations for daily climate summary data in JSON format\n    wetterdienst stations --provider=dwd --network=observations --parameter=kl --resolution=daily\n\n    # Get daily climate summary data for specific stations\n    wetterdienst values --provider=dwd --network=observations --station=1048,4411 --parameter=kl --resolution=daily\n\nFurther examples (code samples) can be found in the examples_ folder.\n\n.. _examples: https://github.com/earthobservations/wetterdienst/tree/main/example\n\n.. overview_end_marker\n\nAcknowledgements\n****************\n\nWe want to acknowledge all environmental agencies which provide their data open and free\nof charge first and foremost for the sake of endless research possibilities.\n\nWe want to acknowledge Jetbrains_ and the `Jetbrains OSS Team`_ for providing us with\nlicenses for Pycharm Pro, which we are using for the development.\n\nWe want to acknowledge all contributors for being part of the improvements to this\nlibrary that make it better and better every day.\n\n.. _Jetbrains: https://www.jetbrains.com/\n.. _Jetbrains OSS Team: https://github.com/JetBrains\n\nImportant Links\n***************\n\n- Full documentation: https://wetterdienst.readthedocs.io/\n- Usage: https://wetterdienst.readthedocs.io/en/latest/usage/\n- Contribution: https://wetterdienst.readthedocs.io/en/latest/contribution/\n- Known Issues: https://wetterdienst.readthedocs.io/en/latest/known_issues/\n- Changelog: https://wetterdienst.readthedocs.io/en/latest/changelog.html\n- Examples (runnable scripts): https://github.com/earthobservations/wetterdienst/tree/main/example\n- Benchmarks: https://github.com/earthobservations/wetterdienst/tree/main/benchmarks\n',
    'author': 'Benjamin Gutzmann',
    'author_email': 'gutzemann@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://wetterdienst.readthedocs.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
