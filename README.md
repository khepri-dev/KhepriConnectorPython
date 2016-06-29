# Khepri v0.0.1

## intro

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

# Khepri URL
khepri_url = 'http://test-khepridevelba-1t8aalo9fz0t1-723475646.eu-west-1.elb.amazonaws.com'

# Khepri parameters needed
api_key = '213e71dd6e9f354de2c42eee366d4263'
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
