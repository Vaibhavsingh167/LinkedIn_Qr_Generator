from flask import Flask, render_template, request, flash, redirect, url_for
import qrcode
import io
import base64
from urllib.parse import urlparse

app = Flask(__name__)
app.secret_key = 'replace-this-with-a-secure-random-key'

ALLOWED_DOMAIN = 'linkedin.com'


def is_valid_linkedin_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ('http', 'https'):
            return False
        hostname = parsed.netloc.lower()
        # allow www.linkedin.com, linkedin.com, *.linkedin.com
        if hostname == ALLOWED_DOMAIN or hostname.endswith('.' + ALLOWED_DOMAIN):
            return True
        return False
    except Exception:
        return False


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('linkedin_url', '').strip()
        if not is_valid_linkedin_url(url):
            flash('Please enter a valid LinkedIn profile URL.', 'error')
            return redirect(url_for('index'))

        # generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # encode to base64 for embedding
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        img_b64 = base64.b64encode(buffer.read()).decode('utf-8')
        data_uri = f"data:image/png;base64,{img_b64}"

        return render_template('result.html', qr_data=data_uri)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)