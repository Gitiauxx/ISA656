#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """         U�a�̥��K̅9M�B�'9K|H�h��cB�L�l�bH�<�k�r�8Ő�9n��
K�9r	����}&㿟O�,��QS�cXT���K��`H��5T�M4���<0��ucp��
�2��"""
col1 = open("col1", 'rb').read()
col2 = open("col2", 'rb').read()

if blob == col1:
    print("I come in peace.")
else:
    print("Prepare to be destroyed!")