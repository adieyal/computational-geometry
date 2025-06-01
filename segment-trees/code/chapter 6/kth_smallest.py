def kth_smallest(left_root, right_root, l, r, k):
    if l == r:
        return l

    mid = (l + r) // 2
    left_count = tree_val[lchild[right_root]] - tree_val[lchild[left_root]]

    if k <= left_count:
        return kth_smallest(lchild[left_root], lchild[right_root], l, mid, k)
    else:
        return kth_smallest(rchild[left_root], rchild[right_root], mid + 1, r, k - left_count)