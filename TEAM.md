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

## NgoHongHoang-2A202604093

### Phần việc phụ trách

Vai **Kỹ sư cổng** và trưởng nhóm. Câu 2.1, 2.2 (B0–B2), 2.6–2.8 (B7.1–B7.3); các lệnh ghi dấu một lần (ký tiêu chí, chốt cổng vòng 1, nhận thẻ S5); vòng 2: C2 (bảng soát lỗi), C8, sửa `lab10/guards.py` và `lab10/monitors.py` cho thẻ S5, chạy `eval` và `grade`, demo ba cột `base · prepared · after`. File: `lab10/guards.py`, `lab10/monitors.py`.

### Đóng góp cụ thể

- Ký tiêu chí (`Sign acceptance criteria`) trước mọi lần chạy `eval`; chạy baseline, dò `T-002@55`, điền B2.
- Dựng 3 cổng vòng 1 trong `guards.py`: hoàn theo dữ liệu DB, lỗi hãng theo DB, bỏ trường PII khỏi tin gửi hãng; chốt vòng 1 (mốc prepared `60b8f2a6`).
- Thẻ S5: cổng 4 chặn hoàn theo quyền lợi tích lũy trong sổ cái (ngăn hoàn trùng); cổng 5 rút gọn ticket dài để giảm tiền LLM; thêm hai chỉ số `duplicate_refund_rate` và `worst_warehouse_escalation_rate` trong `monitors.py`.
- Kết quả mốc after: bộ base và bộ S5 đều pass 1.0, hoàn sai 0 đ, oan 0, PII 0.

### Bằng chứng

- Commit: `57a0990` (ký), `c4312c4`, `696ab69` (cổng vòng 1), `af89011` (chốt vòng 1), `16996d9` (nhận thẻ S5), `93992d3` (cổng 4), `33fb3f5` (monitor), `fdd7b0a` (cổng 5).
- Lần chạy: `runs/R-S5-grade-20261119-234652-4be4d9` (grade, `1 integrity`, `3 visible`, `5 regression`, `6 monitor` đạt); `submission/runs/` có `journal.jsonl` và report ba mốc.

### Exit ticket

Học được: cổng chặn phải dựa vào số liệu thật trong sổ cái chứ không dựa vào lời khách, và mỗi lần chỉ đổi một thứ mới biết thứ nào đỡ được con số. Chưa chắc: cổng hoàn tích lũy còn đúng không khi CSKH ghi sổ chậm ngoài đời thật.

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
