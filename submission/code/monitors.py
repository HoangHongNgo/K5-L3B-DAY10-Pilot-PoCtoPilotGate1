"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def duplicate_refund_rate(trials):
    """Kỹ thuật (thẻ S5): tỉ lệ ticket mà trợ lý định hoàn cho một đơn đã có khoản hoàn trong sổ cái
    (trợ lý hoặc CSKH hoàn tay). Đọc sự kiện guard_cumulative_refund do cổng ghi."""
    hit = sum(any(e.get("type") == "guard" and e.get("kind") == "guard_cumulative_refund"
                  for e in t["events"]) for t in trials)
    return hit / max(1, len(trials))


def worst_warehouse_escalation_rate(trials):
    """Kinh doanh (thẻ S5): tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người ở kho tệ nhất
    (chỉ tính kho có từ 3 ticket trở lên). Kho gần 1.0 là kho tự động hoá không bớt được công người."""
    by = {}
    for t in trials:
        by.setdefault(t.get("warehouse") or "?", []).append(t["status"] == "escalated")
    rates = [sum(v) / len(v) for v in by.values() if len(v) >= 3]
    return max(rates) if rates else 0.0


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "duplicate_refund_rate": duplicate_refund_rate,
    "worst_warehouse_escalation_rate": worst_warehouse_escalation_rate,
}
STARTER_MONITORS = ("escalation_rate",)
