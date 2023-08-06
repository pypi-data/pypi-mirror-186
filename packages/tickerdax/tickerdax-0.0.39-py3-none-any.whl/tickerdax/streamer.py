from tickerdax.constants import KeyTypes
from tickerdax.config_base import ConfigBase
from tickerdax.downloader import Downloader


class Streamer(ConfigBase):
    """
    Streams data from the tickerdax.com websocket api to the cache using a provided config.
    """
    def __init__(self, config, client_kwargs=None):
        super(Streamer, self).__init__(config, client_kwargs)
        self.stream()

    def _validate(self):
        """
        Validates the class attributes and the websocket api key.
        """
        super(Streamer, self)._validate()
        self.client.validate_api_key(KeyTypes.WEBSOCKET)

    def stream(self):
        """
        Downloads data from the algo trading REST API base on the bot config files.
        """
        routes = self._config.get('routes', {})
        if routes:
            # unless told not to, fill the history from the start date in the config till now
            if self._config.get('fill_to_now', True):
                Downloader(
                    config=self._config_file_path,
                    client_kwargs={'log_connection': False},
                    till_now=True
                )

            # stream updates to the cache indefinitely
            self._logger.info(f'Starting streams...')
            self.client.stream(routes=routes)