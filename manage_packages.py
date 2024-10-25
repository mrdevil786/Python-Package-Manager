import subprocess
import sys

BASIC_PACKAGES = ['pip', 'setuptools', 'wheel']

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def install_package(package_name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])

def ensure_basic_packages_installed():
    for package in BASIC_PACKAGES:
        try:
            __import__(package)
        except ImportError:
            print(f"{RED}{package} not found. Installing...{RESET}")
            install_package(package)

def list_installed_packages():
    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'list']).decode('utf-8')
    packages = installed_packages.strip().split('\n')[2:]
    return [pkg for pkg in packages if pkg.split()[0] not in BASIC_PACKAGES]

def uninstall_package(package_name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', package_name, '-y'])

def main():
    ensure_basic_packages_installed()

    while True:
        print("Installed Packages:")
        packages = list_installed_packages()

        if not packages:
            print(f"{RED}No packages found.{RESET}")
        else:
            for i, package in enumerate(packages, 1):
                print(f"{GREEN}{i}. {package}{RESET}")

        print("\nOptions:")
        print("1. Uninstall a package")
        print("2. Uninstall all packages")
        print("3. Refresh package list")
        print("0. Exit")
        
        choice = input("Select an option (0-3): ")

        if choice == '1':
            package_index = int(input(f"Enter the package number to uninstall (1-{len(packages) if packages else 0}): ")) - 1
            if 0 <= package_index < len(packages):
                package_name = packages[package_index].split()[0]
                uninstall_package(package_name)
                print(f"{GREEN}Uninstalled {package_name}.{RESET}")
            else:
                print(f"{RED}Invalid package number.{RESET}")
        
        elif choice == '2':
            for package in packages:
                package_name = package.split()[0]
                uninstall_package(package_name)
            print(f"{GREEN}Uninstalled all packages.{RESET}")
        
        elif choice == '3':
            print(f"{GREEN}Refreshing package list...{RESET}")
            continue
        
        elif choice == '0':
            print("Exiting.")
            break
        
        else:
            print(f"{RED}Invalid choice.{RESET}")

if __name__ == "__main__":
    main()
