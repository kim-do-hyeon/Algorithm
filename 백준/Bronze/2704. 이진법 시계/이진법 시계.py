import sys

def to_3col_bits(h, m, s):
    values = [h, m, s]
    bits = []

    power = 5
    while power >= 0:
        idx = 0
        while idx < 3:
            value = values[idx]
            if (value >> power) & 1:
                bits.append('1')
            else:
                bits.append('0')
            idx += 1
        power -= 1

    return "".join(bits)


def to_3row_bits(h, m, s):
    values = [h, m, s]
    bits = []

    idx_val = 0
    while idx_val < 3:
        power = 5
        while power >= 0:
            value = values[idx_val]
            if (value >> power) & 1:
                bits.append('1')
            else:
                bits.append('0')
            power -= 1
        idx_val += 1

    return "".join(bits)


def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    t = int(data[0])
    line_idx = 1

    out_lines = []

    i = 0
    while i < t:
        time_str = data[line_idx].strip()
        line_idx += 1

        h_str, m_str, s_str = time_str.split(':')
        h = int(h_str)
        m = int(m_str)
        s = int(s_str)

        bits_3col = to_3col_bits(h, m, s)
        bits_3row = to_3row_bits(h, m, s)

        out_lines.append(bits_3col + " " + bits_3row)
        i += 1

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
