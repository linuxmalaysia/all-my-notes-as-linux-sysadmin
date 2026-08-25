# /// script
# requires-python = ">=3.12"
# ///
"""Pengurus Pelayan dan Pembinaan MkDocs Material.

Modul ini menyiapkan pautan pementasan direktori mkdocs_src dan menguruskan
pelaksanaan MkDocs Material untuk pembangunan dan pembinaan tapak web statik.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def create_junction(src: Path, dest: Path):
    """Cipta pautan persimpangan direktori (junction) bagi Windows atau pautan simbolik (symlink) bagi POSIX.

    Args:
        src (Path): Direktori sumber sasaran.
        dest (Path): Laluan pautan destinasi.
    """
    if dest.exists() or dest.is_symlink():
        if dest.is_symlink() or dest.is_file():
            dest.unlink()
        elif dest.is_dir():
            try:
                os.rmdir(dest) # os.rmdir works for junctions
            except OSError:
                shutil.rmtree(dest)
    
    if sys.platform.startswith('win'):
        subprocess.run(["cmd", "/c", "mklink", "/J", str(dest), str(src)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        os.symlink(src.resolve(), dest)

def create_hardlink(src: Path, dest: Path):
    """Cipta pautan keras (hardlink) fail atau pautan simbolik sandaran merentas pelantar.

    Args:
        src (Path): Fail sumber sasaran.
        dest (Path): Laluan pautan destinasi.
    """
    if dest.exists() or dest.is_symlink():
        dest.unlink()
    if sys.platform.startswith('win'):
        subprocess.run(["cmd", "/c", "mklink", "/H", str(dest), str(src)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        try:
            os.link(src, dest)
        except OSError:
            os.symlink(src.resolve(), dest)

def prepare_docs_dir(root_dir: Path, build_dir: Path):
    """Sediakan direktori persinggahan mkdocs_src dengan memautkan folder dokumentasi.

    Args:
        root_dir (Path): Direktori punca repositori.
        build_dir (Path): Direktori persinggahan destinasi untuk MkDocs.
    """
    if not build_dir.exists():
        build_dir.mkdir(parents=True)
        
    # Directories to junction
    dirs_to_link = ['docs', 'openwiki', 'manual', '.agents', 'assets']
    for d in dirs_to_link:
        src = root_dir / d
        dest = build_dir / d
        if src.exists():
            create_junction(src, dest)
            
    # Files to hardlink
    files_to_link = [
        'README.md',
        'START-HERE.md',
        'AGENTS.md',
        'HISTORY.md',
        'CHANGELOG.md',
        'LEGAL-NOTICE.md',
        'NOTICE.md',
        'llms.txt',
        'llms-full.txt',
        'llms_context.xml',
    ]
    for f in files_to_link:
        src = root_dir / f
        dest = build_dir / f
        if src.exists():
            create_hardlink(src, dest)

def main():
    """Laksanakan fungsi utama untuk menguruskan perkhidmatan atau pembinaan MkDocs Material."""
    root_dir = Path.cwd()
    build_dir = root_dir / 'mkdocs_src'
    
    args = sys.argv[1:]
    command = "serve"
    
    if "--build-only" in args:
        command = "build"
        args.remove("--build-only")
        if "--clean" not in args:
            args.append("--clean")
        
    print("?? Menyiapkan symlinks untuk DSOM (docs_dir: mkdocs_src)...")
    prepare_docs_dir(root_dir, build_dir)
    
    print(f"?? Memulakan MkDocs Material (Mod: {command.upper()})")
    
    cmd = [
        "uvx", 
        "--with", "mkdocs-material",
        "mkdocs", 
        command,
        "-f", "mkdocs.yml"
    ] + args
    
    try:
        result = subprocess.run(cmd, cwd=root_dir, check=False)
        if result.returncode != 0:
            print(f"\n? Ralat: MkDocs terhenti dengan kod {result.returncode}")
            sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\n?? Pelayan MkDocs dihentikan oleh pengguna.")
        sys.exit(0)

if __name__ == '__main__':
    main()
