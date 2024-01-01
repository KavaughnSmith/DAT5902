def linear_regression(x, y):
    meanx = np.mean(x)
    meany = np.mean(y)
    sigmax  = np.std(x)
    sigmay  = np.std(y)
    sigmaxy = np.sum(np.multiply(x-meanx,y-meany))/(len(x)-1)
    m = sigmaxy/(sigmax*sigmax) 
    q = meany-m*meanx
    return m,q
