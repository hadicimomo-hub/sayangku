from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Halaman 1: Kata-kata Romantis
@app.route('/')
def home():
    return render_template('index.html')

# Halaman 2: Teka-teki
@app.route('/riddle', methods=['GET', 'POST'])
def riddle():
    error = None
    if request.method == 'POST':
        # Jawaban teka-teki diubah ke huruf kecil semua agar tidak case-sensitive
        jawaban = request.form.get('jawaban').lower().strip()
        
        # Ganti 'cinta' dengan jawaban teka-teki rahasia kamu
        if jawaban == 'cinta' or jawaban == 'cinta kita':
            return redirect(url_for('surprise'))
        else:
            error = 'Jawabannya kurang tepat sayang, coba lagi ya! 🤭'
            
    return render_template('riddle.html', error=error)

# Halaman 3: Ucapan & Foto
@app.route('/surprise')
def surprise():
    return render_template('surprise.html')

if __name__ == '__main__':
    app.run(debug=True)