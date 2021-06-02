def createlps(p):
    # every lps is 0
    lps = [0]*len(p)
    # two pointers,
    # prefix at index 0
    # curr at index 1
    prefix = 0
    curr = 1

    while curr < len(p):
        # if found equal move both index
        # and check for next word
        if p[curr] == p[prefix]:
            lps[curr] = prefix + 1
            curr += 1
            prefix += 1
        else:  # if not found equal and
            # if prefix is at index 0
            # that is, if it cannot go backwards anymore then
            # obviously curr will have to move forward
            # to check for next word
            if prefix == 0:
                lps[curr] = 0
                curr += 1
            else:  # if not found equal and
                # if prefix is at random index except 0
                # then keep moving prefix backwards
                prefix = lps[prefix-1]
    return lps


def kmp(s, p):
    n, m = len(s), len(p)
    lps = createlps(p)

    # string pointer
    # pattern pointer
    sp, pp = 0, 0

    while sp < n:
        # if words are found equal
        # then move both index forward
        if s[sp] == p[pp]:
            sp += 1
            pp += 1
        else:  # if not equal then
            # check if pattern pointer(pp)
            # cannot go backward anymore
            # if it cant, then move the
            # string pointer(sp) and check
            # for next word
            if pp == 0:
                sp += 1
            else:  # if not equal and
                # pp can move backwards then
                # move it to the position where
                # last equal was found
                pp = lps[pp-1]
        # if pp has reached the end of pattern string
        # that means all s[sp] == p[pp],
        # that means, a pattern has been found
        # so we print the pattern
        if pp == m:
            print("pattern found starting at", sp-pp)
            pp = lps[pp-1]


kmp("abc", "c")
