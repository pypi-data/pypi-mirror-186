# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aio_usb_hotplug', 'aio_usb_hotplug.backends']

package_data = \
{'': ['*']}

install_requires = \
['anyio>=3.0.0,<4.0.0', 'pyusb>=1.1.0,<2.0.0']

extras_require = \
{':sys_platform == "linux"': ['pyudev>=0.22.0']}

setup_kwargs = {
    'name': 'aio-usb-hotplug',
    'version': '5.2.0',
    'description': 'Asynchronous generators yielding detected hotplug events on the USB buses',
    'long_description': '# aio-usb-hotplug\n\n`aio-usb-hotplug` is a Python library that provides asynchronous generators\nyielding detected hotplug events on the USB buses.\n\nRequires Python >= 3.7.\n\nWorks with [`asyncio`](https://docs.python.org/3/library/asyncio.html)\nand [`trio`](https://trio.readthedocs.io/en/stable/).\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install\n`aio-usb-hotplug`.\n\n```bash\npip install aio-usb-hotplug\n```\n\n`aio-usb-hotplug` depends on [PyUSB](https://pypi.org/pypi/pyusb), which\nin turn requires [libusb](https://libusb.info) or\n[openusb](https://sourceforge.net/projects/openusb/). An easy way to satisfy\nthis requirement is to install\n[libusb-package](https://pypi.org/pypi/libusb-package), which supplies\npre-compiled binaries for most platforms:\n\n```bash\npip install libusb-package\n```\n\n`aio-usb-hotplug` will make use of\n[libusb-package](https://pypi.org/pypi/libusb-package) if it is installed in\nthe current Python environment.\n\n## Usage\n\n### Dump all hotplug events related to a specific USB device\n\n```python\nfrom aio_usb_hotplug import HotplugDetector\nfrom trio import run  # ...or asyncio\n\nasync def dump_events():\n    detector = HotplugDetector.for_device(vid="1050", pid="0407")\n    async for event in detector.events():\n        print(repr(event))\n\ntrio.run(dump_events)\n```\n\n### Run an async task for each USB device matching a VID/PID pair\n\n```python\nfrom aio_usb_hotplug import HotplugDetector\nfrom trio import sleep_forever\n\n\nasync def handle_device(device):\n    print("Handling device:", repr(device))\n    try:\n        # Do something meaningful with the device. The task gets cancelled\n        # when the device is unplugged.\n        await sleep_forever()\n    finally:\n        # Device unplugged or an exception happened\n        print("Stopped handling device:", repr(device))\n\n\nasync def handle_detected_devices():\n    detector = HotplugDetector.for_device(vid="1050", pid="0407")\n    await detector.run_for_each_device(handle_device)\n\n\ntrio.run(handle_detected_devices)\n```\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to\ndiscuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Tamas Nepusz',
    'author_email': 'tamas@collmot.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ntamas/aio-usb-hotplug/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
