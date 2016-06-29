# Khepri

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

# Install Khepri using pip: $ sudo pip install khepri
from khepri import *

# Khepri URL (sandbox environment)
khepri_url = 'http://sb.khepri.tech'

# Initialize the client with your API-Key. You can find it on your Khepri account.
api_key = 'MY_API_KEY' 
instance_id = '1'

# Create Khepri object
khepri = Khepri(khepri_url, api_key, instance_id)

# Method to ask Khepri
result = khepri.ask()
print 'Status : ' + result['status'] + '; Solution : ' + result['solution']

# Method to call on success
result = khepri.success(result['solution'])
print 'Status : ' + result['status']
```
