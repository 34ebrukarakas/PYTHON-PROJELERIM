import numpy as np
import matplotlib.pyplot as plt

urunler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"]

satis_miktarlari = np.random.randint(10, 101, size=(5, 30))

toplam_satislar = np.sum(satis_miktarlari, axis=1)
ortalama_satislar = np.mean(satis_miktarlari, axis=1)

for urun, toplam, ortalama in zip(urunler, toplam_satislar, ortalama_satislar):
    print(f"{urun} - Toplam Satış: {toplam}, Ortalama Satış: {ortalama:.2f}")

plt.figure(figsize=(10, 6))
plt.bar(urunler, toplam_satislar, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Ürünler")
plt.ylabel("Toplam Satış Miktarı")
plt.title("Ürün Bazında Toplam Satış Miktarları")
plt.show()
