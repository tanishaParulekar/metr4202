import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/tparu001k/metr4202_ws/install/m4202_py_pkg'
