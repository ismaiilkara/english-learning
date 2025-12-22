# 📝 English Learning Hub - Yapılacaklar

## ✅ Tamamlanan
- [x] Web sitesi temel yapısı (Alpine.js + Tailwind)
- [x] Yan menüde konu başlıkları
- [x] Video bölümü (sürükle-bırak arayüzü)
- [x] Egzersiz bölümü (çoktan seçmeli)
- [x] Türkçe → İngilizce çeviri soruları
- [x] Skor sistemi ve ilerleme çubuğu

---

## 📋 Yapılacaklar

### 🎬 YouTube Videoları Ekleme
1. [ ] Her konu için video kaydet veya uygun YouTube videoları bul
2. [ ] Videoları YouTube'a yükle (gizli/unlisted olarak)
3. [ ] `data.json` dosyasına embed linklerini ekle

**Örnek format:**
```json
"video": "https://www.youtube.com/embed/VIDEO_ID"
```

**Mevcut Konular:**
| Konu | Video Durumu |
|------|-------------|
| Present Simple Tense | ⏳ Bekleniyor |
| Past Simple Tense | ⏳ Bekleniyor |
| Future Tense (Will) | ⏳ Bekleniyor |
| Common Vocabulary | ⏳ Bekleniyor |
| Articles (A, An, The) | ⏳ Bekleniyor |

---

### 📚 İçerik Ekleme (Opsiyonel)
- [ ] Daha fazla konu ekle
- [ ] Her konuya daha fazla soru ekle
- [ ] Farklı soru tipleri ekle (eşleştirme, dinleme vs.)

---

## 🔧 data.json Düzenleme Rehberi

Video eklemek için `data.json` dosyasını aç ve ilgili konunun `video` alanını güncelle:

```json
{
  "id": 1,
  "title": "Present Simple Tense",
  "video": "https://www.youtube.com/embed/BURAYA_VIDEO_ID",
  ...
}
```

**YouTube Video ID Nasıl Bulunur:**
- YouTube video URL'si: `https://www.youtube.com/watch?v=ABC123`
- Embed URL'si: `https://www.youtube.com/embed/ABC123`

---

## 📁 Dosya Yapısı
```
english-learning/
├── index.html    # Ana site dosyası
├── data.json     # Konular, videolar, sorular
└── NOTLAR.md     # Bu dosya
```

## 🚀 Siteyi Çalıştırma
```bash
cd english-learning
python3 -m http.server 8080
```
Tarayıcıda: http://localhost:8080
