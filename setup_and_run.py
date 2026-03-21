import os
import subprocess
import glob

def setup():
    print("🛠️ Juggernaut XL v9 (Xet-Bypass) İndirme Başlatılıyor...")
    
    # Bozuk küçük dosyaları (pointerları) temizle
    for f in glob.glob("/content/Fooocus/models/checkpoints/juggernautXL*"):
        os.remove(f)
        print(f"🗑️ Temizlendi: {f}")

    # Doğrudan indirme linki (Bu link Xet engelini aşar)
    juggernaut_url = "https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors?download=true"
    
    models = {
        "/content/Fooocus/models/checkpoints/juggernautXL_v9_photo.safetensors": juggernaut_url,
        "/content/inswapper_128.onnx": "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx",
        "/content/Fooocus/models/instantid/diffusion_pytorch_model.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors"
    }
    
    os.makedirs("/content/Fooocus/models/instantid", exist_ok=True)

    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 Gerçek Model Verisi İndiriliyor: {path}")
            # --header ekleyerek tarayıcı gibi davranmasını sağlıyoruz
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])
            print(f"✅ Başarıyla İndi: {path}")
    
    print("🚀 Model Doğrulandı! Fooocus v9 ile başlatılıyor...")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram", "--preset", "realistic"])

if __name__ == "__main__":
    setup()