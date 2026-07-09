FROM vllm/vllm-openai:v0.24.0

RUN curl -LsSf https://astral.sh/uv/install.sh | UV_INSTALL_DIR=/usr/local/bin sh
RUN apt-get update && apt-get install -y python3.10-dev


WORKDIR /app


# 1. cài Python packages trước để tận dụng cache
COPY pyproject.toml uv.lock ./
RUN uv sync

# 2. copy code
COPY . .

# 3. tải model NGAY LÚC BUILD — bake vào image
# 3. tải model NGAY LÚC BUILD — bake vào image
RUN uv run python -m VLLM.downloads_models

ENTRYPOINT []
CMD ["uv", "run", "python", "-m", "VLLM.main"]
