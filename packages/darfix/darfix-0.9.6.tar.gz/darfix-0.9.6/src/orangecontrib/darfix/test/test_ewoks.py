import unittest
import shutil
import tempfile
from ewoks import load_graph
from darfix.core.process import graph_data_selection
from darfix.app.__main__ import execute_graph

try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources


class EwoksTest(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.tmpdir)

    def test_darfix_example2(self):
        from orangecontrib.darfix import tutorials

        with resources.path(tutorials, "darfix_example2.ows") as filename:
            graph = load_graph(str(filename))

            with resources.path(tutorials, "strain_0000.edf") as image0:
                with resources.path(tutorials, "strain_0001.edf") as image1:
                    filenames = [str(image0), str(image1)]
                    graph_data_selection(
                        graph=graph,
                        filenames=filenames,
                        root_dir=str(self.tmpdir),
                        in_memory=True,
                    )
                    results = graph.execute(output_tasks=True)
                    for node_id, task in results.items():
                        assert task.succeeded, node_id

    def test_darfix_example2_cli(self):
        from orangecontrib.darfix import tutorials

        with resources.path(tutorials, "darfix_example2.ows") as filename:
            argv = [
                None,
                "-wf",
                str(filename),
                "-fd",
                str(filename.parent),
                "-td",
                str(self.tmpdir),
            ]
            results = execute_graph(argv=argv, output_tasks=True)
            for node_id, task in results.items():
                assert task.succeeded, node_id
