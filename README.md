# 🚀 Co-Maintainers Wanted!

Hello everyone!

Thank you to everyone who uses, stars, and contributes to this project.

Due to work commitments and a busy schedule, I am no longer able to dedicate the time this project deserves. To keep the repository active and moving forward, I am looking for **co-maintainers** or a **new primary maintainer** to help lead the project.

### How You Can Help:
* **Triage Issues:** Review, label, and respond to incoming issue reports.
* **Review Pull Requests:** Help test, review, and merge community contributions.
* **Maintenance & Enhancements:** Keep dependencies updated and work on planned roadmap features.

### Interested?
If you've enjoyed using this project and would like to step up as a maintainer, please:
1. Write an email to me.
2. Briefly introduce yourself and share any prior experience or ideas you have for the project.

Even if you can only contribute a few hours a month, your help would be hugely appreciated!

Thanks for being part of the community! 🙌

[![CodeQL](https://github.com/fustom/ariston-remotethermo-home-assistant-v3/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/fustom/ariston-remotethermo-home-assistant-v3/actions/workflows/codeql.yml)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)
[![HACS Action](https://github.com/fustom/ariston-remotethermo-home-assistant-v3/actions/workflows/hacs.yml/badge.svg)](https://github.com/fustom/ariston-remotethermo-home-assistant-v3/actions/workflows/hacs.yml)
[![Validate with hassfest](https://github.com/fustom/ariston-remotethermo-home-assistant-v3/actions/workflows/hassfest.yml/badge.svg)](https://github.com/fustom/ariston-remotethermo-home-assistant-v3/actions/workflows/hassfest.yml)
# Ariston NET remotethermo integration for Home Assistant
This integration inspired by chomupashchuk fantastic work https://github.com/chomupashchuk/ariston-remotethermo-home-assistant-v2
But it does not use Ariston website. It uses Ariston API what I reversed engineered.


| [This integration](https://github.com/fustom/ariston-remotethermo-home-assistant-v3)  | [Chomupashchuk's v2 integration](https://github.com/chomupashchuk/ariston-remotethermo-home-assistant-v2) |
| ------------- | ------------- |
| Uses real API  | Uses Ariston website  |
| Faster set/get data  | Sometimes needs minutes to set/get data |
| Easy to setup with UI | Not so easy to setup (only with configuration.yaml) |
| Integration & devices & entites | Only entites |
| Proper asynchronous integration, clean code | Hard to understand and maintain (ariston.py has more than 4000 lines) |
| Less sensors, switches, etc |  More sensors, switches, etc |
| New code, may contains lot of bugs | Old, tested code |

## TODO
- Localization. Avaliable in english, catalan, italian, russian and ukranian.
- More sensors, switches, binary sersors, selectors, services.
- Exception handling.
- More logs.
- Fun.

## Integration was tested on and works with:
- Ariston Alteas One 24
- Ariston Velis Evo
- Ariston Velis Lux
- Ariston Lydos Hybrid

Feel free to test something else and create new issue / pull request if something goes wrong.

## Tests

The test suite uses Home Assistant's pytest fixtures and reports line coverage for
the integration. It runs on Python 3.14.2, matching CI.

```sh
python -m pip install --require-hashes --only-binary=:all: -r requirements_test.txt
python -m pytest
```

To update test dependencies, edit `requirements_test.in` and regenerate the hashed lock:

```sh
uv pip compile requirements_test.in --python 3.14.2 --python-version 3.14.2 --universal --generate-hashes --upgrade --output-file requirements_test.txt
```

### Testing GALEVO resilience for issue #1

The resilience changes live in the companion [python-ariston-api](https://github.com/fustom/python-ariston-api)
checkout at `.ariston-library`, on `fix/issue-1-galevo-resilience` based on
tag `0.19.15`. Run
`python -m unittest discover -s tests` from that checkout after installing its
runtime dependencies. To test both changes together, use a disposable Linux
Home Assistant test environment. Install the locked test dependencies, then
point `PYTHONPATH` at the library checkout before running `python -m pytest`.
Verify the source in use with `python -c "import ariston; print(ariston.__file__)"`.
For a hardware check, run a separate Home Assistant Core instance with the
same import override. Check that heating and hot water controls still work,
that changes from the Ariston app appear on the next successful poll, and
that availability returns after a transient cloud failure.

The library still asks for every GALEVO property and all applicable menu items
on each configured poll. It splits a failed property batch, with at most
eight additional requests, four consecutive failures, or 15 seconds of
recovery. A 429 immediately stops retries. Requests for the same account
and API origin share the server's cooldown, or a fallback of 60 seconds
that doubles up to 15 minutes.

Home Assistant uses its existing coordinator to make entities unavailable
when a refresh fails. The device retains its last accepted properties, menu
items, and feature flags. Incomplete or provider-cached recovery results
never replace that snapshot. A later complete refresh restores availability.

For a release, first build and validate a new `ariston` package from the
library branch. Once the package is available, update the integration
manifest, `requirements.txt`, and the test lock to use that release, then run
the integration suite before publishing the integration. A checkout using the
current package pin still uses the published `ariston==0.19.15`.

## Installation
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=fustom&repository=ariston-remotethermo-home-assistant-v3&category=integration) or copy ariston folder to your configuration/custom_components path.
Use the add integration UI to set up your device.

| ![Kazam_screenshot_00003](https://user-images.githubusercontent.com/6751243/146653448-ff7b6f9d-cbf1-4555-9a75-61bf68bc9d3e.png) | ![Kazam_screenshot_00004](https://user-images.githubusercontent.com/6751243/146653484-52e39d78-7c6f-44ae-888d-acf246147290.png) | ![Kazam_screenshot_00010](https://user-images.githubusercontent.com/6751243/147890590-6c4ebf38-16d9-421f-9b81-8f43298ec62f.png) |
:-------------------------:|:-------------------------:|:-------------------------:

![Kazam_screenshot_00011](https://user-images.githubusercontent.com/6751243/147890611-54ae2d28-bf5a-45f8-ba92-e7a00a22615c.png)

![Kazam_screenshot_00012](https://user-images.githubusercontent.com/6751243/147989103-cdac510f-e6f6-461f-a88e-b8ff0204c34f.png)

| ![Kazam_screenshot_00013](https://user-images.githubusercontent.com/6751243/148247717-5211c01c-561f-4a4e-b4b5-47a680e04a68.png) | ![Kazam_screenshot_00009](https://user-images.githubusercontent.com/6751243/146657797-ed14b741-595a-48a6-9126-1acca3beb69f.png) |
:-------------------------:|:-------------------------:

<h1 align="center">Peace Love Freedom</h1>
