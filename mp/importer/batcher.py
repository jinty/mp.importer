# -*- coding: utf-8 -*-
""" Create batches of elements from and iterable

This module contains utilities for creating batches of elements from an iterable
The user can select the batch size, the maximum number of batches and the starting batch for yielding elements
Other function will be added to randomly sample elements and to retrieve the last batch  
"""
def run_in_batches(iterable, end_batch_callback=None, batch_size=2, batch_start=0, max_batches=None):	
    """ Create batches from an iterable
   
    This function is a generator that creates batches of elements from an iterable 
    The callback function is called when a) maximum batches are reached or b) iterable is exhausted 
    All batches (complete and incomplete) are ended by a callback function
    """ 	
    c = 0
    ended = False
    for k in iterable:
        c = c + 1			
        current_batch, position_in_batch = divmod(c, batch_size)
        if position_in_batch == 0:
            current_batch = current_batch - 1						# last element of a batch has position=0, value=current_batch+1
        if current_batch >= batch_start and (max_batches is None or current_batch < batch_start + max_batches):
            ended = False
            yield k 
            if position_in_batch == 0: 							# ends completed batches
                end_batch_callback()
                ended = True
        if max_batches is not None and current_batch == batch_start + max_batches:	# if gets maximum allowed batches, break 
            break
    if ended is False:
        end_batch_callback()	


def parse_arguments(parser):		 						
    """ Adds batcher arguments to the parser									 

    This function gets the parser containing user inputs
    It adds arguments and returns a parser
    The parsing of args is performed in the main script 
    """ 
    parser.add_argument('--batch-size', dest='batch_size', action='store', type=int, help="Number of elements in each batch")			# set default values here? now in batcher		
    parser.add_argument('--batch-start', dest='batch_start', action='store', type=int, help="starts importing batches from a given batch")
    parser.add_argument('--max-batches', dest='max_batches', action='store', type=int, help="Maximum amount of batches imported")
    return parser		 


def get_batcher_args(options):									
    """ Takes namespace and filters batcher arguments

    Gets namespace with arguments parsed by parse_arguments 
    Filters only the batcher arguments 
    Stores arguments in a dictionary of keywords (**kw) for "run_in_batches"
    e.g. run_in_batches(iterable, end_batch, **get_batcher_args(options))
    """ 
    kw_temp = vars(options)
    kw = dict()											
    for i, j in kw_temp.items():							 
        if i in ('batch_size', 'batch_start', 'max_batches'):
            if j is not None:
                kw.update({i:j})
    return kw										

									



