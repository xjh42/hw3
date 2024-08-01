from needle import backend_ndarray as nd

a = nd.NDArray([1,2,3], device=nd.cuda())
print(a ** 2)