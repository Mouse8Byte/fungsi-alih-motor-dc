# README - Analisis Motor DC dengan Transformasi Laplace

## 1. Deskripsi Project
Project ini bertujuan untuk menganalisis model matematika dari motor DC, melakukan transformasi Laplace, dan menentukan fungsi alih hubungan antara kecepatan sudut (\( \omega \)) terhadap tegangan (\( V \)). Implementasi dilakukan menggunakan Python dengan library SymPy untuk perhitungan simbolik.

## 2. Model Matematika
Model matematika motor DC terdiri dari dua persamaan diferensial yang merepresentasikan sistem listrik dan mekanik:

- **Persamaan Listrik:**
  \[ L \frac{dI}{dt} + R I = V - K \omega \]

- **Persamaan Mekanik:**
  \[ J \frac{d\omega}{dt} + b \omega = K I \]

Implementasi dalam Python:
```python
# Deklarasi variabel simbolik
t = sp.Symbol('t')
L, R, V, K, J, b = sp.symbols('L R V K J b')
I_t, omega_t = sp.Function('I')(t), sp.Function('omega')(t)

# Persamaan diferensial
pers_listrik = L * I_t.diff(t) + R * I_t - V + K * omega_t
pers_mekanik = J * omega_t.diff(t) + b * omega_t - K * I_t
```

## 3. Transformasi Laplace
Dengan menggunakan transformasi Laplace (diasumsikan kondisi awal nol), didapatkan bentuk dalam domain s:

- **Transformasi Laplace Persamaan Listrik:**
  \[ L (s I(s)) + R I(s) = V(s) - K \Omega(s) \]

- **Transformasi Laplace Persamaan Mekanik:**
  \[ J (s \Omega(s)) + b \Omega(s) = K I(s) \]

Implementasi dalam Python:
```python
s, I_s, Omega_s, V_s = sp.symbols('s I_s Omega_s V_s')
laplace_listrik = pers_listrik.subs({I_t.diff(t): s * I_s, I_t: I_s, omega_t: Omega_s, V: V_s})
laplace_mekanik = pers_mekanik.subs({omega_t.diff(t): s * Omega_s, omega_t: Omega_s, I_t: I_s})
```

## 4. Transfer Function
Untuk mendapatkan fungsi alih \( G(s) \), kita menyelesaikan \( I(s) \) dari persamaan mekanik, kemudian menggantikannya dalam persamaan listrik:

- **Fungsi Alih:**
  \[ G(s) = \frac{\Omega(s)}{V(s)} \]

Implementasi dalam Python:
```python
# Menyelesaikan I_s dari persamaan mekanik
I_s_solusi = sp.solve(laplace_mekanik, I_s)[0]

# Substitusi ke persamaan listrik
ganti_I = laplace_listrik.subs(I_s, I_s_solusi)
Omega_s_solusi = sp.solve(ganti_I, Omega_s)[0]

# Fungsi Alih G(s)
G_s = sp.simplify(Omega_s_solusi / V_s)
```

Dengan hasil akhir berupa fungsi alih yang menggambarkan hubungan antara kecepatan sudut dan tegangan input pada motor DC.
