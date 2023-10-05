# Assignment1 (Data Profiling and Data Validation from CSV/Excel Files)

### Project Descrition 
Using Pandas data profiling to generate a data profiling report and using great expectations to validate the same. The data here used as an input file from https://freddiemac.embs.com/. 

### Project Resources

(https://codelabs-preview.appspot.com/?file_id=1t61T-7IzchvC1qUAso0RRaTfmnOdUZSInwzfCeEK8QM#1)

https://freddiemac.embs.com/

### Architecture diagram ###

![image](https://github.com/BigDataIA-Fall2023-Team2/Assignment1/assets/131703516/19a6bf44-b491-4506-8673-5670ae1d30c3)

### Project Flow

The user uploads a csv/excel file from Freddieemac website and specifies what type of file it is - orgigination/monthly. The data will be then profiled using pandas profiling and validated using great expectations (python suite). A datadoc will be generated that will show case the data validation results.

### Code Explaination

There are two important files expectation_suits_builder.py and home.py. The expectation_suits_builder.py is used for generating the great expectation suit and home.py is used for showcasing the validation results of great expectation and generating data profling report of the uploaded excel/csv. Apart from that there is an expectation.json file that we are using that contains all the required expectations in json format. 

***expectation_suits_builder.py***

```
from great_expectations.core.expectation_configuration import ExpectationConfiguration
from great_expectations.data_context import FileDataContext
from great_expectations.core.expectation_configuration import ExpectationConfiguration
import json

with open("expectations.json", "r") as expectations_file:
    expectations = json.load(expectations_file)
    
context = FileDataContext.create(project_root_dir="./.")
datasource = context.sources.add_pandas("pandas_dataframe_datasource")

```
In the above code, we are loading our expectations written in json format from expectation.json and creating a data source 

```
origination_expectations_suite = context.create_expectation_suite("origination_expectations_suite")
with open('origination_columns.txt', 'r') as file:
    column_names = [line.strip() for line in file]
ordered_list_origination_expectation_configuration = ExpectationConfiguration(
    expectation_type="expect_table_columns_to_match_ordered_list",
    kwargs={
        "column_list": column_names
    },
)
```
In the above part, we are checking if the schema is correct or not by checking if the column names mentioned in the data set are in the same order of 

### Repo Structure
    │   │           │   │   ├── cache.py
    │   │           │   │   ├── common.py
    │   │           │   │   ├── compat.py
    │   │           │   │   ├── dataframe.py
    │   │           │   │   ├── imghdr_patch.py
    │   │           │   │   ├── notebook.py
    │   │           │   │   ├── paths.py
    │   │           │   │   ├── progress_bar.py
    │   │           │   │   └── versions.py
    │   │           │   ├── version.py
    │   │           │   └── visualisation
    │   │           │       ├── __init__.py
    │   │           │       ├── __pycache__
    │   │           │       │   ├── __init__.cpython-310.pyc
    │   │           │       │   ├── context.cpython-310.pyc
    │   │           │       │   ├── missing.cpython-310.pyc
    │   │           │       │   ├── plot.cpython-310.pyc
    │   │           │       │   └── utils.cpython-310.pyc
    │   │           │       ├── context.py
    │   │           │       ├── missing.py
    │   │           │       ├── plot.py
    │   │           │       └── utils.py
    │   │           ├── ydata_profiling-4.5.1.dist-info
    │   │           │   ├── INSTALLER
    │   │           │   ├── LICENSE
    │   │           │   ├── METADATA
    │   │           │   ├── RECORD
    │   │           │   ├── REQUESTED
    │   │           │   ├── WHEEL
    │   │           │   ├── entry_points.txt
    │   │           │   └── top_level.txt
    │   │           ├── zipp
    │   │           │   ├── __init__.py
    │   │           │   ├── __pycache__
    │   │           │   │   ├── __init__.cpython-310.pyc
    │   │           │   │   ├── glob.cpython-310.pyc
    │   │           │   │   └── py310compat.cpython-310.pyc
    │   │           │   ├── glob.py
    │   │           │   └── py310compat.py
    │   │           ├── zipp-3.17.0.dist-info
    │   │           │   ├── INSTALLER
    │   │           │   ├── LICENSE
    │   │           │   ├── METADATA
    │   │           │   ├── RECORD
    │   │           │   ├── REQUESTED
    │   │           │   ├── WHEEL
    │   │           │   └── top_level.txt
    │   │           └── zmq
    │   │               ├── __init__.pxd
    │   │               ├── __init__.py
    │   │               ├── __init__.pyi
    │   │               ├── __pycache__
    │   │               │   ├── __init__.cpython-310.pyc
    │   │               │   ├── _future.cpython-310.pyc
    │   │               │   ├── _typing.cpython-310.pyc
    │   │               │   ├── asyncio.cpython-310.pyc
    │   │               │   ├── constants.cpython-310.pyc
    │   │               │   ├── decorators.cpython-310.pyc
    │   │               │   └── error.cpython-310.pyc
    │   │               ├── _future.py
    │   │               ├── _typing.py
    │   │               ├── asyncio.py
    │   │               ├── auth
    │   │               │   ├── __init__.py
    │   │               │   ├── __pycache__
    │   │               │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   ├── asyncio.cpython-310.pyc
    │   │               │   │   ├── base.cpython-310.pyc
    │   │               │   │   ├── certs.cpython-310.pyc
    │   │               │   │   ├── ioloop.cpython-310.pyc
    │   │               │   │   └── thread.cpython-310.pyc
    │   │               │   ├── asyncio.py
    │   │               │   ├── base.py
    │   │               │   ├── certs.py
    │   │               │   ├── ioloop.py
    │   │               │   └── thread.py
    │   │               ├── backend
    │   │               │   ├── __init__.py
    │   │               │   ├── __init__.pyi
    │   │               │   ├── __pycache__
    │   │               │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   └── select.cpython-310.pyc
    │   │               │   ├── cffi
    │   │               │   │   ├── __init__.py
    │   │               │   │   ├── __pycache__
    │   │               │   │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   │   ├── _poll.cpython-310.pyc
    │   │               │   │   │   ├── context.cpython-310.pyc
    │   │               │   │   │   ├── devices.cpython-310.pyc
    │   │               │   │   │   ├── error.cpython-310.pyc
    │   │               │   │   │   ├── message.cpython-310.pyc
    │   │               │   │   │   ├── socket.cpython-310.pyc
    │   │               │   │   │   └── utils.cpython-310.pyc
    │   │               │   │   ├── _cdefs.h
    │   │               │   │   ├── _poll.py
    │   │               │   │   ├── context.py
    │   │               │   │   ├── devices.py
    │   │               │   │   ├── error.py
    │   │               │   │   ├── message.py
    │   │               │   │   ├── socket.py
    │   │               │   │   └── utils.py
    │   │               │   ├── cython
    │   │               │   │   ├── __init__.pxd
    │   │               │   │   ├── __init__.py
    │   │               │   │   ├── __pycache__
    │   │               │   │   │   └── __init__.cpython-310.pyc
    │   │               │   │   ├── _device.cpython-310-x86_64-linux-gnu.so
    │   │               │   │   ├── _poll.cpython-310-x86_64-linux-gnu.so
    │   │               │   │   ├── _proxy_steerable.cpython-310-x86_64-linux-gnu.so
    │   │               │   │   ├── _version.cpython-310-x86_64-linux-gnu.so
    │   │               │   │   ├── checkrc.pxd
    │   │               │   │   ├── constant_enums.pxi
    │   │               │   │   ├── context.cpython-310-x86_64-linux-gnu.so
    │   │               │   │   ├── context.pxd
    │   │               │   │   ├── error.cpython-310-x86_64-linux-gnu.so
    │   │               │   │   ├── libzmq.pxd
    │   │               │   │   ├── message.cpython-310-x86_64-linux-gnu.so
    │   │               │   │   ├── message.pxd
    │   │               │   │   ├── socket.cpython-310-x86_64-linux-gnu.so
    │   │               │   │   ├── socket.pxd
    │   │               │   │   └── utils.cpython-310-x86_64-linux-gnu.so
    │   │               │   └── select.py
    │   │               ├── constants.py
    │   │               ├── decorators.py
    │   │               ├── devices
    │   │               │   ├── __init__.py
    │   │               │   ├── __pycache__
    │   │               │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   ├── basedevice.cpython-310.pyc
    │   │               │   │   ├── monitoredqueue.cpython-310.pyc
    │   │               │   │   ├── monitoredqueuedevice.cpython-310.pyc
    │   │               │   │   ├── proxydevice.cpython-310.pyc
    │   │               │   │   └── proxysteerabledevice.cpython-310.pyc
    │   │               │   ├── basedevice.py
    │   │               │   ├── monitoredqueue.cpython-310-x86_64-linux-gnu.so
    │   │               │   ├── monitoredqueue.pxd
    │   │               │   ├── monitoredqueue.py
    │   │               │   ├── monitoredqueuedevice.py
    │   │               │   ├── proxydevice.py
    │   │               │   └── proxysteerabledevice.py
    │   │               ├── error.py
    │   │               ├── eventloop
    │   │               │   ├── __init__.py
    │   │               │   ├── __pycache__
    │   │               │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   ├── _deprecated.cpython-310.pyc
    │   │               │   │   ├── future.cpython-310.pyc
    │   │               │   │   ├── ioloop.cpython-310.pyc
    │   │               │   │   └── zmqstream.cpython-310.pyc
    │   │               │   ├── _deprecated.py
    │   │               │   ├── future.py
    │   │               │   ├── ioloop.py
    │   │               │   └── zmqstream.py
    │   │               ├── green
    │   │               │   ├── __init__.py
    │   │               │   ├── __pycache__
    │   │               │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   ├── core.cpython-310.pyc
    │   │               │   │   ├── device.cpython-310.pyc
    │   │               │   │   └── poll.cpython-310.pyc
    │   │               │   ├── core.py
    │   │               │   ├── device.py
    │   │               │   ├── eventloop
    │   │               │   │   ├── __init__.py
    │   │               │   │   ├── __pycache__
    │   │               │   │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   │   ├── ioloop.cpython-310.pyc
    │   │               │   │   │   └── zmqstream.cpython-310.pyc
    │   │               │   │   ├── ioloop.py
    │   │               │   │   └── zmqstream.py
    │   │               │   └── poll.py
    │   │               ├── log
    │   │               │   ├── __init__.py
    │   │               │   ├── __main__.py
    │   │               │   ├── __pycache__
    │   │               │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   ├── __main__.cpython-310.pyc
    │   │               │   │   └── handlers.cpython-310.pyc
    │   │               │   └── handlers.py
    │   │               ├── py.typed
    │   │               ├── ssh
    │   │               │   ├── __init__.py
    │   │               │   ├── __pycache__
    │   │               │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   ├── forward.cpython-310.pyc
    │   │               │   │   └── tunnel.cpython-310.pyc
    │   │               │   ├── forward.py
    │   │               │   └── tunnel.py
    │   │               ├── sugar
    │   │               │   ├── __init__.py
    │   │               │   ├── __init__.pyi
    │   │               │   ├── __pycache__
    │   │               │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   ├── attrsettr.cpython-310.pyc
    │   │               │   │   ├── context.cpython-310.pyc
    │   │               │   │   ├── frame.cpython-310.pyc
    │   │               │   │   ├── poll.cpython-310.pyc
    │   │               │   │   ├── socket.cpython-310.pyc
    │   │               │   │   ├── stopwatch.cpython-310.pyc
    │   │               │   │   ├── tracker.cpython-310.pyc
    │   │               │   │   └── version.cpython-310.pyc
    │   │               │   ├── attrsettr.py
    │   │               │   ├── context.py
    │   │               │   ├── frame.py
    │   │               │   ├── poll.py
    │   │               │   ├── socket.py
    │   │               │   ├── stopwatch.py
    │   │               │   ├── tracker.py
    │   │               │   └── version.py
    │   │               ├── tests
    │   │               │   ├── __init__.py
    │   │               │   ├── __pycache__
    │   │               │   │   ├── __init__.cpython-310.pyc
    │   │               │   │   ├── conftest.cpython-310.pyc
    │   │               │   │   ├── test_asyncio.cpython-310.pyc
    │   │               │   │   ├── test_auth.cpython-310.pyc
    │   │               │   │   ├── test_cffi_backend.cpython-310.pyc
    │   │               │   │   ├── test_constants.cpython-310.pyc
    │   │               │   │   ├── test_context.cpython-310.pyc
    │   │               │   │   ├── test_cython.cpython-310.pyc
    │   │               │   │   ├── test_decorators.cpython-310.pyc
    │   │               │   │   ├── test_device.cpython-310.pyc
    │   │               │   │   ├── test_draft.cpython-310.pyc
    │   │               │   │   ├── test_error.cpython-310.pyc
    │   │               │   │   ├── test_etc.cpython-310.pyc
    │   │               │   │   ├── test_ext.cpython-310.pyc
    │   │               │   │   ├── test_future.cpython-310.pyc
    │   │               │   │   ├── test_imports.cpython-310.pyc
    │   │               │   │   ├── test_includes.cpython-310.pyc
    │   │               │   │   ├── test_ioloop.cpython-310.pyc
    │   │               │   │   ├── test_log.cpython-310.pyc
    │   │               │   │   ├── test_message.cpython-310.pyc
    │   │               │   │   ├── test_monitor.cpython-310.pyc
    │   │               │   │   ├── test_monqueue.cpython-310.pyc
    │   │               │   │   ├── test_multipart.cpython-310.pyc
    │   │               │   │   ├── test_mypy.cpython-310.pyc
    │   │               │   │   ├── test_pair.cpython-310.pyc
    │   │               │   │   ├── test_poll.cpython-310.pyc
    │   │               │   │   ├── test_proxy_steerable.cpython-310.pyc
    │   │               │   │   ├── test_pubsub.cpython-310.pyc
    │   │               │   │   ├── test_reqrep.cpython-310.pyc
    │   │               │   │   ├── test_retry_eintr.cpython-310.pyc
    │   │               │   │   ├── test_security.cpython-310.pyc
    │   │               │   │   ├── test_socket.cpython-310.pyc
    │   │               │   │   ├── test_ssh.cpython-310.pyc
    │   │               │   │   ├── test_version.cpython-310.pyc
    │   │               │   │   ├── test_win32_shim.cpython-310.pyc
    │   │               │   │   ├── test_z85.cpython-310.pyc
    │   │               │   │   └── test_zmqstream.cpython-310.pyc
    │   │               │   ├── conftest.py
    │   │               │   ├── cython_ext.pyx
    │   │               │   ├── test_asyncio.py
    │   │               │   ├── test_auth.py
    │   │               │   ├── test_cffi_backend.py
    │   │               │   ├── test_constants.py
    │   │               │   ├── test_context.py
    │   │               │   ├── test_cython.py
    │   │               │   ├── test_decorators.py
    │   │               │   ├── test_device.py
    │   │               │   ├── test_draft.py
    │   │               │   ├── test_error.py
    │   │               │   ├── test_etc.py
    │   │               │   ├── test_ext.py
    │   │               │   ├── test_future.py
    │   │               │   ├── test_imports.py
    │   │               │   ├── test_includes.py
    │   │               │   ├── test_ioloop.py
    │   │               │   ├── test_log.py
    │   │               │   ├── test_message.py
    │   │               │   ├── test_monitor.py
    │   │               │   ├── test_monqueue.py
    │   │               │   ├── test_multipart.py
    │   │               │   ├── test_mypy.py
    │   │               │   ├── test_pair.py
    │   │               │   ├── test_poll.py
    │   │               │   ├── test_proxy_steerable.py
    │   │               │   ├── test_pubsub.py
    │   │               │   ├── test_reqrep.py
    │   │               │   ├── test_retry_eintr.py
    │   │               │   ├── test_security.py
    │   │               │   ├── test_socket.py
    │   │               │   ├── test_ssh.py
    │   │               │   ├── test_version.py
    │   │               │   ├── test_win32_shim.py
    │   │               │   ├── test_z85.py
    │   │               │   └── test_zmqstream.py
    │   │               └── utils
    │   │                   ├── __init__.py
    │   │                   ├── __pycache__
    │   │                   │   ├── __init__.cpython-310.pyc
    │   │                   │   ├── garbage.cpython-310.pyc
    │   │                   │   ├── interop.cpython-310.pyc
    │   │                   │   ├── jsonapi.cpython-310.pyc
    │   │                   │   ├── monitor.cpython-310.pyc
    │   │                   │   ├── strtypes.cpython-310.pyc
    │   │                   │   ├── win32.cpython-310.pyc
    │   │                   │   └── z85.cpython-310.pyc
    │   │                   ├── buffers.pxd
    │   │                   ├── compiler.json
    │   │                   ├── config.json
    │   │                   ├── garbage.py
    │   │                   ├── getpid_compat.h
    │   │                   ├── interop.py
    │   │                   ├── ipcmaxlen.h
    │   │                   ├── jsonapi.py
    │   │                   ├── monitor.py
    │   │                   ├── mutex.h
    │   │                   ├── pyversion_compat.h
    │   │                   ├── strtypes.py
    │   │                   ├── win32.py
    │   │                   ├── z85.py
    │   │                   └── zmq_compat.h
    │   ├── lib64 -> lib
    │   ├── pyvenv.cfg
    │   └── share
    │       ├── applications
    │       │   ├── jupyter-notebook.desktop
    │       │   └── jupyterlab.desktop
    │       ├── doc
    │       │   └── networkx-3.1
    │       │       ├── LICENSE.txt
    │       │       └── examples
    │       │           ├── 3d_drawing
    │       │           │   ├── README.txt
    │       │           │   ├── __pycache__
    │       │           │   │   ├── mayavi2_spring.cpython-310.pyc
    │       │           │   │   └── plot_basic.cpython-310.pyc
    │       │           │   ├── mayavi2_spring.py
    │       │           │   └── plot_basic.py
    │       │           ├── README.txt
    │       │           ├── algorithms
    │       │           │   ├── README.txt
    │       │           │   ├── WormNet.v3.benchmark.txt
    │       │           │   ├── __pycache__
    │       │           │   │   ├── plot_beam_search.cpython-310.pyc
    │       │           │   │   ├── plot_betweenness_centrality.cpython-310.pyc
    │       │           │   │   ├── plot_blockmodel.cpython-310.pyc
    │       │           │   │   ├── plot_circuits.cpython-310.pyc
    │       │           │   │   ├── plot_davis_club.cpython-310.pyc
    │       │           │   │   ├── plot_dedensification.cpython-310.pyc
    │       │           │   │   ├── plot_girvan_newman.cpython-310.pyc
    │       │           │   │   ├── plot_iterated_dynamical_systems.cpython-310.pyc
    │       │           │   │   ├── plot_krackhardt_centrality.cpython-310.pyc
    │       │           │   │   ├── plot_maximum_independent_set.cpython-310.pyc
    │       │           │   │   ├── plot_parallel_betweenness.cpython-310.pyc
    │       │           │   │   ├── plot_rcm.cpython-310.pyc
    │       │           │   │   ├── plot_snap.cpython-310.pyc
    │       │           │   │   └── plot_subgraphs.cpython-310.pyc
    │       │           │   ├── hartford_drug.edgelist
    │       │           │   ├── plot_beam_search.py
    │       │           │   ├── plot_betweenness_centrality.py
    │       │           │   ├── plot_blockmodel.py
    │       │           │   ├── plot_circuits.py
    │       │           │   ├── plot_davis_club.py
    │       │           │   ├── plot_dedensification.py
    │       │           │   ├── plot_girvan_newman.py
    │       │           │   ├── plot_iterated_dynamical_systems.py
    │       │           │   ├── plot_krackhardt_centrality.py
    │       │           │   ├── plot_maximum_independent_set.py
    │       │           │   ├── plot_parallel_betweenness.py
    │       │           │   ├── plot_rcm.py
    │       │           │   ├── plot_snap.py
    │       │           │   └── plot_subgraphs.py
    │       │           ├── basic
    │       │           │   ├── README.txt
    │       │           │   ├── __pycache__
    │       │           │   │   ├── plot_properties.cpython-310.pyc
    │       │           │   │   ├── plot_read_write.cpython-310.pyc
    │       │           │   │   └── plot_simple_graph.cpython-310.pyc
    │       │           │   ├── plot_properties.py
    │       │           │   ├── plot_read_write.py
    │       │           │   └── plot_simple_graph.py
    │       │           ├── drawing
    │       │           │   ├── README.txt
    │       │           │   ├── __pycache__
    │       │           │   │   ├── plot_center_node.cpython-310.pyc
    │       │           │   │   ├── plot_chess_masters.cpython-310.pyc
    │       │           │   │   ├── plot_custom_node_icons.cpython-310.pyc
    │       │           │   │   ├── plot_degree.cpython-310.pyc
    │       │           │   │   ├── plot_directed.cpython-310.pyc
    │       │           │   │   ├── plot_edge_colormap.cpython-310.pyc
    │       │           │   │   ├── plot_ego_graph.cpython-310.pyc
    │       │           │   │   ├── plot_eigenvalues.cpython-310.pyc
    │       │           │   │   ├── plot_four_grids.cpython-310.pyc
    │       │           │   │   ├── plot_house_with_colors.cpython-310.pyc
    │       │           │   │   ├── plot_knuth_miles.cpython-310.pyc
    │       │           │   │   ├── plot_labels_and_colors.cpython-310.pyc
    │       │           │   │   ├── plot_multipartite_graph.cpython-310.pyc
    │       │           │   │   ├── plot_node_colormap.cpython-310.pyc
    │       │           │   │   ├── plot_rainbow_coloring.cpython-310.pyc
    │       │           │   │   ├── plot_random_geometric_graph.cpython-310.pyc
    │       │           │   │   ├── plot_sampson.cpython-310.pyc
    │       │           │   │   ├── plot_selfloops.cpython-310.pyc
    │       │           │   │   ├── plot_simple_path.cpython-310.pyc
    │       │           │   │   ├── plot_spectral_grid.cpython-310.pyc
    │       │           │   │   ├── plot_tsp.cpython-310.pyc
    │       │           │   │   ├── plot_unix_email.cpython-310.pyc
    │       │           │   │   └── plot_weighted_graph.cpython-310.pyc
    │       │           │   ├── chess_masters_WCC.pgn.bz2
    │       │           │   ├── knuth_miles.txt.gz
    │       │           │   ├── plot_center_node.py
    │       │           │   ├── plot_chess_masters.py
    │       │           │   ├── plot_custom_node_icons.py
    │       │           │   ├── plot_degree.py
    │       │           │   ├── plot_directed.py
    │       │           │   ├── plot_edge_colormap.py
    │       │           │   ├── plot_ego_graph.py
    │       │           │   ├── plot_eigenvalues.py
    │       │           │   ├── plot_four_grids.py
    │       │           │   ├── plot_house_with_colors.py
    │       │           │   ├── plot_knuth_miles.py
    │       │           │   ├── plot_labels_and_colors.py
    │       │           │   ├── plot_multipartite_graph.py
    │       │           │   ├── plot_node_colormap.py
    │       │           │   ├── plot_rainbow_coloring.py
    │       │           │   ├── plot_random_geometric_graph.py
    │       │           │   ├── plot_sampson.py
    │       │           │   ├── plot_selfloops.py
    │       │           │   ├── plot_simple_path.py
    │       │           │   ├── plot_spectral_grid.py
    │       │           │   ├── plot_tsp.py
    │       │           │   ├── plot_unix_email.py
    │       │           │   ├── plot_weighted_graph.py
    │       │           │   └── unix_email.mbox
    │       │           ├── graph
    │       │           │   ├── README.txt
    │       │           │   ├── __pycache__
    │       │           │   │   ├── plot_dag_layout.cpython-310.pyc
    │       │           │   │   ├── plot_degree_sequence.cpython-310.pyc
    │       │           │   │   ├── plot_erdos_renyi.cpython-310.pyc
    │       │           │   │   ├── plot_expected_degree_sequence.cpython-310.pyc
    │       │           │   │   ├── plot_football.cpython-310.pyc
    │       │           │   │   ├── plot_karate_club.cpython-310.pyc
    │       │           │   │   ├── plot_morse_trie.cpython-310.pyc
    │       │           │   │   ├── plot_mst.cpython-310.pyc
    │       │           │   │   ├── plot_napoleon_russian_campaign.cpython-310.pyc
    │       │           │   │   ├── plot_roget.cpython-310.pyc
    │       │           │   │   ├── plot_triad_types.cpython-310.pyc
    │       │           │   │   └── plot_words.cpython-310.pyc
    │       │           │   ├── plot_dag_layout.py
    │       │           │   ├── plot_degree_sequence.py
    │       │           │   ├── plot_erdos_renyi.py
    │       │           │   ├── plot_expected_degree_sequence.py
    │       │           │   ├── plot_football.py
    │       │           │   ├── plot_karate_club.py
    │       │           │   ├── plot_morse_trie.py
    │       │           │   ├── plot_mst.py
    │       │           │   ├── plot_napoleon_russian_campaign.py
    │       │           │   ├── plot_roget.py
    │       │           │   ├── plot_triad_types.py
    │       │           │   ├── plot_words.py
    │       │           │   ├── roget_dat.txt.gz
    │       │           │   └── words_dat.txt.gz
    │       │           └── subclass
    │       │               ├── README.txt
    │       │               ├── __pycache__
    │       │               │   ├── plot_antigraph.cpython-310.pyc
    │       │               │   └── plot_printgraph.cpython-310.pyc
    │       │               ├── plot_antigraph.py
    │       │               └── plot_printgraph.py
    │       ├── icons
    │       │   └── hicolor
    │       │       └── scalable
    │       │           └── apps
    │       │               ├── jupyterlab.svg
    │       │               └── notebook.svg
    │       ├── jupyter
    │       │   ├── kernels
    │       │   │   └── python3
    │       │   │       ├── kernel.json
    │       │   │       ├── logo-32x32.png
    │       │   │       ├── logo-64x64.png
    │       │   │       └── logo-svg.svg
    │       │   ├── lab
    │       │   │   ├── schemas
    │       │   │   │   ├── @jupyter-notebook
    │       │   │   │   │   ├── application-extension
    │       │   │   │   │   │   ├── menus.json
    │       │   │   │   │   │   ├── package.json.orig
    │       │   │   │   │   │   ├── pages.json
    │       │   │   │   │   │   ├── shell.json
    │       │   │   │   │   │   ├── title.json
    │       │   │   │   │   │   ├── top.json
    │       │   │   │   │   │   └── zen.json
    │       │   │   │   │   ├── documentsearch-extension
    │       │   │   │   │   │   └── package.json.orig
    │       │   │   │   │   ├── help-extension
    │       │   │   │   │   │   ├── open.json
    │       │   │   │   │   │   └── package.json.orig
    │       │   │   │   │   ├── notebook-extension
    │       │   │   │   │   │   ├── checkpoints.json
    │       │   │   │   │   │   ├── kernel-logo.json
    │       │   │   │   │   │   ├── package.json.orig
    │       │   │   │   │   │   └── scroll-output.json
    │       │   │   │   │   └── tree-extension
    │       │   │   │   │       ├── file-actions.json
    │       │   │   │   │       ├── package.json.orig
    │       │   │   │   │       └── widget.json
    │       │   │   │   └── @jupyterlab
    │       │   │   │       ├── application-extension
    │       │   │   │       │   ├── commands.json
    │       │   │   │       │   ├── context-menu.json
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   ├── property-inspector.json
    │       │   │   │       │   ├── shell.json
    │       │   │   │       │   └── top-bar.json
    │       │   │   │       ├── apputils-extension
    │       │   │   │       │   ├── notification.json
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   ├── palette.json
    │       │   │   │       │   ├── print.json
    │       │   │   │       │   ├── sanitizer.json
    │       │   │   │       │   ├── themes.json
    │       │   │   │       │   ├── utilityCommands.json
    │       │   │   │       │   └── workspaces.json
    │       │   │   │       ├── cell-toolbar-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── celltags-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── codemirror-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── completer-extension
    │       │   │   │       │   ├── manager.json
    │       │   │   │       │   └── package.json.orig
    │       │   │   │       ├── console-extension
    │       │   │   │       │   ├── completer.json
    │       │   │   │       │   ├── foreign.json
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── tracker.json
    │       │   │   │       ├── csvviewer-extension
    │       │   │   │       │   ├── csv.json
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── tsv.json
    │       │   │   │       ├── debugger-extension
    │       │   │   │       │   ├── main.json
    │       │   │   │       │   └── package.json.orig
    │       │   │   │       ├── docmanager-extension
    │       │   │   │       │   ├── download.json
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── documentsearch-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── extensionmanager-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── filebrowser-extension
    │       │   │   │       │   ├── browser.json
    │       │   │   │       │   ├── download.json
    │       │   │   │       │   ├── open-browser-tab.json
    │       │   │   │       │   ├── open-with.json
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── widget.json
    │       │   │   │       ├── fileeditor-extension
    │       │   │   │       │   ├── completer.json
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── help-extension
    │       │   │   │       │   ├── about.json
    │       │   │   │       │   ├── jupyter-forum.json
    │       │   │   │       │   ├── launch-classic.json
    │       │   │   │       │   └── package.json.orig
    │       │   │   │       ├── htmlviewer-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── hub-extension
    │       │   │   │       │   ├── menu.json
    │       │   │   │       │   └── package.json.orig
    │       │   │   │       ├── imageviewer-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── inspector-extension
    │       │   │   │       │   ├── consoles.json
    │       │   │   │       │   ├── inspector.json
    │       │   │   │       │   ├── notebooks.json
    │       │   │   │       │   └── package.json.orig
    │       │   │   │       ├── launcher-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── logconsole-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── lsp-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── mainmenu-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── markdownviewer-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── mathjax-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── metadataform-extension
    │       │   │   │       │   ├── metadataforms.json
    │       │   │   │       │   └── package.json.orig
    │       │   │   │       ├── notebook-extension
    │       │   │   │       │   ├── completer.json
    │       │   │   │       │   ├── export.json
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   ├── panel.json
    │       │   │   │       │   ├── tools.json
    │       │   │   │       │   └── tracker.json
    │       │   │   │       ├── running-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── settingeditor-extension
    │       │   │   │       │   ├── form-ui.json
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── shortcuts-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── shortcuts.json
    │       │   │   │       ├── statusbar-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── terminal-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── plugin.json
    │       │   │   │       ├── toc-extension
    │       │   │   │       │   ├── package.json.orig
    │       │   │   │       │   └── registry.json
    │       │   │   │       ├── tooltip-extension
    │       │   │   │       │   ├── consoles.json
    │       │   │   │       │   ├── files.json
    │       │   │   │       │   ├── notebooks.json
    │       │   │   │       │   └── package.json.orig
    │       │   │   │       └── translation-extension
    │       │   │   │           ├── package.json.orig
    │       │   │   │           └── plugin.json
    │       │   │   ├── static
    │       │   │   │   ├── 1036.3ccde0c0c5240fa0e85e.js
    │       │   │   │   ├── 1036.3ccde0c0c5240fa0e85e.js.LICENSE.txt
    │       │   │   │   ├── 1085.0b67f0736d85ec41fdd4.js
    │       │   │   │   ├── 1142.d5442a459b18907c1f91.js
    │       │   │   │   ├── 1168.e4d38ba5d2b37479ba8a.js
    │       │   │   │   ├── 1294.9d27be1098bc8abebe3f.js
    │       │   │   │   ├── 141.f110448d494068ebcc87.js
    │       │   │   │   ├── 141.f110448d494068ebcc87.js.LICENSE.txt
    │       │   │   │   ├── 1410.e2302ff5f564d6e596bb.js
    │       │   │   │   ├── 1420.e8486ed074346bc629ca.js
    │       │   │   │   ├── 1448.c391061d8a8344f9d177.js
    │       │   │   │   ├── 1452.4cc17f31511d1f9c6052.js
    │       │   │   │   ├── 1467.dcd89539f6477c1367af.js
    │       │   │   │   ├── 1550.09375e869bc25429b07a.js
    │       │   │   │   ├── 1581.e988a625b879002dcc04.js
    │       │   │   │   ├── 1581.e988a625b879002dcc04.js.LICENSE.txt
    │       │   │   │   ├── 1608.61240f3db67d3d952790.js
    │       │   │   │   ├── 1716.a6bbe1ae8a1986a73623.js
    │       │   │   │   ├── 1776.4f9305d35480467b23c9.js
    │       │   │   │   ├── 1861.4fc7b4afe2b09eb6b5c0.js
    │       │   │   │   ├── 1903.3b452e8ec30e57dbaba5.js
    │       │   │   │   ├── 1945.0fbbfe93a4aedd91875c.js
    │       │   │   │   ├── 1954.07d96e4020ed6e543d25.js
    │       │   │   │   ├── 1993.f8c5682f95ffa75cbaf6.js
    │       │   │   │   ├── 1cb1c39ea642f26a4dfe.woff
    │       │   │   │   ├── 2039.aa079dac5c520f93b234.js
    │       │   │   │   ├── 2090.abc86741318f76c3d726.js
    │       │   │   │   ├── 2091.600b1c32af186f6405f9.js
    │       │   │   │   ├── 2104.296346db0067b4883fbf.js
    │       │   │   │   ├── 2145.be9ec610f29703694fcf.js
    │       │   │   │   ├── 2254.55c69210925ec9b28dd9.js
    │       │   │   │   ├── 2295.cda0f7182bf2a1a03c5a.js
    │       │   │   │   ├── 2320.04abae549b19363c2fdd.js
    │       │   │   │   ├── 2363.6eef078cb37c32d7fbc3.js
    │       │   │   │   ├── 2459.9f9cb02561de1bec73ff.js
    │       │   │   │   ├── 2485.dab750ed66209df61fe1.js
    │       │   │   │   ├── 2617.9c299e26785f7646cb39.js
    │       │   │   │   ├── 2646.0864fb63d7ab1ed16893.js
    │       │   │   │   ├── 26683bf201fb258a2237.woff
    │       │   │   │   ├── 2800.680b1fa0a4c66c69bb1e.js
    │       │   │   │   ├── 2857.27a6e85f5c4c092ab8a2.js
    │       │   │   │   ├── 2909.e190307f7f84c7691068.js
    │       │   │   │   ├── 292.3f7844a129f16ec1ffbc.js
    │       │   │   │   ├── 2929.b88233153dbf33f40b29.js
    │       │   │   │   ├── 2953.92ff8f12bad6ee06859c.js
    │       │   │   │   ├── 2987.d9b80c90eb8c9e4e276d.js
    │       │   │   │   ├── 2990.ea15322a41d3f133989b.js
    │       │   │   │   ├── 2995.9791e1071c5f095421bf.js
    │       │   │   │   ├── 3056.3d6572b392dc81bc6193.js
    │       │   │   │   ├── 30e889b58cbc51adfbb0.woff
    │       │   │   │   ├── 3123.4d894ae9a109d4911829.js
    │       │   │   │   ├── 3127.75e12687687a3de3b59d.js
    │       │   │   │   ├── 32792104b5ef69eded90.woff
    │       │   │   │   ├── 3306.8bdc49ad1a7ca593a838.js
    │       │   │   │   ├── 3308.92a1e305c62cc91845b9.js
    │       │   │   │   ├── 3520.3495b98946de6960ace8.js
    │       │   │   │   ├── 3528.3b5ef5f31d460b5fcd01.js
    │       │   │   │   ├── 3547.bd90e90bfe79911486e8.js
    │       │   │   │   ├── 3549.24f2fe646d8128bc9db0.js
    │       │   │   │   ├── 355254db9ca10a09a3b5.woff
    │       │   │   │   ├── 3601.5c17c015d71b69ddcab3.js
    │       │   │   │   ├── 36e0d72d8a7afc696a3e.woff
    │       │   │   │   ├── 3724.a4657dc16be2ffc49282.js
    │       │   │   │   ├── 373c04fd2418f5c77eea.eot
    │       │   │   │   ├── 378.6d0f0fc4c8a2eb80ac43.js
    │       │   │   │   ├── 3783.6121fa44ad854b45accf.js
    │       │   │   │   ├── 3807.08a8fd824036c30b3746.js
    │       │   │   │   ├── 383.db345dbeef5ef774e50c.js
    │       │   │   │   ├── 3871.ba96e5b53bb16df56618.js
    │       │   │   │   ├── 3923.f29c06abdcb560130471.js
    │       │   │   │   ├── 3935.905285b8e22c337968ed.js
    │       │   │   │   ├── 3935.905285b8e22c337968ed.js.LICENSE.txt
    │       │   │   │   ├── 3962.50786e3ed9a01329a4a0.js
    │       │   │   │   ├── 3bc6ecaae7ecf6f8d7f8.woff
    │       │   │   │   ├── 3de784d07b9fa8f104c1.woff
    │       │   │   │   ├── 3f6d3488cf65374f6f67.woff
    │       │   │   │   ├── 4008.86acbefff6de679f77b5.js
    │       │   │   │   ├── 4008.86acbefff6de679f77b5.js.LICENSE.txt
    │       │   │   │   ├── 4017.096a74a538e031b6d346.js
    │       │   │   │   ├── 4043.aa012978c41d1d1b2f14.js
    │       │   │   │   ├── 4139.303ee7374c742287be85.js
    │       │   │   │   ├── 4155.5a8d6736017097028d78.js
    │       │   │   │   ├── 4283.f6092d8b7f2e53118d1b.js
    │       │   │   │   ├── 4291.e5d8997127541f75fdaf.js
    │       │   │   │   ├── 4405.43dab120fea32f30bbb9.js
    │       │   │   │   ├── 4419.93938494f456cd76a7e3.js
    │       │   │   │   ├── 4452.2f8819684b96ecff5231.js
    │       │   │   │   ├── 4519.6b784d052db42e93eff2.js
    │       │   │   │   ├── 4523.87224ea442d42316dda0.js
    │       │   │   │   ├── 4562.72444a09f5f092646490.js
    │       │   │   │   ├── 4591.428531724f49fe824ffa.js
    │       │   │   │   ├── 46.fb119c5e5b1e0c72a00f.js
    │       │   │   │   ├── 4743.d4e9658ea25301e15a94.js
    │       │   │   │   ├── 481e39042508ae313a60.woff
    │       │   │   │   ├── 4878.73004381601237a3ef9c.js
    │       │   │   │   ├── 49.7233f68f95d10b85a83e.js
    │       │   │   │   ├── 4986.a497cdda4b7152902568.js
    │       │   │   │   ├── 5041.cdc120bda0a0dec4cfc2.js
    │       │   │   │   ├── 5157.9c77dc27a251d4135876.js
    │       │   │   │   ├── 5201.8866042bae350659528a.js
    │       │   │   │   ├── 5203.c002d40ac647dc6e1d61.js
    │       │   │   │   ├── 5331.0cd3f010bb08983ec3fd.js
    │       │   │   │   ├── 5440.2541fcda12b661665148.js
    │       │   │   │   ├── 5521.ce4a0274596e0325374c.js
    │       │   │   │   ├── 5746.e4434ef2027bcc5ed0c9.js
    │       │   │   │   ├── 581.2b878ed37172aced15b5.js
    │       │   │   │   ├── 5881.3946238aa4afdcf4f964.js
    │       │   │   │   ├── 5959.a6b1fd3b03d3649ea8b1.js
    │       │   │   │   ├── 5cda41563a095bd70c78.woff
    │       │   │   │   ├── 6059.d83e7323b2ee1aa16009.js
    │       │   │   │   ├── 6163.f5b51a9f0df4846ba40f.js
    │       │   │   │   ├── 6207.a8079c8d8a61039dd530.js
    │       │   │   │   ├── 6243.2efd673d1304c43b7b78.js
    │       │   │   │   ├── 6267.1def2916929e185ab9fc.js
    │       │   │   │   ├── 6359.4b994bfd6b1dea2d6fe3.js
    │       │   │   │   ├── 6443.e6b52d3732b3e8513a71.js
    │       │   │   │   ├── 6532.bb7137729a2d6d4e6ddf.js
    │       │   │   │   ├── 6560.f42276a0b1b92aea515b.js
    │       │   │   │   ├── 6595.6a1d7e1abbf186dd119b.js
    │       │   │   │   ├── 6686.3c518aa6e5f9785fb486.js
    │       │   │   │   ├── 6815.0b699f0c162a24b0dbe3.js
    │       │   │   │   ├── 6888.9d3914817f3290827a64.js
    │       │   │   │   ├── 7080.1330328bb6f46b4da81e.js
    │       │   │   │   ├── 7112.d5120c85ebd17620dda0.js
    │       │   │   │   ├── 7173.e28f63dbd553818e07d3.js
    │       │   │   │   ├── 721921bab0d001ebff02.woff
    │       │   │   │   ├── 7245.c0cae8787dcd00b991b7.js
    │       │   │   │   ├── 7294.badf85a3180703d63f62.js
    │       │   │   │   ├── 7294.badf85a3180703d63f62.js.LICENSE.txt
    │       │   │   │   ├── 72bc573386dd1d48c5bb.woff
    │       │   │   │   ├── 7317.af8a7da0f881a22752c1.js
    │       │   │   │   ├── 7318.397bf8e913e825b2be27.js
    │       │   │   │   ├── 7363.abe8e31a91e113753bae.js
    │       │   │   │   ├── 7384.60351e008d8f687e8fcc.js
    │       │   │   │   ├── 7390.8253478b90f756692702.js
    │       │   │   │   ├── 745.85516a9bb83bcd94d00d.js
    │       │   │   │   ├── 7451.c0257dbfdd320e2c21f5.js
    │       │   │   │   ├── 7451.c0257dbfdd320e2c21f5.js.LICENSE.txt
    │       │   │   │   ├── 7472.58ba8647a489d019c2ef.js
    │       │   │   │   ├── 7473.5012397d10d3b945ecaa.js
    │       │   │   │   ├── 7508.13cbca6737f2c3de2e93.js
    │       │   │   │   ├── 7511.b381a696cf806983c654.js
    │       │   │   │   ├── 7517.f3e5d420f4af90d442dd.js
    │       │   │   │   ├── 7669.343e259c4c8269479f5b.js
    │       │   │   │   ├── 7702.c479c69f7a532f7b3fd5.js
    │       │   │   │   ├── 7730.7e3a9fb140d2d55a51fc.js
    │       │   │   │   ├── 7731.26db150e967313b7a7e2.js
    │       │   │   │   ├── 7763.19a095394000f9ef62bd.js
    │       │   │   │   ├── 7763.19a095394000f9ef62bd.js.LICENSE.txt
    │       │   │   │   ├── 7775.3e0dee729369fe3d5008.js
    │       │   │   │   ├── 7823.817687f13e9a6781fdd3.js
    │       │   │   │   ├── 7827.e36d073d947bf02a05e3.js
    │       │   │   │   ├── 7848.e83aa4b90ae87209abb8.js
    │       │   │   │   ├── 786.8a99ee7dbd7bd0eb9dce.js
    │       │   │   │   ├── 7877.a4c46a784149533b91d4.js
    │       │   │   │   ├── 7887.128a155df5d25e88c0ce.js
    │       │   │   │   ├── 795.47ab66037ef33f808f09.js
    │       │   │   │   ├── 79d088064beb3826054f.eot
    │       │   │   │   ├── 8002.25f64485372af5158c83.js
    │       │   │   │   ├── 8010.1cf8237e9def8404f355.js
    │       │   │   │   ├── 8012.40cb006f0c180ebafa91.js
    │       │   │   │   ├── 812.93b4681c78d38d76145b.js
    │       │   │   │   ├── 8285.1eac7b7582569be1c3a8.js
    │       │   │   │   ├── 830.8ddf7d2d91f66a8e4d36.js
    │       │   │   │   ├── 8302.4c190e10b00fe083570e.js
    │       │   │   │   ├── 8319.80fcbc832e1eb20b71e7.js
    │       │   │   │   ├── 8347.573b699e3590729bfa8a.js
    │       │   │   │   ├── 8405.154ba4b17a2dec22a355.js
    │       │   │   │   ├── 8493.fc635229db38e6fc6aa2.js
    │       │   │   │   ├── 8498.27a245b23921914bf5c2.js
    │       │   │   │   ├── 8512.1af96655287fd124877b.js
    │       │   │   │   ├── 8678.dcd3dab9025b13eb9be8.js
    │       │   │   │   ├── 870673df72e70f87c91a.woff
    │       │   │   │   ├── 8710.5fc5ecb762fb4494db02.js
    │       │   │   │   ├── 8768.4a80caab00174c50eb10.js
    │       │   │   │   ├── 8768.4a80caab00174c50eb10.js.LICENSE.txt
    │       │   │   │   ├── 8771.327a202178f82f3b15b8.js
    │       │   │   │   ├── 8787.4d36d28dcf94bf59cbfe.js
    │       │   │   │   ├── 8805.0f14a91b024b59c039a7.js
    │       │   │   │   ├── 8823.2ff947bcd96cc0723058.js
    │       │   │   │   ├── 8875.88988caaba1e33edad5b.js
    │       │   │   │   ├── 88b98cad3688915e50da.woff
    │       │   │   │   ├── 8ea8791754915a898a31.woff2
    │       │   │   │   ├── 8ea8dbb1b02e6f730f55.woff
    │       │   │   │   ├── 9.0e0cba0ccc2a4b670600.js
    │       │   │   │   ├── 9030.260bc05e28eccff70ae8.js
    │       │   │   │   ├── 9041.df39043656c7233552e4.js
    │       │   │   │   ├── 9055.bd710a8db8883a836b59.js
    │       │   │   │   ├── 9065.5305259c65dfa1c99874.js
    │       │   │   │   ├── 9109.fa3ee74a5c0f378f4d51.js
    │       │   │   │   ├── 9192.db4337a516b7f38d1f89.js
    │       │   │   │   ├── 9222.1c2a8e69a2de57dd1984.js
    │       │   │   │   ├── 9230.58b8c42b730e1a56e69b.js
    │       │   │   │   ├── 9265.bc2b66a4502cdfcfc14f.js
    │       │   │   │   ├── 9362.823dcfac216f8057452d.js
    │       │   │   │   ├── 9409.34c33ed11e2d6f318480.js
    │       │   │   │   ├── 942.93c8de61ea9ea08ec097.js
    │       │   │   │   ├── 9421.022dc7b4e9a2c80c32c2.js
    │       │   │   │   ├── 9445.fe5e9e5b728de8d15873.js
    │       │   │   │   ├── 9621.9cbfa52c42927bb398b4.js
    │       │   │   │   ├── 9653.d93c93e084cd5e93cd2d.js
    │       │   │   │   ├── 9674eb1bd55047179038.svg
    │       │   │   │   ├── 9738.c0234a1f7f6ac262f560.js
    │       │   │   │   ├── 9747.6dd327f4928c6989ea8a.js
    │       │   │   │   ├── 9747.6dd327f4928c6989ea8a.js.LICENSE.txt
    │       │   │   │   ├── 9826.406d2a71dc45995bc549.js
    │       │   │   │   ├── 9826.406d2a71dc45995bc549.js.LICENSE.txt
    │       │   │   │   ├── 9834b82ad26e2a37583d.woff2
    │       │   │   │   ├── a009bea404f7a500ded4.woff
    │       │   │   │   ├── a3b9817780214caf01e8.svg
    │       │   │   │   ├── af04542b29eaac04550a.woff
    │       │   │   │   ├── af6397503fcefbd61397.ttf
    │       │   │   │   ├── af96f67d7accf5fd2a4a.woff
    │       │   │   │   ├── b418136e3b384baaadec.woff
    │       │   │   │   ├── be0a084962d8066884f7.svg
    │       │   │   │   ├── bootstrap.js
    │       │   │   │   ├── build_log.json
    │       │   │   │   ├── c49810b53ecc0d87d802.woff
    │       │   │   │   ├── c56da8d69f1a0208b8e0.woff
    │       │   │   │   ├── cb9e9e693192413cde2b.woff
    │       │   │   │   ├── cda59d6efffa685830fd.ttf
    │       │   │   │   ├── e4299464e7b012968eed.eot
    │       │   │   │   ├── e42a88444448ac3d6054.woff2
    │       │   │   │   ├── e8711bbb871afd8e9dea.ttf
    │       │   │   │   ├── f9217f66874b0c01cd8c.woff
    │       │   │   │   ├── fc6ddf5df402b263cfb1.woff
    │       │   │   │   ├── index.html
    │       │   │   │   ├── index.out.js
    │       │   │   │   ├── jlab_core.be6103fe6f6cc2c18378.js
    │       │   │   │   ├── main.df4a154f94063e34ef18.js
    │       │   │   │   ├── package.json
    │       │   │   │   ├── style.js
    │       │   │   │   └── third-party-licenses.json
    │       │   │   └── themes
    │       │   │       └── @jupyterlab
    │       │   │           ├── theme-dark-extension
    │       │   │           │   ├── index.css
    │       │   │           │   └── index.js
    │       │   │           └── theme-light-extension
    │       │   │               ├── index.css
    │       │   │               └── index.js
    │       │   ├── labextensions
    │       │   │   ├── @jupyter-notebook
    │       │   │   │   └── lab-extension
    │       │   │   │       ├── package.json
    │       │   │   │       ├── schemas
    │       │   │   │       │   └── @jupyter-notebook
    │       │   │   │       │       └── lab-extension
    │       │   │   │       │           ├── interface-switcher.json
    │       │   │   │       │           ├── launch-tree.json
    │       │   │   │       │           └── package.json.orig
    │       │   │   │       └── static
    │       │   │   │           ├── 568.354aeb1f4c9e8771e30e.js
    │       │   │   │           ├── 713.bd864629003c5c2651c8.js
    │       │   │   │           ├── 776.c7baadfaddfd4518c935.js
    │       │   │   │           ├── 928.03334a8369a0f3a46d9a.js
    │       │   │   │           ├── remoteEntry.eadf9b5c39b5ec520158.js
    │       │   │   │           ├── style.js
    │       │   │   │           └── third-party-licenses.json
    │       │   │   ├── @jupyter-widgets
    │       │   │   │   └── jupyterlab-manager
    │       │   │   │       ├── install.json
    │       │   │   │       ├── package.json
    │       │   │   │       ├── schemas
    │       │   │   │       │   └── @jupyter-widgets
    │       │   │   │       │       └── jupyterlab-manager
    │       │   │   │       │           ├── package.json.orig
    │       │   │   │       │           └── plugin.json
    │       │   │   │       └── static
    │       │   │   │           ├── 113.e4cfda62b59ddbe550d3.js
    │       │   │   │           ├── 113.e4cfda62b59ddbe550d3.js.LICENSE.txt
    │       │   │   │           ├── 134.a63a8d293fb35a52dc25.js
    │       │   │   │           ├── 291.cff5ef71b29e18850479.js
    │       │   │   │           ├── 291.cff5ef71b29e18850479.js.LICENSE.txt
    │       │   │   │           ├── 336.ebc7a55ea1768712771f.js
    │       │   │   │           ├── 345.17494fea1ff555b26294.js
    │       │   │   │           ├── 495.79062b4ce5ec7920dcb1.js
    │       │   │   │           ├── 595.74686e2543ce21f10975.js
    │       │   │   │           ├── 596.df8214a14175baf1ee16.js
    │       │   │   │           ├── 61.21f571face17e35076c2.js
    │       │   │   │           ├── 644.558670f1aa9ae5791769.js
    │       │   │   │           ├── 699.e966b1425a7d4e8c3f4e.js
    │       │   │   │           ├── 965.9a2bfc1116cea35345ca.js
    │       │   │   │           ├── remoteEntry.a37e37c87d212fe85e13.js
    │       │   │   │           ├── style.js
    │       │   │   │           └── third-party-licenses.json
    │       │   │   └── jupyterlab_pygments
    │       │   │       ├── install.json
    │       │   │       ├── package.json
    │       │   │       └── static
    │       │   │           ├── 568.1e2faa2ba0bbe59c4780.js
    │       │   │           ├── 747.8eb3ddccc7ec4987bff9.js
    │       │   │           ├── remoteEntry.aa1060b2d1221f8e5688.js
    │       │   │           ├── style.js
    │       │   │           └── third-party-licenses.json
    │       │   ├── nbconvert
    │       │   │   └── templates
    │       │   │       ├── asciidoc
    │       │   │       │   ├── conf.json
    │       │   │       │   └── index.asciidoc.j2
    │       │   │       ├── base
    │       │   │       │   ├── cell_id_anchor.j2
    │       │   │       │   ├── celltags.j2
    │       │   │       │   ├── display_priority.j2
    │       │   │       │   ├── jupyter_widgets.html.j2
    │       │   │       │   ├── mathjax.html.j2
    │       │   │       │   └── null.j2
    │       │   │       ├── basic
    │       │   │       │   ├── conf.json
    │       │   │       │   └── index.html.j2
    │       │   │       ├── classic
    │       │   │       │   ├── base.html.j2
    │       │   │       │   ├── conf.json
    │       │   │       │   ├── index.html.j2
    │       │   │       │   └── static
    │       │   │       │       └── style.css
    │       │   │       ├── compatibility
    │       │   │       │   ├── display_priority.tpl
    │       │   │       │   └── full.tpl
    │       │   │       ├── lab
    │       │   │       │   ├── base.html.j2
    │       │   │       │   ├── conf.json
    │       │   │       │   ├── index.html.j2
    │       │   │       │   ├── mermaidjs.html.j2
    │       │   │       │   └── static
    │       │   │       │       ├── index.css
    │       │   │       │       ├── theme-dark.css
    │       │   │       │       └── theme-light.css
    │       │   │       ├── latex
    │       │   │       │   ├── base.tex.j2
    │       │   │       │   ├── conf.json
    │       │   │       │   ├── display_priority.j2
    │       │   │       │   ├── document_contents.tex.j2
    │       │   │       │   ├── index.tex.j2
    │       │   │       │   ├── null.j2
    │       │   │       │   ├── report.tex.j2
    │       │   │       │   ├── style_bw_ipython.tex.j2
    │       │   │       │   ├── style_bw_python.tex.j2
    │       │   │       │   ├── style_ipython.tex.j2
    │       │   │       │   ├── style_jupyter.tex.j2
    │       │   │       │   └── style_python.tex.j2
    │       │   │       ├── markdown
    │       │   │       │   ├── conf.json
    │       │   │       │   └── index.md.j2
    │       │   │       ├── python
    │       │   │       │   ├── conf.json
    │       │   │       │   └── index.py.j2
    │       │   │       ├── reveal
    │       │   │       │   ├── base.html.j2
    │       │   │       │   ├── cellslidedata.j2
    │       │   │       │   ├── conf.json
    │       │   │       │   ├── index.html.j2
    │       │   │       │   └── static
    │       │   │       │       └── custom_reveal.css
    │       │   │       ├── rst
    │       │   │       │   ├── conf.json
    │       │   │       │   └── index.rst.j2
    │       │   │       ├── script
    │       │   │       │   ├── conf.json
    │       │   │       │   └── script.j2
    │       │   │       └── webpdf
    │       │   │           ├── conf.json
    │       │   │           └── index.pdf.j2
    │       │   └── nbextensions
    │       │       ├── jupyter-js-widgets
    │       │       │   ├── extension.js
    │       │       │   ├── extension.js.LICENSE.txt
    │       │       │   └── extension.js.map
    │       │       └── pydeck
    │       │           ├── extensionRequires.js
    │       │           ├── index.js
    │       │           └── index.js.map
    │       └── man
    │           └── man1
    │               ├── ipython.1
    │               └── ttx.1
    └── requirements.txt
### Contributions
