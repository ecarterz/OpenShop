# OpenShop API

OpenShop API adalah layanan backend RESTful yang kuat untuk platform e-commerce, dibangun menggunakan **Django** dan **Django REST Framework (DRF)**. Proyek ini dirancang dengan standar pengembangan modern, mencakup fitur-fitur canggih seperti Soft Delete dan kepatuhan terhadap HATEOAS.

## 🚀 Fitur Utama

- **Arsitektur RESTful**: Mengikuti prinsip desain REST yang standar.
- **Operasi CRUD**: Create, Read, Update, dan Delete untuk manajemen produk.
- **Soft Delete Mechanism**:
  - Produk yang dihapus tidak hilang permanen dari database, melainkan ditandai dengan flag `is_delete=True`.
  - _List View_: Secara otomatis menyembunyikan produk yang sudah dihapus.
  - _Detail View_: Masih mengizinkan akses ke produk yang dihapus (berguna untuk audit/history).
- **HATEOAS Support**: Setiap respons JSON menyertakan field `_links` dinamis yang memandu klien mengenai aksi selanjutnya yang tersedia (GET, PUT, DELETE).
- **Pencarian (Search)**: Fitur pencarian produk berdasarkan nama menggunakan query parameter.
- **UUID Primary Keys**: Menggunakan UUID alih-alih integer ID biasa untuk keamanan dan skalabilitas yang lebih baik.
- **Struktur Response Konsisten**: Endpoint list dibungkus dalam key `products` untuk kemudahan parsing di sisi frontend.

## 🛠️ Teknologi yang Digunakan

- **Bahasa**: Python 3.x
- **Framework**: Django 6.0.1
- **API Toolkit**: Django REST Framework
- **Database**: SQLite (Default)

## 📦 Instalasi & Menjalankan Project

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di komputer lokal Anda:

1.  **Clone Repository**

    ```bash
    git clone https://github.com/ecarterz/OpenShop.git
    cd OpenShop
    ```

2.  **Buat dan Aktifkan Virtual Environment**

    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Migrasi Database**

    ```bash
    python manage.py migrate
    ```

5.  **Jalankan Server**
    ```bash
    python manage.py runserver
    ```

API akan tersedia di `http://localhost:8000/`.

## 📖 Dokumentasi API

### Base URL

`http://localhost:8000/`

### Endpoints

| Method   | Endpoint               | Deskripsi                                                                               |
| :------- | :--------------------- | :-------------------------------------------------------------------------------------- |
| `GET`    | `/products/`           | Mengambil daftar semua produk (kecuali yang dihapus). Mendukung filter `?name=keyword`. |
| `POST`   | `/products/`           | Membuat produk baru.                                                                    |
| `GET`    | `/products/<uuid:id>/` | Mengambil detail produk spesifik.                                                       |
| `PUT`    | `/products/<uuid:id>/` | Memperbarui data produk.                                                                |
| `DELETE` | `/products/<uuid:id>/` | Menghapus produk (Soft Delete).                                                         |

### Contoh Request Body (POST)

```json
{
  "name": "Laptop Gaming High-End",
  "sku": "LPT-001",
  "description": "Laptop spesifikasi tinggi untuk gaming dan rendering.",
  "shop": "Official Store",
  "location": "Jakarta",
  "price": 25000000,
  "discount": 5,
  "category": "Electronics",
  "stock": 10,
  "picture": "https://example.com/image.jpg"
}
```

### Contoh Response dengan HATEOAS

```json
{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "Laptop Gaming High-End",
    ...
    "_links": [
        {
            "rel": "self",
            "href": "http://localhost:8000/products/550e8400-...",
            "action": "GET",
            "types": ["application/json"]
        },
        ...
    ]
}
```

---

Dibuat untuk submission OpenShop Backend.
