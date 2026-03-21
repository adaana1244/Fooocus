import os
import subprocess
import json

def setup():
    print("🏗️ Fooocus v8 + InstantID Standart Kurulum Başlatılıyor...")
    
    base_path = "/content/Fooocus"
    ckpt_dir = f"{base_path}/models/checkpoints"
    ctrl_dir = f"{base_path}/models/controlnet"
    os.makedirs(ckpt_dir, exist_ok=True)
    os.makedirs(ctrl_dir, exist_ok=True)

    # V8 ve InstantID Modelleri
    models = {
        f"{ckpt_dir}/juggernautXL_v8Rundiffusion.safetensors": "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/juggernautXL_v8Rundiffusion.safetensors",
        f"{ctrl_dir}/control_instant_id_sdxl.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true"
    }

    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 İndiriliyor: {os.path.basename(path)}")
            # v8 zaten Fooocus'un resmi linki olduğu için çok hızlı iner
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])
            print(f"✅ Hazır: {os.path.basename(path)}")
        else:
            print(f"✔️ Mevcut: {os.path.basename(path)}")

    # Config dosyasını v8'e göre ayarlıyoruz
    config = {
        "path_checkpoints": ckpt_dir,
        "path_controlnet": ctrl_dir,
        "default_model": "juggernautXL_v8Rundiffusion.safetensors",
        "checkpoint_downloads": {} 
    }
    with open(f"{base_path}/config.txt", "w") as f:
        json.dump(config, f, indent=4)

    print("🚀 Sistem v8 Modunda Başlatılıyor...")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()