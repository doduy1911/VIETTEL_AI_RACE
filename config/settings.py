
from pydantic_settings import BaseSettings , SettingsConfigDict
import os 
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
class Settings(BaseSettings):
        hf_repo_id: str
        local_dir: str
        token_hf:str
        host: str = "0.0.0.0"
        port: int = 8000
        gpu_memory_utilization: float = 0.85
        max_model_len: int | None = None          # để trống = dùng giá trị mặc định của model
        tensor_parallel_size: int = 1
        enable_prefix_caching: bool = True
        enable_chunked_prefill: bool = False
        kv_cache_dtype: str | None = None         # vd: "fp8", để trống = dùng mặc định (auto)
        quantization: str | None = None           # vd: "fp8", để trống = không quantize weight
        max_num_seqs: int | None = None           # để trống = dùng giá trị mặc định của vLLM
        extra_flags: str = ""                     # flag vLLM tuỳ ý khác, cách nhau bởi dấu cách. Vd: "--disable-log-reques
       
        model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),  
        env_file_encoding='utf-8',
        extra="ignore"
    )


settings = Settings()