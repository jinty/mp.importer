
def run_in_batches(iterable, end_batch_callback=None, batch_size=2, batch_start=0, max_batches=None):		# what if max_batches = None? TODO
    c = 0
    ended = False
    if max_batches is None:
        for k in iterable:
            c = c + 1			
            current_batch, position_in_batch = divmod(c, batch_size)
            if position_in_batch == 0:
                current_batch = current_batch - 1
            if current_batch >= batch_start:
                ended = False
                yield k 
                if position_in_batch == 0: 							# ends completed batches
                    end_batch_callback()
                    ended = True
        if ended is False:
            end_batch_callback()
    else:
        for k in iterable:
            c = c + 1			
            current_batch, position_in_batch = divmod(c, batch_size)
            if position_in_batch == 0:
                current_batch = current_batch - 1						# last element of a batch has position=0, value=current_batch+1
            if current_batch >= batch_start and current_batch < batch_start+max_batches:
                ended = False
                yield k 
                if position_in_batch == 0: 							# ends completed batches
                    end_batch_callback()
                    ended = True
            if current_batch == batch_start+max_batches:					# if gets maximum allowed batches, break 
                break
        if ended is False:
            end_batch_callback()		


def run_in_batches_with_options(iterable, end_batch_callback, options): 		# arguments can be passed through "options"
    for x in run_in_batches(iterable, end_batch_callback, options.batch_size, options.batch_start, options.max_batches):	
        yield x

