#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thread handler to create and start threads"""

from concurrent.futures import ThreadPoolExecutor
from typing import Tuple

from app.application import Application

app = Application()


def create_threads(process, args: Tuple, thread_count: int) -> None:
    """
    Function to create x threads using ThreadPoolExecutor
    :param process: function for the threads to execute
    :param Tuple args: args for the provided process
    :param int thread_count: # of threads needed
    :return: None
    """
    # set max threads
    max_threads = app.config["maxThreads"]
    # check to see if we need to go over the max threads and
    # assign allowed variable threads accordingly
    threads = max_threads if thread_count > max_threads else thread_count
    # start the threads with the number of threads allowed
    with ThreadPoolExecutor(max_workers=threads) as executor:
        # iterate and start the threads that were requested
        for thread in range(threads):
            # assign each thread the passed process and args along with the thread number
            executor.submit(process, args, thread)


def thread_assignment(thread: int, total_items: int) -> list:
    """
    Function to iterate through items and returns a list the
    provided thread should be assigned and use during its execution
    :param int thread: current thread number
    :param int total_items: Total # of items to process with threads
    :return: List of items to process for the given thread
    :rtype: list
    """
    # set max threads
    max_threads = app.config["maxThreads"]

    # create assigned variable list
    assigned = []
    for x in range(total_items):
        if x % max_threads == thread:
            assigned.append(x)
    return assigned
