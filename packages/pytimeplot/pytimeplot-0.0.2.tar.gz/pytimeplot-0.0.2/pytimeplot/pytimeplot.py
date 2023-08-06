__all__ = ['with_timer', 'make_timedata', 'timeplot']

from collections.abc import Callable, Iterable
from functools import partial
from itertools import repeat
from logging import error, warning
from time import monotonic_ns
from typing import Union

from pycombinators import flip, identity

import pandas as pd
import matplotlib.pyplot as plt

def with_timer(f: Callable) -> Callable:
    """Embellish a function with timing information.

    Given a function f, returns a new function equivalent
    to that original function but returning a tuple containing
    the original results and embellished timing data.
    """
    def timed_f(*args, **kwargs):
        start = monotonic_ns() // (10 ** 6)
        results = f(*args, **kwargs)
        end = monotonic_ns() // (10 ** 6)
        return results, end - start

    return timed_f


def make_timedata(f: Callable,
                  input_data_set: set,
                  interp_as_coll: bool = True,
                  testing_parameter: str = "") -> pd.DataFrame:
    """Measure the runtime performance of a function with differently-sized inputs and return a dataframe with that information.

    Keyword arguments:
    f -- the function to be tested
    input_data_set -- the set of data be input into the function. can be either a set of single arguments to be directly
        inputted or a set of dicts representing kwargs
    interp_as_coll -- whether or not to interpret the data in input_data_set as a collection. if TRUE, it will be interpreted as such
    testing_parameter -- the name of the parameter to be tested, iff input_data_set is a set of dicts represents kwargs (default "")
    """
    input_data = list(input_data_set)

    # function to test if all members of collection 'xs' are an instance of type 't'
    areallinstance = lambda xs, t: all(map(partial(flip(isinstance), t), xs))

    # verify uses_dicts
    uses_dicts = areallinstance(input_data, dict)
    if uses_dicts and not testing_parameter:
        raise ValueError("Name of testing parameter (testing_parameter) required for dict arguments.")

    # time the functions
    timed_f = with_timer(f)
    output_times = tuple(timed_f(**args)[1] for args in input_data) if uses_dicts else tuple(t for _, t in map(timed_f, input_data_set))

    # get input sizes
    size_f = len if interp_as_coll else identity
    input_sizes = tuple(size_f(d[testing_parameter]) for d in input_data) if uses_dicts else tuple(size_f(x) for x in input_data)

    return pd.DataFrame(zip(input_sizes, output_times))

 
def timeplot(fs: Callable | Iterable[Callable],
             input_data_sets: set | Iterable[set],
             filename: str = "",
             interps: bool | Iterable[bool] = repeat(True),
             test_params: str | Iterable[str] = repeat(""), *,
             plot_options: dict = {},
             legends: None | str | Iterable[str] = None,
             preview_plot: bool = True):
    """Plot the runtime of a function based on input data.

    Keyword arguments:
    fs -- either a single function or list of functions to be tested
    input_data_sets-- either a set of data to be input into the function or a list of sets. each set can be either a set of single arguments to be directly
        inputted or a set of dicts representing kwargs
    filename -- output filename (default "")
        supported formats include, but are not limited to:
            - png
            - pdf
            - svg
    interps -- whether or not to interpret the data in input_data_set as a collection. if TRUE, it will be interpreted as such (default repeat(True))
    test_params -- the names of the parameters to be tested as strings, iff input_data_set is a set of dicts represents kwargs (default repeat(""))

    Keyword-only arguments:
    plot_options -- options for the plot's display, as a dictionary
        options include:
            - title
            - x-label
            - y-label
            - colors: an iterator listing the colors that different series will cycle through
    legends -- legend names. if left to None, will default is the calling functions' __name__ properties (default None)
    preview_plot -- whether or not to display a preview of the plot in a window (default True)
    """
    DEFAULT_COLORS = "red", "blue", "green", "purple", "black"

    DEFAULT_PLOT_OPTIONS = {
        "title": "Size vs. Runtime",
        "xlabel": "Size of input",
        "ylabel": "Runtime (ms)",
        "colors": DEFAULT_COLORS
    }

    zipped_parameters = tuple(zip(*[[p] if not isinstance(p, Iterable) or isinstance(p, str) or isinstance(p, set) else p for p in [fs, input_data_sets, interps, test_params]]))

    if isinstance(fs, Iterable) and len(fs) != len(zipped_parameters):
        raise ValueError("One of input_data_sets, interps, or test_params is too short: should be at least {} in length".format(len(fs)))

    if isinstance(legends, str):
        legends = [legends]

    if legends is not None and len(zipped_parameters) != len(legends):
        raise ValueError("Legends is short: should be at least {} in length".format(len(zipped_parameters)))

    timedata = [make_timedata(*args) for args in zipped_parameters]

    real_plot_options = DEFAULT_PLOT_OPTIONS | plot_options

    _, ax = plt.subplots()
    plt.title(real_plot_options["title"])
    plt.xlabel(real_plot_options["xlabel"])
    plt.ylabel(real_plot_options["ylabel"])
    colors = real_plot_options["colors"]

    for i, df in enumerate(timedata):
        ax.scatter(df[0], df[1], c=colors[i % len(colors)], label=fs[i].__name__ if legends is None else legends[i])

    ax.legend()
    
    if filename:
        try:
            plt.savefig(filename)
        except IOError as ioe:
            error(ioe)

    if preview_plot:
        plt.show()

    if not filename and not preview_plot:
        warning("Filename not specified and preview_plot disabled.")
