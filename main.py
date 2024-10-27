# --------------------------------------------------------------------------
# Copyright [2023] [Darie-Dragos Mitoiu]
#
# Licensed under the Darie-Dragos Mitoiu License, Version 1.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.dmitoiu.ro/licenses/LICENSE-1.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# --------------------------------------------------------------------------

import unicodedata
import sys
import re

def remove_unicode_styles(text):
    # Decompose Unicode characters into base characters
    normalized_text = unicodedata.normalize('NFKD', text)
    # Keep only ASCII characters, effectively removing diacritics and styles
    clean_text = ''.join(c for c in normalized_text if ord(c) < 128)
    return clean_text


if __name__ == '__main__':
    # Check if the script has received input and output file paths as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py unicode.txt ascii.txt")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        try:
            # Read the input file with utf-8 encoding
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
                print("Unicode Text:", text)  # Debugging output for verification

            # Remove Unicode styles
            plain_text = remove_unicode_styles(text)
            print("Processed Text:", plain_text)  # Debugging output for verification

            # Write the processed text to the output file with utf-8 encoding
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(plain_text)

            print(f"Processed ASCII text has been saved to {output_file}")

        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")