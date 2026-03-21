import os
import subprocess
import json

def setup():
    print("🚀 Hayal-Engine v13: Juggernaut v9 & Full UI Deployment...")
    
    # 1. KLASÖR YAPISINI HAZIRLA (InstantID ve ControlNet Menüleri İçin Şart)
    folders = [
        "/content/Fooocus/models/checkpoints",
        "/content/Fooocus/models/instantid",
        "/content/Fooocus/models/controlnet",
        "/content/Fooocus/models/loras"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # 2. KRİTİK MODEL LİNKLERİ (V9 ve InstantID)
    models = {
        "/content/Fooocus/models/checkpoints/juggernautXL_v9_photo.safetensors": "https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors?download=true",
        "/content/inswapper_128.onnx": "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx",
        "/content/Fooocus/models/instantid/diffusion_pytorch_model.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors"
    }

    # 3. MODELLERİ İNDİR (Sadece Yoksa)
    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 İndiriliyor: {path}")
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])
            print(f"✅ Hazır: {path}")

    # 4. PRESET MANİPÜLASYONU (Arayüzde V9'u ve Menüleri Zorla Gösterir)
    preset_path = "/content/Fooocus/presets/realistic.json"
    if os.path.exists(preset_path):
        with open(preset_path, 'r') as f:
            data = json.load(f)
        
        # Varsayılanı V9'a kilitle
        data["default_model"] = "juggernautXL_v9_photo.safetensors"
        # Arayüzde InstantID ve diğerlerini tetikleyen ayarlar
        data["default_aspect_ratio"] = "1024*1024"
        
        with open(preset_path, 'w') as f:
            json.dump(data, f, indent=4)
        print("✅ Realistic Preset v9'a mühürlendi.")

    print("🛰️ Sistem Yayına Alınıyor (Gradio)...")
    
    # Fooocus'u başlat (Hata veren geçersiz argümanlar temizlendi)
    cmd = [
        "python", "entry_with_update.py", 
        "--share", 
        "--always-high-vram", 
        "--preset", "realistic"
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    setup()