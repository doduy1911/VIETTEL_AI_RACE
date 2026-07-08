FROM vllm/vllm-openai:v0.22.1
RUN apt-get update && apt-get install -y python3.10-dev
WORKDIR /app
COPY . .
CMD ["uv", "run", "VLLM"]