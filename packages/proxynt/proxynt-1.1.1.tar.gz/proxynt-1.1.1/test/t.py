import os
import base64
import math
from itertools import islice

from importlib_metadata import unique_everseen


def produce_amount_keys(amount_of_keys):
    def gen_keys(_urandom=os.urandom, _encode=base64.b32encode, ):
        factor = math.log(256, 32)
        input_length = [None] * 12 + [math.ceil(l / factor) for l in range(12, 20)]
        while True:
            # count = _randint(12, 20)
            count = 12
            yield _encode(_urandom(input_length[count]))[:count].decode('ascii')
    return list(islice(unique_everseen(gen_keys()), amount_of_keys))


if __name__ == '__main__':
    from base64 import b64encode
    from os import urandom

    random_bytes = urandom(8)
    token = b64encode(random_bytes).decode('utf-8')
    print(token[:8])
    print(len(token))
