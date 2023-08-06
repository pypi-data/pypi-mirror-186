def flatten_list(my_list):
    """flatten nested list"""
    flat_list = []
    for sublist in my_list:
        for num in sublist:
            flat_list.append(num)
    return flat_list


def truncate_list(my_list, maxlen, truncating):
    """truncate list"""
    curlen = len(my_list)
    remlen = curlen - maxlen
    if truncating == 'pre':
        truncated_list = slice(remlen, curlen)
        my_list = my_list[truncated_list]
    elif truncating == 'post':
        for i in range(0, remlen):
            my_list.pop()
    return my_list


def pad_sequences(sequences, maxlen=None, padding='pre', truncating='pre', value=0):
    """
    Pads sequences to the same length.
    :param sequences: List of sequences (integer)
    :param maxlen: maximum length of all sequences.
    :param padding: 'pre' or 'post' (defaults to 'pre')
    :param truncating: 'pre' or 'post' (defaults to 'pre')
    :param value: padding value (defaults to 0. integer)
    :return: Numpy array
    """
    import numpy
    import itertools
    import copy
    sequences = copy.deepcopy(sequences)

    cnt = 0
    for sequence in sequences:
        if len(sequence) < maxlen:  # if current sequence is shorter than maxlen,
            if padding == 'pre':
                temp = [value] * (maxlen - len(sequence))
                nested_seq = [sequence]
                nested_seq.insert(value, temp)
                sequence = list(itertools.chain(*nested_seq))  # flatten
                # sequence = flatten_list(nested_seq)
                sequences[cnt] = sequence
            elif padding == 'post':
                sequence += [value] * (maxlen - len(sequence))  # add padding 0 until maxlen in post-position
        elif len(sequence) > maxlen:  # else if current sequence is larger than maxlen,
            sequence = truncate_list(sequence, maxlen, truncating)
            sequences[cnt] = sequence
        cnt += 1
    return numpy.array(sequences)
