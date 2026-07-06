import os
import json

# Konfigurasi
WALLPAPER_DIR = "wallpapers"
OUTPUT_JSON = "wallpapers.json"
# Ganti dengan username dan nama repo GitHub Anda
BASE_URL = "https://raw.githubusercontent.com/USERNAME/NAMA_REPO/main/wallpapers/"

def generate_wallpaper_json():
    wallpaper_list = []
    id_counter = 1

    if not os.path.exists(WALLPAPER_DIR):
        print(f"Folder {WALLPAPER_DIR} tidak ditemukan.")
        return

    # Membaca semua file di dalam folder wallpapers
    files = sorted(os.listdir(WALLPAPER_DIR))
    
    for file_name in files:
        # Hanya proses file .webp yang sudah dikonversi
        if file_name.lower().endswith('.webp'):
            # Mencoba menebak kategori dari nama file, misal "Mawar_Merah_01.webp" -> Kategori: "Mawar"
            # Jika nama file tidak pakai lambang "_", kategori default jadi "Umum"
            if "_" in file_name:
                category = file_name.split('_')[0].capitalize()
                title = file_name.split('.')[0].replace('_', ' ')
            else:
                category = "Umum"
                title = file_name.split('.')[0].capitalize()

            wallpaper_item = {
                "id": id_counter,
                "title": title,
                "category": category,
                "url": f"{BASE_URL}{file_name}"
            }
            wallpaper_list.append(wallpaper_item)
            id_counter += 1

    # Simpan ke file wallpapers.json dengan format yang rapi
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(wallpaper_list, f, indent=2, ensure_ascii=False)
    
    print(f"Berhasil memperbarui {OUTPUT_JSON} dengan {len(wallpaper_list)} wallpaper.")

if __name__ == "__main__":
    generate_wallpaper_json()
