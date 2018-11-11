import subprocess
import os
import time
import shutil

# Run deploy in a "check" folder to see if deploy_manifest.txt has changed

REFERENCE = "blinkapp/0.1@danimtb/stable"
REMOTE = "artifactory_local"
APP_PATH = "bin/blinkapp"


def run_check_directory():
    remove_directory("check")
    os.mkdir("check")
    os.chdir("check")
    try:
        os.system("conan remove %s -f" % REFERENCE)
    except Exception:
        pass
    time.sleep(1)
    os.system("conan install %s -r %s" % (REFERENCE, REMOTE))
    os.chdir("..")


def remove_directory(dir_name):
    try:
        shutil.rmtree(dir_name)
    except Exception:
        pass


def init_launch_app():
    shutil.copytree("check", "execute")
    # os.chmod("execute/%s" % APP_PATH, 777)
    exe_path = os.path.abspath(os.path.join(os.path.curdir, "execute", "bin", "blinkapp"))
    return subprocess.Popen(exe_path)


def read_deploy_content(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()[1]


if __name__ == "__main__":
    run_check_directory()
    while True:
        remove_directory("execute")
        app_process = init_launch_app()
        time.sleep(5)
        deploy_content = read_deploy_content("execute/deploy_manifest.txt")
        print("[DEPLOY CONTENT]", deploy_content)
        check = True

        while check:
            run_check_directory()
            new_deploy_content = read_deploy_content("check/deploy_manifest.txt")
            print("[NEW DEPLOY CONTENT]", new_deploy_content, "\nChanged:", new_deploy_content != deploy_content)

            if new_deploy_content != deploy_content:
                print("TERMINATE")
                app_process.terminate()
                check = False
