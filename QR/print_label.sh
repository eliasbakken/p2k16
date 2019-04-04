#!/bin/sh
export BROTHER_QL_PRINTER=tcp://10.13.37.201
export BROTHER_QL_MODEL=QL-1060N

python user_qr.py
brother_ql print -l 102 user.png
