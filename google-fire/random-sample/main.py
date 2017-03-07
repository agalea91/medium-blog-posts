#!/usr/bin/env python
'''
A function for generating random samples.
Usage:
For usage instructions execute the following lines:
>>> python main.py -- --help
'''
import fire
import numpy as np

def random_sample(choices, num_samples=1, seed=None):
    '''
    Return a random sample of the given input arguments.
    
    choices : tuple
        The data to sample.
    num_samples : int
        The number of samples to return.
    seed : int
        Variable used to seed random number generator. Set to None for random seed.
    '''
    num_samples = int(num_samples)
    seed = int(seed) if str(seed).isnumeric() else seed

    print('Choices: %s' % repr(choices))
    print('Genreating %d samples' % num_samples)
    print('Random seed: %r' % seed)
    np.random.seed(seed)
    samples = np.random.choice(choices, size=num_samples)
    print('Samples:')
    return '\n'.join(samples)

def main():
    fire.Fire(random_sample)
    # print(random_sample('Bohr', 'Schrodinger', 'Einstein', num_samples=3))

if __name__ == '__main__':
    main()
