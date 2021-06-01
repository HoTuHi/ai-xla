# https://youtu.be/hPCTwxF0qf4 how to haar cascade work ?
# hi, just another day, good job.
# have 3 ways to creat xml file, but gui is better
How to CNN work ?
Convolutional Neural Network (CNNs – Mạng nơ-ron tích chập)
là một trong những mô hình Deep Learning tiên tiến.
Nó giúp cho chúng ta xây dựng được những hệ thống thông minh
với độ chính xác cao như hiện nay.


Haar Cascade là gì?
Về cơ bản là sử dụng các đặc trưng loại Haar
và sau đó sử dụng thật nhiều đặc trưng đó qua nhiều lượt (cascade)
để tạo thành một cỗ máy nhận diện hoàn chỉnh.
Các bộ lọc ở Haar hơi khác 1 chút so với CNN, thay vì là 1 cửa sổ trượt thì ở Haar,
bộ lọc chỉ chiếm một phần trong cả cửa sổ trượt
https://docs.opencv.org/3.3.0/haar.png
how to haar cascade work ?
# https://youtu.be/hPCTwxF0qf4
chỉ cần sử dụng 1 file có đuôi mở rộng là xml thìf có thể sử dụng các đặc trưng của
việc training để phát hiện các vật thể
nó tiện dụng như vậy á ? đéo, đéo và đéo.
nó là 1 file lưu các đặc trưng của vật thể
WTF ? đặc trưng lấy đâu ra ? nó được training từ dữ liệu được gắn nhãn,
là học máy có giám sát, từ 2 tệp dữ liệu bao gồm
positive (tệp hình ảnh tích cực có vật thể)
và negative ( tệp hình ảnh tiêu cực không có vật thể)
sử dụng ToolCascadeTrainerGUI để xuất ra file Xml

Những cái trên để làm gì ?
để từ 2 tệp có thể phát hiện ra có lưới Sudoku ở trong hình ảnh,
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


Có 4 người 4 việc :
- HoTuHi : lên ý tưởng, triển khai ý tưởng, tìm giải pháp và merge code của các bạn
- làm Traing data : kiểm tra data (cụ thể là ảnh) chính xác.
- code :
    - code từ phần ảnh gốc thành ảnh mẫu.
    - code phần từ ảnh mẫu sang thành chữ.
