# UToken - Secure tokens

UToken (or Unhandleable Token) is a library designed to generate secure tokens with a guarantee of integrity for any type of project. With this project you can add payload and token lifetime.

To install UToken, use the `pip` package manager:

```
pip install utokeniz
```

# How to use

Here's a short tutorial on how to use UToken in a simple way.

## Creating a token

Let's start by creating a token, see the code below:

```python
from utoken import encode

# defining our key
KEY = 'secret-key'

# encoding
my_token = encode({'message': 'Hello World!'}, KEY)
print(my_token)
```

First we pass as a parameter to `utoken.encode()` the payload of the token, which must be a dictionary, then we pass the key that will be used to encode the token. After that we have our token in a string returned by the function.

### Define expiration time

We can add the token expiration time using the `expires_in` argument of the `utoken.encode` function. After the maximum time is reached the `ExpiredTokenError` exception will be thrown. In the example below, the token will expire in **5 minutes**:

```python
from utoken import encode
from datetime import timedelta

token = encode({'name': 'Maria'}, 'secret-key', expires_in=timedelta(minutes=5))
```

## Decoding a token

Now, let's decode a token. See the code below:

```python
import utoken

# defining our key
KEY = 'secret-key'

# create a token
token = utoken.encode({'name': 'Maria'}, KEY, expires_in=timedelta(minutes=5))

# decode a token
payload = utoken.decode(token, KEY)
print(payload)
```

Ready! Our token has been decoded. In `utoken.decode()` we pass as a parameter the token and the key used in the encoding, simple.

# License

```
Copyright © 2023 Jaedson Silva
BSD-3-Clause License
```

This project uses the `BSD-3-Clause` license. Please [see the license file](https://github.com/jaedsonpys/utoken/blob/master/LICENSE) to more informations.