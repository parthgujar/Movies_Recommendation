import numpy as np
from lightfm.datasets import fetch_movielens
from lightfn import LightFM

data = fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repr(data['test']))

MODEL = LightFM()