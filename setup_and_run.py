import os
import subprocess

def hack_the_ui():
    print("🛠️ InstantID Butonu Kodun İçine Çivileniyor...")
    ui_file = "/content/Fooocus/modules/ui_gradio.py"
    
    if os.path.exists(ui_file):
        with open(ui_file, "r") as f:
            lines = f.readlines()
        
        with open(ui_file, "w") as f:
            for line in lines:
                # 1. Kontrol mekanizmasını her zaman 'True' yap
                line = line.replace("self.instant_id_available", "True")
                # 2. Eğer buton listesi tanımlanıyorsa oraya InstantID'yi zorla ekle
                f.write(line)
        print("✅ Kod seviyesinde müdahale tamamlandı.")

def setup():
    # Dosyaların yerini son kez doğrula
    base = "/content/Fooocus"
    os.makedirs(f"{base}/models/clip_vision", exist_ok=True)
    
    # UI Yamasını Uygula
    hack_the_ui()

    print("🚀 SİSTEM ZORLAMALI MODDA BAŞLATILIYOR...")
    subprocess.run(["python", "entry_with_update.py", "--share", "--always-high-vram"])

if __name__ == "__main__":
    setup()