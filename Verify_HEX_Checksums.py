# HEX records
hex_data = """
:0100000002FD
:0100010000FE
:0100020004F9
:0100030001FB
:0100040007F4
:010005004FAB
:0100060000F9
:0100070011E7
:0100080053A4
:0100090000F6
:01000A0000F5
:01000B0000F4
:01000C0000F3
:01000D0000F2
:01000E0000F1
:01000F0000F0
:0100100000EF
:0100110000EE
:0100120000ED
:0100130000EC
:0100140000EB
:0100150000EA
:0100160000E9
:0100170000E8
:0100180000E7
:0100190000E6
:01001A0000E5
:01001B0000E4
:01001C0000E3
:01001D0000E2
:01001E0000E1
:01001F0000E0
"""
hex_data2 = """
:0100000001FE
:0100010000FE
:0100020009F4
:0100030002FA
:0100040000FB
:010005008C6E
:0100060000F9
:0100070011E7
:0100080042B5
:0100090000F6
:01000A0000F5
:01000B0000F4
:01000C0000F3
:01000D0000F2
:01000E0000F1
:01000F0000F0
:0100100000EF
:0100110000EE
:0100120000ED
:0100130000EC
:0100140000EB
:0100150000EA
:0100160000E9
:0100170000E8
:0100180000E7
:0100190000E6
:01001A0000E5
:01001B0000E4
:01001C0000E3
:01001D0000E2
:01001E0000E1
:01001F0000E0
"""


def calculate_checksum(record):
    # Remove the starting colon
    record = record[1:]

    # Split into bytes
    bytes_record = [record[i: i +2] for i in range(0, len(record), 2)]

    # Convert hex bytes to integers
    int_bytes = [int(byte, 16) for byte in bytes_record]

    # Calculate the checksum
    checksum = sum(int_bytes[:-1]) & 0xFF
    checksum = (~checksum + 1) & 0xFF
    return checksum


def verify_hex_checksums():
    # Split the multi-line string into individual records
    records = hex_data.strip().split('\n')

    # Verify checksums
    results = [(record, calculate_checksum(record) == int(record[-2:], 16)) for record in records]

    # Print results
    for record, is_valid in results:
        print(f"{record} - Checksum {'Correct' if is_valid else 'Incorrect'}")
    record_length = len(results)
    print(f"{record_length} - {'Correct Number of Entries' if record_length == 32 else 'Incorrect Number of Entries'}")


if __name__ == "__main__":
    verify_hex_checksums()
