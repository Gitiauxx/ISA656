#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = '            c�|0��B,^�/�qU*P�����Qz�(�f���LC���hD�D�]�@��I�K�1������� 4��� ��ř?�N�#&Fm�Z�L�Gn�����,X�MPV�BɃ؛g���1F�iSk'.hexdigest()
col1 = open("col11", 'r').read()
col2 = open("col22", 'r').read()

if blob == col1:
    print("I come in peace.")
else:
    print("Prepare to be destroyed!")