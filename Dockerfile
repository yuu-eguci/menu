FROM python:3.15-slim

# 画面表示に必要な Tk と、日本語を表示するためのフォントだけを追加します。
RUN apt-get update \
    && apt-get install -y --no-install-recommends fonts-ipafont-gothic libtk8.6 \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    XDG_CACHE_HOME=/tmp/.cache

WORKDIR /app
COPY menu.py menu.csv test_menu.py ./

USER nobody
CMD ["python", "menu.py"]
