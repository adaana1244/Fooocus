import os
import subprocess
import json

def setup():
    print("🎯 InstantID Motoru Kuruluyor...")
    
    # 1. KLASÖRÜ GARANTİYE AL
    target_dir = "/content/Fooocus/models/controlnet"
    os.makedirs(target_dir, exist_ok=True)

    # 2. EKSİK OLAN ANA MOTOR (Bu dosya ismi 'InstantID' butonunu açar)
    # Yaklaşık 2.5 GB'lık ana dosya
    instantid_model_path = os.path.join(target_dir, "control_instant_id_sdxl.safetensors")
    instantid_url = "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true"

    if not os.path.exists(instantid_model_path):
        print(f"📥 InstantID Ana Motoru İndiriliyor (2.5GB): {instantid_model_path}")
        subprocess.run(["wget", "-c", "-O", instantid_model_path, instantid_url, "--quiet"])
        print("✅ İndirme Tamamlandı!")

    # 3. DİĞER MODELLERİ KONTROL ET (Inswapper vb.)
    if not os.path.exists("/content/inswapper_128.onnx"):
        subprocess.run(["wget", "-c", "-O", "/content/inswapper_128.onnx", "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx", "--quiet"])

    print("🚀 Fooocus v9 + InstantID Yayına Hazır...")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram", "--preset", "realistic"])

if __name__ == "__main__":
    setup()