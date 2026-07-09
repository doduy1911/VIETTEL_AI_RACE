import os , sys ,subprocess
from config.settings import settings

def build_command() -> list[str]:
    cmd = [
        sys.executable, "-m", "vllm.entrypoints.openai.api_server",
        f"--model={settings.local_dir}",
        f"--served-model-name={settings.served_model_name}",
        f"--host={settings.host}",
        f"--port={settings.port}",
        f"--gpu-memory-utilization={settings.gpu_memory_utilization}",
        f"--tensor-parallel-size={settings.tensor_parallel_size}",
    ]

    if settings.enable_prefix_caching:
        cmd.append("--enable-prefix-caching")
    if settings.enable_chunked_prefill:
        cmd.append("--enable-chunked-prefill")
    if settings.max_model_len is not None:
        cmd.append(f"--max-model-len={settings.max_model_len}")
    if settings.kv_cache_dtype:
        cmd.append(f"--kv-cache-dtype={settings.kv_cache_dtype}")
    if settings.quantization:
        cmd.append(f"--quantization={settings.quantization}")
    if settings.max_num_seqs is not None:
        cmd.append(f"--max-num-seqs={settings.max_num_seqs}")
    if settings.extra_flags.strip():
        cmd.extend(settings.extra_flags.strip().split())

    return cmd

 
def main():
    if not os.path.isdir(settings.local_dir) or not os.listdir(settings.local_dir):
        print(f"Không tìm thấy model tại '{settings.local_dir}'. Chạy downloads_models.py trước.")
        sys.exit(1)

    cmd = build_command()
    print("Đang khởi động vLLM server với lệnh:")
    print(" ".join(cmd))
    print()

    subprocess.run(cmd)
    os.execvp(cmd[0], cmd)  


if __name__ == "__main__":
    main()
