import os
import subprocess
import json

def setup():
    base = "/content/Fooocus"
    # Klasörleri oluştur
    os.makedirs(f"{base}/models/clip_vision", exist_ok=True)
    os.makedirs(f"{base}/models/controlnet", exist_ok=True)

    # BUTONU AÇACAK OLAN EKSİK PARÇA (Clip Vision)
    clip_path = f"{base}/models/clip_vision/clip_vision_g.safetensors"
    if not os.path.exists(clip_path):
        print("📥 Clip Vision indiriliyor (Butonu aktif etmek için şart)...")
        url = "https://huggingface.co/lllyasviel/misc/resolve/main/clip_vision_g.safetensors"
        subprocess.run(["wget", "-O", clip_path, url, "--quiet"])
    
    # DİĞER KRİTİK DOSYALARI KONTROL ET
    models = {
        f"{base}/models/controlnet/control_instant_id_sdxl.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true"
    }
    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 Eksik model indiriliyor: {os.path.basename(path)}")
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])

    print("🚀 Kurulum Tamam. Fooocus Başlatılıyor...")
    # --share ile Gradio linkini oluşturur
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()