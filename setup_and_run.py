import os
import subprocess

def patch_fooocus_ui():
    print("🛠️ InstantID Buton Kilidi Kırılıyor...")
    # Fooocus'un InstantID'yi gizlediği ana dosyayı bulup modifiye ediyoruz
    ui_path = "/content/Fooocus/modules/ui_gradio.py"
    
    if os.path.exists(ui_path):
        with open(ui_path, "r") as f:
            content = f.read()
        
        # 'instant_id_available' kontrolünü 'True' yaparak butonu zorla görünür yapıyoruz
        new_content = content.replace("self.instant_id_available", "True")
        
        with open(ui_path, "w") as f:
            f.write(new_content)
        print("✅ UI yaması başarıyla uygulandı.")

def setup():
    base = "/content/Fooocus"
    # Dosyaların yerlerini ve isimlerini kontrol et (Fooocus bazen isim seçer)
    os.makedirs(f"{base}/models/clip_vision", exist_ok=True)
    
    # Clip Vision dosyasının hem orijinal hem de alternatif ismini garantiye al
    clip_file = f"{base}/models/clip_vision/clip_vision_g.safetensors"
    alt_clip = f"{base}/models/clip_vision/pytorch_model.bin" # Bazı sürümler bunu arar
    
    if os.path.exists(clip_file) and not os.path.exists(alt_clip):
        os.symlink(clip_file, alt_clip)

    # Yamayı uygula
    patch_fooocus_ui()

    print("🚀 SİSTEM ZORLAMALI MODDA BAŞLATILIYOR...")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()