# 1. Chọn image Python chính thức
FROM python:3.10-slim

# 2. Thiết lập thư mục làm việc bên trong container
WORKDIR /app

# 3. Copy toàn bộ project vào container
COPY . .

# 4. Cài đặt các dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Mở port 5000 (port mặc định của Flask)
EXPOSE 5000

# 6. Chạy app
CMD ["python", "app.py"]
