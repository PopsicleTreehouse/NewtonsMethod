from sympy import symbols, Derivative, plot, Function, RootOf, solve
import sympy

x = symbols("x")
b = symbols("b")


def get_tangent(f: Function, x_val: int, y_val: int) -> Function:
    '''Returns a function tangent to the provided function at the provided point'''
    deriv = Derivative(f, x).doit()
    slope = deriv.evalf(subs={x: x_val})
    b_val = solve(slope * x_val + b - y_val, b)[0]
    tangent = slope * x + b_val
    return tangent


def show_approx(line: Function, guess_x: int, iterations=3) -> int:
    '''Displays and prints the approximated root of the given function'''
    root = guess_x
    lines = []
    for _ in range(iterations):
        y_root = line.evalf(subs={x: root})
        tangent = get_tangent(line, root, y_root)
        root = solve(tangent, x)[0]
        lines.append(tangent)
    dct = {'function': line, 'range': [-1000, 1000]}
    plot_iterations(dct, lines)
    return solve(lines[-1], x)[0]


def plot_iterations(parent: dict, lines: list) -> None:
    '''Displays all of the provided functions'''
    parent_line = parent['function']
    ylim = parent['range']
    p1 = plot(parent_line, show=False, ylim=ylim)
    for line in lines:
        p = plot(line, show=False)
        p1.append(p[0])
    p1.show()


if __name__ == "__main__":
    parabola = x ** 3 - 2 * x - 20
    guess_x = 5
    approximation = show_approx(parabola, guess_x, iterations=4)
    actual = RootOf(parabola, 0).evalf()
    print("Approximation: " + str(approximation))
    print("Actual: " + str(actual))
