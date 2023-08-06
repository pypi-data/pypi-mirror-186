from tickerdax.constants import KeyTypes
from tickerdax.config_base import ConfigBase
from tickerdax.formatting import truncate_datetime, convert_timeframe_to_seconds, show_download_summary


class Downloader(ConfigBase):
    """
    Downloads data from the tickerdax.com data api using a provided config.
    """
    def __init__(self, config, client_kwargs=None, till_now=False):
        super(Downloader, self).__init__(config, client_kwargs)
        self._missing_data = {}

        # forces the end to be now
        if till_now:
            self._till = truncate_datetime(self._now, self._timeframe)

        self.download()

    def _validate(self):
        super(Downloader, self)._validate()
        self.client.validate_api_key(KeyTypes.REST)

    def track_missing_ranges(self, route):
        self.client.missing_values.sort(key=lambda i: i['timestamp'])
        for missing_value in self.client.missing_values:
            path = f"{route}/{missing_value['symbol']}/{self._timeframe}"
            if not self._missing_data.get(path):
                self._missing_data[path] = []

            if missing_value not in self._missing_data[path]:
                self._missing_data[path].append(missing_value)

    def get_missing_ranges(self):
        ranges = {}
        for route, missing_values in self._missing_data.items():
            ranges[route] = []

            last_missing_timestamp = None
            gap_start_timestamp = None

            for missing_value in missing_values:
                if not gap_start_timestamp:
                    gap_start_timestamp = missing_value['timestamp']

                if last_missing_timestamp:
                    incremented_timestamp = last_missing_timestamp + convert_timeframe_to_seconds(self._timeframe)
                    if missing_value['timestamp'] != incremented_timestamp:
                        ranges[route].append([gap_start_timestamp, last_missing_timestamp])
                        gap_start_timestamp = None

                last_missing_timestamp = missing_value['timestamp']
            ranges[route].append([gap_start_timestamp, last_missing_timestamp])

        return ranges

    def download(self):
        """
        Downloads data from the algo trading REST API base on the bot config files.
        """
        downloaded_items = 0
        cached_items = 0
        missing_items = 0

        routes = self._config.get('routes', {})
        if routes:
            for route, symbols in routes.items():
                self._logger.info(f'Downloading {route} history from "{self._since}" to "{self._till}"...')
                self.client.get_route(
                    route=route,
                    symbols=symbols,
                    since=self._since,
                    till=self._till,
                    timeframe=self._timeframe
                )
                self._logger.info(f'Completed {len(self.client.rest_values)} "{route}" downloads')
                cached_items += len(self.client.cached_values)
                downloaded_items += len(self.client.rest_values)
                missing_items += len(self.client.missing_values)
                self.track_missing_ranges(route)

            if downloaded_items:
                self._logger.info('Saving download to disk..')
                self.client.redis_client.bgsave()

            self._logger.info('Preparing summary...')
            show_download_summary(
                cached_items=cached_items,
                downloaded_items=downloaded_items,
                missing_items=missing_items,
                missing_ranges=self.get_missing_ranges()
            )