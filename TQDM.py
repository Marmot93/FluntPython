# Author Marmot
from time import sleep
from tqdm import trange,tqdm

pbar = tqdm(total=100)
for i in range(10):
    sleep(0.2)
    pbar.update(10)
pbar.close()



