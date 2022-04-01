import numpy as np
import matplotlib.pyplot as plt

Initial_Capital = 100

Mean = 0.05
Sigma = 0.3

Nsteps = 100  # Number of steps
Npaths = 10000000 # Number of paths

Equity_Curves = np.r_[Initial_Capital * np.ones((1,Npaths)), Initial_Capital  + np.cumsum((np.random.normal(loc=Mean, scale=Sigma, size=(Nsteps-1,Npaths))),axis=0)]

# plt.plot(Equity_Curves)
# plt.show()

# plt.hist(Equity_Curves[-1], bins=50)
# plt.show()

m = np.mean(Equity_Curves[-1])
s = np.std(Equity_Curves[-1])

assert np.abs(m - (Initial_Capital + Mean*Nsteps)) < 1e-2
assert np.abs(s - Sigma*np.sqrt(Nsteps)) < 1e-2

Max_Loss = 0.001

for i in range(Nsteps-1):
    mask = Equity_Curves[i] < Initial_Capital * (1 - Max_Loss)
    Equity_Curves[i+1] = Equity_Curves[i] * mask + Equity_Curves[i+1] * np.logical_not(mask)

m_sl = np.mean(Equity_Curves[-1])
s_sl = np.std(Equity_Curves[-1])


print("Mean: without Stop Loss ", m, ", with Stop Loss ", m_sl)
print("Std: without Stop Loss ", s, ", with Stop Loss ", s_sl)