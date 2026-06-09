Markdown
# 🚀 SubTrack - Akıllı Abonelik Yönetim Merkezi

SubTrack, günümüzün dijital dünyasında kullanıcıların unutulan veya kullanılmayan abonelik (Netflix, Spotify, Gym, Yazılım lisansları vb.) harcamalarını tek bir ekrandan yönetmelerini, takip etmelerini ve gereksiz maliyetlerden kurtulmalarını sağlayan web tabanlı bir yönetim platformudur.

## 💡 Projenin Amacı ve Girişimcilik Vizyonu
"Abonelik yorgunluğu" ve "hayalet harcamalar" gün geçtikçe büyüyen bir finansal problemdir. SubTrack, karmaşık genel bütçe uygulamalarının aksine tamamen **abonelik yönetimine (mikro-niş)** odaklanarak kullanıcılara doğrudan para tasarrufu sağlamayı hedefler. Temel vizyonumuz, gelecekte tüm aboneliklerin tek tıkla başlatılıp durdurulabildiği bir dijital merkez (hub) haline gelmektir.

## ✨ Temel Özellikler (MVP)
* **Kapsamlı Listeleme:** Aktif tüm aboneliklerin detaylı (Platform, Fiyat, Yenilenme Tarihi) listelenmesi.
* **Kolay Ekleme/Çıkarma:** Saniyeler içinde yeni abonelik tanımlama veya iptal edilenleri sistemden silme (CRUD İşlemleri).
* **Kullanıcı Dostu Arayüz:** Modern, sade ve mobil uyumlu ön yüz tasarımı.
* **RESTful API Mimarisi:** Arka planda güvenli ve hızlı veri alışverişi.

## 🛠️ Kullanılan Teknolojiler
Bu proje, modern web geliştirme standartlarına uygun olarak modüler bir mimaride inşa edilmiştir.

* **Backend (Arka Plan):** Python, Flask, Flask-CORS
* **Veritabanı:** MySQL
* **Frontend (Ön Yüz):** HTML5, CSS3, Bootstrap (Jinja2 Template Engine ile entegre)
* **Geliştirme Ortamı:** VS Code
* **Versiyon Kontrolü:** Git & GitHub

## ⚙️ Kurulum Adımları
Projeyi kendi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. **Depoyu Klonlayın:**
   ```bash
   git clone [https://github.com/polat1443/SubTrack.git](https://github.com/polat1443/SubTrack.git)
   cd SubTrack
Gerekli Kütüphaneleri Yükleyin:
Python ortamınızda aşağıdaki paketlerin kurulu olduğundan emin olun:

Bash
pip install Flask flask-cors mysql-connector-python
Veritabanını Yapılandırın:

XAMPP veya benzeri bir yerel sunucu başlatın.

SubTrackDB adında bir MySQL veritabanı oluşturun.

Proje içerisindeki db.py dosyasında yer alan kullanıcı adı ve şifre yapılandırmalarını kendi yerel sunucunuza göre güncelleyin.

Uygulamayı Başlatın:

Bash
python app.py
Uygulama varsayılan olarak http://127.0.0.1:5000 adresinde çalışacaktır.

👨‍💻 Geliştirici
Polat Bilir Iğdır Üniversitesi - Yazılım Mühendisliği
