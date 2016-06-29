# Khepri v0.0.1

## Intro

To install this package, you need to install first python-pip package :

```
$ sudo apt-get install python-pip
```

Then, you can install Khepri package from PyPI using this command line :

```
$ sudo pip install khepri
```

When done, you can use Khepri using this example below :


## Example

```python
#!/usr/bin/python
from khepri import *

# Khepri URL (sandbox environment)
khepri_url = 'http://sb.khepri.tech'

# Khepri parameters needed
api_key = 'MY_APi_KEY' # Replace with your real API key 
instance_id = '1'

# Create instance
instance_khepri = Khepri(khepri_url, api_key, instance_id)

# Method to ask Khepri
result = instance_khepri.ask()
print 'Status : ' + result['status'] + '; Solution : ' + result['solution']

# Method to call on success
result = instance_khepri.success(result['solution'])
print 'Status : ' + result['status']
```