# LISA Weather Station

Basic weather station for Raspberry Pi and 7inch screen

---
## Screenshot

<div align="center">
    <img
        src="https://github.com/Ayckinn/PYTHON/blob/main/LISAWS/img/screenshot.png"
        alt="DEMO"
        style="width:30%">
</div>

---
## Usage
Install virtual environment : ```sudo apt install virtualenv```

Create virualenv folder : ```virtualenv .env --python=python3.x``` where "x" is the version of your choice

Activate virtualenv : ```source .env/bin/activate```

Install packages : ```pip install -r requirements.txt```

Run station : ```python start.py```

Deactivate virtualenv : Just enter ```deactivate```

---

## Changelog
Version 1.1 - June 26' 2020
- Fix bugs
- Add and update weather pics for night mode

Version 1.0 - June 23' 2020
- Initial release containing :
    - Temperature
    - Weather pic and description
    - Wind speed
    - Humidity level
    - Atmospheric pressure