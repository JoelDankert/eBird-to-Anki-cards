# eBird Media Downloader

This repository provides tools to automate the download and preparation of bird sound and image data from the [eBird](https://ebird.org/) and [Macaulay Library](https://macaulaylibrary.org/) platforms. The media is formatted for use in applications such as **Anki** flashcards.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [CSV Output Format](#csv-output-format)
- [Limitations](#limitations)
- [License](#license)

---

## Overview

There are two main scripts:

- `converter.py`  
  Downloads bird audio and images using species codes and prepares them for Anki flashcards.
  
- `generatecsv.py`  
  Scans your downloaded audio files and generates a `CSV` file where each row maps a bird name to an audio clip.

---

## Features

- Downloads bird audio recordings from the eBird Macaulay Library
- Optionally trims audio clips (5s to 35s)
- Downloads a representative bird image per species
- Generates a semicolon-separated `CSV` for Anki import (`bird name ; [sound:filename.mp3]`)
- Automatic fallback if some sound IDs are not available

---

## Requirements

- Python 3.x
- [`pydub`](https://pydub.com/) (`pip install pydub`)
- [`requests`](https://pypi.org/project/requests/`)
- `ffmpeg` installed and in your system path (required by pydub)

---

## Installation

```bash
pip install pydub requests
```

Ensure `ffmpeg` is installed and accessible from your terminal:

```bash
ffmpeg -version
```

---

## Usage

### 1. Prepare Input List

Create a file called `species.txt` with one species per line, in the following format:

```
CommonName;SpeciesCode
```

Example:
```
Eurasian Blackbird;eurbla
European Robin;eurrob
```

### 2. Run the Downloader

```bash
python converter.py
```

This will:

- Fetch and trim 10 top-rated audio recordings per species
- Download one representative image per species
- Store the media in the specified folders

### 3. Generate the CSV for Anki

```bash
python generatecsv.py
```

This creates `out.csv`, mapping each audio file to its bird name using the Anki `[sound:filename.mp3]` format.

---

## CSV Output Format

Each line in `out.csv` has the format:

```
Eurasian Blackbird(1);[sound:Eurasian Blackbird_1.mp3]
Eurasian Blackbird(2);[sound:Eurasian Blackbird_2.mp3]
...
```

You can import this directly into Anki with one column for the bird name and one for the sound.
(i suggest using the mediaimport plugin to import all the audio and image files properly)

---

## Limitations

- The script assumes German-region filtering in eBird (`regionCode=DE`)
- Only the top-rated audio recordings are used
- No automatic retries for failed downloads
- Uses static paths — modify `desiredfolder` and `desiredfolderimg` as needed

---

## License

This project is for educational and personal use only. No official affiliation with eBird or the Macaulay Library.

