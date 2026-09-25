from pynput import keyboard

pressed_keys = set()


def on_press(key):
    if key not in pressed_keys:
        pressed_keys.add(key)
        print(f"Pressed: {key}")


def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)
        print(f"Released: {key}")

    if key == keyboard.Key.esc:
        print("Stopping...")
        return False


with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()