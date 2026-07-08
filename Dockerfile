FROM vllm/vllm-openai:v0.22.1

RUN apt-get update && apt-get install -y python3.10-dev

WORKDIR /app

# 1. cài Python packages trước để tận dụng cache
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# 2. copy code
COPY . .

# 3. tải model NGAY LÚC BUILD — bake vào image
RUN uv run python -m VLLM.dowloads_models

ENTRYPOINT []
CMD ["uv", "run", "python", "-m", "VLLM.main"]
