import os

def save_to_file(filename):
    f = open(filename, "w")
    f.write("")
    f.close()

def extract_sentences_from_chapter(chapter):
    target_file = str('%03d' % chapter) + ".txt"
    file = open(target_file, "r", encoding="utf8").read()

    return [x for x in (file.split("\n\n")) if x]

def format(text, count):
    if text == "\n":
        return
    verbose_out = "<" + str('%03d' % count) + "> '" + text.strip() + "'\n"
    out = text.strip()
    return out

def main(chapter):
    list_of_sentences = extract_sentences_from_chapter(chapter)
    count = 0
    while(count < len(list_of_sentences)):
        current_text = format(list_of_sentences[count], count)
        fname = "c" + str('%03d' % chapter) + '-' + str('%03d' % count) + '.wav'
        tts_handler(text=current_text, filename=fname)
        print(fname)
        count += 1
    save_to_file(str('%03d' % chapter) + ".DONE")

def tts_handler(text, filename):
    path = './' + filename
    if os.path.isfile(path):
        print(path + " already exists")
        return
    from TTS.api import TTS

    model = 'tts_models/en/jenny/jenny'
    tts = TTS(model_name=model)
    tts.tts_to_file(text=text, file_path=path)


def multi(chapters):
    import multiprocessing
    # Create a list of values from 0 to chapters
    values = list(range(chapters))

    # Create a multiprocessing pool with a specified number of processes
    # You can adjust the number of processes as needed
    pool = multiprocessing.Pool(processes=3)

    # Use the pool to execute the main function with each value
    pool.map(main, values)

    # Close the pool and wait for the processes to finish
    pool.close()
    pool.join()