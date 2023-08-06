import calendar
from rich.table import Table
from rich.tree import Tree
from rich.panel import Panel
from rich import print
from datetime import datetime, timezone
from tickerdax.constants import URL


def truncate_datetime(date, timeframe):
    kwargs = {
        'year': date.year
    }
    if timeframe.endswith(('M', 'd', 'h', 'm')):
        kwargs['month'] = date.month

    if timeframe.endswith(('d', 'h', 'm')):
        kwargs['day'] = date.day

    if timeframe.endswith(('h', 'm')):
        kwargs['hour'] = date.hour

    if timeframe.endswith('m'):
        kwargs['minute'] = date.minute

    return datetime(
        tzinfo=timezone.utc,
        **kwargs
    )


def get_unix_time(date, timeframe):
    return float(calendar.timegm(truncate_datetime(date, timeframe).timetuple()))


def get_timestamp_range(since, till, timeframe):
    """
    Gets a range of timestamps between the start and end dates.

    :param datetime since: A start time.
    :param datetime till: A end time.
    :param str timeframe: The string value of the timeframe, i.e. 1m, 1h, 1d, etc.
    :rtype: list[int]
    """
    start = get_unix_time(since, timeframe)
    end = get_unix_time(till, timeframe)
    range_seconds = end - start
    timeframe_in_seconds = convert_timeframe_to_seconds(timeframe)
    time_intervals = range_seconds / timeframe_in_seconds

    timestamps = []
    for time_interval in range(int(time_intervals) + 1):
        timestamps.append(start + (time_interval * timeframe_in_seconds))

    return timestamps


def convert_timeframe_to_seconds(timeframe):
    seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
    return int(timeframe[:-1]) * seconds_per_unit[timeframe[-1]]


def show_download_summary(cached_items, downloaded_items, missing_items, missing_ranges):
    tree = Tree(f'- {cached_items} of the requested items were already cached.\n'
                f'- {downloaded_items} items were downloaded.\n'
                f'- {missing_items} items are missing.',)
    for key, values in missing_ranges.items():
        table = Table(title=key)
        table.add_column("Begins", style="cyan")
        table.add_column("Ends", style="green")

        for start, end in values:
            if start and end:
                table.add_row(
                    datetime.fromtimestamp(start).strftime('%Y-%m-%dT%H:%M:%S'),
                    datetime.fromtimestamp(end).strftime('%Y-%m-%dT%H:%M:%S')
                )
        tree.add(table)
    print(Panel(tree, title="Download Summary"))


def show_routes(routes):
    table = Table(title=f'All Available Routes from {URL}')
    table.add_column("Routes", style="cyan")
    table.add_column("Symbols", style="green")
    table.add_column("Timeframes", style="blue")
    for route in routes:
        table.add_row(
            route['route'],
            ','.join(route['symbols']),
            ','.join(route['timeframes'])
        )
    print()
    print(table)
