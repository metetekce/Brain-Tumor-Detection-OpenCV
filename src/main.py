import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

# --- 1. OTOMATİK DOSYA BULMA ---
# Klasördeki .jpg veya .png ile biten dosyaları bulur
current_folder = os.getcwd()
files = [f for f in os.listdir(current_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Eğer 3'ten fazla resim varsa sadece ilk 3 tanesini al
files = files[:3] 

print(f"İşlenecek Dosyalar: {files}")

def calculate_snr(original, processed):
    # Sinyal Gücü / Gürültü Gücü
    signal = np.mean(original)
    noise = original - processed
    noise_std = np.std(noise)
    if noise_std == 0: return 0
    return signal / noise_std

if len(files) == 0:
    print("HATA: Klasörde hiç resim bulunamadı! Lütfen .jpg dosyalarının kodla aynı yerde olduğundan emin ol.")
else:
    plt.figure(figsize=(15, 10))

    for i, filename in enumerate(files):
        # --- 2. RESİM YÜKLEME ---
        img_path = os.path.join(current_folder, filename)
        img = cv2.imread(img_path, 0) # Gri tonlamalı oku
        
        if img is None:
            print(f"HATA: {filename} okunamadı!")
            continue

        # --- 3. İŞLEME (Preprocessing: Gaussian Blur) ---
        processed = cv2.GaussianBlur(img, (5, 5), 0)

        # --- 4. METRİK (SNR) ---
        snr_val = calculate_snr(img, processed)
        
        # Konsola Verileri Yaz (Rapor için lazım)
        print(f"\n--- {filename} Analizi ---")
        print(f"Boyut (Dimensions): {img.shape}")
        print(f"Piksel Sayısı: {img.size}")
        print(f"SNR Değeri: {snr_val:.4f}")

        # --- 5. GÖRSELLEŞTİRME ---
        # Orijinal
        plt.subplot(3, 2, 2*i + 1)
        plt.imshow(img, cmap='gray')
        plt.title(f"{filename} - Raw (Orijinal)")
        plt.axis('off')

        # İşlenmiş
        plt.subplot(3, 2, 2*i + 2)
        plt.imshow(processed, cmap='gray')
        plt.title(f"Processed (Gaussian Filter) | SNR: {snr_val:.2f}")
        plt.axis('off')

    plt.tight_layout()
    plt.show()