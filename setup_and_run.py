import os
import subprocess
import json

def setup():
    print("🏗️ Fooocus Altyapısı Doğrulanıyor...")
    
    # 1. Klasör Yollarını Sabitleyelim
    base_path = "/content/Fooocus"
    ckpt_path = f"{base_path}/models/checkpoints"
    ctrl_path = f"{base_path}/models/controlnet"
    
    # 2. Config.txt Dosyasını Manuel Oluşturalım (BUTONLARI TETİKLEYEN ASIL KISIM)
    # Eğer bu dosya doğru yolları göstermezse butonlar çıkmaz.
    config_data = {
        "path_checkpoints": ckpt_path,
        "path_controlnet": ctrl_path,
        "path_loras": f"{base_path}/models/loras",
        "path_embeddings": f"{base_path}/models/embeddings",
        "path_vae_approx": f"{base_path}/models/vae_approx",
        "path_upscale_models": f"{base_path}/models/upscale_models",
        "path_inpaint": f"{base_path}/models/inpaint",
        "path_clip_vision": f"{base_path}/models/clip_vision",
        "path_fooocus_expansion": f"{base_path}/models/prompt_expansion/fooocus_expansion",
        "path_outputs": f"{base_path}/outputs",
        "default_model": "juggernautXL_v9_photo.safetensors",
        "checkpoint_downloads": {} 
    }
    
    with open(f"{base_path}/config.txt", "w") as f:
        json.dump(config_data, f, indent=4)
    print("✅ Config.txt güncellendi. Yollar kilitlendi.")

    # 3. BAŞLAT
    print("🚀 Fooocus V9 ve InstantID Modunda Başlatılıyor...")
    # --share ve --always-high-vram ile en stabil halini açıyoruz
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()