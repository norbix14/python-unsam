#import sys
#from tqdm import tqdm

######################################################################

#%%
def calculo(n):
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
