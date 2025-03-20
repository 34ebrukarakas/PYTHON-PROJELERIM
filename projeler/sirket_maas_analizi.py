#görev1
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
maaslar = np.random.randint(3000,15001,500)

print("Ortalama maaş", np.mean(maaslar), "TL")
print("En yüksek maaş", np.max(maaslar), "TL")
print("En düşük maaş", np.min(maaslar), "TL")

plt.hist(maaslar, bins=30, color='skyblue', edgecolor='black')
plt.title("Maaş Dağılımı")
plt.xlabel("Maaş (TL)")
plt.ylabel("Çalışan sayısı")
plt.show()

#görev2
departmanlar = np.random.choice([1,2,3],size=500)

muhendislik_maaslari = maaslar[departmanlar == 1]
muhasebe_maaslari = maaslar[departmanlar == 2]
pazarlama_aaslari = maaslar[departmanlar == 3]

print("Mühendislik alanındaki ortalama maaş", round(np.mean(muhendislik_maaslari),2), "TL")
print("Muhasebe anlanındaki ortalama maaş ", round(np.mean(muhasebe_maaslari),2), "TL")
print("Pazarlama alnaındaki ortalama maaş", round(np.mean(pazarlama_aaslari),2), "TL")

departman_ortalama_maas = [np.mean(muhendislik_maaslari), np.mean(muhasebe_maaslari), np.mean(pazarlama_aaslari)]
departman_adlari = ['Mühendislik','Muhasebe','Pazarlama']

plt.bar(departman_adlari, departman_ortalama_maas, color =['blue', 'green', 'orange'] )
plt.title("Departmanlara Göre Ortalama Maaş")
plt.xlabel("Departman")
plt.ylabel("Ortalama Maaş (TL)")
plt.show()

