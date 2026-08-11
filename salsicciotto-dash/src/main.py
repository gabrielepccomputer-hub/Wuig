import customtkinter as ctk
import os

app = ctk.CTk()
app.geometry("950x90")
app.overrideredirect(True)
app.attributes("-alpha", 0.90)
app.configure(fg_color="#1E293B")

salsicciotto_frame = ctk.CTkFrame(
    app, 
    fg_color=("#38BDF8", "#0284C7"), 
    corner_radius=45, 
    border_width=3, 
    border_color="#1D4ED8"
)
salsicciotto_frame.pack(fill="both", expand=True, padx=10, pady=10)

btn_g = ctk.CTkButton(
    salsicciotto_frame, 
    text="G", 
    font=("Arial", 22, "bold"),
    fg_color="#1D4ED8",
    hover_color="#3B82F6",
    width=50, height=50,
    corner_radius=25,
    command=lambda: print("Torcia G attivata! Menu principale aperto.")
)
btn_g.pack(side="left", padx=15)

def apri_app(nome_app):
    print(f"Apertura a lanterna di: {nome_app}...")

def mostra_menu_contestuale(event, nome_app):
    menu = ctk.CTkToplevel(app)
    menu.geometry("240x220")
    menu.overrideredirect(True)
    menu.attributes("-alpha", 0.95)
    menu.geometry(f"+{event.x_root}+{event.y_root}")
    
    ctk.CTkButton(menu, text="Esegui come amministratore", fg_color="transparent", text_color="white", anchor="w", command=lambda: [print("Eseguito come Admin"), menu.destroy()]).pack(fill="x", padx=5, pady=2)
    ctk.CTkButton(menu, text="Disinstalla", fg_color="transparent", text_color="#EF4444", anchor="w", command=lambda: [print("Disinstallato"), menu.destroy()]).pack(fill="x", padx=5, pady=2)
    ctk.CTkButton(menu, text="Aggiungi alla Dash", fg_color="transparent", text_color="white", anchor="w", command=lambda: [print("Aggiunto"), menu.destroy()]).pack(fill="x", padx=5, pady=2)
    
    menu.bind("<FocusOut>", lambda e: menu.destroy())
    menu.focus()

icone_nomi = ["📁", "🌐", "💬", "⚙️"]
for nome in icone_nomi:
    btn_app = ctk.CTkButton(
        salsicciotto_frame, 
        text=nome, 
        font=("Arial", 18),
        fg_color="#60A5FA",
        hover_color="#93C5FD",
        width=45, height=45,
        corner_radius=20
    )
    btn_app.pack(side="left", padx=8)
    btn_app.configure(command=lambda n=nome: apri_app(n))
    btn_app.bind("<Button-3>", lambda e, n=nome: mostra_menu_contestuale(e, n))

def esegui_comando_sistema(cmd):
    print(f"Esecuzione comando: {cmd}")
    if cmd == "Spegni":
        os.system("shutdown /s /t 1")
    elif cmd == "Riavvia":
        os.system("shutdown /r /t 1")
    elif cmd == "Blocca":
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif cmd == "Iberna":
        os.system("shutdown /h")

sist_frame = ctk.CTkFrame(salsicciotto_frame, fg_color="transparent")
sist_frame.pack(side="right", padx=15)

for simbolo, cmd in [("🔌", "Spegni"), ("🔄", "Riavvia"), ("🔒", "Blocca"), ("💤", "Iberna")]:
    btn_sys = ctk.CTkButton(
        sist_frame, text=simbolo, width=35, height=35, corner_radius=17,
        fg_color="#0F172A", hover_color="#334155",
        command=lambda c=cmd: esegui_comando_sistema(c)
    )
    btn_sys.pack(side="left", padx=3)

app.mainloop()
