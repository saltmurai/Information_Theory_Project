## TÀI LIỆU HƯỚNG DẪN SỬ DỤNG BÀI TẬP LỚN LÝ THUYẾT THÔNG TIN

---

#### Tổng quan

Giới thiệu: Bài tập lớn cho môn lý thuyết thông tin, trường Điện - Điện tử, HUST 

**Tên đề tài:** Mã hoá văn bản theo mã Huffman & mã Hamming cho truyền tín hiệu âm thanh

**Ngôn ngữ lập trình sử dụng:** Python3

**Hệ điều hành:** Windows, Linux, MacOS

---

#### Hướng dẫn cài đặt chương trình

**Yêu cầu:** Máy tính đã cài đặt Python3, pip và git

Đối với các hệ điều hành UNIX như Ubuntu, MacOS mở terminal và chạy các lệnh sau:

```bash
git clone https://github.com/saltmurai/Information_Theory_Project
```

Hoặc có thể giải nén folder bài tập lớn.

Sau đó cài đặt thư viện scipy, matplolib và tabulate sử dụng pip hoặc có thể dùng lệnh sau:

```bash
pip install -r requirements.txt
```

Đối với Windows làm tương tự nhưng với command promt hoặc powershell.

---

#### Hướng dẫn chạy chương trình
*Lưu ý cần cài đặt thư viện scipy, matplotlib và tabulate dùng pip trước*
**Mã hoá văn bản theo Huffman**

Mở thư mục huffman trên terminal

```bash
python3 Huffman.py text.txt
```

Trong đó text.txt là một file văn bản bất kỳ trong đó chứa nội dung cần mã hoá, kết quả mã hoá sẽ được in ra trên màn hình và viết ra 2 file. **binary_text.txt** là văn bản đã được mã hoá theo cơ số 2 và **info_text.txt** là file chứa các thông tin được in ra trên màn hình. 

**Mã Hamming cho truyền tín hiệu âm thanh**

Mở thu mục hamming trên terminal, trong folder đã có sẵn một file âm thanh 8-bit demo là **sound.wav**, có thể sử dụng các file âm thanh 8-bit khác. Để mô phỏng việc truyền tín hiệu âm thanh qua kênh truyền với mức nhiễu là 1% gõ lệnh sau trên terminal:

```bash
python3 main.py sound.wav 1
```

Lần lượt đồ thị của âm thanh gốc, âm thanh bị nhiễu (không sử dụng mã hamming), âm thanh được giải mã và sửa sai (sử dụng mã Hamming) được hiện ra. 

Tắt lần lượt 3 cửa sổ

Chương trình sẽ lưu 2 file là:

**corrupted__sound.wav** (âm thanh bị nhiễu khi không sử dụng mã hamming)

**corrected_sound.wav** (âm thanh được sửa sai sử dụng mã Hamming)

Có thể nghe 2 file này để thấy sự khác biệt

---

**Một số lưu ý**

- Trên windows khi cài đặt python3 trong PATH thay vì là **python3** có thể là **python**

- Cài đặt pip trên ubuntu
  
  ```bash
  sudo apt update
  sudo apt install python3-pip
  ```

- Cài đặt pip trên windows

[How to Install PIP for Python on Windows - Liquid Web](https://www.liquidweb.com/kb/install-pip-windows/)


