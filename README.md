# TextToAudio

**TextToAudio** is a Python program that converts a book’s text into audio files. It also allows you to specify the beginning of each chapter so that the program can generate separate audio files for each chapter.  

## Features

- Converts a full book (text file) into audio.
- Splits audio by chapters based on the starting text of each chapter.
- Saves audio files in a dedicated folder.
- Adjustable voice and speech rate using `pyttsx3`.

## Requirements

- Python 3.x  
- [pyttsx3](https://pypi.org/project/pyttsx3/)  
  Install with:
  ```bash
  pip install pyttsx3
  ```

## Usage

Run the program from the command line:

```bash
python3 TextToAudio.py book.txt starts.txt
```

- `book.txt` – a text file containing the full book.  
- `starts.txt` – a text file listing the beginning of each chapter (one per line).  

The program will:

1. Read the book and chapter start points.
2. Split the book by chapters.
3. Generate audio files for each chapter.
4. Save the audio files in an `audio_chapters` folder.

## Output

- The audio files are saved as WAV files by default:  
```
audio_chapters/chapter_1.wav
audio_chapters/chapter_2.wav
...
```

- You can convert them to MP3 using a tool like `pydub` if desired.

## Example

```bash
python3 TextToAudio.py my_book.txt chapter_starts.txt
```

After running, the folder `audio_chapters` will contain separate audio files for each chapter.
