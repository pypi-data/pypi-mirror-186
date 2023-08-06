# 🧀 PARMESAN

**P**ython **A**tmospheric **R**esearch program for **ME**teorological **S**cientific **AN**alysis

[![pipeline status](https://gitlab.com/tue-umphy/software/parmesan/badges/master/pipeline.svg)](https://gitlab.com/tue-umphy/software/parmesan/-/pipelines)
[![coverage report](https://gitlab.com/tue-umphy/software/parmesan/badges/master/coverage.svg)](https://tue-umphy.gitlab.io/software/parmesan/coverage-report/)
[![documentation](https://img.shields.io/badge/documentation-here%20on%20GitLab-brightgreen.svg)](https://tue-umphy.gitlab.io/software/parmesan)

## What can `PARMESAN` do?

#### 🔢 Physical Calculations

- 📉 calculating [**power spectra** of timeseries](https://tue-umphy.gitlab.io/software/parmesan/notebooks/spectrum.html)
- 📉 calculating [**structure functions** of timeseries](https://tue-umphy.gitlab.io/software/parmesan/notebooks/structure.html)
- 🌫 calculating several [**humidity** measures](https://tue-umphy.gitlab.io/software/parmesan/api/parmesan.gas.humidity.html)
- 🌡 calculating several [**temperature** measures](https://tue-umphy.gitlab.io/software/parmesan/api/parmesan.gas.temperature.html)
- 📜 handling [**physical units** and checking **bounds**](https://tue-umphy.gitlab.io/software/parmesan/settings.html)
- 🍃 **wind direction** calculations

#### 🔧 Utilities

- ⏱ [calculating **temporal cycles**](https://tue-umphy.gitlab.io/software/parmesan/api/parmesan.aggregate.html#parmesan.aggregate.temporal_cycle) (e.g. diurnal/daily cycles)
- 🚦 [finding **conspicuous values**](https://tue-umphy.gitlab.io/software/parmesan/api/parmesan.processing.cleanup.html#parmesan.processing.cleanup.find_conspicuous_values) in a timeseries

## 📦 Installation

Tagged versions of `PARMESAN` are available [on PyPi](https://pypi.org/project/parmesan/).
You can install the latest tagged version of `PARMESAN` via

```bash
# make sure you have pip installed
# Debian/Ubuntu:  sudo apt update && sudo apt install python3-pip
# Manjaro/Arch:  sudo pacman -Syu python-pip
python3 -m pip install -U parmesan
```

To install the latest development version of `PARMESAN` directly from GitLab, run

```bash
# make sure to have pip installed, see above
python3 -m pip install -U git+https://gitlab.com/tue-umphy/software/parmesan
```

You may also use [our workgroup Arch/Manjaro repository](https://gitlab.com/tue-umphy/workgroup-software/repository) and install the `python-parmesan` package with your favourite software installer, for example with `pacman`:

```bash
sudo pacman -Syu python-parmesan
```

## 📖 Documentation

Documentation can be found [here on GitLab](https://tue-umphy.gitlab.io/software/parmesan).

## ➕ Contributing to PARMESAN

If you'd like to contribute to PARMESAN, e.g. by adding new features or fixing bugs, read the [`CONTRIBUTING.md`-file](https://gitlab.com/tue-umphy/software/parmesan/-/blob/master/CONTRIBUTING.md).
