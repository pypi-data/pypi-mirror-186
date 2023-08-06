import os
import json
import yaml
import logging
from tickerdax.constants import NAME, Envs
from tickerdax.formatting import truncate_datetime, show_routes
from datetime import datetime, timezone
from tickerdax.client import TickerDax
from schema import Schema, And, Or, Optional
from pprint import pformat


class ConfigBase:
    """
    The base class that handles the loading and validating of the config.
    """

    def __init__(self, config=None, client_kwargs=None):
        if not client_kwargs:
            client_kwargs = {}

        self.client = TickerDax(**client_kwargs)

        self._logger = logging.getLogger(f'{TickerDax.__name__}.{self.__class__.__name__}')
        self._logger.setLevel(logging.INFO)

        self._config_file_path = os.environ.get(Envs.CONFIG.value, config)
        self._config = self._get_config_data()
        self._validate()

        self._timeframe = self._config.get('timeframe')
        self._now = datetime.now(tz=timezone.utc)
        self._since, self._till = self._get_time_range()

    def _validate(self):
        """
        Validates the class attributes.
        """
        timeframes = self.client.supported_timeframes
        schema = Schema({
            'routes': And(dict),
            'timeframe': And(str, lambda s: s in timeframes,
                             error=f'Your configs timeframe is not one of the supported timeframes {timeframes}'),
            'start': Or(str, datetime),
            Optional('end'): Or(str, datetime),
            Optional('fill_to_now'): And(bool),
            Optional('force'): And(bool)
        })
        schema.validate(self._config)

        available_routes_data = self.client.get_available_routes()
        available_routes = [route_data['route'] for route_data in available_routes_data]
        for route in self._config.get('routes', {}).keys():
            if route not in available_routes:
                show_routes(available_routes_data)
                self.client.report_error(
                    f'The route "{route}" is not valid. Possible routes are shown above.'
                )

    def _get_config_data(self):
        """
        Gets the data from the config file.

        :return dict: A dictionary of config data.
        """
        if os.path.exists(self._config_file_path):
            _, extension = os.path.splitext(self._config_file_path)
            with open(self._config_file_path, 'r') as config_file:
                if extension == '.json':
                    return json.load(config_file).get(NAME, {})
                elif extension in ['.yaml', '.yml']:
                    return yaml.safe_load(config_file).get(NAME, {})
        else:
            raise self.client.report_error(f'The config file "{self._config_file_path}" does not exist on disk')

    def _get_time_range(self):
        """
        Gets the UTC start and end times for the data download.

        :return tuple(datetime, datetime):
        """
        start_string = self._config.get('start')
        end_string = self._config.get('end')

        if isinstance(start_string, str):
            start = datetime.strptime(start_string, '%Y-%m-%dT%H:%M:%S')
        else:
            start = start_string

        # if there is no ending time the current time is used
        if end_string:
            if isinstance(start_string, str):
                end = datetime.strptime(end_string, '%Y-%m-%dT%H:%M:%S')
            else:
                end = end_string
        else:
            end = self._now

        return truncate_datetime(start, self._timeframe), truncate_datetime(end, self._timeframe)
