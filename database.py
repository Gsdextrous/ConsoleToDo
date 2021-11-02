import pickle


def save_progress_and_quit(filename_source, data_source, do_exit):
    for i in range(len(filename_source)):
        with open(filename_source[i], 'wb') as f:
            pickle.dump(data_source[i], f)
    if do_exit:
        exit()


def load_progress(filename):
    global events
    with open(filename, 'rb') as f:
        events = pickle.load(f)


events = []

load_progress('events.pickle')

