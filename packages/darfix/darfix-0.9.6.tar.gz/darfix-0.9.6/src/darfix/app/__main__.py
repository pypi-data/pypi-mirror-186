import os
import sys
import glob
from pprint import pformat
from ewoks import load_graph
from ewoks import execute_graph as _execute_graph
from darfix.core.process import graph_data_selection


def is_image_file(filename):
    if not os.path.isfile(filename):
        return False
    return all(not filename.endswith(ext) for ext in [".py", ".ows"])


def execute_graph(argv=None, **extra_options):
    import argparse

    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(
        description="Execute a darfix workflow", prog="darfix"
    )
    parser.add_argument("-wf", "--workflow", help="Filename of the workflow", type=str)
    parser.add_argument(
        "-fd",
        "--file_directory",
        help="Directory containing images",
        type=str,
        default=None,
    )
    parser.add_argument(
        "-ff",
        "--first_filename",
        help="Filename to the first file of the stack",
        type=str,
        default=None,
    )
    parser.add_argument(
        "-td",
        "--treated_data",
        help="Directory to save treated data",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--in-disk",
        help="Do not load data into memory",
        dest="in_disk",
        action="store_true",
        default=None,
    )

    args = parser.parse_args(argv[1:])
    if not args.workflow:
        parser.error("Please enter the workflow filename")
    if not (args.file_directory or args.first_filename):
        parser.error("Please enter the file directory or first filename")

    root_dir = args.file_directory
    if args.first_filename:
        filenames = args.first_filename
    else:
        filenames = sorted(
            [x for x in glob.glob(os.path.join(root_dir, "*")) if is_image_file(x)]
        )
    if args.treated_data:
        root_dir = args.treated_data
    in_memory = not args.in_disk

    print("\nLoading workflow", repr(args.workflow), "...")
    graph = load_graph(args.workflow)

    print("Setting workflow inputs parameters ...")
    graph_data_selection(
        graph=graph, filenames=filenames, root_dir=root_dir, in_memory=in_memory
    )

    print("Executing workflow ...")
    results = _execute_graph(graph, **extra_options)
    print("Result of workflow '%s':\n%s" % (args.workflow, pformat(results)))
    print("Finished\n")

    return results


def main(argv=None):
    execute_graph(argv=argv)


if __name__ == "__main__":
    sys.exit(main())
