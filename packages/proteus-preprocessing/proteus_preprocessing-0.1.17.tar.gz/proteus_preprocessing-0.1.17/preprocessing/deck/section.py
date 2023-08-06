import os
import re


def get_includes(input_file_loc, download_func=None, allow_missing_files=tuple(), base_dir=None):
    with open(input_file_loc, "r") as data_file:
        content = data_file.read()
    # recursively finds the include files
    abs_path = os.path.abspath(input_file_loc)
    return find_includes(content, abs_path, download_func, allow_missing_files=allow_missing_files, base_dir=base_dir)


def find_section(input_file_loc, section_header, download_func=None, allow_missing_files=tuple(), base_dir=None):
    file_list = [input_file_loc] + get_includes(
        input_file_loc, download_func, allow_missing_files=allow_missing_files, base_dir=base_dir
    )

    for file_loc in file_list:
        with open(file_loc, "r") as f:
            section = scan_file(f.read(), section_header)
            if section is not None:
                return section.group("content")


def parse_dependency_path(file_absolute_path, dependency):
    """Parse relative dependencies path to absolute ones
    Arguments:
        file_absolute_path {string} -- the absolute file path
        dependency {string} -- the relative path of the dependency
    Returns:
        absolute_dependency {string} -- the absolute path of the dependency
    """
    file_name_expression = re.compile(r"/(?P<file_name>[^/]+\.[^/]+)$")

    # Split directories by folders. Create a list with the folders
    file_name = file_name_expression.search(file_absolute_path).group()
    file_path = file_absolute_path.replace(file_name, "")
    file_path_list = file_path.split("/")

    # Count and remove previous directories: ../
    previous_directories_expression = re.compile(r"(?P<previous_directories>(\.\./)|(\.\.\\))")
    previous_directories = previous_directories_expression.finditer(dependency)
    previous_directories = [
        previous_directory.groupdict().get("previous_directories") for previous_directory in previous_directories
    ]
    number_of_previous_directories = len(previous_directories)
    dependency_name = dependency.replace("../", "").replace("..\\", "")

    # Remove `./` just in case
    dependency_name = dependency_name.replace("./", "")

    # Create absolute path
    list_length = len(file_path_list)
    file_path_list = file_path_list[: list_length - number_of_previous_directories]
    return f"{'/'.join(file_path_list)}/{dependency_name}".replace("\\", "/")


def find_includes(content, filepath, download_func=None, allow_missing_files=tuple(), base_dir=None):
    include_expression_re = re.compile(r"\s*INCLUDE[^\'\/]+'(?P<path>[^']+)'")
    inc_found = include_expression_re.finditer(content)
    includes_list = [inc.groupdict().get("path") for inc in inc_found]
    fixed_includes_list = []
    for include_file_loc in includes_list:
        actual_path = parse_dependency_path(filepath, include_file_loc)
        fixed_includes_list.append(actual_path)

        try:
            if base_dir and not actual_path.startswith(base_dir):
                raise FileNotFoundError(f"File {actual_path} is outside sandboxed base dir {base_dir}")

            if download_func:
                relative_path = actual_path.replace(base_dir, "") if base_dir else remove_tmp_folder(actual_path)
                download_func(relative_path, actual_path)

            with open(actual_path, "r") as include_file:
                content = include_file.read()
        except FileNotFoundError as e:
            relative_path_parent = filepath.replace(base_dir, "") if base_dir else remove_tmp_folder(filepath)
            relative_path_parent = relative_path_parent or filepath
            not_found_file = os.path.realpath(actual_path)

            error_message = (
                f'File "{relative_path_parent}" includes subfile '
                f"{include_file_loc}, but the file was not found. Reason: {str(e)}"
            )

            skip = False
            for skipable_file_rel in allow_missing_files:
                skipable_file = os.path.realpath(skipable_file_rel)

                if (
                    skipable_file == not_found_file
                    or not skipable_file_rel.startswith(os.path.sep)
                    and not_found_file.endswith(skipable_file_rel)
                ):
                    skip = True
                    break

            if skip:
                print(f"{error_message}. skipping because it was explicitly whitelisted.")
                continue
            else:
                raise FileNotFoundError(error_message)

        fixed_includes_list += find_includes(
            content, actual_path, download_func, allow_missing_files=allow_missing_files, base_dir=base_dir
        )

    return fixed_includes_list


def scan_file(content, section_header):
    section_expression_re = re.compile(
        section_header + r"\s+=*(?P<content>[\S\s]*?)(RUNSPEC|GRID|PROPS|REGIONS|SOLUTIONS|SUMMARY|SCHEDULE)\s"
    )
    section_found = section_expression_re.finditer(content)

    section_content = next(section_found)
    if section_content is not None:
        return section_content


def remove_tmp_folder(path):
    # FIXME: this method of obtaining relative paths is hideous
    path_expression_re = re.compile(r"^\/tmp\/tmp[^\/]*(?P<path>.*)$")
    try:
        return next(path_expression_re.finditer(path)).groupdict().get("path")
    except StopIteration:
        return None
