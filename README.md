# hi, just another day, good job.
#Detect and solve Sudoku
what is sudoku ?
Sudoku (数独すうどく (số độc) sūdoku?) (/[invalid input: 'Sudoku.ogg']suːˈdoʊkuː/, /-ˈdɒ-/, /sə-/, ban đầu có tên gọi là Number Place)[1] là một trò chơi câu đố sắp xếp chữ số dựa trên logic[2][3] theo tổ hợp.[4] Mục tiêu của trò chơi là điền các chữ số vào một lưới 9×9 sao cho mỗi cột, mỗi hàng, và mỗi phần trong số chín lưới con 3×3 cấu tạo nên lưới chính (cũng gọi là "hộp", "khối", hoặc "vùng") đều chứa tất cả các chữ số từ 1 tới 9. Câu đố đã được hoàn thành một phần, người chơi phải giải tiếp bằng việc điền số. Mỗi câu đố được thiết lập tốt có một cách làm duy nhất.

Những bảng trò chơi đã được hoàn chỉnh luôn tạo thành một loại ma trận hình vuông Latinh với một điều kiện hạn chế được bổ sung về nội dung của từng khu vực lưới con. Ví dụ, mỗi số nguyên duy nhất sẽ có thể không xuất hiện hai lần trong cùng một hàng, cột hoặc bất kỳ một trong chín tiểu khu/lưới con 3×3 nào của bảng trò chơi 9x9.
nguồn : 
##https://vi.wikipedia.org/wiki/Sudoku

#How to CNN work ?
Convolutional Neural Network (CNNs – Mạng nơ-ron tích chập)
là một trong những mô hình Deep Learning tiên tiến.
Nó giúp cho chúng ta xây dựng được những hệ thống thông minh
với độ chính xác cao như hiện nay.
#Haar Cascade là gì?
Về cơ bản là sử dụng các đặc trưng loại Haar
và sau đó sử dụng thật nhiều đặc trưng đó qua nhiều lượt (cascade)
để tạo thành một cỗ máy nhận diện hoàn chỉnh.
Các bộ lọc ở Haar hơi khác 1 chút so với CNN, thay vì là 1 cửa sổ trượt thì ở Haar,
bộ lọc chỉ chiếm một phần trong cả cửa sổ trượt

##https://docs.opencv.org/3.3.0/haar.png

#how to haar cascade work ?

###chỉ cần sử dụng 1 file có đuôi mở rộng là xml thif có thể sử dụng các đặc trưng của việc training để phát hiện các vật thể nó tiện dụng như vậy á ? đéo, đéo và đéo. nó là 1 file lưu các đặc trưng của vật thể WTF ? đặc trưng lấy đâu ra ? nó được training từ dữ liệu được gắn nhãn, là học máy có giám sát, từ 2 tệp dữ liệu bao gồm positive (tệp hình ảnh tích cực có vật thể) và negative ( tệp hình ảnh tiêu cực không có vật thể) sử dụng ToolCascadeTrainerGUI để xuất ra file Xml
https://youtu.be/hPCTwxF0qf4

###how to make a haar cascade file

use Tool CascadeTrainer Gui để xuất file Xml.

https://amin-ahmadi.com/cascade-trainer-gui/

##Những cái trên để làm gì ?

để từ 1 tệp có thể phát hiện ra có lưới Sudoku ở trong hình ảnh,
xác định vị trí của lưới,
sử dụng thư viện OpenCv để biến đổi ảnh, đưa ảnh về ảnh hình vuông có lưới 9x9 
nhưng, trong thời điểm mà giá coin lên cao, trời nắng 40 độ, 
Tool casecade lại dùng quá nhiều GPU, nên chỉ có thể sử dụng 
tầm 30 mẫu(trong 1tr mẫu text được tải xuống từ kaggle) để train
(60 tệp hình ảnh mất 30h chạy)
Garbage in garbage out.
sau khi đã chuyển về lưới 9x9 như hình mẫu
thì để phát hiện ra chữ số ở trong ảnh thì thực hiện chia ảnh thành các 9*9=81 cell nhỏ để tiến hành 
nhận dạng chữ cái.
Có thể sử dụng KNN( hàng xóm cận kề) để xác định chữ cái, 
nhưng mà tìm thấy 1 tool ORC chữ khá là ổn nên dùng tạm ( repo mã nguồn mở tesseract ocr : https://github.com/tesseract-ocr/tesseract)
hoạt động ổn điijnh nhưng cần tinh chỉnh đầu vào để tănng độ chính xác của việc nhận định bằng cách :
nối dài cell của ảnh ( vd cell đấy là 5) thì nối thành 55555 để tăng xác suất chĩnh xác.
sau khi xác định được chữ thì sử dụng backtracking để giải.
Phát triển, tạo thành 1 tính năng ở trên telegram để làm chat bot


## Mô tả File
  - [data](https://github.com/HoTuHi/ai-xla/tree/main/data) chứa các file *.csv dữ liệu

  - [./data/bad](https://github.com/HoTuHi/ai-xla/tree/main/data/bad) chứa các mẫu nhãn regative

  - [./data/good](https://github.com/HoTuHi/ai-xla/tree/main/data/good) chứa các mẫu nhãn positive

  - [./data/samp](https://github.com/HoTuHi/ai-xla/tree/main/data/samp) chứa các đầu vào là bài báo render từ unititle.blend
### Run 
- để training ra file haar cascade, sử dụng CascadeTrainerGui, chọn đường dẫn folder ./data/bad và ./data/good
để chọn dữ liệu.
chi tiết xem thêm tại [đây](https://amin-ahmadi.com/cascade-trainer-gui/)
- cài đặt tool tesseract ocr, thay đổi đường dẫn ở File Image2String
  ```python 
  pytesseract.pytesseract.tesseract_cmd = "D:\\SteamGame\\New folder\\tesseract.exe"
  ```
- thay đổi đường dẫn trong solver.py 
  ```python
  path = './data/good/5.png'
  
- nếu đã có file mở rộng xml, gõ python solver.py để chạy
  ```angular2html
  python solver.py
  ```

# All tools and large file in project in my drive, please check the link bellow :
      https://drive.google.com/drive/folders/12QYtYtWz0AT7mm2KUMt7_YboVlAdH5hP?usp=sharing

Có 4 người 4 việc :
- HoTuHi : lên ý tưởng, triển khai ý tưởng, tìm giải pháp và merge code của các bạn
- làm Traing data : kiểm tra data (cụ thể là ảnh) chính xác.
- code :
    - code từ phần ảnh gốc thành ảnh mẫu.
    - code phần từ ảnh mẫu sang thành chữ.
  
