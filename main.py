import keyboard
import threading
import tkinter as tk
from popup_window import ClipboardProgressPopup
from clipboard_processor import process_clipboard

correction_enabled = True

def toggle_correction(popup):
    global correction_enabled
    correction_enabled = not correction_enabled
    status = "ENABLED" if correction_enabled else "DISABLED"
    print(f"\n🚀 Clipboard AI Correction is now {status}.\n")
    popup.update_message(f"🚀 AI Clipboard is {status}")

def on_copy_hotkey(popup):
    global correction_enabled
    if correction_enabled:
        threading.Thread(target=process_clipboard, args=(popup,), daemon=True).start()

def start_keyboard_listener(popup):
    keyboard.on_press_key("c", lambda e: on_copy_hotkey(popup) if keyboard.is_pressed("ctrl") else None)
    keyboard.add_hotkey("ctrl+shift+e", lambda: toggle_correction(popup))
    print("🚀 Clipboard AI Corrector is running (Press Ctrl+Shift+E to enable/disable)\n")
    keyboard.wait()

def main():
    root = tk.Tk()
    popup = ClipboardProgressPopup(root)
    threading.Thread(target=start_keyboard_listener, args=(popup,), daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    main()
