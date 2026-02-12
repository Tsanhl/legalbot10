"""
Download the pre-built ChromaDB index from Hugging Face.

Run this once after cloning the repo:
    python download_index.py
"""

import os
import subprocess
import sys

HF_REPO = "Agnes999/legalbot10"
LOCAL_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")


def main():
    if os.path.exists(LOCAL_DIR) and os.listdir(LOCAL_DIR):
        print(f"[INFO] chroma_db/ already exists at {LOCAL_DIR}")
        resp = input("Re-download and overwrite? (y/N): ").strip().lower()
        if resp != "y":
            print("Skipped.")
            return

    # Try huggingface_hub Python package first, fall back to CLI
    try:
        from huggingface_hub import snapshot_download

        print(f"[INFO] Downloading ChromaDB index from HF dataset: {HF_REPO} ...")
        snapshot_download(
            repo_id=HF_REPO,
            repo_type="dataset",
            local_dir=LOCAL_DIR,
            allow_patterns=["chroma_db/**"],
        )
        # snapshot_download puts files under local_dir/chroma_db — move them up
        nested = os.path.join(LOCAL_DIR, "chroma_db")
        if os.path.isdir(nested):
            import shutil
            for item in os.listdir(nested):
                src = os.path.join(nested, item)
                dst = os.path.join(LOCAL_DIR, item)
                if os.path.exists(dst):
                    if os.path.isdir(dst):
                        shutil.rmtree(dst)
                    else:
                        os.remove(dst)
                shutil.move(src, dst)
            shutil.rmtree(nested, ignore_errors=True)
        print("[OK] ChromaDB index downloaded successfully.")

    except ImportError:
        print("[INFO] huggingface_hub not found, trying CLI ...")
        try:
            subprocess.run(
                ["huggingface-cli", "download", HF_REPO, "--repo-type=dataset",
                 "--include", "chroma_db/*", "--local-dir", LOCAL_DIR],
                check=True,
            )
            nested = os.path.join(LOCAL_DIR, "chroma_db")
            if os.path.isdir(nested):
                import shutil
                for item in os.listdir(nested):
                    src = os.path.join(nested, item)
                    dst = os.path.join(LOCAL_DIR, item)
                    if os.path.exists(dst):
                        if os.path.isdir(dst):
                            shutil.rmtree(dst)
                        else:
                            os.remove(dst)
                    shutil.move(src, dst)
                shutil.rmtree(nested, ignore_errors=True)
            print("[OK] ChromaDB index downloaded successfully.")
        except FileNotFoundError:
            print("[ERROR] Neither huggingface_hub nor huggingface-cli found.")
            print("Install one of:")
            print("  pip install huggingface_hub")
            print("  brew install huggingface-cli")
            sys.exit(1)


if __name__ == "__main__":
    main()
