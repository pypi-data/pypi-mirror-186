# Coiote Python

`python-coiote` is a Python package providing access to the Coiote DM server API. It supports `v3` Coiote DM API.

## Features

`python-coiote` enables you to:

- interact with Coiote DM `v3` API to manage your devices, groups and domains,
- automatically URL-encode path parameters whenever needed,
- convert API responses to convenient Python data classes,
- conveniently deal with batch/paginated responses from `v3` API,
- handle authentication errors and retries,

and more.

| API                                     | Endpoints covered | Status |
|-----------------------------------------|-------------------|--------|
| AssignedDeviceProperties                | 5/5               | ✅      |
| AwsIntegration                          | 2/2               | ✅      |
| CachedDataModels                        | 1/1               | ✅      |
| CertificatesAuth                        | 2/2               | ✅      |
| DeviceLifecycleManagement               | 2/2               | ✅      |
| DeviceMonitoring                        | 10/10             | ✅      |
| DeviceTests                             | 4/4               | ✅      |
| Devices                                 | 7/7               | ✅      |
| DeviceResources (InstantiatedResources) | 2/2               | ✅      |
| Dialects                                | 2/2               | ✅      |
| Domains                                 | 5/5               | ✅      |
| Extensions                              | 16/16             | ✅      |
| Groups                                  | 5/5               | ✅      |
| Observations                            | 6/6               | ✅      |
| Resources                               | 3/3               | ✅      |
| Sessions                                | 2/2               | ✅      |
| SettingValues                           | 4/4               | ✅      |
| TaskReports                             | 6/6               | ✅      |
| Tasks                                   | 7/7               | ✅      |
| TasksFromTemplates                      | 3/3               | ✅      |
| Users                                   | 6/6               | ✅      |

## Installation

`python-coiote` is compatible with Python `>= 3.7`.

Use pip to install the latest stable version of `python-coiote`:

```bash
pip install --upgrade python-coiote
```

## Authentication

There are two ways of authenticating in Coiote API when using this SDK:

- Using credentials to your Coiote account:

```
from coiote.auth import Credentials
from coiote.client import Coiote


client = Coiote(url="https://eu.iot.avsystem.cloud", auth=Credentials("<your-username>", "<your-password>")) 
```

Since Coiote does not support generating API tokens yet, preferably, you should create a separate account in your Coiote
domain
that will have the permissions only to access the API endpoints you intend to use.

- Using a raw token acquired manually using the `oauth` endpoint in v3 API:

```
from coiote.client import Coiote

client = Coiote(url="https://eu.iot.avsystem.cloud", auth="<your-token>") 
```

## Using device client

`python-coiote` comes with builtin high level client designed for accessing specific device and to do so, composes
multiple API calls.
To read more, see [Device Client class](src/coiote/device_client.py). The device client supports a set of basic
operations:

```python3
client = Coiote(url="https://eu.iot.avsystem.cloud", auth="<token>")
endpoint_name = "device_name"
device = client.create_device_client(endpoint_name)
```

Get the whole datamodel or its parts:

```python3
device.get_all_data()
device.get_resource_value("Device.0.Timezone")
```

Schedule writing value to device's data model (it's async, method returns task ID):

```python3
write_task_id = device.write_to_resource("Device.0.Timezone", "Kraków/Radzikowskiego")
```

Schedule reading value from the actual device into its data model (it's async, method returns task ID):

```python3
read_task_id = device.read_resource("Device.0.Timezone")
```

Manually schedule executing a resource on a device (it's async, method returns task ID):

```python3
execute_task_id = device.execute_resource("Device.0.Reboot")
```

Schedule reboot of the device (it's async, method returns task ID):

```python3
reboot_task_id = device.reboot_device()
```

Get recently reported location:

```python3
device.get_location()
```

Access the device historical data - only for resources from objects with ID > 502:

```python3
from datetime import datetime, timedelta

start_time = datetime.now() - timedelta(minutes=180)
end_time = datetime.now() - timedelta(minutes=90)
data = c.device_monitoring.get_data_batch(endpoint_name, "/3303/0/5700", start_time=start_time, end_time=end_time)
```

## Documentation

Docs are yet to come.
