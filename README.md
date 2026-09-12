# MINI_PROJECT_Muhammad_Favian_Daffa

Nama: Muhammad Favian Daffa<br>
Kelas: 26A<br>
NIM: 2609116021<br>
<br>
Penjelasan kode :<br>

1. Inisialisasi Data dan Menu Utama<br>
<img width="338" height="162" alt="image" src="https://github.com/user-attachments/assets/661570b0-976f-40d4-9f5c-fc68f84ba209" />

Bagian ini merupakan awal program. data_mahasiswa = [] digunakan untuk membuat list kosong sebagai tempat penyimpanan data mahasiswa. Kemudian while True digunakan agar menu terus berjalan dan ditampilkan berulang kali sampai pengguna memilih menu keluar. Pengguna dapat memilih menu dari 1 sampai 5<br>
<br>

2. Menambahkan Data Mahasiswa<br>
<img width="454" height="617" alt="image" src="https://github.com/user-attachments/assets/0a9a9652-a6de-4d92-bdd1-46457cf9ecf5" />

Bagian ini digunakan untuk menambahkan data mahasiswa. Pengguna diminta memasukkan nama, nilai Tugas, UTS, dan UAS. Setiap nilai diperiksa agar berada pada rentang 0–100. try-except digunakan untuk menangani kesalahan apabila pengguna memasukkan input yang bukan angka. Setelah semua data valid, data disimpan ke dalam list menggunakan append()<br>
<br>

3. Menampilkan Data dan Menghitung Grade<br>
<img width="476" height="446" alt="image" src="https://github.com/user-attachments/assets/afb06a2c-2f18-42a9-b0c5-4a58e0a7d108" />

Bagian ini digunakan untuk menampilkan seluruh data mahasiswa. Program terlebih dahulu mengecek apakah data mahasiswa sudah tersedia. Jika ada, program mengambil data nama, Tugas, UTS, dan UAS kemudian menghitung nilai akhir<br>

Perhitungan nilai akhir menggunakan bobot:<br>

Nilai Tugas = 30%<br>
Nilai UTS = 30%<br>
Nilai UAS = 40%<br>

Selanjutnya, program menentukan grade berdasarkan nilai akhir, yaitu A, B, C, D, atau E menggunakan percabangan if, elif, dan else<br>
<br>

4. Mengubah Data Mahasiswa<br>
<img width="556" height="698" alt="image" src="https://github.com/user-attachments/assets/e1cc38aa-6b1e-4615-99ac-c4cfd59cab42" />

Bagian ini digunakan untuk mengubah data mahasiswa yang sudah tersimpan. Pengguna memasukkan nama mahasiswa yang ingin diubah. Program kemudian mencari nama tersebut di dalam data_mahasiswa. Jika data ditemukan, pengguna dapat memasukkan nilai Tugas, UTS, dan UAS yang baru. Nilai tersebut kemudian menggantikan nilai sebelumnya. Jika nama tidak ditemukan, program menampilkan pesan "Data mahasiswa tidak ditemukan"<br>
<br>

5. Menghapus Data Mahasiswa<br>
<img width="496" height="220" alt="image" src="https://github.com/user-attachments/assets/df8e3f33-d162-4653-a350-e11642b088e4" />

Bagian ini digunakan untuk menghapus data mahasiswa. Pengguna memasukkan nama mahasiswa yang ingin dihapus. Program mencari nama tersebut di dalam list. Jika ditemukan, data mahasiswa dihapus menggunakan fungsi remove(). Jika nama yang dimasukkan tidak terdapat dalam list, program menampilkan pesan "Data Mahasiswa Tidak Ditemukan"<br>
<br>

6. Keluar Program dan Validasi Menu<br>
<img width="400" height="103" alt="image" src="https://github.com/user-attachments/assets/88c10491-624b-4be5-b7da-77fe75aa313c" />

Bagian terakhir digunakan untuk mengakhiri program sekaligus melakukan validasi pilihan menu. Jika pengguna memilih menu 5, program menampilkan pesan terima kasih dan break digunakan untuk menghentikan perulangan while. Jika pengguna memasukkan pilihan selain 1–5, program akan menampilkan pesan "Pilihan Menu Tidak Tersedia!" dan pengguna dapat kembali memilih menu yang benar<br>
<br>
<br>

OUTPUT :<br>
<img width="266" height="460" alt="Screenshot 2026-09-12 211930" src="https://github.com/user-attachments/assets/250b052e-02e3-4864-b98e-62be555180b8" /><br>
<img width="288" height="578" alt="Screenshot 2026-09-12 211945" src="https://github.com/user-attachments/assets/b7a70ace-fb7c-4d1d-9dcc-2f2db3b48d9c" /><br>
<img width="305" height="515" alt="Screenshot 2026-09-12 212002" src="https://github.com/user-attachments/assets/4c6e5e1c-f0e7-4026-8eea-b7ce86f830cf" /><br>
<img width="317" height="407" alt="Screenshot 2026-09-12 212017" src="https://github.com/user-attachments/assets/360c5cfc-3e0f-4ada-a109-9e9934130f56" /><br>

<br>
<br>
<br>

FLOWCHART :<br>
<br>
<img width="2147" height="2203" alt="MINI_PROJECT_DDP-1" src="https://github.com/user-attachments/assets/d5c1620e-3bdb-432e-a4c6-e16af37920c5" />


