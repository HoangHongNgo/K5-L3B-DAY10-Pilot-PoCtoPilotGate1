# Tự kiểm tra sự cố S5 · FAIL

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S5-grade-20261119-173323-c05120` · bàn: `K5-L3B-DAY10-Pilot-PoCtoPilotGate1` · grader `lab10-1.0` · 0.953s
- Ba mốc: base `R-S5-before-20261119-173324-c05120` · prepared `R-S5-prepared-20261119-173324-c05120` · after `R-S5-after-20261119-173324-c05120` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `60b8f2a6`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `c05120681612`
- Hash Bản tiêu chí chấp nhận: `105727825e11` · đã ký: `105727825e11` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S5` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S5 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ✅ | file khoá bị đổi: không |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ❌ | base có vấn đề: True; after sạch: False; ticket còn hỏng: không; trần còn vượt: ['ROI 0.13 < ngưỡng bàn đặt 0.5', 'kho HCM-B2B: mỗi ticket tốn 10382đ > làm tay 10000đ'] |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['duplicate_refund_rate', 'worst_warehouse_escalation_rate']; sáng đèn: [('duplicate_refund_rate', 'after', 0.0, 0.166667)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.4 | 0.5 | 0.6333 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 2 · 12 | 2 · 12 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 6083 · 10000 | 7504 · 10000 | 8861 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 2412 · 1500 | 668 · 1500 | 765 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | -60486 | -103130 | 34170 |
| ROI | -0.33 | -0.46 | 0.13 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 196000 · 2000000 | 196000 · 2000000 | 98000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 178000 · 2000000 | 178000 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 1.0 | 1.0 |
| số kho đắt hơn làm tay | 1 | 1 | 1 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 20 | 20 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 0.6667; hoàn sai 50000; oan 0; PII 0; chi phí 664đ | pass 0.6667; hoàn sai 50000; oan 0; PII 0; chi phí 664đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 764đ |
| kho DN | pass 0.8; hoàn sai 490000; oan 5; PII 0; chi phí 663đ | pass 0.8; hoàn sai 490000; oan 5; PII 0; chi phí 663đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2723đ |
| kho HCM | pass 0.5; hoàn sai 100000; oan 5; PII 0; chi phí 662đ | pass 0.5; hoàn sai 100000; oan 5; PII 0; chi phí 662đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 5662đ |
| kho HCM-B2B | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 11326đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10382đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10382đ > làm tay |
| kho HN | pass 0.75; hoàn sai 250000; oan 10; PII 0; chi phí 1244đ | pass 0.75; hoàn sai 250000; oan 10; PII 0; chi phí 4239đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 6752đ |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 0.8; hoàn sai 250000; oan 10; PII 0 | pass 0.8; hoàn sai 250000; oan 10; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 0.8333; hoàn sai 50000; oan 0; PII 0 | pass 0.8333; hoàn sai 50000; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.75; hoàn sai 590000; oan 10; PII 0 | pass 0.75; hoàn sai 590000; oan 10; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.2364 | 0.2727 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 2 · 12 | 2 · 12 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 5656 · 10000 | 5874 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 670 · 1500 | 770 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 95562 | 90782 |
| ROI | 1.34 | 0.77 | 0.7 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 1.0 | 1.0 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 665đ |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4646đ |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2967đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3683đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- VƯỢT TRẦN: ROI 0.13 < ngưỡng bàn đặt 0.5 (trên visible)
- VƯỢT TRẦN: kho HCM-B2B: mỗi ticket tốn 10382đ > làm tay 10000đ (trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: cost_per_ticket_vnd ≤ 6000 (thực tế 8861, trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: roi ≥ 0.5 (thực tế 0.13, trên visible)
- KHÔNG đủ căn cứ để chọn 'Tiếp tục'. Thu hẹp, Cải tiến thêm hoặc Dừng, kèm lý do và con số, vẫn là quyết định đạt.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.2364 | 0.2364 | +0.0091 |
| visible | pass_rate | 0.8333 | 0.8333 | 1.0 | +0.1667 |
| visible | pass_k | 0.8333 | 0.8333 | 1.0 | +0.1667 |
| visible | wrongful_refund_vnd | 890000 | 890000 | 0 | -890000 |
| visible | under_refund_vnd | 0 | 0 | 0 | +0 |
| visible | wrongful_carrier_faults | 20 | 20 | 0 | -20 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.4 | 0.5 | 0.6333 | +0.2333 |
