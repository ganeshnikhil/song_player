
# Music Player

This is a simple music player program written in Python. It allows you to navigate through a list of songs, play, pause, and resume them. The program uses the pynput and pygame libraries to handle keyboard input and audio playback.

## Prerequisites

Before running the program, make sure you have the following dependencies installed:

- pynput
- pygame
- mutagen

You can install these dependencies using pip:

```
pip install -r requirements.txt
```

The `requirements.txt` file contains a list of the required Python packages along with their versions. Running the above command will install all the dependencies automatically.

## Usage

1. Clone the repository or download the code files.

2. Open the terminal or command prompt and navigate to the directory where the code files are located.

3. Run the program using the following command:

```
python music_player.py
```

4. The program will display a list of songs available for playback. Use the arrow keys to navigate through the list and press Enter to play a song. You can also use the left and right arrow keys to navigate through the history of played songs.

5. While a song is playing, you can press 'q' to pause the song and 'r' to resume playback.

6. Press the Esc key to exit the program.

## Configuration

The program uses a JSON file, `data.json`, to store the number of times each song has been played. If the file doesn't exist or is empty, the program will create it and initialize the play count for each song to zero.

You can modify the `path.json` file to specify the directory where your music files are located. Update the `path` value with the appropriate path to your music directory.

## Contributing

Contributions to this music player program are welcome. If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This music player is open-source and released under the [MIT License](LICENSE).

Feel free to customize and modify the code to suit your needs.

## Acknowledgments

- The program uses the pynput and pygame libraries to handle keyboard input and audio playback.
- The mutagen library is used to retrieve the duration of audio files.
- Thanks to the open-source community for providing helpful resources and libraries.