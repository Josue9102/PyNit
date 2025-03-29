import subprocess
import sys

def install_dependency(package, from_github=False):
    """Installs a package using pip. Supports GitHub installations."""
    try:
        if from_github:
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"git+{package}"])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} installed successfully.")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}. Check your internet connection.")

def install_smafu_dev():
    """Installs dependencies for SMAFU_DEV."""
    dependencies = ["pillow", "flask", "opencv-python", "pydroid3"]
    github_dependencies = ["https://github.com/kramcat/CharacterAI"]

    print("🔹 Installing dependencies for SMAFU_DEV...")
    for package in dependencies:
        install_dependency(package)

    for package in github_dependencies:
        install_dependency(package, from_github=True)

if __name__ == "__main__":
    install_smafu_dev()
