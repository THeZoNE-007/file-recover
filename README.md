# File Recovery and Carving Tool

## Overview

This Python script automates file recovery and carving using either **Scalpel** or **MagicRescue**, based on the user's choice. It allows users to specify the tool, input file/disk, output directory, and configuration file (if applicable). This tool is useful for digital forensics and data recovery tasks.

---

## Features

### Key Functionality
1. **File Carving with Scalpel**:
   - Uses Scalpel to carve files from a disk image or raw data.
   - Requires a configuration file to define file types and patterns.

2. **File Recovery with MagicRescue**:
   - Uses MagicRescue to recover files based on predefined recipes.
   - Extracts recoverable files to a specified output directory.

3. **User Choice**:
   - The script dynamically selects between Scalpel and MagicRescue based on the user's input.

---

## Requirements

### Prerequisites
- Python 3.x
- Required tools installed on your system:
  - [Scalpel](https://github.com/sleuthkit/scalpel)
  - [MagicRescue](https://www.forensicswiki.org/wiki/Magic_Rescue)

### Installation
1. Install the required tools:
   ```bash
   sudo apt-get install scalpel magicrescue
   ```

2. Clone this repository:
   ```bash
   git clone "https://github.com/THeZoNE-007/file-recover.git"
   cd file-recover
   ```

---

## Usage

### Running the Script
1. Ensure you have the necessary inputs ready:
   - Input file/disk (e.g., a disk image or raw data).
   - Output directory where recovered/carved files will be stored.
   - Configuration file for Scalpel (if using Scalpel).

2. Run the script using the following command:
   ```bash
   python recovery.py <tool_name> <input_file> <output_directory> <config_file>
   ```
   Example for Scalpel:
   ```bash
   python recovery.py scalpel disk_image.dd /path/to/output /path/to/scalpel.conf
   ```

   Example for MagicRescue:
   ```bash
   python recovery.py magicrescue disk_image.dd /path/to/output recipe_name
   ```

3. The script will execute the chosen tool and store the results in the specified output directory.

---

## Notes

1. **Permissions**: Both Scalpel and MagicRescue require root privileges. Ensure the script is executed with `sudo` if necessary.
2. **Configuration Files**:
   - For Scalpel, provide a valid configuration file (e.g., `scalpel.conf`).
   - For MagicRescue, specify the recipe name (e.g., `jpg`, `pdf`, etc.) corresponding to the file type you want to recover.
3. **Output Directory**: Ensure the output directory exists or is writable by the script.

---

## Acknowledgments

- Inspired by digital forensics techniques for file recovery and carving.
- Built using the Scalpel and MagicRescue tools for efficient data extraction.
