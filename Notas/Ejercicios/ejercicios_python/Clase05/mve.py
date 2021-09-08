import sys
#from tqdm import tqdm

######################################################################

#%%
def calculo(n):
	#arg = int(sys.argv[1]) if len(sys.argv) > 0 else n
	for i in range(n):
		if i % 1000 == 0:
			print(f'{int(i/n*100)} simulacion', end='\r')
	print()

#%%
'''
def calculo_v2(n):
	for i in tqdm(range(n)):
		n = i ** 2
'''

#%%
if __name__ == '__main__':
	calculo(10000)
