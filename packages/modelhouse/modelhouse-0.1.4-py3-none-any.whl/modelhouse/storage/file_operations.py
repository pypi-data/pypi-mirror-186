import os

from cloudfiles import CloudFiles

def get_files_and_contents(path):
    cf = CloudFiles(path)
    files = cf.list(flat=False)
    read_files = cf.get(files)

    files_and_contents = []
    for read_file in read_files:
        file_relpath = read_file['path']
        if read_file['error'] is not None:
            raise Exception("Error while reading {}: {}".format(
                os.path.join(path, file_relpath), read_file['error']))

        files_and_contents.append((file_relpath, read_file['content']))
    return files_and_contents

def put_files_and_contents(path, files_and_contents):
    if path.startswith("/"):
        path = f"file://{path}"
    cf = CloudFiles(path)
    cf.puts(
        files_and_contents,
        content_type='application/octet-stream',
        compress=None,
        cache_control='no-cache'
    )
