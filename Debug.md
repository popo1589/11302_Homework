### 1. 清除舊檔與舊容器
rm -f generated_flag.pcap
docker ps -a | grep forensics_ctf | awk '{print $1}' | xargs -r docker rm -f

### 建置 Docker 映像
docker build -t forensics_image .

### 2. 再次執行容器（加上必要權限）
docker run --rm \
  --cap-add=NET_ADMIN \
  --cap-add=NET_RAW \
  -v "$(pwd)":/app:rw \
  forensics_image


### 確認輸出
ls -l flag.txt generated_flag.pcap
