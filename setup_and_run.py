import os
import subprocess
import shutil

def final_patch():
    print("🛠️ Kritik UI yaması uygulanıyor...")
    # Fooocus'un 'mevcut mu?' kontrolü yaptığı dosyaya sızıyoruz
    ui_config_file = "/content/Fooocus/modules/ui_gradio.py"
    if os.path.exists(ui_config_file):
        with open(ui_config_file, "r") as f:
            content = f.read()
        # InstantID kontrolünü tamamen devre dışı bırak ve 'True' yap
        content = content.replace("self.instant_id_available", "True")
        with open(ui_config_file, "w") as f:
            f.write(content)

def setup():
    base = "/content/Fooocus"
    
    # 1. Dosyaları Garantiye Al (Her ihtimale karşı kopyala)
    clip_src = f"{base}/models/clip_vision/clip_vision_g.safetensors"
    clip_dst = f"{base}/models/controlnet/clip_vision_g.safetensors" # Alternatif yol
    
    if os.path.exists(clip_src) and not os.path.exists(clip_dst):
        shutil.copy(clip_src, clip_dst)

    # 2. Yamayı Uygula
    final_patch()

    print("🚀 SİSTEM GÜNCELLEMESİZ (NO-UPDATE) MODDA BAŞLATILIYOR...")
    # 'entry_with_update.py' yerine direkt 'launch.py' veya 'main.py' benzeri 
    # güncellemeyi tetiklemeyen ana dosyayı çalıştırıyoruz.
    subprocess.run(["python", "launch.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()