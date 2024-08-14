import os
import sys
import subprocess

def run_app_executable(app_path):
    if not os.path.isdir(app_path) or not app_path.endswith('.app'):
        print("The provided path is not a valid .app bundle.")
        return


    contents_path = os.path.join(app_path, 'Contents')
    if not os.path.isdir(contents_path):
        print("The 'Contents' directory does not exist inside the .app bundle.")
        return

    app_name = os.path.basename(app_path).replace('.app', '')

    executable_path = os.path.join(contents_path, app_name)
    
    if not os.path.isfile(executable_path):
        print("No executable file found with the name '{}' in the 'Contents' directory.".format(app_name))
        return

    print("Attempting to open '{}'".format(app_name))

    try:
        print("Opening '{}'".format(app_name))
        with open(os.devnull, 'wb') as devnull:
            subprocess.call([executable_path], stdout=devnull, stderr=devnull)
        print("Closed '{}'.".format(app_name))
    except OSError as e:
        print("Failed to Open '{}': {}".format(app_name, e))

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/YourApp.app")
        sys.exit(1)

    app_path = sys.argv[1]
    run_app_executable(app_path)

if __name__ == "__main__":
    main()
