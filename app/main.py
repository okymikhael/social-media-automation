import os
import importlib

def list_apps():
    bin_folder = os.path.join(os.path.dirname(__file__), 'bin')
    apps = [f for f in os.listdir(bin_folder) if f.endswith('.py') and f != '__init__.py']
    return apps

def format_app_name(app_name):
    formatted_name = app_name.replace('_', ' ').capitalize()
    return formatted_name

def run_selected_app(app_name):
    module_name = f'bin.{app_name[:-3]}'  # Remove '.py' from the filename
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, 'main'):
            module.main()
        else:
            print(f"The selected app '{app_name}' doesn't have a 'main' function.")
    except ImportError as e:
        print(f"Error importing the selected app: {e}")
    except Exception as e:
        print(f"An error occurred while running the app: {e}")

def main():
    apps = list_apps()
    
    if not apps:
        print("No apps found in the 'bin' folder.")
        return

    print("Available apps:")
    for i, app in enumerate(apps, 1):
        tech_emojis = ["💻", "🖥️", "⌨️", "🖱️", "🔌", "🔋", "📱", "🖨️", "🎧", "🕹️", "🛰️", "📡"]
        random_emoji = __import__('random').choice(tech_emojis)
        formatted_app = format_app_name(app.replace(".py", ""))
        print(f"{i}. {formatted_app} {random_emoji}")

    while True:
        try:
            choice = int(input("Enter the number of the app you want to run: "))
            if 1 <= choice <= len(apps):
                selected_app = apps[choice - 1]
                print(f"Running {selected_app}...")
                run_selected_app(selected_app)
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()