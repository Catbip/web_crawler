import os


def create_project_dir(directory):
    """
    Creates a new directory for each website you crawl.
    """
    if not os.path.exists(directory):
        print('Creating project {}'.format(directory))
        os.makedirs(directory)


def create_data_files(project_name, base_url):
    """
    Create queue and crawled files (if not created).
    """
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    """
    Write new data to file.
    """
    f = open(path, 'w')
    f.write(data)
    f.close()


def file_to_set(file_name):
    """
    Read file and convert each line to set items.
    """
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(set_name, file_name):
    """
    Add each item in a set as a new line in a file.
    """
    with open(file_name, "w") as f:
        for l in sorted(set_name):
            f.write(l + "\n")
