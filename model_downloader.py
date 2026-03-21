import os
import subprocess

def download_everything():
    # Klasörleri hazırla
    paths = [
        "/root/.insightface/models/unconditional",
        "/content/Fooocus/models/instantid",
        "/content/Fooocus/models/checkpoints"
    ]
    for p in paths:
        os.makedirs(p, exist_ok=True)

    models = {
        # Juggernaut XL v9 (Gerçekçiliğin Kralı)
        "/content/Fooocus/models/checkpoints/juggernautXL_v9.safetensors": "https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL-v9.safetensors?download=true",
        
        # Inswapper Optimize (MonsterMMORPG)
        "/content/inswapper_128.onnx": "https://huggingface.co/MonsterMMORPG/ai_models_swap/resolve/main/inswapper_128_fp16.onnx?download=true",
        
        # InstantID ControlNet
        "/content/Fooocus/models/instantid/diffusion_pytorch_model.safetensors": "https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true",
        
        # Analiz Modelleri
        "/root/.insightface/models/unconditional/scrfd_10g_bnkps.onnx": "https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/scrfd_10g_bnkps.onnx?download=true",
        "/root/.insightface/models/unconditional/w600k_r50.onnx": "https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/w600k_r50.onnx?download=true"
    }
    
    for path, url in models.items():
        if not os.path.exists(path):
            print(f"📥 İndiriliyor (Büyük Dosya): {path}")
            # Juggernaut çok büyük olduğu için wget ile stabil indiriyoruz
            subprocess.run(["wget", "-c", "-O", path, url, "--quiet"])
            print(f"✅ Bitti: {path}")
        else:
            print(f"✅ Zaten mevcut: {path}")

if __name__ == "__main__":
    download_everything()