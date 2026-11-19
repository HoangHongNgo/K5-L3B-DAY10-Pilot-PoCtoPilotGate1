# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Pilot
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Pilot-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S5

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Ngô Hồng Hoàng | 2A202604093 | Kỹ sư cổng | ✓ |
|   2 | Đỗ Hồng Vỹ | 2A202604107 | Sản phẩm và kinh doanh |             |
|   3 | Nguyễn Quang Thành | 2A202604085 | Vận hành và pháp lý |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## DoHongVy-2A202604107

### Phần việc phụ trách

Vai **Sản phẩm và kinh doanh**. Câu 1.1–1.6 (Phiếu A mục A1–A5), câu 2.3 (Phiếu B mục B3), câu 2.9 (B7.4), lăng kính kinh doanh của pre-mortem (B6), cột v1 (B8); vòng 2: C0–C1 (câu 3.0), C3.5 và C5 (câu 3.1–3.3), sửa `business.pilot_scope` (câu 3.5), quyết định v2 và ba dòng bắt buộc (C12). File: `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`, `templates/form-a-criteria.md`, các mục kể trên của `templates/form-b-evaluation-gates.md` và `templates/form-c-incident.md`.

### Đóng góp cụ thể

- Viết Bản tiêu chí trước khi chạy đánh giá: 5 ngưỡng bắt buộc, `escalation_rate_max` 0,25, nhóm `business_ops` (chi phí ≤ 6.000đ, ROI ≥ 0,5, 0 ca ùn) tính từ `ops_facts`, `stop_condition` và bốn dòng `decision_rule`.
- Phát hiện hash file tiêu chí (và sau đó bản chốt vòng 1) chỉ khớp trên bản xuống dòng CRLF của máy ký, nên sẽ báo "đã bị sửa" trên máy chấm; sửa bằng `.gitattributes` mà không đụng file đã khoá.
- Đặt cổng `business` (trần hoàn 800.000đ/ngày, ngân sách 1.200đ/ticket, ROI 0,5) sau khi so ba phương án phạm vi; cổng ngân sách là cổng vòng 1 duy nhất đỡ được thẻ S5 (tiền LLM 2.412đ → 668đ).
- Vòng 2: cắt kho sỉ HCM-B2B khỏi phạm vi (kho duy nhất đắt hơn làm tay), viết quyết định v2 **Thu hẹp** khớp dòng `decision_rule` đã ký.

### Bằng chứng

- Commit: `8476735` (tiêu chí, Phiếu A A1–A4), `311e60d` (A5, `.gitattributes`), `1420064` (B3), `44cf8ef` (B7.4, cổng `business`), `5e31f50` (B8 v1), `ed47545` (C0 dòng 1, C1, `.gitattributes` cho file khoá), `3555298` (C3.5, C5), `362e709` (`pilot_scope`, C0 dòng 3), cùng commit C12. Các commit này đứng tên Git `2A202604093` vì máy dùng chung cấu hình Git của trưởng nhóm, nội dung do Đỗ Hồng Vỹ viết.
- Lần chạy: `R-S5-after-20261119-170621-e86e61` (đổi `pilot_scope`), `R-base-after-20261119-170626-e86e61` (kiểm bộ nền sau khi đổi).
- Phiếu: A mục A1–A5; B mục B3, B7.4, B8; C mục C0 dòng 1 và 3, C1, C3.5, C5, C12.

### Exit ticket

Học được: ngưỡng phải viết trước khi nhìn số, và bộ thử quyết định mình thấy gì. Bộ nền không có đơn sỉ nào nên v1 nói "không kho nào đắt hơn làm tay", và thẻ S5 cho thấy nhận định đó sai. Còn chưa chắc: cổng hoàn tích lũy chỉ đúng khi CSKH ghi sổ kịp thời, mà điều đó chưa đo được trên dữ liệu mock.
