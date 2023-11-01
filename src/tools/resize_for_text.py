base_px = 700
char_px = 11

def resize_for_text(text):
    size = len(text)
    if size > 6:
        print(f'size: {size}')
        x = base_px - char_px*(size-6)
        return x
    else:
        return base_px