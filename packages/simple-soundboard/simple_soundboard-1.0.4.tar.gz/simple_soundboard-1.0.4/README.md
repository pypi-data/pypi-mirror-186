# Simple Soundboard
Simple soundboard web app that plays sounds on a central server

## Installation
Install through pip with

`pip install simple_soundboard`

## Usage
Edit config in ~/simple_soundboard/config.json
Start by running
`simple_soundboard`

### MQTT API
MQTT Server is configured in ~/simple_soundboard/config.json
MQTT API includes
```
simple_soundboard/stop_all
simple_soundboard/stop_sounds
simple_soundboard/fadeout
simple_soundboard/pause_music
simple_soundboard/resume_music
simple_soundboard/play/<topic_from_web_ui>
```

No payload required

The server output two MQTT topic
```
simple_soundboard/stopped_all
simple_soundboard/stopped_sounds
simple_soundboard/playing/<topic_from_web_ui> (If MQTT Topic is set)
```
will be published

## TODO
- Make the config editable online
- Multiple music?


## Development
git clone this project

Create a new venv

`python3 -m venv --system-site-packages ./venv`

Source it

`source ./venv/bin/activate`

Install all dependancies with poetry

`poetry install`

Install git hooks

`pre-commit install`

### Upload to pypi

Source the venv

`source ./venv/bin/activate`

Install twine

`pip install twine`

Config your pypi credentials in the file `~/.pypirc`

```python
[pypi]
username = pypi_username
password = pypi_password
```

Run

```python
poetry install
twine check dist/*
twine upload dist/*
```
