from typing import Optional, Any, TypedDict
import subprocess
import argparse
import requests
import platform
import tempfile
import shutil
import sys
import os


try:
    from tomllib import load as toml_load
except ModuleNotFoundError:
    from tomli import load as toml_load


PYPROJECT_SECTION = "tool.pyproject-appimage"


PyprojectDict = TypedDict("PyprojectDict", {
    "script": str,
    "icon": str,
    "rename-icon": str,
    "desktop-entry": str,
    "rename-desktop-entry": str,
    "appstream": str,
    "rename-appstream": str,
    "python-version": str,
    "output": str
}, total=False)


def check_key(project_dir: str, pyproject: PyprojectDict, key: str, error_list: list[str], checks: list[str]) -> None:
    if key not in pyproject:
        if "required" in checks:
            error_list.append(f"\"{key}\" is required but not present")
        return

    if "string" in checks:
        if not isinstance(pyproject[key], str):
            error_list.append("\"{key}\" must be a string")
        elif pyproject[key].strip() == "":
            error_list.append(f"\"{key}\" must not be empty")
        elif "path" in checks and not os.path.isfile(os.path.join(project_dir, pyproject[key])):
            error_list.append("The path " + os.path.join(project_dir, pyproject[key]) + f" for \"{key}\" is not valid")


def check_pyproject(project_dir: str, pyproject: PyprojectDict) -> None:
    error_list: list[str] = []

    check_key(project_dir, pyproject, "script", error_list, ["required", "string"])
    check_key(project_dir, pyproject, "icon", error_list, ["string", "path"])
    check_key(project_dir, pyproject, "rename-icon", error_list, ["string"])
    check_key(project_dir, pyproject, "desktop-entry", error_list, ["string", "path"])
    check_key(project_dir, pyproject, "rename-desktop-entry", error_list, ["string"])
    check_key(project_dir, pyproject, "appstream", error_list, ["string", "path"])
    check_key(project_dir, pyproject, "rename-appstream", error_list, ["string"])
    check_key(project_dir, pyproject, "python-version", error_list, ["string"])
    check_key(project_dir, pyproject, "output", error_list, ["string"])
    check_key(project_dir, pyproject, "updateinformation", error_list, ["string"])
    check_key(project_dir, pyproject, "compression", error_list, ["string"])

    if len(error_list) > 0:
        print(f"There are errors in the {PYPROJECT_SECTION} section of your pyproject.toml:", file=sys.stderr)
        print("\n".join(error_list), file=sys.stderr)
        sys.exit(1)


def download_file(url: str, path: str) -> None:
    print(f"Donwload {url} as {path}")
    r = requests.get(url, stream=True)
    if r.status_code != 200:
        print(f"{url} returns {r.status_code}", file=sys.stderr)
        sys.exit(1)
    with open(path, "wb") as f:
        shutil.copyfileobj(r.raw, f)


def get_python_download_link(version: str) -> str:
    for i in requests.get("https://api.github.com/repos/niess/python-appimage/releases").json():
        if i["tag_name"] == f"python{version}":
            for asset in i["assets"]:
                if asset["name"].endswith("manylinux2014_x86_64.AppImage"):
                    return asset["browser_download_url"]
    return None


def get_image_magick_command(work_dir: str) -> str:
    if shutil.which("magick") is not None:
        return "magick"

    work_magick = os.path.join(work_dir, "magick")

    if os.path.isfile(work_magick):
        return work_magick

    download_file("https://download.imagemagick.org/ImageMagick/download/binaries/magick", work_magick)
    subprocess.run(["chmod", "+x", work_magick], check=True)
    return work_magick


def get_icon_size(work_dir: str, icon_path: str) -> tuple[int, int]:
    cmd = [get_image_magick_command(work_dir), "identify", "-format", '%w %h', icon_path]
    size = subprocess.run(cmd, check=True, capture_output=True).stdout.decode("utf-8")
    width, height = size.split(" ")
    return (int(width), int(height))


def build_appimage(project_dir: str, work_dir: str, pyproject: PyprojectDict, args: argparse.Namespace) -> None:
    if args.python_version is not None:
        python_version = args.python_version
    elif "python-version" in pyproject:
        python_version = pyproject["python-version"]
    else:
        python_version = platform.python_version_tuple()[0] + "." + platform.python_version_tuple()[1]

    download_link = get_python_download_link(python_version)

    if download_link is None:
        print(f"Python version {python_version} is not aviable. Use --list-available-versions to get all aviable versions.", file=sys.stderr)
        sys.exit(1)

    download_file(download_link, os.path.join(work_dir, "Python.AppImage"))

    if args.appimagekit_url:
        download_file(args.appimagekit_url, os.path.join(work_dir, "Appimagetool.AppImage"))
    else:
        download_file("https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage", os.path.join(work_dir, "Appimagetool.AppImage"))

    subprocess.run(["chmod", "+x", os.path.join(work_dir, "Python.AppImage")], check=True)
    subprocess.run(["chmod", "+x", os.path.join(work_dir, "Appimagetool.AppImage")], check=True)

    subprocess.run([os.path.join(work_dir, "Python.AppImage"), "--appimage-extract"], cwd=work_dir, check=True, stdout=subprocess.DEVNULL)

    app_root = os.path.join(work_dir, "squashfs-root")

    shutil.rmtree(os.path.join(work_dir, "squashfs-root", "usr", "share"))
    for i in os.listdir(app_root):
        full_path = os.path.join(app_root, i)
        if os.path.isfile(full_path) or os.path.islink(full_path):
            os.remove(full_path)

    subprocess.run([os.path.join(app_root, "usr", "bin", "pip"), "install", "--no-warn-script-location", project_dir], check=True)

    if not os.path.isfile(os.path.join(app_root, "usr", "bin", pyproject["script"])):
        print("The script " + pyproject["script"] + " as not found")
        sys.exit(1)

    os.symlink(os.path.join("usr", "bin", pyproject["script"]), os.path.join(app_root, "AppRun"))

    if "icon" in pyproject:
        if pyproject["icon"].endswith(".png"):
            shutil.copyfile(os.path.join(project_dir, pyproject["icon"]), os.path.join(app_root, os.path.basename(pyproject["icon"])))
        else:
            # If a Icon is not PNG, convert it
            subprocess.run([get_image_magick_command(work_dir), os.path.join(project_dir, pyproject["icon"]), "PNG:" + os.path.join(app_root, os.path.basename(pyproject["icon"]))], check=True)

        if "rename-icon" in pyproject:
            os.rename(os.path.join(app_root, os.path.basename(pyproject["icon"])), os.path.join(app_root, pyproject["rename-icon"]))
            icon_name = pyproject["rename-icon"]
        else:
            icon_name = os.path.basename(pyproject["icon"])

        os.symlink(icon_name, os.path.join(app_root, ".DirIcon"))

        if icon_name.endswith(".svg"):
            icon_dir = os.path.join(app_root, "usr", "share", "icons", "hicolor", "scalable", "apps")
        else:
            icon_size = get_icon_size(work_dir, os.path.join(app_root, icon_name))
            icon_dir = os.path.join(app_root, "usr", "share", "icons", "hicolor", f"{icon_size[0]}x{icon_size[1]}", "apps")

        if not os.path.isdir(icon_dir):
            os.makedirs(icon_dir)

        shutil.copyfile(os.path.join(app_root, icon_name), os.path.join(icon_dir, icon_name))
    else:
        shutil.copyfile(os.path.join(os.path.dirname(__file__), "default.png"), os.path.join(app_root, ".DirIcon"))

    if "desktop-entry" in pyproject:
        shutil.copyfile(os.path.join(project_dir, pyproject["desktop-entry"]), os.path.join(app_root, pyproject.get("rename-desktop-entry", os.path.basename(pyproject["desktop-entry"]))))
    else:
        shutil.copyfile(os.path.join(os.path.dirname(__file__), "default.desktop"), os.path.join(app_root, "App.desktop"))
        os.symlink(".DirIcon", os.path.join(app_root, "Icon.png"))

    if "appstream" in pyproject:
        appstream_path = os.path.join(app_root, "usr", "share", "metainfo")

        if not os.path.isdir(appstream_path):
            os.makedirs(appstream_path)

        shutil.copyfile(os.path.join(project_dir, pyproject["appstream"]), os.path.join(appstream_path, pyproject.get("rename-appstream", os.path.basename(pyproject["appstream"]))))

    if args.output is not None:
        output = args.output
    elif "output" in pyproject:
        output = pyproject["output"]
    else:
        output = "MyApp.AppImage"

    imagetool_cmd = [os.path.join(work_dir, "Appimagetool.AppImage")]

    if args.no_fuse:
        imagetool_cmd.append("--appimage-extract-and-run")

    if "updateinformation" in pyproject:
        imagetool_cmd.append("--updateinformation")
        imagetool_cmd.append(pyproject["updateinformation"])

    if "compression" in pyproject:
        imagetool_cmd.append("--comp")
        imagetool_cmd.append(pyproject["compression"])

    imagetool_cmd.append(app_root)
    imagetool_cmd.append(output)

    subprocess.run(imagetool_cmd, check=True)

    print()
    print(f"Saving AppImage as {os.path.abspath(output)}")


def list_available_versions() -> None:
    version_dict: dict[int, list[int]] = {}
    for i in requests.get("https://api.github.com/repos/niess/python-appimage/releases").json():
        version_split = i["tag_name"].removeprefix("python").split(".")

        if int(version_split[0]) not in version_dict:
            version_dict[int(version_split[0])] = []

        version_dict[int(version_split[0])].append(int(version_split[1]))

    for key in sorted(version_dict.keys()):
        for value in sorted(version_dict[key]):
            print(f"{key}.{value}")


def get_toml_section(data: dict[str, Any], name: str) -> Optional[dict[str, Any]]:
    current_data = data
    for i in name.split("."):
        if i not in current_data:
            return None

        current_data = current_data[i]

    return current_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", help="Sets the putput filename")
    parser.add_argument("--project-dir", help="Sets the project dir", default=os.getcwd())
    parser.add_argument("--python-version", help="Set a custom Python version")
    parser.add_argument("--appimagekit-url", help="Set a custom download URL for AppImageKit")
    parser.add_argument("--work-dir", help="Set a custom directory to work in. Existing Directories will be removed.")
    parser.add_argument("--list-available-versions", action="store_true", help="Print available Python versions and exit")
    parser.add_argument("--no-fuse", action="store_true", help="Use this, if FUSE is not available e.g. inside a Docker container")
    parser.add_argument("-v", "--version", action="store_true", help="Prints the version and exit")
    parser.prog = "pyproject-appimage"
    args = parser.parse_args()

    if args.version:
        with open(os.path.join(os.path.dirname(__file__), "version.txt"), "r", encoding="utf-8") as f:
            print("pyproject-appimage " + f.read().strip())
        sys.exit(0)

    if args.list_available_versions:
        list_available_versions()
        sys.exit(0)

    if not os.path.isfile(os.path.join(args.project_dir, "pyproject.toml")):
        print(os.path.join(args.project_dir, "pyproject.toml") + " does not exists", file=sys.stderr)
        sys.exit(1)

    with open(os.path.join(args.project_dir, "pyproject.toml"), "rb") as f:
        try:
            data = toml_load(f)
        except Exception as ex:
            if len(ex.args) == 1:
                print("Error while parsing " + os.path.join(args.project_dir, "pyproject.toml") + f": {ex.args[0]}", file=sys.stderr)
            else:
                print("Error while parsing " + os.path.join(args.project_dir, "pyproject.toml"), file=sys.stderr)
            sys.exit(1)

    pyproject = get_toml_section(data, PYPROJECT_SECTION)

    if pyproject is None:
        print(os.path.join(args.project_dir, "pyproject.toml") + " has no section " + PYPROJECT_SECTION, file=sys.stderr)
        sys.exit(1)

    check_pyproject(args.project_dir, pyproject)

    if args.work_dir is not None:
        try:
            shutil.rmtree(args.work_dir)
        except Exception:
            pass

        try:
            os.makedirs(args.work_dir)
        except Exception:
            pass

        try:
            build_appimage(args.project_dir, args.work_dir, pyproject, args)
        except subprocess.CalledProcessError as ex:
            print("Error while running " + str(ex.cmd), file=sys.stderr)
            sys.exit(1)
    else:
        with tempfile.TemporaryDirectory() as tmpdir:
            try:
                build_appimage(args.project_dir, tmpdir, pyproject, args)
            except subprocess.CalledProcessError as ex:
                print("Error while running " + str(ex.cmd), file=sys.stderr)
                sys.exit(1)


if __name__ == "__main__":
    main()
