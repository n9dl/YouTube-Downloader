import os
import glob
import time
from flask import Flask, request, jsonify, render_template, send_file
import yt_dlp

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'


os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def cleanup_old_files():
    """حذف الملفات المؤقتة اللي مر عليها أكثر من ساعة لتوفير المساحة"""
    for f in glob.glob(os.path.join(DOWNLOAD_FOLDER, '*')):
        if os.path.getmtime(f) < time.time() - 3600:
            try:
                os.remove(f)
            except:
                pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    cleanup_old_files()
    
    url = request.form.get('video_url')
    quality = request.form.get('quality')

    if not url:
        return jsonify({"error": "الرجاء إدخال الرابط"}), 400


    if quality == 'audio':
        format_opt = 'bestaudio/best'
        postprocessors = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
    elif quality == 'low':
        format_opt = 'worst[ext=mp4]'
        postprocessors = []
    else:

        format_opt = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        postprocessors = []

    ydl_opts = {
        'format': format_opt,
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'quiet': True,
        'postprocessors': postprocessors
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            

            if quality == 'audio':
                filename = filename.rsplit('.', 1)[0] + '.mp3'
                
            return jsonify({
                "success": True, 
                "title": info.get('title'), 
                "filename": os.path.basename(filename)
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/serve/<filename>')
def serve(filename):
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000)