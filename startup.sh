#!/bin/bash

# 如果 output.tar.gz 還沒解壓，就解壓它
if [ -f output.tar.gz ]; then
    echo "Extracting output.tar.gz..."
    tar -xzf output.tar.gz -C .
fi

# 啟動 FastAPI (或 Flask) App
exec uvicorn main:app --host=0.0.0.0 --port=8000