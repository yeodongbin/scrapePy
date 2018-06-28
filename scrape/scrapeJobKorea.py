from my_package import my_module
import sys
for path in sys.path:
    print(path)

my_module.info()
