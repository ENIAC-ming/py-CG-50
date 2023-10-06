import math


def main():
    formulas = {
        1: {"formula": "v_t = v_0 + a*t", "variables": ["v_t", "v_0", "a", "t"]},
        2: {"formula": "x = (v_0 + v_t) / 2", "variables": ["x", "v_0", "v_t"]},
        3: {"formula": "x = v_0*t + 0.5*a*t^2", "variables": ["x", "v_0", "t", "a"]},
        4: {"formula": "v_t^2 - v_0^2 = 2*a*x", "variables": ["v_t", "v_0", "a", "x"]},
    }

    print("请选择一个公式：")
    for i in range(1, 5):
        print("{}. {}".format(i, formulas[i]["formula"]))

    formula_choice = int(input("输入公式序号："))
    chosen_formula = formulas[formula_choice]

    print("请选择一个未知变量：")
    for i, var in enumerate(chosen_formula["variables"]):
        print("{}. {}".format(i + 1, var))

    unknown_var_index = int(input("输入未知变量序号：")) - 1
    unknown_var = chosen_formula["variables"].pop(unknown_var_index)

    known_values = {}
    for var in chosen_formula["variables"]:
        known_values[var] = float(input("请输入 {} 的值：".format(var)))

    if formula_choice == 1:
        known_values[unknown_var] = solve_formula1(known_values)
    elif formula_choice == 2:
        known_values[unknown_var] = solve_formula2(known_values)
    elif formula_choice == 3:
        known_values[unknown_var] = solve_formula3(known_values)
    elif formula_choice == 4:
        known_values[unknown_var] = solve_formula4(known_values)

    print("{} 的值是 {}".format(unknown_var, known_values[unknown_var]))


def solve_formula1(values):
    if "v_t" not in values:
        return values["v_0"] + values["a"] * values["t"]
    elif "v_0" not in values:
        return values["v_t"] - values["a"] * values["t"]
    elif "a" not in values:
        return (values["v_t"] - values["v_0"]) / (values["t"])
    else:  # 't' not in values
        return (values["v_t"] - values["v_0"]) / (values["a"])


def solve_formula2(values):
    if "x" not in values:
        return (values["v_0"] + values["v_t"]) / 2
    elif "v_0" not in values:
        return 2 * values["x"] - values["v_t"]
    else:  # 'v_t' not in values
        return 2 * values["x"] - values["v_0"]


def solve_formula3(values):
    if "x" not in values:
        return values["v_0"] * values["t"] + 0.5 * values["a"] * values["t"] ** 2
    elif "v_0" not in values:
        return (values["x"] - 0.5 * values["a"] * values["t"] ** 2) / values["t"]
    elif "a" not in values:
        return (values["x"] - values["v_0"] * values["t"]) / (0.5 * values["t"] ** 2)
    else:  # 't' not in values
        # This is a quadratic equation, we need to use the quadratic formula to solve it
        a = 0.5 * values["a"]
        b = values["v_0"]
        c = -values["x"]
        t1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        t2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

        # We assume that time is always positive, so we choose the positive root
        return t1 if t1 > 0 else t2


def solve_formula4(values):
    if "v_t" not in values:
        return math.sqrt(values["v_0"] ** 2 + 2 * values["a"] * values["x"])
    elif "v_0" not in values:
        return math.sqrt(values["v_t"] ** 2 - 2 * values["a"] * values["x"])
    elif "a" not in values:
        return (values["v_t"] ** 2 - values["v_0"] ** 2) / (2 * values["x"])
    else:  # 'x' not in values
        return (values["v_t"] ** 2 - values["v_0"] ** 2) / (2 * values["a"])


if __name__ == "__main__":
    main()
