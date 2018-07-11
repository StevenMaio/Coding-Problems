def checkio(words_set):
    for w in words_set:
        w_length = len(w)

        # Generate a list of all the other words in words_set whose length is
        # at least as long as w's 
        cand = (list(filter(lambda x: len(x) >= w_length and x != w, words_set)))

        # Determine if any of the candidates ending is equal to w
        for c in cand:
            c_length = len(c)

            if c[c_length - w_length:] == w:
                return True

    return False

def main():
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print('Tests complete!')

if __name__ == '__main__':
    main()