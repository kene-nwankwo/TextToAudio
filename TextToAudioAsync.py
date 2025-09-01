import multiprocessing
import sys
import pyttsx3
import os
from multiprocessing import Pool


def generate_audio(args):
    output_folder, input_text, chapter_number = args
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200)

    filename = os.path.join(output_folder, f'chapter_{str(chapter_number).zfill(3)}.wav')
    engine.save_to_file(input_text, filename)
    engine.runAndWait()
    print(f"Saved audio to {filename}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python TextToAudio.py <book_file_path> <starts_file_path>")
        sys.exit(1)

    book_file_path = sys.argv[1]
    starts_file_path = sys.argv[2]

    with open(book_file_path, 'r', encoding='utf-8') as f:
        book = f.read()
    with open(starts_file_path, 'r', encoding='utf-8') as f:
        start_lines = [line.strip() for line in f]

    chapters = []
    start_lines = start_lines[::-1]
    end_index = len(book) - 1

    for line in start_lines:
        start_index = book.find(line)
        new_chapter = book[start_index:end_index].strip()
        end_index = start_index
        chapters.append(new_chapter)

    chapters = chapters[::-1]

    output_folder = book_file_path + "_audio_chapters"
    os.makedirs(output_folder, exist_ok=True)

    print("Generating Audio Files...")
    maxCores = multiprocessing.cpu_count()

    with Pool(processes=maxCores) as pool:  # adjust number of workers
    # with Pool(processes=4) as pool:  # adjust number of workers
        pool.map(generate_audio, [(output_folder, c, i + 1) for i, c in enumerate(chapters)])

    print("Done.")


if __name__ == "__main__":
    main()
