# /// script
# requires-python = ">=3.12"
# ///
import sys
import os
import subprocess
import shutil
from pathlib import Path

def create_junction(src: Path, dest: Path):
    if dest.exists():
        if dest.is_symlink() or dest.is_dir():
            try:
                os.rmdir(dest) # os.rmdir works for junctions
            except OSError:
                shutil.rmtree(dest)
    
    # cmd /c mklink /J dest src
    subprocess.run(["cmd", "/c", "mklink", "/J", str(dest), str(src)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def create_hardlink(src: Path, dest: Path):
    if dest.exists():
        dest.unlink()
    # cmd /c mklink /H dest src
    subprocess.run(["cmd", "/c", "mklink", "/H", str(dest), str(src)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def prepare_docs_dir(root_dir: Path, build_dir: Path):
    if not build_dir.exists():
        build_dir.mkdir(parents=True)
        
    # Directories to junction
    dirs_to_link = ['docs', 'openwiki', 'palace', '.agents', 'assets']
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
    root_dir = Path.cwd()
    build_dir = root_dir / 'mkdocs_src'
    
    args = sys.argv[1:]
    command = "serve"
    
    if "--build-only" in args:
        command = "build"
        args.remove("--build-only")
        if "--clean" not in args:
            args.append("--clean")
        
    print(f"?? Menyiapkan symlinks untuk DSOM (docs_dir: mkdocs_src)...")
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
