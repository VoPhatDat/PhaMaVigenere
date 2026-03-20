# PhaMaVigenere

Chương trình phá mã Vigenère tự động sử dụng phương pháp thống kê, không cần biết khóa trước.

## Mô tả

Vigenère là một phương pháp mã hóa cổ điển sử dụng chuỗi khóa lặp lại để mã hóa từng ký tự trong bản rõ. Chương trình này thực hiện phá mã hoàn toàn tự động qua 2 bước:

1. **Kasiski Test** — Tìm các chuỗi ký tự lặp lại trong bản mã, tính khoảng cách giữa chúng và phân tích ước số chung để ước lượng độ dài khóa.
2. **Chi-squared Analysis** — Với mỗi vị trí trong khóa, thử 26 ký tự Caesar và chọn ký tự có giá trị Chi-squared nhỏ nhất so với tần suất chuẩn tiếng Anh.

## Công nghệ

- **Python**
- Không sử dụng thư viện ngoài (built-in only)

## Cách chạy

```bash
python main.py
```

Nhập bản mã khi được yêu cầu, chương trình sẽ tự động in ra khóa ước lượng và bản rõ.

## Lý thuyết áp dụng

### Kasiski Test
Nếu một chuỗi ký tự xuất hiện nhiều lần trong bản mã, khoảng cách giữa các lần xuất hiện đó có khả năng là bội số của độ dài khóa. Lấy GCD của các khoảng cách đó để ước lượng độ dài khóa.

### Chi-squared
Với mỗi nhóm ký tự tương ứng cùng một vị trí trong khóa, thử giải mã Caesar với 26 giá trị shift. Ký tự khóa đúng là shift cho ra phân phối tần suất gần nhất với tần suất chuẩn tiếng Anh, tức là có giá trị Chi-squared nhỏ nhất:

$$\chi^2 = \sum_{i=0}^{25} \frac{(O_i - E_i)^2}{E_i}$$
