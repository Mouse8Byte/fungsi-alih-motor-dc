# Aslam Azharan Wade Laode | 235150307111029
import sympy as sp

# Deklarasi variabel simbolik
t, s = sp.symbols('t s')
L, R, V, K, J, b = sp.symbols('L R V K J b')  # Parameter motor
I_t, omega_t = sp.Function('I')(t), sp.Function('omega')(t)

# Persamaan diferensial
pers_listrik = L * I_t.diff(t) + R * I_t - V + K * omega_t
pers_mekanik = J * omega_t.diff(t) + b * omega_t - K * I_t

# Transformasi Laplace (diasumsikan kondisi awal nol)
I_s, Omega_s, V_s = sp.symbols('I_s Omega_s V_s')
laplace_listrik = pers_listrik.subs({I_t.diff(t): s * I_s, I_t: I_s, omega_t: Omega_s, V: V_s})
laplace_mekanik = pers_mekanik.subs({omega_t.diff(t): s * Omega_s, omega_t: Omega_s, I_t: I_s})

# Menyelesaikan I_s dari persamaan mekanik
I_s_solusi = sp.solve(laplace_mekanik, I_s)[0]

# Substitusi ke persamaan listrik
ganti_I = laplace_listrik.subs(I_s, I_s_solusi)
Omega_s_solusi = sp.solve(ganti_I, Omega_s)[0]

# Fungsi Alih G(s) = Omega(s) / V(s)
G_s = sp.simplify(Omega_s_solusi / V_s)

# Cetak hasil
print("Model Matematika Motor DC:")
print("Persamaan Listrik:")
sp.pprint(pers_listrik)
print("Persamaan Mekanik:")
sp.pprint(pers_mekanik)

print("\nTransformasi Laplace:")
print("Listrik:")
sp.pprint(laplace_listrik)
print("Mekanik:")
sp.pprint(laplace_mekanik)

print("\nFungsi Alih G(s):")
sp.pprint(G_s)
