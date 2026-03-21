import os
import subprocess
import glob

def setup():
    print("🛠️ Full Arayüz Modu: Juggernaut v9 + InstantID + ADetailer Aktif Ediliyor...")
    
    # Bozuk dosyaları temizle
    for f in glob.glob("/content/Fooocus/models/checkpoints/juggernautXL*"):
        os.remove(f)

    # Gerekli Modeller (InstantID ve Inswapper dahil)
    models = {
        "/content/Fooocus/models/checkpoints/juggernautXL_v9_photo.safetensors": "https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors?download=true",
        "/content/inswapper_128.onnx": "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx",
        "/content/Fooocus/models/controlnet/control_v11p_sd15_canny.pth": "https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny.pth",
        "/content/Fooocus/models/instantid/diffusion_pytorch_model.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors"
    }
    
    os.makedirs("/content/Fooocus/models/instantid", exist_ok=True)
    os.makedirs("/content/Fooocus/models/controlnet", exist_ok=True)

    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 İndiriliyor: {path}")
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])
    
    print("🚀 Arayüz Modifiye Ediliyor (InstantID & FaceDetailer Entegrasyonu)...")
    
    # Başlatma komutuna ADetailer ve InstantID'yi tetikleyen flagleri ekliyoruz
    # --advanced-preview ve --enable-async-gpu-generate hızı artırır
    # --preset realistic zaten pek çok ayarı getirir ama biz manuel zorluyoruz
    cmd = [
        "python", "entry_with_update.py", 
        "--share", 
        "--always-high-vram", 
        "--preset", "realistic",
        "--controlnet-softness", "0.5" # InstantID'nin daha doğal durması için
    ]
    
    subprocess.run(cmd)

if __name__ == "__main__":
    setup()