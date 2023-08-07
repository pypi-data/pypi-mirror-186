from pathlib import Path
from PIL import ImageOps, Image


def exif_transpose_pic(pic: str | Path) -> None:
    pic = Path(pic)
    image = Image.open(pic)
    image = ImageOps.exif_transpose(image)
    image.save(pic)


def exif_transpose_folder(folder: str | Path, recursive=False, verbose=False) -> None:
    folder = Path(folder)
    if verbose:
        print(f"Transposing pictures of folder \"{folder}\"")
    for entry in folder.iterdir():
        if entry.is_dir() and recursive:
            exif_transpose_folder(entry, recursive=True, verbose=verbose)
        else:
            try:
                if verbose:
                    print(f"Transposing file \"{entry}\"")
                exif_transpose_pic(entry)
            except Exception as e:
                if verbose:
                    print(e)


def exif_transpose_pics(pics: list[list[str | Path]] | list[str | Path], verbose=False) -> None:
    for item in pics:
        if isinstance(item, list):
            exif_transpose_pics(item, verbose=verbose)
        else:
            pic = Path(item)
            if verbose:
                print(f"Transposing file \"{pic}\"")
            exif_transpose_pic(pic)
