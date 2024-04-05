# utils/loading.py

from colorama import Fore, Style
import time

def display_loading_indicator(label):
    for i in range(1, 4):
        print(f"{label}: {'.' * i}", end="\r")
        time.sleep(0.3)
    print(f"{label}: {'.' * 3}", end="\r")

def display_progress_bar(label, progress, total, length=20):
    filled_length = int(length * progress / total)
    bar = '█' * filled_length + '░' * (length - filled_length)
    percentage = int(100 * progress / total)
    print(f"{label}: [{bar}] {percentage}%", end="\r")
    if progress == total:
        print(f"{label}: [{'█' * length}] 100%", end="\r")
        time.sleep(0.5)  # Slight delay to ensure the progress bar is fully loaded
        print(f"{Fore.GREEN}{label}: [{'█' * length}] 100% COMPLETE{Style.RESET_ALL}")
        print()