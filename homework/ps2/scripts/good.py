#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = r"""          ��\�[f=c����\P�m���
	��{��
㫳�����E��n3�Ӝ��i���#,�o��Kq'�^�t���W �� ��.� ѻ��L"y�Gi�?����y��_L��C�M�nk�?)W�Z�]�"""
col1 = open("col1", 'r').read()
col2 = open("col2", 'r').read()

if blob == col1:
    print("I come in peace.")
else:
    print("Prepare to be destroyed!")