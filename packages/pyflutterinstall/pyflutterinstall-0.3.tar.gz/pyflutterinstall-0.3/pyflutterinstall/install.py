"""
Contains the install functions for the various components
"""

# pylint: disable=missing-function-docstring,consider-using-with,disable=invalid-name,subprocess-run-check,line-too-long

import os
from pathlib import Path
import shutil
import subprocess
from download import download  # type: ignore

from pyflutterinstall.resources import (
    JAVA_SDK_URL,
    FLUTTER_GIT_DOWNLOAD,
    ANDROID_SDK_URL,
    CHROME_URL,
    CMDLINE_TOOLS,
    INSTALL_DIR,
    DOWNLOAD_DIR,
    ANDROID_SDK,
    FLUTTER_TARGET,
    JAVA_DIR,
)

from pyflutterinstall.util import (
    execute,
    make_title,
)

from pyflutterinstall.setenv import add_env_path, set_env_var


def install_java_sdk() -> None:
    make_title("Installing Java SDK")
    print(f"Install Java SDK from {JAVA_SDK_URL} to {INSTALL_DIR}")
    java_sdk_zip_file = Path(
        download(JAVA_SDK_URL, DOWNLOAD_DIR / os.path.basename(JAVA_SDK_URL))
    )
    print(f"Unpacking {java_sdk_zip_file} to {JAVA_DIR}")
    shutil.unpack_archive(java_sdk_zip_file, JAVA_DIR)
    base_java_dir = JAVA_DIR / os.listdir(JAVA_DIR)[0]
    print(base_java_dir)
    java_bin_dir = base_java_dir / "bin"
    print(java_bin_dir)
    add_env_path(java_bin_dir)
    set_env_var("JAVA_HOME", str(base_java_dir))
    print("Java SDK installed.\n")


def install_android_sdk() -> None:
    make_title("Installing Android SDK")
    print(
        f"Install Android commandline-tools SDK from {ANDROID_SDK_URL} to {INSTALL_DIR}"
    )
    # sdk\Android\tools\bin\sdkmanager.bat
    path = download(ANDROID_SDK_URL, DOWNLOAD_DIR / os.path.basename(ANDROID_SDK_URL))
    print(f"Unpacking {path} to {INSTALL_DIR}")
    shutil.unpack_archive(path, ANDROID_SDK / "cmdline-tools" / "tools")
    sdkmanager_path = (
        ANDROID_SDK
        / "cmdline-tools"
        / "tools"
        / "cmdline-tools"
        / "bin"
        / "sdkmanager.bat"
    )
    # add_system_path(sdkmanager_path.parent)
    if not os.path.exists(sdkmanager_path):
        raise FileNotFoundError(f"Could not find {sdkmanager_path}")
    print("About to install Android SDK tools")
    # install latest
    execute(
        f'{sdkmanager_path} --sdk_root="{ANDROID_SDK}" --install "platform-tools"',
        send_confirmation="y\n",
        ignore_errors=False,
    )
    set_env_var("ANDROID_SDK_ROOT", ANDROID_SDK)
    set_env_var("ANDROID_HOME", ANDROID_SDK)
    # update tools
    print(f"Updating Android SDK with {sdkmanager_path}")
    execute(
        f'{sdkmanager_path} --sdk_root="{ANDROID_SDK}" --update',
        send_confirmation="y\n",
        ignore_errors=False,
    )
    tools_to_install = [f'"{tool}"' for tool in CMDLINE_TOOLS]
    for tool in tools_to_install:
        execute(
            f'{sdkmanager_path} --sdk_root="{ANDROID_SDK}" --install {tool}',
            send_confirmation="y\n",
            ignore_errors=False,
        )
    execute(
        f'{sdkmanager_path} --licenses --sdk_root="{ANDROID_SDK}"',
        send_confirmation="y\ny\ny\ny\ny\ny\ny\nn\n",
        ignore_errors=False,
    )
    add_env_path(ANDROID_SDK / "cmdline-tools" / "latest" / "bin")


def install_flutter() -> None:
    make_title("Installing Flutter")
    if shutil.which("git") is None:
        error_msg = "'git' not found in path"
        error_msg += "\npath = \n"
        for path in os.environ["PATH"].split(os.path.pathsep):
            error_msg += f"  {path}\n"
        raise FileNotFoundError(error_msg)
    print(f"Install Flutter from {FLUTTER_GIT_DOWNLOAD} to {FLUTTER_TARGET}")
    if not FLUTTER_TARGET.exists():
        execute(f'{FLUTTER_GIT_DOWNLOAD} "{FLUTTER_TARGET}"', ignore_errors=False)
    else:
        print(f"Flutter already installed at {FLUTTER_TARGET}")
    if not os.path.exists(FLUTTER_TARGET):
        print(
            f"!!!!!!!!!!!!! FLUTTER FOLDER {FLUTTER_TARGET} DOES NOT EXIST EITHER DOES NOT EXIST !!!!!!!!!!!!!!!"
        )
        path = os.environ["PATH"]
        error_msg = f"Could not find {FLUTTER_TARGET} in path"
        error_msg += "\npath = \n"
        for path in path.split(os.pathsep):
            error_msg += f"  {path}\n"
        raise FileNotFoundError(error_msg)
    # Add flutter to path
    add_env_path(FLUTTER_TARGET / "bin")
    execute(
        f'flutter config --android-sdk "{ANDROID_SDK}" --no-analytics',
        send_confirmation="y\n",
        ignore_errors=False,
    )
    execute(
        "flutter doctor --android-licenses",
        send_confirmation="y\n",
        ignore_errors=False,
    )

    print("Flutter installed.\n")


def install_chrome() -> None:
    print("\n################# Installing Chrome #################")
    # Install chrome for windows
    try:
        stdout = subprocess.check_output(
            "flutter doctor",
            shell=True,
            text=True,
            encoding="utf-8",
            universal_newlines=True,
        )
        if "Cannot find Chrome" in stdout:
            print("Chrome not found, installing")
            print(f"Install Chrome from {CHROME_URL} to {INSTALL_DIR}")
            path = download(CHROME_URL, DOWNLOAD_DIR / os.path.basename(CHROME_URL))
            print(f"Downloaded chrome at {path}")
            # install it
            os.system(f'"{path}"')
    except subprocess.CalledProcessError as exc:
        print(
            f"Error while installing chrome:\n  status={exc.returncode},\n  output={exc.output}"
        )
