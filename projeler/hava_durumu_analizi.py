#bölüm2 
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
sicakliklar = np.random.randint(-10,41,365)

print("Ortalama sıcaklık",round( np.mean(sicakliklar),2),"°C")
print("En sıcak gün", np.max(sicakliklar),"°C")
print("En soğuk gün", np.min(sicakliklar),"°C")

plt.plot(sicakliklar, color= 'skyblue', label = "sıcaklık")
plt.title("Günlük Sıcaklık Değişimi (Bir Yıl)")
plt.xlabel("Gün")
plt.ylabel("Sıcaklık (°C)")
plt.show()

