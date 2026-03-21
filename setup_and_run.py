import os
import subprocess
import json

def setup():
    base = "/content/Fooocus"
    # Tüm gerekli klasörleri tek seferde oluştur
    for d in ["models/checkpoints", "models/controlnet", "models/clip_vision"]:
        os.makedirs(f"{base}/{d}", exist_ok=True)

    # BUTONU AKTİF EDEN KRİTİK DOSYALAR
    models = {
        # InstantID için şart olan Clip Vision (3.7 GB)
        f"{base}/models/clip_vision/clip_vision_g.safetensors": "https://huggingface.co/lllyasviel/misc/resolve/main/clip_vision_g.safetensors",
        
        # InstantID Motoru
        f"{base}/models/controlnet/control_instant_id_sdxl.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true",
        
        # Ana Model (V8)
        f"{base}/models/checkpoints/juggernautXL_v8Rundiffusion.safetensors": "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/juggernautXL_v8Rundiffusion.safetensors"
    }

    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 Eksik dosya indiriliyor: {os.path.basename(path)}")
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])
        else:
            print(f"✔️ Mevcut: {os.path.basename(path)}")

    # CONFIG.TXT (Yolları doğrula)
    config = {
        "path_checkpoints": f"{base}/models/checkpoints",
        "path_controlnet": f"{base}/models/controlnet",
        "path_clip_vision": f"{base}/models/clip_vision",
        "default_model": "juggernautXL_v8Rundiffusion.safetensors",
        "checkpoint_downloads": {} 
    }
    with open(f"{base}/config.txt", "w") as f:
        json.dump(config, f, indent=4)

    print("🚀 Sistem Başlatılıyor... InstantID Butonu Artık Aktif Olmalı.")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()