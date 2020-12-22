# IAAS (Internet as a Service)

Have you ever wanted a simple REST API that enabled you to check if your application has internet connection?

Look no further.

Internet as a Service (IAAS) provides users with an easy, robust, reliable, and atomic REST API for most internet connection needs. If your requirements for internet availability fall under the following:

1. Your application needs to check if it has internet availability
2. You want to receive either a positive or negative confirmation of availability, or the lack thereof
3. You only need to check for internet availability once every 24 hours or less

Then you are welcome to use IAAS for your internet connection needs!

IAAS can be reached at https://iaas.woohoojin.dev/

# Table of Contents

1. [Usage](#usage-example)
2. [API Documentation](#api-documentation)

# Usage Example

```python
import requests

def checkInternetConnectionAffirmative():
    try:
        result = requests.get(f"https://iaas.woohoojin.dev/do-i-the-invoker-of-iaas-have-internet-availability-right-now-at-this-current-point-in-time-assuming-iaas-is-currently-properly-functional-and-live-for-any-get-request")

        return result.text == "YES" # Internet is available
    except:
        return False # Internet is unavailable (probably)

def checkInternetConnectionNegated():
    try:
        result = requests.get(f"https://iaas.woohoojin.dev/do-i-the-invoker-of-iaas-not-have-internet-availability-right-now-at-this-current-point-in-time-assuming-iaas-is-currently-properly-functional-and-live-for-any-get-request")

        return result.text == "NO" # Internet is available
    except:
        return False # Internet is unavailable (probably)
```

# API Documentation

**URL** : `/do-i-the-invoker-of-iaas-have-internet-availability-right-now-at-this-current-point-in-time-assuming-iaas-is-currently-properly-functional-and-live-for-any-get-request`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 1 request per day

**Description** : Returns the string "YES".

## Success Response

**Code** : `200 OK`

**Content examples**

```json
YES
```

**URL** : `/do-i-the-invoker-of-iaas-not-have-internet-availability-right-now-at-this-current-point-in-time-assuming-iaas-is-currently-properly-functional-and-live-for-any-get-request`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 1 request per day

**Description** : Returns the string "NO".

## Success Response

**Code** : `200 OK`

**Content examples**

```json
NO
```

**Code** : `429 Too Many Requests`

**Content examples**

For a request made less than 24 hours before the previous request

```json
Too Many Requests
1 per 1 day
```