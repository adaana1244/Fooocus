import os
import subprocess
import json

def setup():
    print("🏗️ Fooocus + InstantID Tam Kurulum Başlatılıyor...")
    
    base = "/content/Fooocus"
    # Klasörleri garanti altına al
    dirs = [
        f"{base}/models/checkpoints",
        f"{base}/models/controlnet",
        f"{base}/models/clip_vision"
    ]
    for d in dirs: os.makedirs(d, exist_ok=True)

    # BUTONU TETİKLEYEN 3 KRİTİK DOSYA
    models = {
        # 1. Ana Model (v8)
        f"{base}/models/checkpoints/juggernautXL_v8Rundiffusion.safetensors": 
        "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/juggernautXL_v8Rundiffusion.safetensors",
        
        # 2. InstantID ControlNet (İsim çok önemli!)
        f"{base}/models/controlnet/control_instant_id_sdxl.safetensors": 
        "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true",
        
        # 3. Clip Vision (Bu olmadan buton bazen tetiklenmez)
        f"{base}/models/clip_vision/clip_vision_g.safetensors": 
        "https://huggingface.co/lllyasviel/misc/resolve/main/clip_vision_g.safetensors"
    }

    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 İndiriliyor: {os.path.basename(path)}")
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])

    # FaceSwap dosyası (İsteğe bağlı ama tam olsun)
    if not os.path.exists("/content/inswapper_128.onnx"):
        subprocess.run(["wget", "-O", "/content/inswapper_128.onnx", "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx", "--quiet"])

    # CONFIG.TXT (Butonları görünür kılan asıl anahtar)
    config = {
        "path_checkpoints": f"{base}/models/checkpoints",
        "path_controlnet": f"{base}/models/controlnet",
        "path_clip_vision": f"{base}/models/clip_vision",
        "default_model": "juggernautXL_v8Rundiffusion.safetensors",
        "checkpoint_downloads": {} 
    }
    with open(f"{base}/config.txt", "w") as f:
        json.dump(config, f, indent=4)

    print("🚀 Sistem Hazır. InstantID Aktif Ediliyor...")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()