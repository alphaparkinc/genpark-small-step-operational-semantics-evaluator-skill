from client import OperationalSemanticsEvaluator

def main():
    print("=== Small-Step Operational Semantics ===")
    evaluator = OperationalSemanticsEvaluator()
    expr = {"op": "+", "left": "x", "right": 10}
    env = {"x": 15}

    res = evaluator.step_eval(expr, env)
    print("Evaluated Result:", res)
    assert res["reduced_value"] == 25

    print("Operational Semantics Evaluator verified successfully!")

if __name__ == "__main__":
    main()
