import subprocess

def check_containers():
    result = subprocess.run(
        ["docker", "ps"],
        stdout=subprocess.PIPE,
        text=True
    )

    if result.stdout:
        print("🚀 Running Containers:")
        print(result.stdout)
    else:
        print("❌ No running containers found")

if __name__ == "__main__":
    check_containers()
