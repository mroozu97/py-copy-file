def copy_file(command: str) -> None:
    if command.count(".txt") < 2:
        return
    if command.split(" ")[0] != "cp":
        return

    file1 = command.split(" ")[1]
    file2 = command.split(" ")[2]

    if file1 == file2:
        return

    try:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            read_content = file_in.read()
            file_out.write(read_content)
    except FileNotFoundError:
        print(f"Error: {file1} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
