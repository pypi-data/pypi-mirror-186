import base64
import math
from typing import Dict


def binary_to_dict(binary_secret: str) -> Dict[str, str]:
    d = binary_secret.ljust((int)(math.ceil(len(binary_secret) / 4)) * 4, '=')
    sec_json = eval(base64.b64decode(d))
    return sec_json
