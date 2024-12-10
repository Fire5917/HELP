import pyautogui
import time

def main():
    repetitions = 1000
    delay_between_repeats = 0.1  # Délai en secondes
    delay_between_chars = 0.05   # Délai entre chaque caractère

    # Définir la commande complète avec /factorize
    commande = "/factorize sqrt((sin(x)*cos(x))/x)/cos(x))"

    print("Le script va démarrer dans 5 secondes. Veuillez placer le curseur dans la fenêtre cible.")
    time.sleep(5)  # Temps pour permettre à l'utilisateur de placer le curseur

    for i in range(repetitions):
        pyautogui.write(commande, interval=delay_between_chars)
        pyautogui.press('enter')
        time.sleep(delay_between_repeats)

    print(f"{repetitions} commandes ont été envoyées.")

if __name__ == "__main__":
    main()
