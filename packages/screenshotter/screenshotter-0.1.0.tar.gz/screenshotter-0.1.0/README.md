# Screenshotter

A simple utility for automatically taking full-screen screenshots at a fixed rate.

## Installation

Note that `screenshotter` requires [Python 3](https://www.python.org/downloads/).

```
git clone https://github.com/cvaugh/screenshotter.git
cd screenshotter
pip install -e .
```

## Usage

```
screenshotter [--screen <id>] [--outdir <path>] [--list-screens] <rate> <unit>
```

|Argument|Description|
|--------|-----------|
|`rate`|The rate at which to take screenshots.|
|`unit`|The unit of the rate argument. This must be one of `seconds`, `minutes`, `hours`, `s`, `m`, or `h`.|
|`--screen`|Screenshots will be taken of this screen. Use `--list-screens` to find your desired screen's ID. Defaults to the primary screen.|
|`--outdir`|Screenshots will be saved in this directory. Defaults to the current working directory.|
|`--list-screens`|List available screens and exit.|
|`--silent`|Do not print any output during normal operation.|

### Example

Take 15 screenshots per minute of screen `1` and save them in the directory `screenshots`:

```
screenshotter --screen 1 --outdir 'screenshots' 15 m
```
