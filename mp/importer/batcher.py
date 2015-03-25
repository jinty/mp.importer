# this function is intentionally get empty for now
# this program takes an iterable and splits in a number of batches using context arguments
# result of the run_in_batches is that each batch element is yielded and passed to the process_one function 

from itertools import *
from itertools import count

def get_batches(context, iterable, nb):
    count = 0
    bsize = context.batch_size
    ssize = context.start_batch
    start = ssize*bsize
    for i in iterable:
        count += 1
        if start+bsize*nb <= count-1 <= start++bsize*nb+bsize-1:     # for now takes only the first batch 
            yield i

def run_in_batches(context, iterable, process_one):
    bmax = context.max_batches
    tot_result = []
    for nbatch in range(0,bmax):				      # for each batch launches the pipeline (get-batches and process)
        got_batch = get_batches(context, iterable, nbatch)
        for k in got_batch:
       	    result = process_one(k)
            tot_result.append(result)						
    return tot_result


# TODO
# yield got_batch.next() for next function in pipeline (statistics)
# add try-except to call the end_batch function when each batch is over

