
from sympy import symbols, expand, simplify
x = symbols('x')
def get_lagrange_formula(X, Y):
    n = len(X)
    L = 0
    for j in range(n):
        basis = 1
        for i in range(n):
            if i != j:
                basis *= (x - X[i]) / (X[j] - X[i])
        L += Y[j] * basis
    return simplify(expand(L))

X_pts = list(map(float, input("Введите координаты X: ").split()))
Y_pts = list(map(float, input("Введите координаты Y: ").split()))

if len(X_pts) != len(Y_pts):
    print("Ошибка: количество X и Y должно совпадать!")
elif len(set(X_pts)) != len(X_pts):
    print("Ошибка: координаты X не должны повторяться!")
elif len(X_pts) == 0:
    print("Ошибка: необходимо ввести хотя бы одну точку!")
else:
   
    X_target = float(input("Введите точку, для которой решать: "))
   
    formula = get_lagrange_formula(X_pts, Y_pts)
    print(f"\nФормула полинома: L(x) = {formula}")
  
    result_numeric = formula.subs(x, X_target)
    print(f"Значение полинома в точке x = {X_target} равно: {result_numeric}")
