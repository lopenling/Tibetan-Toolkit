def string_to_segments(string, as_list=False, to_clipboard=False):

    '''Takes in a string and returns a list of segments. Segments are defined as
    a string of characters between two །. The ། are included in the segments.
    
    string | str | A string of Tibetan text.
    as_list | bool | If True, returns a list of segments. If False, prints the
    segments to the console.
    '''

    import pyperclip

    out = [i + '།' for i in string.replace(' ', '').split('།') if len(i) > 0]
    
    if to_clipboard:
        pyperclip.copy('\n'.join(out))

    if as_list:
        return out

    else:
        for i in out:
            print(i)
