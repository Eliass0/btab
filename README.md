# Book to Audiobook Converter
## Usage and Setup
> This setup guide is for WSL (Debian)
1. Clone repository
2. Setup envrioment
```bash
sudo apt install python3
sudo apt install python3-venv
sudo apt install python3-pip
pip install buildtools wheel pip -U
python3 -m venv .
source bin/activate
pip install tts
```
3. Convert your Book to txt files (calibre is recommended)
4. Split the chapters into their own files in this format:
```
 * 000.txt
 * 001.txt
 * 002.txt
```
Note that currently only 1000 chapters are supported. To change this edit the reader.py, visitor.py and watcher.py file and replace '%03d' with the respective amount of digits used.
5. For progress reports first run the visitor.py file.
```bash
python3 -i visitor.py
```
```python
multi(number_of_chapters)
```
6. Now set up the watcher by adding your WEBHOOK_URL (from Discord). Alternatively change post_message() to log_message() in main() to only log to console
7. Run the reader.py
```bash
python3 -i reader.py
```
```python
multi(number_of_chapters)
```
8. Run the watcher.py, this is doesn't have to be in interactive mode, so launch however you want.
9. After all this you have a bunch of generated sentenced, to merge do the following
```bash
apt install sox
ls c000*.wav | sed -z -e 's/\n/ /g' | sed -e 's/^/sox /g' | sed -e 's/$/c000-merged.wav/g' | sh
ls c001*.wav | sed -z -e 's/\n/ /g' | sed -e 's/^/sox /g' | sed -e 's/$/c001-merged.wav/g' | sh
ls c002*.wav | sed -z -e 's/\n/ /g' | sed -e 's/^/sox /g' | sed -e 's/$/c002-merged.wav/g' | sh
ls c003*.wav | sed -z -e 's/\n/ /g' | sed -e 's/^/sox /g' | sed -e 's/$/c003-merged.wav/g' | sh
```
Note that the chapter is mentioned twice, at ls and at the last sed

10. You know have your whole chapter in a wav file. You might notice it's quite big, so I recommend the following
```bash
apt install fmmpeg
ffmpeg -i c000-merged.wav -c:a mp3 c000-merged.mp3
```
This makes the file 10-12x smaller, while not really sacraficing quality.

11. For a final touch I recommend using Mp3Tag or other programs to add album, author and images to the mp3 files.