import os
import subprocess

def setup():
    print("🚀 Sistem Stabilize Ediliyor...")
    
    # Modellerin yerini kontrol et (zaten indiler, sadece emin oluyoruz)
    os.makedirs("/content/Fooocus/models/instantid", exist_ok=True)
    os.makedirs("/content/Fooocus/models/controlnet", exist_ok=True)

    print("✨ Fooocus v2.5.5 Başlatılıyor...")
    
    # Hata veren --controlnet-softness kaldırıldı.
    # Bu ayarı arayüz açılınca "Advanced" kısmından elle yapabileceğiz.
    cmd = [
        "python", "entry_with_update.py", 
        "--share", 
        "--always-high-vram", 
        "--preset", "realistic"
    ]
    
    subprocess.run(cmd)

if __name__ == "__main__":
    setup()