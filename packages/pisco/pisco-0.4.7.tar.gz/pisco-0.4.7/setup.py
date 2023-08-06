# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['pisco']
install_requires = \
['Pillow>=9.4,<10.0',
 'click>=8.1,<9.0',
 'python-json-logger>=2.0,<3.0',
 'requests>=2.28,<3.0',
 'soco>=0.29.0,<0.30.0',
 'xdg>=5.1,<6.0']

entry_points = \
{'console_scripts': ['pisco = pisco:main']}

setup_kwargs = {
    'name': 'pisco',
    'version': '0.4.7',
    'description': 'Keyboard only controller for Sonos speakers',
    'long_description': "# Pisco\n\nPisco is a keyboard only controller for Sonos speakers.\nWhile Pisco's graphical interface displays the album art of the currently running track,\nyou can control playback with your keyboard.\n\nPisco has been tested on Linux and on macOS.\nIt is particularly well-suited for usage with\nsmall displays (e.g. [Pimoroni HyperPixel 4.0 Square](https://shop.pimoroni.com/products/hyperpixel-4-square?variant=30138251477075)) and\nmedia remotes (e.g. [Satechi Bluetooth Multi-Media Remote](https://satechi.net/products/satechi-bluetooth-multi-media-remote?variant=27129644617)).\n\n\n## Setup\n\nProceed as follows to set up Pisco on an ordinary Linux or macOS machine:\n\n1. Make sure you are using Python 3.7 or newer.\n2. Create a virtual environment if you do not want to clutter up your default environment.\n3. Install Pisco:\n    ```shell\n    pip3 install pisco\n    ```\n\nFor a clean and minimalistic deployment\non a [Raspberry Pi Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/),\nplease check the directory `deployment`.\n\n\n## Usage\n\nWhen starting Pisco,\nyou need to provide the name of the Sonos device (i.e. Sonos room) you want to control:\n\n```shell\npisco Leseecke  # Replace 'Leseecke' by the name of your Sonos device.\n```\n\nYou can use the option `--help` to find additional options:\n```text\n$ pisco --help\nUsage: pisco [OPTIONS] SONOS_DEVICE_NAME\n\n  Control your Sonos device with your keyboard\n\nOptions:\n  -b, --backlight DIRECTORY    sysfs directory of the backlight that should be\n                               deactivated when the device is not playing\n  -w, --width INTEGER RANGE    width of the Pisco window  [default: 320; x>=0]\n  -h, --height INTEGER RANGE   height of the Pisco window  [default: 320;\n                               x>=0]\n  -r, --refresh INTEGER RANGE  time in milliseconds after which playback\n                               information is updated  [default: 40; x>=1]\n  --help                       Show this message and exit.\n```\n\nAs soon as Pisco is running, you can use the following keys to control playback:\n- ⏯ (or return) to pause or resume playback\n- ⏹ to stop playback\n- ⏮ and ⏭ (or left and right arrow) to play previous or next track\n- 0️⃣ to 9️⃣ to play the top 10 tracks (or radio stations) of your Sonos favorites\n- ➕ and ➖ (or up and down arrow) to raise or lower volume\n- 🔇 to mute or unmute\n",
    'author': 'Christoph Gietl',
    'author_email': 'christophgietl@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/christophgietl/pisco',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
