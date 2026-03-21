import os
import subprocess
import time

def setup():
    print("🚀 Hayal-Engine Otonom Sistem Başlatılıyor...")
    
    # 1. Kütüphaneleri Kur
    print("⚙️ Kütüphaneler Mart 2026 standartlarına sabitleniyor...")
    subprocess.run(["pip", "install", "-r", "requirements.txt", "--quiet"])
    subprocess.run(["pip", "install", "deep-translator", "onnxruntime-gpu", "--quiet"])

    # 2. Modelleri Kontrol Et ve İndir
    models = {
        "/content/Fooocus/models/checkpoints/juggernautXL_v9.safetensors": "https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL-v9.safetensors?download=true",
        "/content/inswapper_128.onnx": "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx?download=true",
        "/content/Fooocus/models/instantid/diffusion_pytorch_model.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true",
        "/root/.insightface/models/unconditional/scrfd_10g_bnkps.onnx": "https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/scrfd_10g_bnkps.onnx?download=true",
        "/root/.insightface/models/unconditional/w600k_r50.onnx": "https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/w600k_r50.onnx?download=true"
    }
    
    os.makedirs("/root/.insightface/models/unconditional", exist_ok=True)
    os.makedirs("/content/Fooocus/models/instantid", exist_ok=True)

    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 Eksik Model İndiriliyor: {path}")
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])
    
    # 3. Fooocus'u Başlat
    print("✨ Her şey hazır! Gradio linki hazırlanıyor...")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram", "--preset", "realistic"])

if __name__ == "__main__":
    setup()