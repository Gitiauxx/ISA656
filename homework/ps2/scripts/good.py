#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = r"""           �4*���԰G��T=�[+��ϵR9Q�B&X���^���p�뤈���3F�'¯�Z_�-}x�T��:$TV$�n<���
��9&��K��=Ww*Z�m�2j�i�8�\��4n��im��F\D["""
from hashlib import sha256
b = sha256(blob).hexdigest()

if (b == "3c3c442f67804e50bf8c784835e01dfdf6d17653c4db66b7d07176ce755aeecd"):
    print "I come in peace."
elif (b == "bdf62f1db8ddb955fb1ee27892685da186869fc2c4bbf476a1d1d332e56902ec"):
    print "Prepare to be destroyed!"