# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hyper_systems', 'hyper_systems.devices', 'hyper_systems.http']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hyper-systems',
    'version': '1.1.3',
    'description': 'Python SDK for interacting with the Hyper.systems platform.',
    'long_description': '# hyper-python-sdk\n\nPython SDK for interacting with the Hyper.systems platform.\n\n## Installing\n\nInstall the latest version globally using pip:\n\n```shell\npip install -U hyper-systems\n```\n\n### Adding as a dependency to your project\n\nAdd to `requirements.txt` for pip:\n\n```shell\necho "hyper-systems==1.1.3" >> requirements.txt\n```\n\nAlternatively, install with poetry:\n\n```shell\npoetry add "hyper-systems==1.1.3"\n```\n\n## Usage\n\nThe first thing we need to do to start using the Python SDK is provide a valid API key. This will allow the library to make requests to Hyper\'s services for publishing and receiving messages.\n\nYou can obtain an API key from your hyper.systems dashboard instance. In the sidebar, click on your account name, select "Account", go to the "API Keys" section.\n\nIn additon to the API settings, you need to specify a site identifier. Sites can be helpful to namespace devices and messages across different physical locations.\n\n```python\nHYPER_API_KEY = "<insert your key here>"\nHYPER_API_URL = "https://<your organization name>.hyper.systems/api"\nHYPER_SITE_ID = 1\n```\n\n\n### Creating a device schema\n\nBefore you can start publishing messages from your device, we need to provide the attribute schema for your device.\n\nThe schema can be obtained from your hyper.systems dashboard.\n\n![image](docs/images/device_schema_download.png)\n\nDownload the JSON schema file and place it somewhere in your project directory.\n\n```python\nfrom hyper_systems.devices import Device, Schema\nfrom hyper_systems.http import Client\n\n# Load the device schema.\nSCHEMA_FILE = "<path to downloaded schema file>"\nschema = hyper.Schema.load(SCHEMA_FILE)\n\n# Initialize the device with a schema and a unique id.\ndevice_id = "00:00:00:00:01"\ndevice = hyper.Device.from_schema(schema, device_id)\n```\n\nThe device schema contains the full description of the properties of the device. Note that multiple devices can match the same device schema as long as they have different device ids.\n\n> Note: You can can inspect the schema files to see the metadata and the available attributes.\n\nThe device is now ready to be used to start recording values.\n\n\n### Recording device values\n\nThe `device` object we created in the previous section has setters for every attribute from the device schema. We can start recording values for the attributes of the device.\n\n```python\n# Print the list of all available attributes.\nprint(device.attributes)\n```\n\nThis will give you the list of available property names. For example, if the list above contains a property called "sht31_relative_humidity_1", you can set the value for this attribute with:\n\n```python\n# The the value of the attribute.\ndevice.sht31_relative_humidity_1 = 55.0\n```\n\n> Note: The `_1` suffix in the attribute name is the unique slot of the attribute in the device schema.\n\nAlternatively, the attribute values can be set by specifying their slot. The following sets the value for the `sht31_relative_humidity_1` attribute using its slot.\n\n```python\n# Set attribute values using the attribute slot.\ndevice[1] = 60.0\nassert device[1] == 60.0\n```\n\nYou can set any attribute values available on the device. Setting all attributes is not required.\n\n\n### Publishing device values\n\nOnce your device is initialized and has the attribute values set, you can publish them to the hyper.systems platform.\n\n```python\nhyper_client = hyper.http.Client(\n    api_url=HYPER_API_URL,\n    api_key=HYPER_API_KEY,\n    site_id=HYPER_SITE_ID\n)\nhyper_client.publish_device_message(device.message)\n```\n',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://hyper.systems',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
