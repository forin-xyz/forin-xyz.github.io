# 'heap' is a heap at all indices >= startpos, except possibly for pos.  pos

# is the index of a leaf with a possibly out-of-order value.  Restore the

# heap invariant.

def _siftdown(heap, startpos, pos):

    newitem = heap[pos]

    # Follow the path to the root, moving parents down until finding a place

    # newitem fits.

    while pos > startpos:

        parentpos = (pos - 1) >> 1

        parent = heap[parentpos]

        if newitem < parent:

            heap[pos] = parent

            pos = parentpos

            continue

        break

    heap[pos] = newitem


def _siftup(heap, pos):

    endpos = len(heap)

    startpos = pos

    newitem = heap[pos]

    # Bubble up the smaller child until hitting a leaf.

    childpos = 2*pos + 1    # leftmost child position

    while childpos < endpos:

        # Set childpos to index of smaller child.

        rightpos = childpos + 1

        if rightpos < endpos and not heap[childpos] < heap[rightpos]:

            childpos = rightpos

        # Move the smaller child up.

        heap[pos] = heap[childpos]

        pos = childpos

        childpos = 2*pos + 1

    # The leaf at pos is empty now.  Put newitem there, and bubble it up

    # to its final resting place (by sifting its parents down).

    heap[pos] = newitem
