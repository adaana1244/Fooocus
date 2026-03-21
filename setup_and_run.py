import os
import subprocess

def setup():
    print("🏗️ Standart Fooocus Altyapısı Hazırlanıyor...")
    
    # Klasörleri oluştur (Orijinal yapıya uygun)
    os.makedirs("/content/Fooocus/models/checkpoints", exist_ok=True)
    os.makedirs("/content/Fooocus/models/controlnet", exist_ok=True)
    os.makedirs("/content/Fooocus/models/instantid", exist_ok=True)

    # İndirilecek modeller (Orijinal isimleriyle)
    models = {
        # Juggernaut XL v9 (Senin istediğin ana model)
        "/content/Fooocus/models/checkpoints/juggernautXL_v9_photo.safetensors": "https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors?download=true",
        
        # InstantID Kontrolcü (Arayüzde butonun çıkması için şart)
        "/content/Fooocus/models/controlnet/control_instant_id_sdxl.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true",
        
        # FaceSwap Motoru (Inswapper)
        "/content/inswapper_128.onnx": "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx"
    }

    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 Model İndiriliyor: {os.path.basename(path)}")
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])

    print("🚀 Fooocus Orijinal Ayarlarıyla Başlatılıyor...")
    
    # Hiçbir preset zorlaması yapmıyoruz. 
    # Kullanıcı arayüzden istediği preseti (Realistic, Anime vb.) seçebilir.
    # Varsayılan olarak Juggernaut zaten klasörde olduğu için seçilebilir olacak.
    cmd = [
        "python", "entry_with_update.py", 
        "--share", 
        "--always-high-vram"
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    setup()