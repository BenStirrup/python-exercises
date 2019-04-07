import os
import hashlib

def find_duplicate_files(starting_path):
    """ Return duplicates files as a list of tuples: (duplicate, original)

    Assumptions:
    1. We assume the file which was modified last is the duplicate
    2. Each file is duplicated at most once
    3. Two files with the same content are duplicates
    4. Two different files wont have the same hash
    """
    duplicates = []
    seen_files = dict()
    stack = [starting_path]

    while stack:
        current_path = stack.pop()

        # If current path is a directory
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        # Else current path is a file
        else:
            # Get the file's hash
            file_hash = sample_hash_file(current_path)

            # Get the file's last edited time
            current_last_edited_time = os.path.getmtime(current_path)

            # If file content seen previously
            if file_hash in seen_files:
                existing_last_edited_time, existing_path = seen_files[file_hash]

                # If current file is the last one to have been modified
                if current_last_edited_time > existing_last_edited_time:
                    duplicates.append((current_path, existing_path))

                # Else the already seen file is the last one to have been modified
                else:
                    duplicates.append((existing_path, current_path))
                    # Update already seen files with the new file's info
                    seen_files[file_hash] = (current_last_edited_time, current_path)

            else:
                seen_files[file_hash] = (current_last_edited_time, current_path)


    return duplicates

def sample_hash_file(path):
    num_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(path)
    hasher = hashlib.sha512()

    with open(path, 'rb') as file:
        # If the file is too short to take 3 samples, hash the entire file
        if total_bytes < num_bytes_to_read_per_sample * 3:
            hasher.update(file.read())
        else:
            num_bytes_between_samples = (
                (total_bytes - num_bytes_to_read_per_sample * 3) / 2
            )

            # Read first, middle, and last bytes
            for offset_multiplier in range(0, 3):
                start_of_sample = (
                    offset_multiplier
                    * (num_bytes_to_read_per_sample + num_bytes_between_samples)
                )
                file.seek(start_of_sample)
                sample = file.read(num_bytes_to_read_per_sample)
                hasher.update(sample)

    return hasher.hexdigest()