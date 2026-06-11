# 🚀 SubTrack - Akıllı Abonelik Yönetim Merkezi

SubTrack, günümüzün dijital dünyasında kullanıcıların unutulan veya kullanılmayan abonelik (Netflix, Spotify, Gym, Yazılım lisansları vb.) harcamalarını tek bir ekrandan yönetmelerini, takip etmelerini ve gereksiz maliyetlerden kurtulmalarını sağlayan web tabanlı bir yönetim platformudur.

## 💡 Projenin Amacı ve Girişimcilik Vizyonu
"Abonelik yorgunluğu" ve "hayalet harcamalar" gün geçtikçe büyüyen bir finansal problemdir. SubTrack, karmaşık genel bütçe uygulamalarının aksine tamamen **abonelik yönetimine (mikro-niş)** odaklanarak kullanıcılara doğrudan para tasarrufu sağlamayı hedefler. Temel vizyonumuz, gelecekte tüm aboneliklerin tek tıkla başlatılıp durdurulabildiği bir dijital merkez (hub) haline gelmektir.

## ✨ Temel Özellikler (MVP)
* **📊 Dinamik Finansal Dashboard:** Chart.js entegrasyonu ile harcama dağılımı grafikleri ve yıllık "hayalet harcama" projeksiyonu.
* **🤖 Akıllı İptal Asistanı:** Kullanıcıyı platformun resmi iptal sayfalarına yönlendiren tek tıkla iptal simülasyonu.
* **Kapsamlı Listeleme ve CRUD:** Saniyeler içinde yeni abonelik tanımlama, düzenleme ve iptal edilenleri sistemden silme.
* **Kullanıcı Dostu Arayüz:** Modern, sade ve Bootstrap tabanlı mobil uyumlu ön yüz tasarımı.

## 🛠️ Kullanılan Teknolojiler
Bu proje, modern web geliştirme standartlarına uygun olarak (Server-Side Rendering) modüler bir mimaride inşa edilmiştir.

* **Backend (Arka Plan):** Python, Flask
* **Veritabanı:** SQLite (Hafif ve dosya tabanlı mimari)
* **Frontend (Ön Yüz):** HTML5, CSS3, Bootstrap, Chart.js (Jinja2 Template Engine ile entegre)
* **Geliştirme Ortamı:** VS Code
* **Versiyon Kontrolü:** Git & GitHub

## ⚙️ Kurulum Adımları
Projeyi kendi yerel bilgisayarınızda çalıştırmak oldukça basittir. SQLite kullanıldığı için **XAMPP veya ekstra bir veritabanı sunucusu kurmanıza gerek yoktur.**

**1. Depoyu Klonlayın:**
```bash
git clone [https://github.com/polat1443/SubTrack.git](https://github.com/polat1443/SubTrack.git)
cd SubTrack
```

**2. Gerekli Kütüphaneleri Yükleyin:**
Python ortamınızda Flask'ın kurulu olduğundan emin olun:
```bash
pip install Flask
```

**3. Uygulamayı Başlatın:**
Proje dizinindeyken aşağıdaki komutu çalıştırın. Veritabanı (`subtrack.db`) otomatik olarak oluşturulacaktır:
```bash
python app.py
```
*Uygulama varsayılan olarak `http://127.0.0.1:5000` adresinde çalışacaktır.*

---

## 👨‍💻 Geliştirici
**Polat Bilir** | *Iğdır Üniversitesi - Yazılım Mühendisliği*
