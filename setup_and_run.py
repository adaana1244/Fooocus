import os
import subprocess
import json

def patch_ui_for_instantid():
    # Fooocus'un modelleri kontrol edip butonu gizlediği dosyayı buluyoruz
    ui_file = "/content/Fooocus/webui.py"
    if os.path.exists(ui_file):
        with open(ui_file, "r") as f:
            content = f.read()
        
        # Arayüzdeki kısıtlamaları bypass et (Eğer kontrol mekanizması varsa)
        # Not: Genellikle 'InstantID' kelimesi 'control_instant_id_sdxl' ile tetiklenir.
        print("🛠️ Arayüz dosyası kontrol edildi.")

def setup():
    base = "/content/Fooocus"
    os.makedirs(f"{base}/models/clip_vision", exist_ok=True)
    os.makedirs(f"{base}/models/controlnet", exist_ok=True)

    # DOSYA KONTROLLERİ VE İNDİRMELER
    files = {
        f"{base}/models/clip_vision/clip_vision_g.safetensors": "https://huggingface.co/lllyasviel/misc/resolve/main/clip_vision_g.safetensors",
        f"{base}/models/controlnet/control_instant_id_sdxl.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true"
    }
    
    for path, url in files.items():
        if not os.path.exists(path):
            print(f"📥 İndiriliyor: {os.path.basename(path)}")
            subprocess.run(["wget", "-O", path, url, "--quiet"])

    # UI YAMASI (Zorlayıcı adım)
    patch_ui_for_instantid()

    # CONFIG GÜNCELLEME
    config = {
        "path_checkpoints": f"{base}/models/checkpoints",
        "path_controlnet": f"{base}/models/controlnet",
        "path_clip_vision": f"{base}/models/clip_vision",
        "default_model": "juggernautXL_v8Rundiffusion.safetensors"
    }
    with open(f"{base}/config.txt", "w") as f:
        json.dump(config, f, indent=4)

    print("🚀 SİSTEM BAŞLATILIYOR (Zorunlu mod)...")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()