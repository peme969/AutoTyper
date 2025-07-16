import time
import json
import os
import pyautogui
import tkinter as tk
from tkinter import ttk, messagebox, colorchooser, font

# Configuration file in user's home directory
CONFIG_FILE = os.path.join(os.path.expanduser('~'), '.text_writer_config.json')

def load_config():
    default = {
        'start_delay': 3.0,
        'delay': 0.0,
        'font': 'Segoe UI',
        'font_size': 12,
        'text_color': '#000000',
        'bg_color': '#ffffff',
        'always_on_top': False
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                cfg = json.load(f)
                default.update(cfg)
        except Exception:
            pass
    return default

def save_config(cfg):
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(cfg, f, indent=4)
    except Exception as e:
        messagebox.showerror('Error', f'Failed to save settings: {e}')

def write_text(text, delay):
    # Use pyautogui.write for bulk typing with interval
    pyautogui.write(text, interval=delay)

class SettingsDialog(tk.Toplevel):
    def __init__(self, parent, config):
        super().__init__(parent)
        self.title('Settings')
        self.config = config
        self.resizable(False, False)
        self.configure(padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        frm = ttk.Frame(self)
        frm.pack(fill='both', expand=True)

        # Start Delay slider
        ttk.Label(frm, text='Start Delay (sec):').grid(row=0, column=0, sticky='w')
        self.start_var = tk.DoubleVar(value=self.config['start_delay'])
        start_scale = ttk.Scale(frm, from_=1.0, to=5.0, variable=self.start_var, orient='horizontal', command=self.update_start_label)
        start_scale.grid(row=0, column=1, sticky='ew')
        self.start_label = ttk.Label(frm, text=f"{self.start_var.get():.1f}s")
        self.start_label.grid(row=1, column=1, sticky='w', pady=(0, 10))

        # Per-char Delay slider
        ttk.Label(frm, text='Per-char Delay (sec):').grid(row=2, column=0, sticky='w')
        self.delay_var = tk.DoubleVar(value=self.config['delay'])
        delay_scale = ttk.Scale(frm, from_=0.0, to=0.1, variable=self.delay_var, orient='horizontal', command=self.update_delay_label)
        delay_scale.grid(row=2, column=1, sticky='ew')
        self.delay_label = ttk.Label(frm, text=f"{self.delay_var.get():.3f}s")
        self.delay_label.grid(row=3, column=1, sticky='w', pady=(0, 10))

        # Font family dropdown
        ttk.Label(frm, text='Font:').grid(row=4, column=0, sticky='w')
        available = list(font.families())
        self.font_var = tk.StringVar(value=self.config['font'])
        combo = ttk.Combobox(frm, textvariable=self.font_var, values=sorted(available), state='readonly')
        combo.grid(row=4, column=1, columnspan=2, sticky='ew', pady=(5, 10))

        # Font Size
        ttk.Label(frm, text='Font Size:').grid(row=5, column=0, sticky='w')
        self.size_var = tk.IntVar(value=self.config['font_size'])
        ttk.Spinbox(frm, from_=8, to=32, textvariable=self.size_var, width=5).grid(row=5, column=1, sticky='w', pady=(5, 10))

        # Color pickers
        ttk.Label(frm, text='Text Color:').grid(row=6, column=0, sticky='w')
        ttk.Button(frm, text='Choose...', command=self.choose_text_color).grid(row=6, column=1, sticky='w')
        ttk.Label(frm, text='Background Color:').grid(row=7, column=0, sticky='w')
        ttk.Button(frm, text='Choose...', command=self.choose_bg_color).grid(row=7, column=1, sticky='w')

        # Always on top
        self.always_var = tk.BooleanVar(value=self.config['always_on_top'])
        ttk.Checkbutton(frm, text='Always on Top', variable=self.always_var).grid(row=8, column=0, columnspan=3, pady=10)

        # Buttons
        btn_frame = ttk.Frame(frm)
        btn_frame.grid(row=9, column=0, columnspan=3, pady=(5,0))
        ttk.Button(btn_frame, text='Save', command=self.on_save).pack(side='left', padx=5)
        ttk.Button(btn_frame, text='Cancel', command=self.destroy).pack(side='left', padx=5)

        frm.columnconfigure(1, weight=1)

    def update_start_label(self, val):
        self.start_label.config(text=f"{float(val):.1f}s")

    def update_delay_label(self, val):
        self.delay_label.config(text=f"{float(val):.3f}s")

    def choose_text_color(self):
        color = colorchooser.askcolor(title='Select Text Color', initialcolor=self.config['text_color'])
        if color[1]:
            self.config['text_color'] = color[1]

    def choose_bg_color(self):
        color = colorchooser.askcolor(title='Select Background Color', initialcolor=self.config['bg_color'])
        if color[1]:
            self.config['bg_color'] = color[1]

    def on_save(self):
        self.config.update({
            'start_delay': round(self.start_var.get(), 1),
            'delay': round(self.delay_var.get(), 3),
            'font': self.font_var.get(),
            'font_size': self.size_var.get(),
            'always_on_top': self.always_var.get()
        })
        save_config(self.config)
        self.master.apply_settings()
        self.destroy()

class TextWriterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_dict = load_config()
        self.title('AutoTyper')
        self.geometry('500x360')
        self.configure(padx=10, pady=10)
        self.setup_style()
        self.create_widgets()
        self.apply_settings()

    def setup_style(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TButton', padding=6, font=(self.config_dict['font'], self.config_dict['font_size']))
        style.map('TButton', background=[('active', '#e1e1e1')])

    def create_widgets(self):
        # Menu bar
        menubar = tk.Menu(self)
        options_menu = tk.Menu(menubar, tearoff=0)
        options_menu.add_command(label='Settings...', command=self.open_settings)
        menubar.add_cascade(label='Options', menu=options_menu)
        self.config(menu=menubar)

        # Heading
        heading = ttk.Label(self, text='AutoTyper', font=(self.config_dict['font'], 18, 'bold'))
        heading.pack(pady=(0, 10))

        # Toolbar icon-only settings
        toolbar = ttk.Frame(self)
        toolbar.pack(fill='x')
        btn = ttk.Button(toolbar, text='⚙️', command=self.open_settings, width=2)
        btn.pack(side='right')

        # Main input area
        frm = ttk.Frame(self)
        frm.pack(fill='both', expand=True, pady=10)
        ttk.Label(frm, text='Enter text to write:', font=(self.config_dict['font'], self.config_dict['font_size'])).pack(anchor='w')
        self.text_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.text_var, width=70).pack(pady=5, fill='x')
        ttk.Button(frm, text='Write Now', command=self.on_write).pack(pady=15)

    def apply_settings(self):
        cfg = self.config_dict
        self.attributes('-topmost', cfg['always_on_top'])

    def open_settings(self):
        SettingsDialog(self, self.config_dict)

    def on_write(self):
        text = self.text_var.get().strip()
        if not text:
            messagebox.showwarning('No Text', 'Please enter some text to write.')
            return
        self.withdraw()
        # schedule typing after start_delay (non-blocking)
        delay_ms = int(self.config_dict['start_delay'] * 1000)
        self.after(delay_ms, lambda: write_text(text, self.config_dict['delay']))
        # schedule result popup
        total_time = delay_ms + int(len(text) * self.config_dict['delay'] * 1000)
        self.after(total_time, self.show_result)

    def show_result(self):
        self.deiconify()
        msg = tk.Toplevel(self)
        msg.title('Success!')
        msg.configure(padx=20, pady=20)
        ttk.Label(msg, text='✔ Text written successfully!', font=(self.config_dict['font'], 14), foreground='green').pack()
        msg.after(2000, msg.destroy)

if __name__ == '__main__':
    app = TextWriterApp()
    app.mainloop()
