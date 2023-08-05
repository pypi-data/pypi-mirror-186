# pyspt - python simple pomodoro timer
[![PyPI version](https://badge.fury.io/py/pythonspt.svg)](https://badge.fury.io/py/pythonspt)

pyspt is a simple terminal timer that uses the pomodoro technique.

![screenshot](https://github.com/irizwaririz/pyspt/raw/main/screenshot.png)

## Installation

```
$ pip install pythonspt
```

## Usage

```
$ pyspt -h

usage: pyspt [-h] [-p POMODORO] [-sb SHORT_BREAK] [-lb LONG_BREAK] [-lbi LONG_BREAK_INTERVAL]

A simple terminal timer that uses the pomodoro technique.

options:
  -h, --help            show this help message and exit
  -p POMODORO, --pomodoro POMODORO
                        Pomodoro duration in minutes (default: 25)
  -sb SHORT_BREAK, --short-break SHORT_BREAK
                        Short break duration in minutes (default: 5)
  -lb LONG_BREAK, --long-break LONG_BREAK
                        Long break duration in minutes (default: 15)
  -lbi LONG_BREAK_INTERVAL, --long-break-interval LONG_BREAK_INTERVAL
                        Long break interval (default: 3)
```
