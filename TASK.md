# TASK · Chia việc theo vai, theo từng checkpoint

Vai theo [`TEAM.md`](TEAM.md). Số checkpoint, thời gian, sản phẩm: [`CHECKPOINTS.md`](CHECKPOINTS.md). Chi tiết từng bước: [README mục 3](README.md#timeline). Số câu khớp [`problem-set.md`](problem-set.md), mỗi câu có ô trả lời trong phiếu ở `templates/`.

| Viết tắt | Người | MSSV | Vai | File chính |
|---|---|---|---|---|
| **HOÀNG** | Ngô Hồng Hoàng (trưởng nhóm) | 2A202604093 | Kỹ sư cổng | `lab10/guards.py`, `lab10/monitors.py` |
| **VỸ** | Đỗ Hồng Vỹ | 2A202604107 | Sản phẩm và kinh doanh | `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`, Phiếu A, B8, C12 |
| **THÀNH** | Nguyễn Quang Thành | 2A202604085 | Vận hành và pháp lý | `config/operating_gates.json` mục `operations` và `legal`, B4–B5, B7.5–B7.6, C11, `submission/` |

## Quy tắc chung

- **Một người cầm bút một file** tại một thời điểm, để tránh xung đột Git. Trước khi sửa: `git pull`. Sửa xong: commit, push ngay, rồi báo cả nhóm.
- **Mọi quyết định (v1, v2) do cả bàn chốt**; người không viết code vẫn đọc trace cùng HOÀNG.
- **Chỉ HOÀNG chạy các lệnh ghi dấu một lần** (lệnh 1 ký, lệnh 5 chốt vòng 1, lệnh nhận thẻ) để mã commit và `runs/` không bị lệch giữa các máy. Người khác đọc kết quả sau khi `git pull`.
- **Không sửa** `config/acceptance_criteria.json` sau khi ký, và không sửa `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`.
- Không xử lý riêng theo mã ticket hay câu chữ cụ thể; không chặn hết, không thu hẹp phạm vi về 0 ([README mục 5](README.md#5-luật)).

---

## CP1 · Cài đặt và chia vai (phút 0–15) ✅ xong

| Ai | Việc | Xong khi |
|---|---|---|
| HOÀNG | Tạo repo, đặt danh tính Git, gắn `upstream`, mời collaborator, push `TEAM.md` | Đã xong |
| VỸ, THÀNH | `git clone` repo của bàn về máy; chạy `python3 -m unittest discover -s tests` (thử `python` nếu `python3` không chạy) | In `Ran 13 tests … OK` |
| Cả bàn | Chọn một eval card và một PRD v1.1 từ Lab 9 làm bản chung | Cả ba cùng đọc được file |

## CP2 · Ký tiêu chí (phút 15–65) · Phiếu A

**Chưa chạy trợ lý** ở checkpoint này. Viết ngưỡng trước khi biết trợ lý đạt hay trượt.

| Ai | Việc | Sản phẩm |
|---|---|---|
| VỸ | Câu 1.1–1.2 (A1) · câu 1.3–1.4, bảng thước đo → dữ liệu → cách tính (A2) · câu 1.5 khoảng tin cậy (A3) · câu 1.6, câu "Nếu … thì chúng tôi sẽ …", bốn câu soát, hai câu ranh giới đầu ra (A4) | Phiếu A mục A1–A4 |
| VỸ | Điền `config/acceptance_criteria.json`: `team` (đúng tên repo), `signed_by`, `required.*`, `nice_to_have.escalation_rate_max`, `business_ops.*`, `stop_condition`, bốn dòng `decision_rule`. Xem `config/acceptance_criteria.example.json`, đừng chép ngưỡng | File tiêu chí đã điền |
| HOÀNG | Soát các ngưỡng `pass_rate_min`, `pass_k_min`, `pii_leaks_max`, `wrongful_*` có đo được bằng báo cáo của `lab10.eval` không; góp ý cho VỸ | Danh sách góp ý |
| THÀNH | Soát `queue_stuck_max`, `stop_condition` và các ngưỡng liên quan người trực, dữ liệu cá nhân; góp ý cho VỸ | Danh sách góp ý |
| Cả bàn | Đọc lại toàn bộ tiêu chí, cùng đồng ý trước phút 60 | Đồng thuận |
| **HOÀNG** | Phút 60–65, ngay khi điền xong: `python3 -m lab10.criteria sign`, rồi `git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main` | Máy in `ĐÃ KÝ.`; commit ký có trên GitHub |
| VỸ | Điền A5 (giờ ký, mã commit) | Phiếu A mục A5 |

**Xong khi:** máy in `ĐÃ KÝ.`; commit ký có trên GitHub **trước** mọi lần chạy `eval`.

## CP3 · Đo, rủi ro, cổng vòng 1, quyết định v1 (phút 65–115) · Phiếu B

### 65–85 · Khối 2A (chưa sửa code hay config), ba người làm song song

| Ai | Việc | Sản phẩm |
|---|---|---|
| HOÀNG | Câu 2.1 (B1, ghi mã vào B0): `python3 -m lab10.eval --suite base --stage base --note "baseline"`, rồi `python3 -m lab10.gate --run runs/<mã>/report.json`; đọc `[ĐẠT ]`/`[CHƯA]`, khối "kinh doanh và vận hành", khối "theo kho và hãng" | B0, B1, mã lần chạy base |
| HOÀNG | Câu 2.2 (B2): `python3 -m lab10.trace --suite base --ticket T-002 --seed 55`, điền bảng soát lỗi | B2; `T-002@55` được xếp loại lỗi |
| VỸ | Câu 2.3 (B3): bản đồ dữ liệu và một ví dụ drift | B3 |
| THÀNH | Câu 2.4 (B4): HAZOP vòng 1, ≥ 3 dòng, trong đó ≥ 2 dòng ngoài kỹ thuật · (B5): checklist 9 nhóm, mỗi dòng một PIC có tên | B4, B5 |
| Cả bàn | Câu 2.5 (B6): pre-mortem bốn lăng kính; đánh dấu 2–3 lý do sẽ thành cổng | B6 đủ bốn lăng kính |

### 85–105 · Khối 2B: dựng cổng phòng ngừa

| Ai | Việc | Sản phẩm |
|---|---|---|
| HOÀNG | Câu 2.6 (B7.1): 2–3 cổng trong `lab10/guards.py` (`pre_guard`, `write_gate`; đặt kiểm tra trước dòng `return Verdict.allow()`) | `lab10/guards.py` |
| HOÀNG | Câu 2.7 (B7.2): hai bước tránh rò rỉ dữ liệu · câu 2.8 (B7.3): một tính chất + hai ticket hiểm chạy bằng `--adhoc` | B7.2, B7.3 |
| VỸ | Câu 2.9 (B7.4): `config/operating_gates.json` mục `business` (`daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`); mỗi số một câu lý do từ `data/world.json` → `ops_limits`, `ops_facts` | `business` đã điền, B7.4 |
| THÀNH | Câu 2.10 (B7.5, B7.6): mục `operations` (`pic`, `approver_id`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`) và `legal` (`pii_fields_blocked_to_third_party`, `carrier_fault_requires_recorded_cause`); runbook phần 1–3 và mục **Giờ cao điểm** khớp các con số đó | `operations`, `legal`, runbook |
| HOÀNG | Thử cổng sau khi VỸ và THÀNH push: `python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."`, một lần `lab10.trace ... --adhoc`, và `python3 -m unittest discover -s tests` | Report `base · after` không có ca mới hỏng; test `OK`; `operations.pic` không còn trống |

> `config/operating_gates.json` có hai người cùng sửa (VỸ mục `business`, THÀNH mục `operations`/`legal`). Hai người sửa **tuần tự**: người này push xong, người kia `git pull` rồi mới sửa.

### 105–115 · Chốt cổng vòng 1, quyết định v1 (B8)

| Ai | Việc | Sản phẩm |
|---|---|---|
| Cả bàn | Chốt quyết định v1: một quyết định, ba bằng chứng có mã lần chạy, dòng `decision_rule`, kho hoặc hãng có số xấu nhất, ngày quyết định lại | Thống nhất |
| **HOÀNG** | Đúng thứ tự: `python3 -m lab10.checkpoint` → `python3 -m lab10.eval --suite base --stage prepared` → `python3 -m lab10.gate --run runs/<mã>/report.json` | `ĐÃ CHỐT cổng vòng 1 (mốc prepared). 8 ký tự đầu: …` |
| VỸ | Điền cột v1 ở B8 | B8 |
| HOÀNG | Chạy lệnh commit và push ở cuối B8 | Push thành công |

**Xong khi:** có mã lần chạy base; `T-002@55` được xếp loại lỗi; lệnh 5 chạy thành công; đã commit và push.

## CP4 · Sự cố (phút 125–185) · Phiếu C

### 125–135 · Nhận thẻ, đo trước khi sửa (câu 3.0)

| Ai | Việc | Sản phẩm |
|---|---|---|
| Cả bàn | Nghe Lab Coach báo số thẻ (S1–S8); **chỉ làm đúng thẻ của bàn** | Số thẻ |
| **HOÀNG** | `git fetch https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_cards.git main` → `git checkout FETCH_HEAD -- incidents/Sx` → `git commit -m "Nhận thẻ Sx"` → `python3 -m lab10.grade --incident Sx` → `git push -u origin main` (gõ từng dòng, thay `Sx`) | `ls incidents/Sx` đủ 4 file; report `1 integrity ✅` |
| THÀNH | Ghi `Thẻ đã bốc:` ở đầu Phiếu C và `TEAM.md` | Dòng `Thẻ đã bốc:` |
| VỸ | Điền C0 (mã prepared) và C1 (cổng vòng 1 đỡ được gì; đối chiếu pre-mortem bằng bút khác màu) | C0, C1 |

### 135–155 · Phân tích (câu 3.1–3.4)

| Ai | Việc | Sản phẩm |
|---|---|---|
| HOÀNG | Dò ít nhất hai ticket hỏng, hai kiểu khác nhau: `python3 -m lab10.trace --suite Sx --ticket Sx-01 --seed 11`; điền C2 (bảng soát lỗi của thẻ) | C2 |
| VỸ | C3 phần riêng theo thẻ (chỉ phần của số đã bốc; bàn bốc thẻ S4 không cần điền C3) · C5 specification và giả định môi trường | C3, C5 |
| THÀNH | C4 HAZOP của thẻ (≥ 3 dòng, không ghi đè HAZOP vòng 1) | C4 |
| Cả bàn | C6 fault tree **trước khi sửa**, có nhánh ngoài kỹ thuật | C6 |

### 155–185 · Sửa đúng chỗ (câu 3.5–3.6), ghi phần đã sửa (câu 3.7)

| Ai | Việc | Sản phẩm |
|---|---|---|
| HOÀNG | Sửa `lab10/guards.py` cho nguyên nhân kỹ thuật; thêm ≥ 1 hàm chỉ số trong `lab10/monitors.py` phía trên dict `MONITORS`, đăng ký `"tên_chỉ_số": tên_hàm` (`escalation_rate` có sẵn không tính) | `guards.py`, `monitors.py` |
| VỸ | Sửa `business.pilot_scope`, trần tiền theo nguyên nhân về tiền/phạm vi; không thu hẹp phạm vi về 0 | `operating_gates.json` mục `business` |
| THÀNH | Sửa `operations.reviewers_on_shift`, `review_sampling_pct`, `decision_note`, `legal.*` theo nguyên nhân về người/pháp lý | `operating_gates.json` mục `operations`, `legal` |
| HOÀNG | Mỗi lần **đổi MỘT thứ** rồi chạy: `python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."`; kiểm lại nền `python3 -m lab10.eval --suite base --stage after --note "kiểm lại bộ nền sau khi sửa"`; `python3 -m lab10.grade --incident Sx` | Report `base · prepared · after` |
| HOÀNG | C7 bảng sửa (giảm hay ngăn) · C8 chỉ số theo dõi mới (ba ô) · C9 fault tree sau khi sửa | C7, C8, C9 |
| VỸ | C10 ≥ 1 dòng risk register | C10 |
| THÀNH | C11 cập nhật checklist và runbook phần 4–5 | C11 |

**Xong khi:** report có `1 integrity ✅`, `3 visible ✅`, `5 regression ✅`, `6 monitor ✅`; `visible` và `regression` chỉ ✅ khi độ phủ pilot lớn hơn 0.

## CP5 · Quyết định v2, demo, nộp (phút 185–240)

| Ai | Việc | Sản phẩm |
|---|---|---|
| Cả bàn | Chốt quyết định v2. Chọn **Tiếp tục** khi report còn vượt trần hoặc còn ngưỡng đã ký chưa đạt là quyết định không đạt | Thống nhất |
| VỸ | Điền C12 (cột v2, mục "Chỉ ở v2", ba dòng bắt buộc) | C12 |
| THÀNH | Điền `submission/submission.json`: `team` giống tiêu chí đã ký, `members` dạng `"HoVaTen-MSSV"` (`NgoHongHoang-2A202604093`, `DoHongVy-2A202604107`, `NguyenQuangThanh-2A202604085`), `incident`, `decision_v1`, `decision_v2`, ba câu `three_lines` chép từ C12 | `submission.json` |
| **THÀNH** | Lệnh 7: `python3 -m lab10.check_submission --collect`; sửa từng dòng `[THIẾU]` theo `->` rồi chạy lại | In `ĐỦ THÀNH PHẦN` |
| HOÀNG | Demo ba cột `base · prepared · after` (5 phút): cổng vòng 1 đã đỡ được gì; phần sửa vòng 2 là code, con số hay người. Chuẩn bị một ticket hiểm cho bàn phản biện | Demo |
| VỸ | Trình bày con số nào đỡ cho v2 | Demo |
| THÀNH | Sau demo: trả mọi con số đã đổi thử về bản v2, chạy lại `python3 -m lab10.grade --incident Sx` và lệnh 7 | Lệnh 7 vẫn `ĐỦ THÀNH PHẦN` |
| HOÀNG | Đẩy bài lần cuối, gửi link repo cho team chấm ([README mục 6](README.md#6-nộp-gì-và-khi-nào)) | Push thành công |
| **Mỗi người** | Viết mục cá nhân trong `TEAM.md` (đổi tiêu đề thành `## HoVaTen-MSSV`: phần việc, đóng góp, bằng chứng là mã commit/`runs/<mã>`, exit ticket) và nộp link repo trên LMS ([`SUBMISSION.md`](SUBMISSION.md)) | Mục cá nhân + link LMS |

**Xong khi:** lệnh 7 không báo mục phiếu nào còn nguyên mẫu và in `ĐỦ THÀNH PHẦN`; cả ba thành viên đã nộp link trên LMS.
