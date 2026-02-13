import lzma

lzma2_filter = [{
    "id": lzma.FILTER_LZMA2,
    "dict_size": 32 * 1024 * 1024,
    "lc": 3,
    "lp": 0,
    "pb": 2
}]


with open("Final Telemetric dataset.xlsx", 'rb') as f_in, lzma.open(
    'CFinal Telemetric dataset.xlsx', 'wb', format=lzma.FORMAT_RAW, filters=lzma2_filter
) as f_out:
    f_out.write(f_in.read())


with lzma.open(
    'CFinal Telemetric dataset.xlsx', 'rb', format=lzma.FORMAT_RAW, filters=lzma2_filter
) as f_in, open('DFinal Telemetric dataset.xlsx', 'wb') as f_out:
    f_out.write(f_in.read())

with open("Final Telemetric dataset.xlsx", 'rb') as f1, open('DFinal Telemetric dataset.xlsx', 'rb') as f2:
    original = f1.read()
    decompressed = f2.read()
    match_count = sum(a == b for a, b in zip(original, decompressed))
    total = max(len(original), len(decompressed))
    percent = (match_count / total * 100) if total > 0 else 0
    print(f"Accuracy: {percent:.2f}%")