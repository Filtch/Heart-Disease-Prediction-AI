import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import sys

#Optimized by Zvalsky

def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Input harus ≥ {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Input harus ≤ {max_val}")
                continue
            return value
        except ValueError:
            print("Input tidak valid! Masukkan angka bulat.")


def input_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Input harus ≥ {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Input harus ≤ {max_val}")
                continue
            return value
        except ValueError:
            print("Input tidak valid! Masukkan angka.")


def input_choice(prompt, choices: dict):
    choices_lower = {k.lower(): v for k, v in choices.items()}
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in choices_lower:
            return choices_lower[user_input]
        print("Input salah! Pilihan valid:", ", ".join(choices.keys()))



try:
    data = pd.read_csv("heart.csv")
except FileNotFoundError:
    print("❌ File heart.csv tidak ditemukan!")
    sys.exit()

if data.empty:
    print("❌ Dataset kosong!")
    sys.exit()



X = data.drop("output", axis=1)
y = data["output"]

if X.shape[0] == 0:
    print("❌ Tidak ada data setelah pemisahan fitur!")
    sys.exit()



scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



model = RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    random_state=42
)
model.fit(X_train, y_train)



def input_pasien():
    print("\n=== INPUT DATA PASIEN ===")

    return {
        "age": input_int("Umur: ", 1),
        "sex": input_choice(
            "Jenis kelamin (laki-laki / perempuan): ",
            {"laki-laki": 1, "perempuan": 0}
        ),
        "cp": input_choice(
            "Tipe nyeri dada (typical / atypical / non-anginal / asymptomatic): ",
            {
                "typical": 0,
                "atypical": 1,
                "non-anginal": 2,
                "asymptomatic": 3
            }
        ),
        "trestbps": input_int("Tekanan darah: "),
        "chol": input_int("Kolesterol: "),
        "fbs": input_choice(
            "Gula darah puasa tinggi? (ya / tidak): ",
            {"ya": 1, "tidak": 0}
        ),
        "restecg": input_choice(
            "Hasil ECG (normal / abnormal): ",
            {"normal": 0, "abnormal": 1}
        ),
        "thalach": input_int("Detak jantung maksimum: "),
        "exang": input_choice(
            "Nyeri saat olahraga? (ya / tidak): ",
            {"ya": 1, "tidak": 0}
        ),
        "oldpeak": input_float("Depresi ST: "),
        "slope": input_choice(
            "Kemiringan ST (upsloping / flat / downsloping): ",
            {
                "upsloping": 0,
                "flat": 1,
                "downsloping": 2
            }
        ),
        "ca": input_int("Jumlah pembuluh darah (0–4): ", 0, 4),
        "thal": input_choice(
            "Thalassemia (normal / fixed defect / reversible defect): ",
            {
                "normal": 1,
                "fixed defect": 2,
                "reversible defect": 3
            }
        )
    }



pasien = input_pasien()

X_input = scaler.transform([list(pasien.values())])
prob = model.predict_proba(X_input)[0][1]

print("\n=== HASIL PREDIKSI ===")

if prob < 0.5:
    print("✅ RISIKO RENDAH penyakit jantung")
elif prob < 0.75:
    print("⚠️ RISIKO SEDANG (perlu pemeriksaan lanjutan)")
else:
    print("🚨 RISIKO TINGGI penyakit jantung")

print(f"Confidence model: {prob * 100:.2f}%")
print("\n⚠️ Catatan: Ini adalah alat skrining awal, bukan diagnosis medis.")
