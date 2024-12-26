Nama : Lathiifah Hanuun

## Deskripsi Proyek
Proyek dirrancang sebagai sarana pembelajaran bagi mahasiswa untuk memahami dan menerapkan konsep dalam Pembelajaran Mesin. Disini saya mengambil tema Memprediksi tempat wisata di USA dengan berbagai macam informasi yang diberikan. Proyek ini juga digunakan untuk membandingkan dua jenis model, yaitu Random forest dan Feedforward Neural Network (FNN).

## Dataset
Menggunakan Dataset dari Kaggle :
https://www.kaggle.com/datasets/thedevastator/us-travel-check-ins-analysis?select=Location.csv

## Deskripsi Model
### Model Random Forest
- **Deskripsi:**
  Random Forest digunakan sebagai baseline model. Model ini mampu menangani fitur kategori dan numerik dengan baik tanpa memerlukan preprocessing yang kompleks.
- **Performa:**
  Model menghasilkan akurasi lebih dari 50% pada dataset balanced setelah oversampling dengan SMOTE.

  ### Model Feedforward Neural Network (FNN)
- **Deskripsi:**
  Model FNN dirancang menggunakan TensorFlow/Keras dengan beberapa lapisan fully connected. Model ini memanfaatkan fitur yang telah di-scaled dan menggunakan dropout untuk mengurangi overfitting.
- **Performa:**
  FNN memberikan akurasi lebih rendah dibandingkan Random Forest pada konfigurasi awal, tetapi performanya dapat ditingkatkan dengan fine-tuning hyperparameter dan penggunaan class weights.

  ## Preprocessing dan Modelling
  ### Preprocessing
  Preprocessing yang dilakukan yaitu membagi state menjadi beberapa region yaitu West, East, South, North, dan Other. Lalu memeriksa Missing value dan mengisi kolom yang kosong dengan modus dari kolom tersebut, lalu encoding variabel kategorikal yaitu Region dan Categories. Selanjutnya membagi fitur dan target dengan target yaitu 'Categories_enc', membagi data train dan test dengan rasio 80:20. Yang terakhir yaitu oversampling target dengan SMOTE.

  ### Modelling
#### Random Forest
  ![Screenshot 2024-12-26 073411](https://github.com/user-attachments/assets/be297aeb-b5e5-4c7b-aca6-15f7249d5e6b)
  ![Screenshot 2024-12-26 072330](https://github.com/user-attachments/assets/0bd38349-df79-4fd4-b512-cab06bde5d8c)

![download (38)](https://github.com/user-attachments/assets/83678f08-f523-4912-a9d0-f4ec4e451cf8)

#### FeedForward Neural Network (FNN)
![Screenshot 2024-12-26 073841](https://github.com/user-attachments/assets/94989342-ae95-4a51-9a53-2a7209c8db77)
![Screenshot 2024-12-26 072555](https://github.com/user-attachments/assets/9cf5abe1-d879-4733-a02b-d006df0f4516)
![download (39)](https://github.com/user-attachments/assets/793a5589-4a51-4c91-b5a2-dcf14aa470df)
