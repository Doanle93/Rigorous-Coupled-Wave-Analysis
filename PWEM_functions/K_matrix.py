'''
functions which generate the K matrices along each direction

'''
import numpy as np
from scipy import sparse

def K_matrix_cubic_2D(beta_x, beta_y, a_x, a_y, N_p, N_q):
    #    K_i = beta_i - pT1i - q T2i - r*T3i
    # but here we apply it only for cubic and tegragonal geometries in 2D
    '''
    :param beta_i:
    :param T1:reciprocal lattice vector 1
    :param T2:
    :param T3:
    :return:
    '''
    k_x = beta_x - 2*np.pi*np.arange(-int(N_p), int(N_p)+1)/a_x;
    k_y = beta_y - 2*np.pi*np.arange(-int(N_q), int(N_q)+1)/a_y;

    kx, ky = np.meshgrid(k_x, k_y)
    # final matrix should be sparse...since it is diagonal at most
    Kx = sparse.diags(np.ndarray.flatten(kx)); #NxNy dimension matrix
    Ky = sparse.diags(np.ndarray.flatten(ky))
    Kx = Kx.astype('complex');
    Ky = Ky.astype('complex')

    return Kx, Ky

def K_matrix_cubic_3D(beta_x, beta_y, a_x, a_y, N_p, N_q):
    #    K_i = beta_i - pT1i - q T2i - r*T3i
    # but here we apply it only for cubic and tegragonal geometries in 2D
    '''
    :param beta_i:
    :param T1:reciprocal lattice vector 1
    :param T2:
    :param T3:
    :return:
    '''
    return None;