# 🫀 Heart Disease Risk Prediction AI

Repositori ini berisi program *Machine Learning* yang dikembangkan menggunakan Python untuk menganalisis data kesehatan pasien dan memprediksi probabilitas risiko penyakit jantung. Proyek ini juga dilengkapi dengan konfigurasi Docker untuk kemudahan *deployment*.

## 🎯 Tujuan Proyek
* Menganalisis data historis kesehatan pasien.
* Memprediksi risiko penyakit jantung secara dini berbasis probabilitas.
* Membantu tenaga medis dalam proses deteksi dini.

## 🌍 Dampak (Social Impact)
Proyek ini sejalan dengan **SDG 3: Good Health and Well-Being**, yang bertujuan untuk meningkatkan kesadaran kesehatan masyarakat dan membantu tindakan pencegahan sejak dini.

## ⚙️ Cara Kerja & Proses AI
1. **Input Data**: Membaca dataset pasien yang sudah ada (mencakup berbagai metrik kesehatan).
2. **Proses Machine Learning**: Algoritma mempelajari pola risiko penyakit dari dataset tersebut.
3. **Output Prediksi**: Menghasilkan prediksi berbasis probabilitas apakah seorang pasien berisiko terkena penyakit jantung.

## 🛠️ Teknologi yang Digunakan
* **Python** (`heart_AI.py`): Script utama pemrosesan *Machine Learning*.
* **Docker** (`docker-compose.yml`): Konfigurasi *container* untuk menjalankan aplikasi.
* **Dataset**: Menggunakan dataset klinis (`dataset_heart` & `heart_cleveland_upload`).

## 👥 Target Pengguna
* Tenaga Medis (Dokter/Klinik)
* Institusi Kesehatan
* Masyarakat Umum

## ⚠️ Peringatan (Disclaimer)
Proyek ini merupakan eksperimen akademis (*Proof of Concept*) untuk eksplorasi pengolahan data. Model AI yang digunakan masih memiliki keterbatasan akurasi dan validasi metrik. Oleh karena itu, hasil prediksi dari program ini bersifat **simulasi** dan **tidak valid 100% untuk dijadikan rujukan atau diagnosis medis profesional**.
