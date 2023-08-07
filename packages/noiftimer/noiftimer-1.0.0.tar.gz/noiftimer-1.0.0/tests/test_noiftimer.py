import time

import pytest

import noiftimer


def test_noiftimer_start():
    timer = noiftimer.Timer()
    timer.start()
    assert timer.start_time
    assert timer.started is True


def test_noiftimer_stop():
    timer = noiftimer.Timer()
    timer.start()
    time.sleep(2)
    timer.stop()
    assert timer.stop_time
    assert not timer.started
    assert timer.elapsed_time > 1
    assert timer.elapsed_time == timer.average_elapsed_time


def test_noiftimer__save_elapsed_time():
    averaging_window_length = 10
    timer = noiftimer.Timer(averaging_window_length)
    timer.start()
    timer.stop()
    assert len(timer.history) == 1
    for _ in range(averaging_window_length):
        timer.start()
        timer.stop()
    assert len(timer.history) == averaging_window_length


def test_noiftimer_current_elapsed_time():
    timer = noiftimer.Timer()
    timer.start()
    time.sleep(1)
    elapsed_time = timer.current_elapsed_time(format=False)
    time.sleep(1)
    assert 0 < elapsed_time and elapsed_time < timer.current_elapsed_time(format=False)
    assert type(timer.current_elapsed_time()) == str


@pytest.mark.parametrize(
    "num_seconds,seconds_per_unit,unit_suffix,expected",
    [
        (124, 60, "m", (4, "2m")),
        (16200, 3600, "h", (1800, "4h")),
        (16202, 60, "m", (2, "270m")),
        (14837284, 604800, "w", (322084, "24w")),
    ],
)
def test_noiftimer__get_time_unit(num_seconds, seconds_per_unit, unit_suffix, expected):
    timer = noiftimer.Timer()
    assert timer._get_time_unit(num_seconds, seconds_per_unit, unit_suffix) == expected


@pytest.mark.parametrize(
    "num_seconds,subsecond_resolution,expected",
    [
        (3600, False, "1h"),
        (1800, False, "30m"),
        (5400, False, "1h 30m"),
        (
            (29030400) + (604800 * 2) + (3600 * 3) + (44.250043),
            True,
            "1y 2w 3h 44s 250ms 43us",
        ),
        (
            (29030400) + (604800 * 2) + (3600 * 3) + (44.250043),
            False,
            "1y 2w 3h 44s",
        ),
    ],
)
def test_noiftimer_format_time(num_seconds, subsecond_resolution, expected):
    timer = noiftimer.Timer()
    assert timer.format_time(num_seconds, subsecond_resolution) == expected


def test_noiftimer_get_stats():
    timer = noiftimer.Timer()
    timer.start()
    time.sleep(1)
    timer.stop()
    assert type(timer.get_stats()) == str
    assert type(timer.get_stats(False)) == str
