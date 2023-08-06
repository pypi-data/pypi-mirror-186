import numpy as np
from numpy.polynomial import Polynomial
import pytest

import utils

def check_npf_array(arr, expected_func_arr):
    expected_func_arr = np.array(expected_func_arr)
    expected_shape = expected_func_arr.shape
    assert isinstance(arr, utils.npf.ndarray)
    assert arr.shape == expected_shape
    xs = np.array([-2.0,-1.0,0.0,1.0,2.0,-2.0j,-1.0j,1.0j,2.0j,2.0-2.0j,2.0-1.0j,2.0+0.0j,2.0+1.0j,2.0+2.0j])
    for x in xs:
        res = arr(x)
        assert res.shape == expected_shape
        assert np.allclose(res.reshape(-1), np.array([func(x) for func in expected_func_arr.reshape(-1)]))
    res = arr(xs)
    assert res.shape == (*xs.shape, *expected_shape)
    assert np.allclose(res.reshape(-1), np.array([[func(x) for func in expected_func_arr.reshape(-1)] for x in xs]).reshape(-1))
    xs = xs.reshape(2,7)
    assert arr(xs).shape == (*xs.shape, *expected_shape)
    
def test_shape():
    f1, f2 = lambda x: 2*x, lambda x: 3*x
    a = utils.npf.array([[f1, f2]])
    x = np.ones((3,4))
    assert a(x).shape == (3,4,1,2)
    assert a(x, batch='trailing').shape == (1,2,3,4)

def test():
    f1, f2 = lambda x: 2*x, lambda x: 3*x
    g1, g2 = lambda x: 4*x, lambda x: 5*x
    a = utils.npf.array([[f1, f2]])
    b = utils.npf.array([g1, g2])
    
    # check shape
    # print(a, b)
    check_npf_array(a, [[f1, f2]])
    check_npf_array(b, [g1, g2])
    
    # check add two functions
    c = a+b
    # print(c)
    check_npf_array(c, [[lambda x: f1(x)+g1(x), lambda x: f2(x)+g2(x)]])
    
    # check slicing
    d = c[:,:1]
    # print(d)
    check_npf_array(d, [[lambda x: f1(x)+g1(x)]])
    
    # check that new function does not retain reference to old function
    a[0] = lambda x: x
    b[0] = lambda x: x
    # print(a, b)
    check_npf_array(a, [[lambda x: x, lambda x: x]])
    check_npf_array(b, [lambda x: x, g2])
    check_npf_array(a+b, [[lambda x: x+x, lambda x: x+g2(x)]])
    check_npf_array(c, [[lambda x: f1(x)+g1(x), lambda x: f2(x)+g2(x)]]) # should be invariant to assignments to a and b
    check_npf_array(d, [[lambda x: f1(x)+g1(x)]]) # should be invariant to assignments to a and b
    
    a = utils.npf.array([[f1, f2]])
    b = utils.npf.array([g1, g2])
    
    # check a bunch of basic operators
    c = b+a
    # print(c)
    check_npf_array(c, [[lambda x: f1(x)+g1(x), lambda x: f2(x)+g2(x)]])
    
    c = a-b
    # print(c)
    check_npf_array(c, [[lambda x: f1(x)-g1(x), lambda x: f2(x)-g2(x)]])
    
    c = a*b
    # print(c)
    check_npf_array(c, [[lambda x: f1(x)*g1(x), lambda x: f2(x)*g2(x)]])
    
    g1, g2 = lambda x: 4*x+3, lambda x: 5*x+4
    b = utils.npf.array([g1, g2])
    c = a/b
    # print(c)
    check_npf_array(c, [[lambda x: f1(x)/g1(x), lambda x: f2(x)/g2(x)]])
    
    c = a**b
    # print(c)
    check_npf_array(c, [[lambda x: f1(x)**g1(x), lambda x: f2(x)**g2(x)]])
    
#     # check operations respect parantheses
#     c = b**((a+b)*b-a)
#     print(c)
    
    # check that operations work with scalars
    b = np.pi
    check_npf_array(a+b, [[lambda x: f1(x)+b, lambda x: f2(x)+b]]) # scalar + npf_func
    check_npf_array(b+a, [[lambda x: f1(x)+b, lambda x: f2(x)+b]]) # npf_func + scalar
    
    b = np.array([np.pi, 2*np.pi])
    check_npf_array(a+b, [[lambda x: f1(x)+b[0], lambda x: f2(x)+b[1]]]) # npf_func + array_scalar
    check_npf_array(b+a, [[lambda x: f1(x)+b[0], lambda x: f2(x)+b[1]]]) # array_scalar + npf_func
    
    b = utils.npf.array([np.pi, 2*np.pi])
    check_npf_array(a+b, [[lambda x: f1(x)+b[0], lambda x: f2(x)+b[1]]]) # npf_func + npf_scalar
    check_npf_array(b+a, [[lambda x: f1(x)+b[0], lambda x: f2(x)+b[1]]]) # npf_scalar + npf_func
    
    a = utils.npf.array([[1.0,2.0]])
    check_npf_array(a+b, [[lambda x: a[0,0]+b[0], lambda x: a[0,1]+b[1]]]) # npf_scalar + array_scalar
    check_npf_array(b+a, [[lambda x: a[0,0]+b[0], lambda x: a[0,1]+b[1]]]) # array_scalar + npf_scalar
    
    # check that operations work with polynomials
    a = utils.npf.array([[Polynomial([3,2,1]), Polynomial([1,2,3])]])
    b = utils.npf.array([Polynomial([4,5]), Polynomial([5,4])])
    check_npf_array(a+b, [[a[0,0]+b[0], a[0,1]+b[1]]]) # npf_poly + npf_poly
    
    b = utils.npf.array([g1, g2])
    check_npf_array(a+b, [[lambda x: a[0,0](x)+g1(x), lambda x: a[0,1](x)+g2(x)]]) # npf_poly + npf_func
    check_npf_array(b+a, [[lambda x: a[0,0](x)+g1(x), lambda x: a[0,1](x)+g2(x)]]) # npf_func + npf_poly
    
    # b = Polynomial([1,2])
    # check_npf_array(a+b, [[lambda x: a[0,0](x)+b(x), lambda x: a[0,1](x)+b(x)]]) # npf_poly + poly
    # check_npf_array(b+a, [[lambda x: a[0,0](x)+b(x), lambda x: a[0,1](x)+b(x)]]) # poly + npf_poly
    
    b = utils.npf.array([np.pi, 2*np.pi])
    check_npf_array(a+b, [[a[0,0]+b[0], a[0,1]+b[1]]]) # npf_poly + npf_scalar
    check_npf_array(b+a, [[a[0,0]+b[0], a[0,1]+b[1]]]) # npf_scalar + npf_poly
    
    b = np.array([np.pi, 2*np.pi])
    check_npf_array(a+b, [[a[0,0]+b[0], a[0,1]+b[1]]]) # npf_poly + array_scalar
    check_npf_array(b+a, [[a[0,0]+b[0], a[0,1]+b[1]]]) # array_scalar + npf_poly
    
    b = np.pi
    check_npf_array(a+b, [[a[0,0]+b, a[0,1]+b]]) # npf_poly + scalar
    check_npf_array(b+a, [[a[0,0]+b, a[0,1]+b]]) # scalar + npf_poly
    
@pytest.mark.parametrize('a, b, inv', [
    (utils.npf.array([[lambda x: 2*x, lambda x: 3*x],[lambda x: 4*x, lambda x: 5*x]]),
     utils.npf.array([[lambda x: 6*x, lambda x: 7*x],[lambda x: 8*x, lambda x: 9*x]]), True),
    (utils.npf.array([[Polynomial([1,2,3]), Polynomial([4,5])],[Polynomial([2,1]), Polynomial([6,5,4])]]),
     utils.npf.array([[Polynomial([2,3]), Polynomial([5,6,7])],[Polynomial([3,2]), Polynomial([5,4,3])]]), False),
    (utils.npf.array([[1,2],[3.0,5.0]]),
     utils.npf.array([[3,4],[5.0,6.0]]), True),
])
def test_linalg(a, b, inv):
    x = np.linspace(1,2,num=3)
    
    result, expected = (a @ b)(x), a(x) @ b(x)
    assert (result.shape == expected.shape) and np.allclose(result, expected)
    
    result, expected = utils.npf.trace(a)(x), np.trace(a(x), axis1=-2, axis2=-1)
    assert (result.shape == expected.shape) and np.allclose(result, expected)
    
    result, expected = utils.npf.det(a)(x), np.linalg.det(a(x))
    assert (result.shape == expected.shape) and np.allclose(result, expected)
    
    result, expected = utils.npf.adj(a)(x), np.linalg.inv(a(x))*np.linalg.det(a(x))[:,None,None]
    assert (result.shape == expected.shape) and np.allclose(result, expected)
    
    if inv:
        result, expected = utils.npf.inv(a)(x), np.linalg.inv(a(x))
        assert (result.shape == expected.shape) and np.allclose(result, expected)
