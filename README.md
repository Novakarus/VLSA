# Vietnam Legal Advisor

![Vietnam Legal Advisor](docs/assets/vietnam-legal-advisor-icon-v4.png)

Bộ kỹ năng hỗ trợ nghiên cứu, rà soát và soạn thảo pháp lý Việt Nam, do Thanh Nguyen phát hành. Phiên bản plugin hiện tại: **0.69.3**.

- [Website](https://novakarus.github.io/VietnamLegalAdvisor/) · [Hướng dẫn](https://novakarus.github.io/VietnamLegalAdvisor/guide/)
- [Plugin trên nền tảng](https://chatgpt.com/plugins/plugin_a0d9ed08c8288191a1b91e0d7ed3f238): hiện riêng tư; công khai nguồn không tự mở quyền truy cập.
- [Nguồn plugin](plugin/) · [Kết quả kiểm thử](tests/reports/0.69.3/summary.md) · [Lịch sử thay đổi](CHANGELOG.md)

## Chức năng

Một kỹ năng điều phối và 12 kỹ năng chuyên môn: nghiên cứu pháp luật; kiểm tra hiệu lực; rà soát hợp đồng; thẩm định pháp lý; soạn thảo; lập luận; phản biện; quản trị doanh nghiệp; đầu tư và M&A; tuân thủ; kiểm tra nguồn; kiểm toán chất lượng. Mặc định trả lời tiếng Việt. Đây là quy trình chỉ dẫn, không phải 13 tác nhân tự chạy.

## Bắt đầu

Tải nguồn từ GitHub, đọc [hướng dẫn](docs/guide/index.html), chọn thư mục plugin/ trong nền tảng hỗ trợ plugin cục bộ. Kiểm tra bằng `python scripts/validate.py`; tạo gói bằng `python scripts/package.py`. Khả năng cài đặt phụ thuộc nền tảng. [Tải gói 0.69.3 dựng lại](https://github.com/Novakarus/VietnamLegalAdvisor/releases/tag/v0.69.3), có mã kiểm tra riêng và giấy phép đi kèm. Nội dung 20 tệp khớp bản đã kiểm thử; toàn ZIP có thể khác mã ZIP lịch sử do cách nén.

## Quyền sử dụng

Nhà phát hành không thu phí sử dụng plugin; phí và điều kiện nền tảng áp dụng riêng. Được sử dụng kết quả cho công việc thương mại theo [Điều khoản](https://novakarus.github.io/VietnamLegalAdvisor/terms/). Nguồn công khai có điều kiện, không phải giấy phép mã nguồn mở: xem [LICENSE.md](LICENSE.md). Quyền xem/fork theo GitHub được bảo lưu; phát hành lại ngoài phạm vi quyền đó cần chấp thuận qua email.

## Trạng thái và giới hạn

22/22 tình huống đạt đánh giá AI tạm thời; chưa nghiệm thu pháp lý độc lập. Đã đối chiếu nội dung sau cập nhật plugin, chưa kiểm thử lại hành vi trên nền tảng. Không kèm cơ sở dữ liệu pháp luật hoặc tự động cập nhật luật. Phải kiểm tra nguồn quyết định và hiệu lực theo thời điểm; không thay thế đại diện pháp lý có giấy phép.

## Cấu trúc

- plugin/ — nguồn đóng gói;
- docs/ — nguồn website;
- tests/ — tình huống và báo cáo công khai;
- releases/ — hồ sơ phát hành; scripts/ — kiểm tra và đóng gói;
- github/ — kiểm tra tự động và mẫu báo lỗi.

Website hiện có bản tương thích ở gốc để tiếp tục phục vụ cấu hình GitHub Pages hiện tại. Sửa docs/ rồi chạy `python scripts/sync_site.py` để đồng bộ. Có thể chuyển Pages sang main:/docs rồi bỏ bản tương thích trong một thay đổi riêng.

Hỗ trợ: ntthanh912@gmail.com. Không gửi thông tin nhạy cảm qua Issues. 
[Privacy](https://novakarus.github.io/VietnamLegalAdvisor/privacy/) · [Đóng góp](CONTRIBUTING.md).

