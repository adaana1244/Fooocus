import os
import subprocess
import json

def setup():
    print("🛰️ Fooocus Akıllı Kurulum Başlatılıyor...")
    
    # 1. Klasörleri Hazırla
    base_path = "/content/Fooocus"
    ckpt_dir = f"{base_path}/models/checkpoints"
    ctrl_dir = f"{base_path}/models/controlnet"
    os.makedirs(ckpt_dir, exist_ok=True)
    os.makedirs(ctrl_dir, exist_ok=True)

    # 2. Modelleri Kontrol Et (Yoksa İndir)
    # Bu liste InstantID butonunu ve V9 modelini garanti eder.
    models = {
        f"{ckpt_dir}/juggernautXL_v9_photo.safetensors": "https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors?download=true",
        f"{ctrl_dir}/control_instant_id_sdxl.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true",
        "/content/inswapper_128.onnx": "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx"
    }

    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 İndiriliyor (İlk Kurulum): {os.path.basename(path)}")
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])
            print(f"✅ Hazır: {os.path.basename(path)}")
        else:
            print(f"✔️ Mevcut (Atlanıyor): {os.path.basename(path)}")

    # 3. Ayarları (Config) Sabitle (InstantID Butonu İçin Şart)
    config = {
        "path_checkpoints": ckpt_dir,
        "path_controlnet": ctrl_dir,
        "default_model": "juggernautXL_v9_photo.safetensors",
        "checkpoint_downloads": {} 
    }
    with open(f"{base_path}/config.txt", "w") as f:
        json.dump(config, f, indent=4)

    print("🚀 Fooocus Yayına Alınıyor...")
    # Standart başlatma komutu
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()