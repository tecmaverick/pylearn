import sys
import calc
from calc import add, substract, multiply

print('main loaded')

def process():

		funcs = {"+":getattr(add, 'add'),
				"*":getattr(multiply, 'multiply'),
				"-":getattr(substract,'substract')}

		fno = sys.argv[1]
		operator = sys.argv[2]
		sno = sys.argv[3]
		print "fno:{} {} sno:{}".format(fno,operator,sno)

		func = funcs[operator]
		print func(fno,sno)

process()
