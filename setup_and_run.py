import os
import subprocess
import glob

def setup():
    print("🛠️ Kritik Juggernaut onarımı başlatılıyor...")
    
    # Bozuk Juggernaut kalıntılarını tamamen temizle
    for f in glob.glob("/content/Fooocus/models/checkpoints/juggernautXL_v9*"):
        print(f"🗑️ Siliniyor: {f}")
        os.remove(f)

    # Kütüphaneleri tazele
    subprocess.run(["pip", "install", "-r", "requirements.txt", "--quiet"])

    # Modeller - Juggernaut için alternatif ve daha stabil bir link kullanıyoruz
    models = {
        "/content/Fooocus/models/checkpoints/juggernautXL_v9.safetensors": "https://huggingface.co/stablediffusionapi/juggernaut-xl-v9/resolve/main/juggernautXL_v9.safetensors",
        "/content/inswapper_128.onnx": "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx",
        "/content/Fooocus/models/instantid/diffusion_pytorch_model.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors"
    }
    
    os.makedirs("/content/Fooocus/models/instantid", exist_ok=True)

    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 İndiriliyor (Stabil Link): {path}")
            # wget yerine aria2c kullanarak daha hızlı ve güvenli indirebiliriz ama wget -c de yeterli
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])
    
    print("✨ Model onarıldı! Fooocus başlatılıyor...")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram", "--preset", "realistic"])

if __name__ == "__main__":
    setup()