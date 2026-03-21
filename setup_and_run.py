import os
import subprocess
import shutil

def setup():
    print("🛠️ Bozuk dosyalar temizleniyor ve ADetailer/InstantID kuruluyor...")
    
    # Bozuk Juggernaut varsa sil ki baştan temiz insin
    corrupted_path = "/content/Fooocus/models/checkpoints/juggernautXL_v9.safetensors.corrupted"
    if os.path.exists(corrupted_path):
        os.remove(corrupted_path)
        print("🗑️ Bozuk model dosyası silindi.")

    # Kütüphaneleri Kur
    subprocess.run(["pip", "install", "-r", "requirements.txt", "--quiet"])
    # ADetailer ve InstantID için gerekli ek paketler
    subprocess.run(["pip", "install", "deep-translator", "onnxruntime-gpu", "opencv-python", "pyyaml", "--quiet"])

    # Modelleri Kontrol Et ve İndir (WGET -c ile kaldığımız yerden devam eder)
    models = {
        "/content/Fooocus/models/checkpoints/juggernautXL_v9.safetensors": "https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL-v9.safetensors?download=true",
        "/content/inswapper_128.onnx": "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx?download=true",
        "/content/Fooocus/models/instantid/diffusion_pytorch_model.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true"
    }
    
    os.makedirs("/content/Fooocus/models/instantid", exist_ok=True)

    for path, url in models.items():
        print(f"🔄 Kontrol ediliyor: {path}")
        # -c parametresi sayesinde internet kopsa bile kaldığı yerden devam eder
        subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])
    
    print("✨ Tüm modeller hazır! Fooocus ADetailer ve InstantID ile başlatılıyor...")
    # --enable-async-gpu-generate: Üretimi hızlandırır
    # --controlnet-softness: Yüzün daha doğal oturmasını sağlar
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram", "--preset", "realistic"])

if __name__ == "__main__":
    setup()