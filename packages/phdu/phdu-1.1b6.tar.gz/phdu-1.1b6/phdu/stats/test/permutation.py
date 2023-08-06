"""
2-sample permutation test, with/without pairing (including block pairing), for the difference and the ratio.

Only implemented for the mean and median. Check functions starting with underscore to implement other statistics.
Will be refined in the future.
"""
import numpy as np
from numba import njit


def _permutation_test_2sample_paired(X1, X2, stat_func, ratio=False, N=int(1e6)-1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Paired permutation test. Numba won't compile. This is a sketch such that the only thing to implement is stat_func.
    
    Attrs:
            alternative: 
                                           - greater:    H0: mu_1 / mu_2 < observed,       H1: mu_1 / mu_2  >= observed  
                         ratio             - less:       H0: mu_1 / mu_2 > observed,       H1: mu_1 / mu_2  <= observed  
                                           - two-sided:  H0: mu_1 / mu_2 = observed,       H1: mu_1 / mu_2  != observed 
           
                                           - greater:    H0: mu_1 - mu_2 < observed,       H1: mu_1 - mu_2  >= observed  
                         not ratio         - less:       H0: mu_1 - mu_2 > observed,       H1: mu_1 - mu_2  <= observed  
                                           - two-sided:  H0: mu_1 - mu_2 = observed,       H1: mu_1 - mu_2  != observed 
    Returns: p-value
    """
    if ratio:
        def aux(X_paired):
            return stat_func(X_paired[0]) / stat_func(X_paired[1])
    else:
        def aux(X_paired):
            return stat_func(X_paired[0]) - stat_func(X_paired[1])
        
    n = X1.size
    X_paired = np.vstack((X1, X2))
    stat_0 = aux(X_paired)
    
    perm_sample = np.empty((N))
    np.random.seed(seed)
    for i in range(N):
        shuffle = np.random.randint(0, 2, size=n) == 1
        X_shifted = X_paired[:, shuffle][::-1]
        X_still = X_paired[:, ~shuffle]
        X_perm = np.hstack((X_shifted, X_still))
        perm_sample[i] = aux(X_perm)
    
    if alternative == "greater":
        return (1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")
        
def _permutation_test_2sample_paired_block(X, Y, stat_func, ratio=False, N=int(1e6)-1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Permutation test for paired blocks. Permutations occur only between blocks: X1(block i) <-> X2(block i). 
    Numba won't compile. This is a sketch such that the only thing to implement is stat_func.
    
    Attrs:
            X, Y:                          ragged arrays or tuples. Each element is an array containing the results for a block. 
            alternative: 
                                           - greater:    H0: mu_1 / mu_2 < observed,       H1: mu_1 / mu_2  >= observed  
                         ratio             - less:       H0: mu_1 / mu_2 > observed,       H1: mu_1 / mu_2  <= observed  
                                           - two-sided:  H0: mu_1 / mu_2 = observed,       H1: mu_1 / mu_2  != observed 
           
                                           - greater:    H0: mu_1 - mu_2 < observed,       H1: mu_1 - mu_2  >= observed  
                         not ratio         - less:       H0: mu_1 - mu_2 > observed,       H1: mu_1 - mu_2  <= observed  
                                           - two-sided:  H0: mu_1 - mu_2 = observed,       H1: mu_1 - mu_2  != observed 
    Returns: p-value
    """
    if ratio:
        def aux(X1, X2):
            return stat_func(X1) / stat_func(X2)
    else:
        def aux(X1, X2):
            return stat_func(X1) - stat_func(X2)
        
    def stack(arr_list):
        return np.array([a for arr in arr_list for a in arr])
        
    stat_0 = aux(stack(X), stack(Y))    
    perm_sample = np.empty((N))
    np.random.seed(seed)
    for i in range(N):
        Xi = []
        Yi = []
        for xi, yi in zip(X, Y):
            z = np.hstack((xi, yi))
            np.random.shuffle(z)
            Xi.append(z[:xi.size])
            Yi.append(z[xi.size:])
        perm_sample[i] = aux(stack(Xi), stack(Yi))
    
    if alternative == "greater":
        return (1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")

def _permutation_test_2sample_not_paired(X1, X2, stat_func, ratio=False, N=int(1e6) - 1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Non-paired permutation test. Numba won't compile. This is a sketch such that the only thing to implement is stat_func.
    
    Attrs:
            alternative: 
                                           - greater:    H0: mu_1 / mu_2 < observed,       H1: mu_1 / mu_2  >= observed  
                         ratio             - less:       H0: mu_1 / mu_2 > observed,       H1: mu_1 / mu_2  <= observed  
                                           - two-sided:  H0: mu_1 / mu_2 = observed,       H1: mu_1 / mu_2  != observed 
           
                                           - greater:    H0: mu_1 - mu_2 < observed,       H1: mu_1 - mu_2  >= observed  
                         not ratio         - less:       H0: mu_1 - mu_2 > observed,       H1: mu_1 - mu_2  <= observed  
                                           - two-sided:  H0: mu_1 - mu_2 = observed,       H1: mu_1 - mu_2  != observed 
    Returns: p-value
    """
    n1 = X1.size
    if ratio:
        def aux(X, n1): # pass n1 to avoid numba error.
            return stat_func(X[:n1]) / stat_func(X[n1:])
    else:
        def aux(X, n1):
            return stat_func(X[:n1]) - stat_func(X[n1:])
    X = np.hstack((X1, X2))
    stat_0 = aux(X)
       
    perm_sample = np.empty((N)) # permutation distribution
    np.random.seed(seed)
    for i in range(N):       
        np.random.shuffle(X)
        perm_sample[i] = aux(X, n1)
    
    if alternative == "greater":
        return (1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")

@njit
def permutation_test_2sample_paired_median(X1, X2, ratio=False, N=int(1e6)-1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Paired permutation test for the median.
    
    Attrs:
            alternative: 
                                           - greater:    H0: me_1 / me_2 < observed,       H1: me_1 / me_2  >= observed  
                         ratio             - less:       H0: me_1 / me_2 > observed,       H1: me_1 / me_2  <= observed  
                                           - two-sided:  H0: me_1 / me_2 = observed,       H1: me_1 / me_2  != observed 
           
                                           - greater:    H0: me_1 - me_2 < observed,       H1: me_1 - me_2  >= observed  
                         not ratio         - less:       H0: me_1 - me_2 > observed,       H1: me_1 - me_2  <= observed  
                                           - two-sided:  H0: me_1 - me_2 = observed,       H1: me_1 - me_2  != observed 
            
    Returns: p-value
    """
    if ratio:
        def aux(X_paired):
            return np.median(X_paired[0]) / np.median(X_paired[1])
    else:
        def aux(X_paired):
            return np.median(X_paired[0]) - np.median(X_paired[1])
        
    n = X1.size
    X_paired = np.vstack((X1, X2))
    stat_0 = aux(X_paired)
    
    perm_sample = np.empty((N))
    np.random.seed(seed)
    for i in range(N):
        shuffle = np.random.randint(0, 2, size=n) == 1
        X_shifted = X_paired[:, shuffle][::-1]
        X_still = X_paired[:, ~shuffle]
        X_perm = np.hstack((X_shifted, X_still))
        perm_sample[i] = aux(X_perm)
    
    if alternative == "greater":
        return (1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")

        
@njit
def permutation_test_2sample_paired_block_median(X, Y, ratio=False, N=int(1e6)-1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Permutation test for the mean for paired blocks. Permutations occur only between blocks: X1(block i) <-> X2(block i). 
    Numba won't compile. This is a sketch such that the only thing to implement is stat_func.
    
    Attrs:
            X, Y:                          ragged arrays or tuples. Each element is an array containing the results for a block. 
            alternative: 
                                           - greater:    H0: mu_1 / mu_2 < observed,       H1: mu_1 / mu_2  >= observed  
                         ratio             - less:       H0: mu_1 / mu_2 > observed,       H1: mu_1 / mu_2  <= observed  
                                           - two-sided:  H0: mu_1 / mu_2 = observed,       H1: mu_1 / mu_2  != observed 
           
                                           - greater:    H0: mu_1 - mu_2 < observed,       H1: mu_1 - mu_2  >= observed  
                         not ratio         - less:       H0: mu_1 - mu_2 > observed,       H1: mu_1 - mu_2  <= observed  
                                           - two-sided:  H0: mu_1 - mu_2 = observed,       H1: mu_1 - mu_2  != observed 
    Returns: p-value
    """
    if ratio:
        def aux(X1, X2):
            return np.median(X1) / np.median(X2)
    else:
        def aux(X1, X2):
            return np.median(X1) - np.median(X2)
        
    def stack(arr_list):
        return np.array([a for arr in arr_list for a in arr])
        
    stat_0 = aux(stack(X), stack(Y))    
    perm_sample = np.empty((N))
    np.random.seed(seed)
    for i in range(N):
        Xi = []
        Yi = []
        for xi, yi in zip(X, Y):
            z = np.hstack((xi, yi))
            np.random.shuffle(z)
            Xi.append(z[:xi.size])
            Yi.append(z[xi.size:])
        perm_sample[i] = aux(stack(Xi), stack(Yi))
    
    if alternative == "greater":
        return (1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")
        
        
@njit    
def permutation_test_2sample_not_paired_median(X1, X2, ratio=False, N=int(1e6) - 1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Non-paired permutation test for the median.
    
   Attrs:
            alternative: 
                                           - greater:    H0: me_1 / me_2 < observed,       H1: me_1 / me_2  >= observed  
                         ratio             - less:       H0: me_1 / me_2 > observed,       H1: me_1 / me_2  <= observed  
                                           - two-sided:  H0: me_1 / me_2 = observed,       H1: me_1 / me_2  != observed 
           
                                           - greater:    H0: me_1 - me_2 < observed,       H1: me_1 - me_2  >= observed  
                         not ratio         - less:       H0: me_1 - me_2 > observed,       H1: me_1 - me_2  <= observed  
                                           - two-sided:  H0: me_1 - me_2 = observed,       H1: me_1 - me_2  != observed 
    Returns: p-value
    """
    n1 = X1.size
    if ratio:
        def aux(X, n1): # pass n1 to avoid numba error.
            return np.median(X[:n1]) / np.median(X[n1:])
    else:
        def aux(X, n1):
            return np.median(X[:n1]) - np.median(X[n1:])
    X = np.hstack((X1, X2))
    stat_0 = aux(X, n1)
       
    perm_sample = np.empty((N)) # permutation distribution
    np.random.seed(seed)
    for i in range(N):       
        np.random.shuffle(X)
        perm_sample[i] = aux(X, n1)
    
    if alternative == "greater":
        return (1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")
        
@njit
def permutation_test_2sample_paired_mean(X1, X2, ratio=False, N=int(1e6)-1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Paired permutation test for the mean
    
    Attrs:
            alternative: 
                                           - greater:    H0: mu_1 / mu_2 < observed,       H1: mu_1 / mu_2  >= observed  
                         ratio             - less:       H0: mu_1 / mu_2 > observed,       H1: mu_1 / mu_2  <= observed  
                                           - two-sided:  H0: mu_1 / mu_2 = observed,       H1: mu_1 / mu_2  != observed 
           
                                           - greater:    H0: mu_1 - mu_2 < observed,       H1: mu_1 - mu_2  >= observed  
                         not ratio         - less:       H0: mu_1 - mu_2 > observed,       H1: mu_1 - mu_2  <= observed  
                                           - two-sided:  H0: mu_1 - mu_2 = observed,       H1: mu_1 - mu_2  != observed 
    Returns: p-value
    """
    if ratio:
        def aux(X_paired):
            return np.mean(X_paired[0]) / np.mean(X_paired[1])
    else:
        def aux(X_paired):
            return np.mean(X_paired[0]) - np.mean(X_paired[1])
        
    n = X1.size
    X_paired = np.vstack((X1, X2))
    stat_0 = aux(X_paired)
    
    perm_sample = np.empty((N))
    np.random.seed(seed)
    for i in range(N):
        shuffle = np.random.randint(0, 2, size=n) == 1
        X_shifted = X_paired[:, shuffle][::-1]
        X_still = X_paired[:, ~shuffle]
        X_perm = np.hstack((X_shifted, X_still))
        perm_sample[i] = aux(X_perm)
    
    if alternative == "greater":
        return (1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")

@njit
def permutation_test_2sample_paired_block_mean(X, Y, ratio=False, N=int(1e6)-1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Permutation test for the mean for paired blocks. Permutations occur only between blocks: X1(block i) <-> X2(block i). 
    Numba won't compile. This is a sketch such that the only thing to implement is stat_func.
    
    Attrs:
            X, Y:                          ragged arrays or tuples. Each element is an array containing the results for a block. 
            alternative: 
                                           - greater:    H0: mu_1 / mu_2 < observed,       H1: mu_1 / mu_2  >= observed  
                         ratio             - less:       H0: mu_1 / mu_2 > observed,       H1: mu_1 / mu_2  <= observed  
                                           - two-sided:  H0: mu_1 / mu_2 = observed,       H1: mu_1 / mu_2  != observed 
           
                                           - greater:    H0: mu_1 - mu_2 < observed,       H1: mu_1 - mu_2  >= observed  
                         not ratio         - less:       H0: mu_1 - mu_2 > observed,       H1: mu_1 - mu_2  <= observed  
                                           - two-sided:  H0: mu_1 - mu_2 = observed,       H1: mu_1 - mu_2  != observed 
    Returns: p-value
    """
    if ratio:
        def aux(X1, X2):
            return np.mean(X1) / np.mean(X2)
    else:
        def aux(X1, X2):
            return np.mean(X1) - np.mean(X2)
        
    def stack(arr_list):
        return np.array([a for arr in arr_list for a in arr])
        
    stat_0 = aux(stack(X), stack(Y))    
    perm_sample = np.empty((N))
    np.random.seed(seed)
    for i in range(N):
        Xi = []
        Yi = []
        for xi, yi in zip(X, Y):
            z = np.hstack((xi, yi))
            np.random.shuffle(z)
            Xi.append(z[:xi.size])
            Yi.append(z[xi.size:])
        perm_sample[i] = aux(stack(Xi), stack(Yi))
    
    if alternative == "greater":
        return (1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")
        
@njit
def permutation_test_2sample_not_paired_mean(X1, X2, ratio=False, N=int(1e6) - 1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Permutation test for the differences or ratio of the means (non-paired).
    
    Attrs:
            alternative:  - greater:    H0: mu_1 - mu_2 < observed,       H1: mu_1 - mu_2  >= observed
                          - less:       H0: mu_1 - mu_2 > observed,       H1: mu_1 - mu_2  <= observed
                          - two-sided:  H0: mu_1 - mu_2 = observed,       H1: mu_1 - mu_2  != observed
    Returns: p-value
    """
    n1 = X1.size
    if ratio:
        def aux(X, n1): # pass n1 to avoid numba error.
            return X[:n1].mean() / X[n1:].mean()
    else:
        def aux(X, n1):
            return X[:n1].mean() - X[n1:].mean()
    X = np.hstack((X1, X2))
    stat_0 = aux(X, n1)
       
    perm_sample = np.empty((N)) # permutation distribution
    np.random.seed(seed)
    for i in range(N):       
        np.random.shuffle(X)
        perm_sample[i] = aux(X, n1)
    
    if alternative == "greater":
        return (1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")

@njit
def permutation_test_2sample_paired_diffmean(X1, X2, N=int(1e6)-1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Paired permutation test optimized for the mean of the differences. about 2x faster than the default _permutation_test_2sample_paired with stat_func = np.mean.
    Coincides with the test for the differences in means. (Not as the median)
    Attrs:
            alternative:  - greater:    H0: mu(X1-X2) < <X1-X2>_sample,       H1: mu(X1-X2) >= <X1-X2>_sample
                          - less:       H0: mu(X1-X2) > <X1-X2>_sample,       H1: mu(X1-X2) <= <X1-X2>_sample
                          - two-sided:  H0: mu(X1-X2) = <X1-X2>_sample,       H1: mu(X1-X2) != <X1-X2>_sample
    Returns: p-value
    """
    dX = X1 - X2
    n = dX.size
    mean_0 = dX.mean()
    
    perm_sample = np.empty((N))
    np.random.seed(seed)
    for i in range(N):        
        shuffle = np.random.randint(0, 2, size=n) == 1
        dX_perm = dX.copy()
        dX_perm[shuffle] *= -1
        perm_sample[i] = (dX_perm).mean()
    
    if alternative == "greater":
        return (1 + (perm_sample >= mean_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= mean_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= mean_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= mean_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")
        
@njit
def permutation_test_2sample_paired_diffmedian(X1, X2, N=int(1e6)-1, alternative="two-sided", tolerance=1.5e-8, seed=0):
    """
    Paired permutation test optimized for the median of the differences. about 2x faster than the default _permutation_test_2sample_paired with stat_func = np.mean.
    NOTE: Does not coincide with the test for the differences in medians.
    
    Attrs:
            alternative:  - greater:    H0: me(X1-X2) < observed,       H1: me(X1-X2) >= observed
                          - less:       H0: me(X1-X2) > observed,       H1: me(X1-X2) <= observed
                          - two-sided:  H0: me(X1-X2) = observed,       H1: me(X1-X2) != observed.
    Returns: p-value
    """
    dX = X1 - X2
    n = dX.size
    stat_0 = np.median(dX)
    
    perm_sample = np.empty((N))
    np.random.seed(seed)
    for i in range(N):        
        shuffle = np.random.randint(0, 2, size=n) == 1
        dX_perm = dX.copy()
        dX_perm[shuffle] *= -1
        perm_sample[i] = np.median(dX_perm)
    
    if alternative == "greater":
        return (1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1)
    elif alternative == "less":
        return (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
    elif alternative == "two-sided":
        return 2 * np.fmin((1 + (perm_sample >= stat_0 - tolerance).sum()) / (N + 1),
                           (1 + (perm_sample <= stat_0 + tolerance).sum()) / (N + 1)
                          )
    else:
        raise ValueError("alternative not valid")