# YouTube Embed Link Parser

## Description
This Python script extracts YouTube video IDs from `<iframe>` elements containing `embed` links and converts them into shortened `youtu.be` links. If the input does not contain a properly formatted `<iframe>` tag with a YouTube `embed` URL, the script returns `None`.

## How It Works
- The script prompts the user for an HTML string as input.
- It searches for a valid YouTube embed link within an `<iframe>`'s `src` attribute.
- If a valid link is found, it extracts the video ID and converts it into a `youtu.be` URL.
- If no valid `<iframe>` is found, it returns `None`.

## Installation & Usage
### Requirements
- Python 3.x

### Running the Script
1. Clone this repository or download `watch.py`.
2. Open a terminal and navigate to the script’s directory.
3. Run the script:
   python watch.py
4. Enter an HTML string containing an `<iframe>` tag with a YouTube embed link when prompted.
5. The script will return the converted `youtu.be` link or `None` if no valid iframe is found.

## Example Usage
### ✅ Valid Input
#### Input:
<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>

#### Output:
https://youtu.be/dQw4w9WgXcQ


### ❌ Invalid Inputs
#### Input:
https://www.youtube.com/embed/dQw4w9WgXcQ

#### Output:
None

#### Input:
src="https://www.youtube.com/embed/dQw4w9WgXcQ"

#### Output:
None


## License
This project is open-source and available under the MIT License.

