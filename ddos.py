import threading
import socket

hostname = "phenikaa.com"
target = "13.35.186.88"
port = 80

max_requests = 10
num_threads = 10

already_connected = 0
lock = threading.Lock()


# Lấy IP của hostname
try:
    ip_address = socket.gethostbyname(hostname)
    print(f"Địa chỉ IP của {hostname} là: {ip_address}")
except socket.gaierror:
    print(f"Không thể phân giải hostname: {hostname}")


def test_connection():
    global already_connected

    count = 0

    while count < max_requests:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)

        try:
            # Chỉ kiểm tra kết nối TCP
            s.connect((target, port))

            count += 1

            with lock:
                already_connected += 1
                print(
                    f"[Thread {threading.current_thread().name}] "
                    f"Kết nối thành công: {already_connected}"
                )

        except socket.timeout:
            print(f"[Thread {threading.current_thread().name}] Timeout")

        except ConnectionRefusedError:
            print(f"[Thread {threading.current_thread().name}] Connection refused")

        except OSError as e:
            print(f"[Thread {threading.current_thread().name}] Lỗi: {e}")

        finally:
            s.close()


# Tạo các thread
threads = []

for i in range(num_threads):
    thread = threading.Thread(
        target=test_connection,
        name=f"Thread-{i + 1}"
    )

    threads.append(thread)
    thread.start()


# Chờ tất cả thread hoàn thành
for thread in threads:
    thread.join()


print("\nHoàn thành bài kiểm tra.")
print(f"Tổng số lần kết nối thành công: {already_connected}")
