import os
import subprocess

def setup():
    # 1. Yamayı Uygula (Butonları zorla getir)
    subprocess.run(["python", "patcher.py"])
    
    # 2. Eksik Dosya Varsa İndir (Sessizce)
    base = "/content/Fooocus"
    os.makedirs(f"{base}/models/clip_vision", exist_ok=True)
    
    # Clip Vision kontrolü (Buton için bu dosya şart)
    if not os.path.exists(f"{base}/models/clip_vision/clip_vision_g.safetensors"):
        print("📥 Arayüz bileşenleri yükleniyor...")
        url = "https://huggingface.co/lllyasviel/misc/resolve/main/clip_vision_g.safetensors"
        subprocess.run(["wget", "-O", f"{base}/models/clip_vision/clip_vision_g.safetensors", url, "--quiet"])

    print("🚀 Kendi Sistemimiz Başlatılıyor...")
    # Güncelleme yapmadan (yaptığımız yamayı silmesin diye) direkt başlatıyoruz
    subprocess.run(["python", "launch.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()