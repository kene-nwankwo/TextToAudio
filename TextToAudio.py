import sys
import pyttsx3
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: python TextToAudio.py <book_file_path> <starts_file_path>")
        sys.exit(1)
        
    book_file_path = sys.argv[1]
    starts_file_path = sys.argv[2]
    try:
        with open(book_file_path, 'r', encoding='utf-8') as f:
            book = f.read()
        with open(starts_file_path, 'r', encoding='utf-8') as f:
            start_lines = [line.strip() for line in f]

        #print(f"Parsed lines: {lines}")
        #print(f"Text content: {text_content}")
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    chapters = []

    # start_lines = reversed start_lines
    start_lines = start_lines[::-1]  # Reverse the list to process from last to first

    end_index = len(book)-1
    for line in start_lines:
    
        start_index = book.find(line)

        new_chapter = book[start_index:end_index].strip()

        end_index = start_index
        chapters.append(new_chapter)

    # chapters = reversed chapters
    chapters = chapters[::-1]  # Reverse the list to process from last to first

    # for i, chapter in enumerate(chapters):
    #     print(f"Chapter {i + 1}: {chapter} \n")

    # Instantiate the engine once at the module level
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200)  # default ~200

    output_folder = book_file_path + "audio_chapters"
    os.makedirs(output_folder, exist_ok=True)

    for i, chapter in enumerate(chapters):
        generate_audio(output_folder, engine, chapter, i + 1)

    print("Generating Audio Files")
    engine.runAndWait()
    print("Done")


def generate_audio(output_folder, engine, input_text, chapter_number):
    filename = os.path.join(output_folder, f'chapter_{str(chapter_number).zfill(3)}.wav')
    engine.save_to_file(input_text, filename)
    print(f"Saved audio to {filename}")

main()