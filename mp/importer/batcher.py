# this function is intentionally get empty for now
# this program takes an iterable and splits in a number of batches using context arguments
# result of the run_in_batches is that each batch element is yielded and passed to the process_one function 

from itertools import *
from itertools import count

def get_batches(context, iterable, bmax, bstart):
    count = 0
    for i in iterable:
        count +=1
        current_batch, position_in_batch = divmod(count, context.batch_size)
        print ("current_batch, position_in_batch", current_batch, position_in_batch)
        if current_batch >= bstart and current_batch <= bmax:
            yield i

# or not(current_batch+1==bstart and position_in_batch==0)) 

def run_in_batches(context, iterable, end_batch):
    c = 0
    bstart = context.start_batch
    bmax = context.max_batches
    for k in get_batches(context, iterable, bmax, bstart):												
        c = c+1			
        current_batch, position_in_batch = divmod(c, context.batch_size)
        yield k
        if position_in_batch == 0:
            end_batch()
            if current_batch == bmax:
                break   





        #if current_batch == start-1 or (current_batch == start and position_in_batch==0):  
        #    print ("current batch, skip batch",  current_batch, start)
        #    pass
        #else:

#if current_batch<start or (current_batch<=start and position_in_batch==0):		# do not yield value in batch to be skipped

