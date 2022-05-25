from sympy import symbols, Derivative, plot, Function, RootOf, solve

x = symbols("x")
b = symbols("b")


def get_tangent(f, x_val, y_val):
    deriv = Derivative(f, x).doit()
    slope = deriv.evalf(subs={x: x_val})
    b_val = solve(slope * x_val + b - y_val, b)[0]
    tangent = slope * x + b_val
    return tangent


def show_approx(line: Function, guess_x: int, guess_y: int, iterations=3) -> int:
    root = guess_x
    lines = []
    for _ in range(iterations):
        y_root = line.evalf(subs={x: root})
        tangent = get_tangent(line, root, y_root)
        root = solve(tangent, x)[0]
        lines.append((tangent, (x, root, guess_x + 5)))
    plot_iterations((line, (x, -guess_x - 5, guess_x + 5)), lines)
    return solve(lines[-1][0], x)[0]


def plot_iterations(parent: tuple, lines: list):
    p1 = plot(parent[0], parent[1], show=False)
    for line in lines:
        function = line[0]
        rng = line[1]
        p = plot(function, rng, show=False)
        p1.append(p[0])
    p1.show()


if __name__ == "__main__":
    parabola = x ** 3 - 2 * x - 20
    guess_x = 5
    guess_y = parabola.evalf(subs={x: guess_x})
    approximation = show_approx(parabola, guess_x, guess_y, iterations=4)
    actual = RootOf(parabola, 0).evalf()
    print("Approximation: " + str(approximation))
    print("Actual: " + str(actual))
