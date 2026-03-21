import os

def apply_hard_patch():
    ui_path = "modules/ui_gradio.py"
    if os.path.exists(ui_path):
        with open(ui_path, "r") as f:
            content = f.read()
        
        # InstantID kontrolünü 'True' yaparak kilidi kırıyoruz
        content = content.replace("self.instant_id_available", "True")
        
        with open(ui_path, "w") as f:
            f.write(content)
        print("✅ UI Kilidi Kırıldı!")

if __name__ == "__main__":
    apply_hard_patch()