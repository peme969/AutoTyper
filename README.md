
# AutoTyper

## 📑 Table of Contents

- [About](#-about)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [v2 Release Notes](#-v2-release-notes)
- [Changelog](#changelog)
- [Support](#-support)
- [Contributing](#-contributing)
- [License](#-license)
  
AutoTyper is a lightweight Python application that uses PyAutoGUI and Tkinter to automate typing of large blocks of text. Simply enter your text, hit “Write Now,” and AutoTyper will wait for a configurable delay before “typing” it at the cursor position—perfect for demonstrations, demos, or repetitive text entry.

---

## 🚀 About

- **Cross‑Platform**: Runs on Windows (10+) and macOS (Intel & Apple Silicon).  
- **Configurable Delays**: Set both a start delay and a per‑character typing interval.  
- **Customizable Appearance**: Choose font family, font size, text color, background color, and “always on top” behavior.  
- **Persistent Settings**: All preferences are saved in `~/.text_writer_config.json`.

---

## 📦 Installation
<img width="70%" height="70%" alt="image" src="https://github.com/user-attachments/assets/76a90f52-c4eb-402d-9d10-3bb6134612d9" />

Click the the latest release from the Releases section ^
<img width="70%" height="70%" alt="image" src="https://github.com/user-attachments/assets/187d33ee-8877-4cc4-8adc-8fd524d2e6f3" />

Then, download the appropriate build for your platform:

- **macOS**: Download `AutoTyper.app.zip`.
  1. Double‑click to open. (should auto-extract)
  2. Move **AutoTyper.app** to your **Applications** folder.
  3. Grant Accessibility permissions when prompted (System Preferences → Security & Privacy → Privacy → Accessibility).
  4. (Optional) Right-click AutoTyper in your dock and choose "Keep in Dock" from the menu (Right-click AutoTyper -> Options -> Keep in Dock)

- **Windows**: Download `AutoTyper.exe`.
  1. Double‑click to run. 
  2. (Optional) Right‑click the running app in your taskbar and choose **Pin to taskbar** for quick access.

---

## 🎯 Usage

1. Launch **AutoTyper**.  
2. Enter the text you’d like “typed.”  
3. (Optional) Open **Options → Settings…** to adjust:
   - **Start Delay**: Seconds before typing begins.
   - **Per‑Character Delay**: Interval between each keystroke.
   - **Font & Size**: Preview text appearance.
   - **Text / Background Color**: For the dialog UI.
   - **Always on Top**: Keep the window in front.  
4. Click **Write Now**. The app disappears, waits your start delay, then “types” the text at the active cursor. A “Success!” popup appears when finished (and disappears within 2 seconds).

---

## 📝 Configuration

All settings are stored in JSON at:

```

\~/.text\_writer\_config.json

````

Feel free to edit it directly, or use the GUI **Settings** dialog to change:

```json
{
  "start_delay": 3.0,
  "delay": 0.0,
  "font": "Segoe UI",
  "font_size": 12,
  "text_color": "#000000",
  "bg_color": "#ffffff",
  "always_on_top": false
}
````

---

## 📣 v2 Release Notes

**Version 2.0** — *July 2025*

* **Brand‑new UI**
  Redesigned with Tkinter’s Clam theme for a cleaner, more intuitive look.
* **Settings Page**
  Full settings dialog to tweak start delay, per‑character delay, font, size, colors, and “always on top.”
* **Cross‑Platform Compatibility**
  • **Windows 11** tested
  • **macOS Intel & Apple Silicon** supported
* **Persistent Configuration**
  All preferences saved automatically to your home directory.
* **Toolbar & Menu Integration**
  Quick‑access ⚙️ icon and Options → Settings… menu entry.

---

## Changelog

- **v2.0.0**

  * New settings UI
  * Customizable font, color, and delay options
  * macOS support (Intel & M1/M2)
  * Enhanced “Success!” confirmation popup
- **v1.0.0**

  * Windows‑only initial release
  * Write-Now button ONLY with fixed per-char and start delay

---

## 💖 Support

If you’re finding AutoTyper useful, help me out by:

⭐ Starring this repository

🔔 Following me on GitHub: Peme969

Your support keeps the project going!
---

## 🤝 Contributing

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add awesome feature"`
4. Push to branch: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## 📜 License

MIT © Peme969 (14‑year‑old junior dev)
