def generate_sysex_file(presets):
    syx_data = bytearray()

    # Sysex header
    syx_data.append(0xF0)  # Start of Sysex
    syx_data.append(0x00)  # Manufacturer ID (replace with actual ID)
    syx_data.append(0x20)  # Device ID (replace with actual ID)

    for preset in presets:
        # Start of preset message
        syx_data.append(0x01)  # Model ID (replace with actual ID)
        syx_data.append(0x02)  # Command ID for preset assignment

        # Add preset data
        for parameter in preset:
            syx_data.append(parameter)

        # End of preset message
        syx_data.append(0xF7)  # End of Sysex

    with open('presets.syx', 'wb') as f:
        f.write(syx_data)

# Example presets data (replace with actual presets data)
presets = [
    [0x00, 0x7F, 0x3C, 0x00],  # Preset 1
    [0x01, 0x64, 0x45, 0x7F],  # Preset 2
    # Add more presets as needed
]

generate_sysex_file(presets)
