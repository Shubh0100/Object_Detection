import subprocess

def run_script(option):
    scripts = {
        "1": "YoloWebCam.py",
        "2": "CarCount.py",
        "3": "YoloForVideos.py",
        "4": "YoloImages.py"
    }

    script_to_run = scripts.get(option)
    if script_to_run:
        print(f"Running {script_to_run}...\n")
        subprocess.run(["python", script_to_run])
    else:
        print("Invalid option selected.")

def main():
    while True:
        print("\nChoose a program to run:")
        print("1. YoloWebCam.py")
        print("2. CarCount.py")
        print("3. YoloForVideos.py")
        print("4. YoloImages.py")
        print("q. Quit")

        choice = input("Enter your choice: ").strip().lower()
        if choice == 'q':
            print("Exiting...")
            break
        run_script(choice)

if __name__ == "__main__":
    main()
