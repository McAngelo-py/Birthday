from pathlib import Path
import base64

html_path = Path('c:/Users/Admin/Desktop/Happybirthday/birthday-cake.html')
mp3_path = Path('c:/Users/Admin/Desktop/Happybirthday/song/VoiceAudio.mp3')
html = html_path.read_text(encoding='utf-8')
old = 'src="song/VoiceAudio.mp3" type="audio/mpeg"'
if old not in html:
    old = 'src="song/VoiceAudio.mp3"'
    if old not in html:
        raise SystemExit('Old audio tag not found')

b64 = base64.b64encode(mp3_path.read_bytes()).decode('ascii')
data_uri = 'data:audio/mpeg;base64,' + b64
new = 'src="' + data_uri + '" type="audio/mpeg"'
html = html.replace(old, new, 1)
html_path.write_text(html, encoding='utf-8')
print('Embedded audio length:', len(b64))
