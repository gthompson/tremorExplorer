import sys
sys.path.append('lib')
import wrappers
config = wrappers.read_config()
print(config['general'])
#PRODUCTS_TOP = config['general']
print(config['subnets'])
print(config['traceids'])