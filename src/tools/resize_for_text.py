base_px = 700
char_px = 10

def resize_for_text(text):
    size = len(text)
    if size > 5:
        w_n = len(text.split())
        print(f'size: {size}')
        x = base_px - (char_px*(size-7) + w_n*2)
        return x
    else:
        return base_px
