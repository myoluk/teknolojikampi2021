# teknolojikampi2021
Açıklab Pardus ve Liman Teknoloji Kampı

Bir linux sunucu üzerinde çalıştırılacak **tercihen** python scripti (yapabilen bash de yapabilir ;D ) ile aşağıdaki işlemler yapılacaktır; 
- Genel sorgu fonksiyonu

  Bu fonksiyon değişken almamaktadır
  - İşletim sistemindeki kurulu paket sayısını ekrana yazdırma


- Bir paket sorgusu

  Bu fonksiyon girdi olarak bir paket adı almaktadır
  - Değişken olarak verilen bir paketin kurulu olup olmadığını ekrana yazdırma
  - Değişken olarak verilen ve yüklü olmayan bir paketin kaç adet bağımlılığa sahip olduğunun listelenmesi
  - Değişken olarak verilen ve yüklü olmayan bir paketin kaç adet bağımlıklarından yüklü olanların ve olmayanların ayrı ayrı listelenmesi 
  - Yine aynı paketin kaç adet bağımlılığının yükleneceğinin ekrana yazdırılması

# Anahtar Kelimeler
- python
  -  apt_pkg modülü
  -  apt modülü
  -  apt_deps modülü
-  bash 
  -  dpkg komutu
  -  apt komutu

---
# Çalıştırma
```sh
python3 script.py
```
```sh
python3 script.py <paket_adı>
```
> python3 script.py cowsay

# Ekran Görüntüleri

- Genel Sorgu (Sistemdeki paket sayısı):
![Genel Sorgu](https://raw.githubusercontent.com/myoluk/teknolojikampi2021/main/ss/genel-sorgu.jpg)

- Paket Sorgu 1 (Kurulu olan paket):
![Paket Sorgu 1](https://raw.githubusercontent.com/myoluk/teknolojikampi2021/main/ss/paket-sorgu-1.jpg)

- Paket Sorgu 2 (Kurulu olmayan paket):
![Paket Sorgu 2](https://raw.githubusercontent.com/myoluk/teknolojikampi2021/main/ss/paket-sorgu-2.jpg)
