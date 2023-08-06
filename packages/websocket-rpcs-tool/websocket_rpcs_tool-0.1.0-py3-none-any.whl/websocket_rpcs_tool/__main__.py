from __future__ import annotations
import re
import os
import ast
import wget
import json
import shutil
import pathlib
import zipfile
import requests
import tempfile
import textwrap
import argparse
import functools
import subprocess

from . import __config__

def run(command: str, cwd=None):
    command = textwrap.dedent(command).removeprefix("\n")
    for line in command.splitlines():
        subprocess.run(line, shell=True, cwd=cwd)

@functools.total_ordering
class Version:
    def __init__(self, ss: str) -> None:
        self.versions = list(map(lambda s:int(s), ss.split(".")))
    def __eq__(self, other: Version | str):
        if isinstance(other, str):
            other = Version(other)
        return self.versions == other.versions
    def __gt__(self, other: Version | str):
        if isinstance(other, str):
            other = Version(other)
        for i in range(min(len(self.versions), len(other.versions))):
            if self.versions[i] > other.versions[i]:
                return True
        return len(self.versions) > len(other.versions)
    def __repr__(self) -> str:
        return ".".join(map(lambda i:str(i), self.versions))

def get_all_version():
    l = []
    pattern = re.compile("^protoc-(.*)-")
    for file_name in os.listdir(__config__._appdir):
        m = re.match(pattern, file_name)
        if m is not None:
            l.append([Version(m.group(1)), file_name])
    return l

def ignore_rc_version(releases):
    def is_release(release):
        try:
            Version(release["tag_name"][1:])
            return True
        except:
            return False
    return list(filter(is_release, releases))

def asset_have_win64(asset):
    return re.match(".*win64.zip", asset["browser_download_url"])

def release_have_win64(release):
    for asset in release["assets"]:
        if asset_have_win64(asset):
            return True
    return False

def get_latest_release():
    res = requests.get(__config__.repo_releases).text
    releases = json.loads(res)
    return ignore_rc_version(releases)[0]

def get_release_version(release):
    return Version(release["tag_name"][1:])

def _download_protoc(release):
    assets = list(filter(asset_have_win64, release["assets"]))
    if assets.__len__() > 0:
        url = assets[0]["browser_download_url"]
        filename = os.path.basename(url)
        if __config__.ghproxy_proxy:
            url = "{}/{}".format(__config__.ghproxy_url, url)
        temp_dir = tempfile.TemporaryDirectory()
        zip_path = wget.download(url, os.path.join(temp_dir.name, filename))
        extract_path = os.path.join(__config__._appdir, pathlib.Path(filename).stem)
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)
        with zipfile.ZipFile(zip_path, "r") as zip:
            zip.extractall(extract_path)
        temp_dir.cleanup()
        return [None, os.path.join(extract_path), "bin", "protoc.exe"]

def get_win64_download_url(release):
    assets = list(filter(asset_have_win64, release["assets"]))
    if assets.__len__() > 0:
        return assets[0]["browser_download_url"]

def download_protoc(min_version=None, max_version=None):
    res = requests.get(__config__.repo_releases).text
    releases = json.loads(res)
    releases = ignore_rc_version(releases)
    if min_version is not None:
        releases = list(filter(lambda release: get_release_version(release) >= min_version, releases))
    if max_version is not None:
        releases = list(filter(lambda release: get_release_version(release) <= max_version, releases))
    releases = list(filter(release_have_win64, releases))
    if releases.__len__() > 0:
        assets = list(filter(asset_have_win64, releases[0]["assets"]))
        if assets.__len__() > 0:
            url = assets[0]["browser_download_url"]
            filename = os.path.basename(url)
            if __config__.ghproxy_proxy:
                url = "{}/{}".format(__config__.ghproxy_url, url)
            temp_dir = tempfile.TemporaryDirectory()
            zip_path = wget.download(url, os.path.join(temp_dir.name, filename))
            extract_path = os.path.join(__config__._appdir, pathlib.Path(filename).stem)
            if not os.path.exists(extract_path):
                os.makedirs(extract_path)
            with zipfile.ZipFile(zip_path, "r") as zip:
                zip.extractall(extract_path)
            temp_dir.cleanup()
            return [None, os.path.join(extract_path), "bin", "protoc.exe"]

def get_protoc_path(min_version=None, max_version=None, latest=False):
    if __config__.use_built_in_protoc:
        versions = get_all_version()
        if latest:
            release = get_latest_release()
            url = get_win64_download_url(release)
            version = [get_release_version(release), pathlib.Path(url).stem]
            if version not in versions:
                _download_protoc(release)
            return os.path.join(__config__._appdir, version[1], "bin", "protoc.exe")
        versions.sort(key=lambda l: l[0], reverse=True)
        if min_version is not None:
            versions = list(filter(lambda l: l[0] >= min_version, versions))
        if max_version is not None:
            versions = list(filter(lambda l: l[0] <= max_version, versions))
        if versions.__len__() == 0:
            r = download_protoc(min_version, max_version)
            if r is not None:
                versions.append(r)
        return os.path.join(__config__._appdir, versions[0][1], "bin", "protoc.exe")
    return "protocdddd"

class LanguageHandler:
    def python(self, args: argparse.Namespace):
        run(f"{get_protoc_path()} --python_out=. --pyi_out=. {args.proto}")
    def js(self, args: argparse.Namespace):
        get_protoc_path(max_version="3.19.6")
        proto = args.proto
        proto_name = pathlib.Path(proto).stem
        temp_dir = tempfile.TemporaryDirectory()
        shutil.copy(f"./{proto}", temp_dir.name)
        run("""
            npm install google-protobuf
            npm install browserify -g
            {protoc_path} --js_out=import_style=commonjs,binary:. {proto}
            browserify {proto_name}_pb.js -o {proto_name}_pb_browserify.js
        """.format(proto=proto, protoc_path=get_protoc_path(max_version="3.19.6"), proto_name=proto_name), cwd=temp_dir.name)
        shutil.copy(os.path.join(temp_dir.name, f"{proto_name}_pb_browserify.js"), f"./{proto_name}_pb_browserify.js")
        temp_dir.cleanup()
    def cpp(self, args: argparse.Namespace):
        run(f"{get_protoc_path(latest=True)} --cpp_out=. {args.proto}")
    def _all_handlers(self):
        return {k:getattr(self, k) for k in dir(self) if not k.startswith("_")}

def show_config_handler(args: argparse.Namespace):
    print(__config__._all_config())

def set_config_handler(args: argparse.Namespace):
    key, value = args.key, args.value
    if __config__._all_config().get(key) is not None:
        setattr(__config__, key, ast.literal_eval(value))
    __config__._save_config()

def __main__():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="handler", required=True)
    for name, handler in LanguageHandler()._all_handlers().items():
        sub_parser = subparsers.add_parser(name)
        sub_parser.set_defaults(func=handler)
        sub_parser.add_argument("proto")
    config_parser = subparsers.add_parser("config")
    config_subparsers = config_parser.add_subparsers(required=True)
    show_parser = config_subparsers.add_parser("show")
    show_parser.set_defaults(func=show_config_handler)
    set_parser = config_subparsers.add_parser("set")
    set_parser.add_argument("key")
    set_parser.add_argument("value")
    set_parser.set_defaults(func=set_config_handler)
    args = parser.parse_args()
    args.func(args)
    
if __name__ == "__main__":
    __main__()