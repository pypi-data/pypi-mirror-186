import click
import datetime
import hashlib
import os
import re as regex
import requests
import sys
import zlib
from dateutil.parser import parse
from io import StringIO
from pathlib import Path, WindowsPath
from tqdm import tqdm
from typing import Dict, Tuple, Union
from urllib.parse import urlparse


def crc32_str(string: str) -> str:
    return zlib.crc32(bytes(string, "utf-8"))


def md5_str(string: str) -> str:
    return hashlib.md5(bytes(string, "utf-8")).hexdigest()


def get_filename(url: str) -> str:
    name = urlparse(url).path
    if regex.search("/", name):
        name = regex.split("/", name, flags=regex.I)[-1]
        name = regex.search("(.*\.[\w\d]{1,7})", name, regex.I).group()
    return name


def append_filename(target: WindowsPath) -> WindowsPath:
    cp_count = 1
    while target.exists():
        if cp_count == 1:
            name, ext = target.name.split(".")
            target = Path(f"{target.parent}/{name}-1.{ext}")
        else:
            target = Path(
                regex.sub("(-\d{,3})?(\..*?)$", f"-{cp_count}\\2", str(target), regex.I)
            )
        cp_count += 1
    return target


def hash_filename(link: str, fn: str) -> Tuple[str]:
    crc = crc32_str(link)
    md5 = md5_str(link)
    nm, ext = regex.search("(.*?)(\.[\d\w]{1,7}$)", fn).groups()
    crc_out = f"{nm}_{crc}{ext}"
    md5_out = f"{nm}_{md5}{ext}"
    return crc_out, md5_out


def pywget(
    url: str,
    path: str = "./",
    filename: str = None,
    timestamping: bool = False,
    noclobber: bool = False,
    cont: bool = False,
    overwrite: bool = False,
    quiet: bool = False,
    crc_name: bool = False,
    md5_name: bool = False,
    force_filename: bool = False,
    spder: bool = False,
    stdout=sys.stdout,
    hide_ignore: bool = False,
    session: requests.Session = requests.Session(),
) -> None:
    """
    :param url:
    URL to download.
    :param path:
    Folder to download files to, can be relative or absolute. Accepts pathlib objects.
    :param filename:
    Optional: set file instead of getting it from url
    :param timestamping:
    Don't download if already saved file is newer than url.
    :param noclobber:
    Don't download already saved files, no overwrite.
    :param cont:
    Continue downloads.
    :param overwrite:
    Overwrite original file
    :param rename:
    Rename new downloads instead of overwrite
    :param quiet:
    Hide all download progress
    :param crc_name:
    Append crc32 value of link to filename
    :param md5_name:
    Append md5 value of link to filename
    :param force_filename:
    Don't try and get filename, only use the one provided
    :param spder:
    Print the file name and info for the url. Does not download.
    :param stdout:
    Provide a custom file to output print statements to.
    :param hide_ignore:
    If true, hide the print statements for noclobber and timestamping conflicts. Will be overriden by the quiet parameter.
    :return:
    """

    if spder:
        return spider(url)

    blank = StringIO()  # open("nul", "w")
    fl_out = stdout if not quiet else blank
    ignore_messages = stdout if not any([quiet, hide_ignore]) else blank
    if force_filename or filename:
        fn = filename
    else:
        fn = get_filename(url)

    if not path:
        path = "./"

    crc_fn, md5_fn = hash_filename(url, fn)
    if crc_name:
        fn = crc_fn
    elif md5_name:
        fn = md5_fn

    output = Path(path, fn)
    headers = {}
    # headers[
    #     "user-agent"
    # ] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    writemode = "wb"
    tz = datetime.datetime.now().astimezone().tzinfo

    if output.exists():
        if cont:
            headers["Range"] = f"bytes={output.stat().st_size}-"
            writemode = "ab"
        elif timestamping:
            file_stat = os.stat(output)
            resp = session.get(url, stream=True, allow_redirects=True)
            if "last-modified" in resp.headers.keys():
                modtime = parse(resp.headers["last-modified"]).astimezone(tz=tz)
            else:
                modtime = datetime.datetime.now()
            if file_stat.st_mtime >= modtime.timestamp():
                print(
                    f'"{fn}" exists, ignoring because of timestamping (-n).',
                    file=ignore_messages,
                )
                return
        elif noclobber:
            print(
                f'"{fn}" exists, ignoring because of noclobber (-nc).',
                file=ignore_messages,
            )
            return
        elif overwrite:
            pass
        else:
            output = append_filename(output)

    os.makedirs(output.parent, exist_ok=True)
    if "resp" not in locals():
        resp = session.get(url, stream=True, allow_redirects=True, headers=headers)

    if (status_code := resp.status_code) in range(400, 600):
        raise requests.exceptions.HTTPError(
            f"Error code {status_code} on url, stopping."
        )

    if "modtime" not in locals():
        if "last-modified" in resp.headers.keys():
            modtime = parse(resp.headers["last-modified"]).astimezone(tz=tz)
        else:
            modtime = datetime.datetime.now()

    if "content-length" in resp.headers.keys():
        content_length = int(resp.headers["content-length"])
    else:
        content_length = None

    try:
        with open(output, writemode) as f:
            with tqdm(
                total=content_length,
                unit="B",
                unit_scale=True,
                desc=output.name[:75],
                initial=0,
                ascii=True,
                disable=quiet,
                file=fl_out,
            ) as pbar:
                for chunk in resp.iter_content(chunk_size=1024):
                    f.write(chunk)
                    pbar.update(len(chunk))
        file_stat = os.stat(output)
        os.utime(output, (file_stat.st_atime, modtime.timestamp()))
    except (ConnectionResetError, requests.exceptions.ChunkedEncodingError):
        raise Exception("Connection reset, stopping.")


@click.command()
@click.argument("url", nargs=-1)
@click.option("-p", "--prefix", "path", type=str)
@click.option("-o", "--output", "filename", type=str)
@click.option("-n", "--timestamping", "timestamping", is_flag=True)
@click.option("-nc", "--noclobber", "noclobber", is_flag=True)
@click.option("-c", "--cont", "cont", is_flag=True)
@click.option("-ov", "--overwrite", "overwrite", is_flag=True)
@click.option("-q", "--quiet", "quiet", is_flag=True)
@click.option("-crc", "crc_name", is_flag=True)
@click.option("-md5", "md5_name", is_flag=True)
@click.option("-ff", "--force-filename", "force_filename", is_flag=True)
@click.option("-s", "--spider", "spder", is_flag=True)
@click.option("--hide_ignore", "hide_ignore", is_flag=True)
def cli_pywget(
    url: tuple,
    path: str = "./",
    filename: str = None,
    timestamping: bool = False,
    noclobber: bool = False,
    cont: bool = False,
    overwrite: bool = False,
    quiet: bool = False,
    crc_name: bool = False,
    md5_name: bool = False,
    force_filename: bool = False,
    spder: bool = False,
    hide_ignore: bool = False,
) -> None:
    """
    :param url:
    URL(s) to download.
    :param path:
    Folder to download files to, can be relative or absolute. Accepts pathlib objects.
    :param filename:
    Optional: set file instead of getting it from url
    :param timestamping:
    Don't download if already saved file is newer than url.
    :param noclobber:
    Don't download already saved files, no overwrite.
    :param cont:
    Continue downloads.
    :param overwrite:
    Overwrite original file
    :param rename:
    Rename new downloads instead of overwrite
    :param quiet:
    Hide all download progress
    :param crc_name:
    Append crc32 value of link to filename
    :param md5_name:
    Append md5 value of link to filename
    :param force_filename:
    Don't try and get filename, only use the one provided
    :param spder:
    Print the file name and info for the url. Does not download.
    :param hide_ignore:
    If true, hide the print statements for noclobber and timestamping conflicts. Will be overriden by the quiet parameter.
    :return:
    """

    if spder:
        if len(url) == 1:
            return spider(url[0])
        else:
            for l in url:
                spider(l)
    else:
        for l in url:
            pywget(
                l,
                path=path,
                filename=filename,
                timestamping=timestamping,
                noclobber=noclobber,
                cont=cont,
                overwrite=overwrite,
                quiet=quiet,
                crc_name=crc_name,
                md5_name=md5_name,
                force_filename=force_filename,
                hide_ignore=hide_ignore,
            )


def spider(url: str) -> Dict[str, Union[str, int, requests.Response]]:
    """
    :param url:
    URL to get info on.

    Get the filename, size, and modified time of URL.
    """
    fn = get_filename(url)
    headers = {}
    headers[
        "user-agent"
    ] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    resp = requests.get(url, stream=True, allow_redirects=True, headers=headers)
    size = int(resp.headers["content-length"]) // 1024
    tz = datetime.datetime.now().astimezone().tzinfo
    modtime = parse(resp.headers["last-modified"]).astimezone(tz=tz)
    print(
        f"Filename: {fn}\nSize: {size}kB\nModified: {modtime:%Y-%m-%d %I:%M:%S %p %Z}\n"
    )
    return {"filename": fn, "size": size, "modtime": modtime, "resp": resp}


if __name__ == "__main__":
    cli_pywget()
    # Test
    # pywget(url="https://i.redd.it/jqgnqnq73oaa1.jpg", path=r"C:\Users\Crank\Downloads")
