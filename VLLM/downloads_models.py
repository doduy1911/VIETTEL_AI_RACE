from huggingface_hub import snapshot_download
from config.settings import settings
def download_models():
    print(f"Đang tải {settings.hf_repo_id} về {settings.local_dir} ...")
    snapshot_download(
        repo_id=settings.hf_repo_id,
        local_dir=settings.local_dir,
    )

    print("[DOWNLOAD] tải thành công models")


if __name__ == "__main__":
    download_models()