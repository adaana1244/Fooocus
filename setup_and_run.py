import os
import subprocess

def force_instant_id_ui():
    print("🛠️ Arayüz kilitleri kırılıyor...")
    # Fooocus'un içinde InstantID butonunu gizleyen mantığı devre dışı bırakıyoruz.
    # Bu işlem, modeller klasörde olsa bile bazen tetiklenmeyen UI bug'ını çözer.
    ui_path = "/content/Fooocus/modules/ui_gradio.py"
    if os.path.exists(ui_path):
        with open(ui_path, "r") as f:
            lines = f.readlines()
        
        with open(ui_path, "w") as f:
            for line in lines:
                # InstantID'nin görünmesini engelleyen 'if' kontrollerini etkisizleştiriyoruz
                new_line = line.replace("if self.instant_id_available:", "if True:")
                f.write(new_line)

def setup():
    # Dosyaların yerini bir kez daha garantiye alalım
    base = "/content/Fooocus"
    os.makedirs(f"{base}/models/clip_vision", exist_ok=True)
    
    # Clip Vision dosyasının ismini Fooocus'un en sevdiği formata çevirelim
    src_clip = f"{base}/models/clip_vision/clip_vision_g.safetensors"
    # Bazı sürümler bu ismi arıyor:
    dst_clip = f"{base}/models/clip_vision/pytorch_model.bin" 
    
    if os.path.exists(src_clip) and not os.path.exists(dst_clip):
        os.symlink(src_clip, dst_clip)

    force_instant_id_ui()

    print("🚀 SİSTEM ZORLANMIŞ MODDA BAŞLATILIYOR...")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()