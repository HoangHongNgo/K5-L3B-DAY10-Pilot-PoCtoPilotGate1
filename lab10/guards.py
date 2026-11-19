"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Vòng 1 của bàn Pilot: 3 cổng (hoàn tiền theo DB, lỗi hãng theo DB, không gửi PII cho hãng).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict

# Các trường không được đưa cho bên thứ ba, gộp với config legal.
_PII_DEFAULT = {"customer_note", "customer_id", "phone", "address"}


def _db_facts(ctx, action):
    """Số liệu từ nguồn sự thật (DB), không đọc chữ của khách."""
    order = ctx.tools.lookup_order(action["order_id"])
    if not order:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    return order, parcel, delay, policy


def pre_guard(ctx):
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action["tool"]

    # Cổng 1: tiền hoàn không vượt quyền lợi tính từ DB; vượt thì chuyển người duyệt
    if tool == "issue_refund" and not action.get("approval_id"):
        facts = _db_facts(ctx, action)
        if facts is None:
            return Verdict.escalate("không tra được đơn trong DB")
        order, parcel, delay, policy = facts
        if policy is None:
            return Verdict.escalate("không có chính sách hiệu lực")
        owed = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if action["amount_vnd"] > owed:
            ctx.log("guard_refund_over_entitlement",
                    asked=action["amount_vnd"], owed=owed, db_delay=delay)
            return Verdict.escalate(
                f"hoàn {action['amount_vnd']}đ vượt quyền lợi {owed}đ theo DB")

        # Cổng 4 (vòng 2, thẻ S5): tính quyền lợi TÍCH LŨY. Sổ cái đã có khoản hoàn cho đơn này
        # (trợ lý hoặc CSKH hoàn tay) thì chỉ được hoàn phần còn lại; hết thì chuyển người kiểm.
        paid = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=action["order_id"]))
        if paid:
            remaining = owed - paid
            ctx.log("guard_cumulative_refund", order_id=action["order_id"],
                    owed=owed, already=paid, asked=action["amount_vnd"])
            if remaining <= 0:
                return Verdict.escalate(
                    f"đơn {action['order_id']} đã hoàn {paid}đ, bằng hoặc hơn quyền lợi {owed}đ, chuyển người kiểm")
            if action["amount_vnd"] > remaining:
                return Verdict.modify(f"chỉ hoàn phần còn lại {remaining}đ", amount_vnd=remaining)

    # Cổng 2: chỉ ghi lỗi hãng khi DB xác nhận trễ thật, có nguyên nhân hợp lệ
    if tool == "file_carrier_fault":
        facts = _db_facts(ctx, action)
        if facts is None:
            return Verdict.deny("không tra được đơn trong DB")
        order, parcel, delay, policy = facts
        if policy is None or not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("DB không xác nhận lỗi hãng (số ngày hoặc nguyên nhân)")
        if action.get("delay_days") != delay:
            return Verdict.modify("ghi theo số ngày DB", delay_days=delay)

    # Cổng 3: không gửi dữ liệu cá nhân cho hãng
    if tool == "notify_carrier":
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        legal_blocked = set(
            ctx.gates.get("legal", {}).get("pii_fields_blocked_to_third_party", []))
        payload = action.get("payload", {})
        if policy and policy.get("carrier_notice_fields"):
            # chỉ gửi đúng trường chính sách cho phép, và config pháp lý có quyền chặn thêm
            allowed = set(policy["carrier_notice_fields"]) - legal_blocked
            clean = {k: v for k, v in payload.items() if k in allowed}
        else:
            clean = {k: v for k, v in payload.items() if k not in _PII_DEFAULT | legal_blocked}
        if clean != payload:
            return Verdict.modify("bỏ trường cá nhân khỏi tin gửi hãng", payload=clean)

    return Verdict.allow()
