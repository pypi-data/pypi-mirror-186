""" Class definition for a Klaviyo metric """
from abc import ABC
import logging
from string import Template


class KlaviyoMetricError(Exception):
    """ Klaviyo metric exception class"""

    def __init__(self, msg):
        super(KlaviyoMetricError, self).__init__(msg)


class KlaviyoMetric(ABC):
    """ Base class for a Klaviyo metric

    Attributes:
        metric_name: Name of the Klaviyo metric.
    """
    # Metric related URLs and URL-templates used to make Klaviyo API calls
    _METRICS_INFO_URL = 'https://a.klaviyo.com/api/v1/metrics'
    _METRIC_EVENTS_BASE_URL = 'https://a.klaviyo.com/api/v1/metric'
    _METRIC_EVENTS_URL_TEMPLATE = Template(f'{_METRIC_EVENTS_BASE_URL}/$metric_id/timeline')

    # URL argument templates
    _METRIC_EVENTS_URL_ARGS_TEMPLATE = Template(
        f'since=$since_ts&count=$count&sort=$sort&api_key=$private_key'
    )
    _METRICS_INFO_URL_ARGS_TEMPLATE = Template(f'page=0&count=100&api_key=$private_key')

    def __init__(self, metric_name: str):
        self.metric_name = metric_name
        self._logger = logging.getLogger(__name__)

    @classmethod
    @property
    def metrics_info_url(cls):
        return cls._METRICS_INFO_URL

    @classmethod
    @property
    def metric_events_url(cls):
        return cls._METRICS_INFO_URL

    @classmethod
    def get_metric_events_url(cls, metric_id: str):
        """ Constructs URL for getting metric events given a metric identifier. """
        return cls._METRIC_EVENTS_URL_TEMPLATE.substitute(metric_id=metric_id)

    @classmethod
    def get_metric_events_url_args(cls, since: str, key: str, count: int = 100, sort: str = 'asc'):
        """ Gets the argument string for the Klaviyo API call given the parameters

        Args:
            since: Either a 10-digit Unix timestamp (UTC) to use as starting datetime, OR a
                pagination token obtained from the next attribute of a prior API call. For
                backwards compatibility, UUIDs will continue to be supported for a limited time.
                Defaults to current time.
            key: The Klaviyo API private key.
            count: Number of events to get per Klaviyo call.
            sort: Whether to crawl events going backward (desc) or forward (asc) in time.

        Returns:
            The part of the Klaviyo API call URL corresponding to the call parameters. E.g.
                since=1648368032&count=100&sort=asc&api=pk_000000000000000000000000000000000000
        """
        return cls._METRIC_EVENTS_URL_ARGS_TEMPLATE.substitute(
            since_ts=since,
            private_key=key,
            count=count,
            sort=sort
        )

    @classmethod
    def get_metrics_info_url_args(cls, key: str, count: int = 100):
        """ Gets the argument string for the Klaviyo API call given the parameters

        Args:
            key: The Klaviyo API private key.
            count: Number of events to get per Klaviyo call.

        Returns:
            The part of the Klaviyo API call URL corresponding to the call parameters. E.g.
                page=0&count=100&api_key=pk_000000000000000000000000000000000000
        """
        return cls._METRICS_INFO_URL_ARGS_TEMPLATE.substitute(
            private_key=key,
            count=count
        )
