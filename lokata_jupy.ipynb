import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

freq = 12
rate = 0.05
years = 5
bank = 0.12
pv = 120000

# Ile będzie wynosiła orientacyjna cena mieszkania za 5 lat?
fv = npf.fv(rate,5,0,-pv)
print('Zadanie 1:', np.around(fv,2))

# Output: Zadanie 1: 153153.79

rate /= freq
bank /= freq 
nper = years * freq

# Ile musisz wpłacać do banku każdego miesiąca, aby przy przedstawionej
# ofercie uzbierać na mieszkanie w ciągu 5 lat?

payment_per_month = npf.pmt(bank,nper,0,-fv)
print('Zadanie 2:', np.around(payment_per_month,2))

# Output: Zadanie 2: 1875.28

# Stwórz wykres przedstawiający, jak w interwałach miesięcznych zmieniać 
# się będzie cena mieszkania (liniowy wzrost w całym okresie)
# oraz wartość twojej lokaty.

price = pv*(1+rate)**np.arange(0, nper+1)
deposit = np.zeros(nper+1)
for i in range(1,nper+1):
    deposit[i] = (deposit[i-1]+payment_per_month)*(1+bank)

plt.plot(price,label='Cena mieszkania')
plt.plot(deposit,label='Wartość lokaty')
plt.legend()
plt.xlabel('Liczba okresów')
plt.ylabel('Wartość w złotych')
