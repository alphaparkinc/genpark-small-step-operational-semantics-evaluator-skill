class OperationalSemanticsEvaluator:
    """Small-step operational semantics transition engine."""
    def step_eval(self, expr: dict, env: dict) -> dict:
        op = expr.get("op")
        left = expr.get("left")
        right = expr.get("right")

        val_l = env.get(left, left) if isinstance(left, str) else left
        val_r = env.get(right, right) if isinstance(right, str) else right

        if op == "+":
            ans = val_l + val_r
        elif op == "*":
            ans = val_l * val_r
        else:
            ans = val_l

        return {
            "initial_expr": expr,
            "reduced_value": ans,
            "env_snapshot": env
        }
