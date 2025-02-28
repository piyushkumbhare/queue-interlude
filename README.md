# Erm, Queue Interlude

## Dependencies

Developed under POSIX environment assumptions. Requires:

1. `uv` to manage python environment and dependencies
2. `playerctl` to detect Falling Away With You without any Network calls
3. `.env` to be populated with `CLIENT_SECRET` and `CLIENT_ID` setup. See the *[Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)* for more details

## Running

To run as a standalone foreground process, you can run either:
```sh
python3 main.py
```

or:

```sh
uv run main.py
```
(the latter is recommended).

To background the process, run
```sh
./erm-queue-interlude.sh
```
This will take care of detecting duplicate processes for you and prevent multiple instances from being spawned.

## First execution

Upon the first execution of the program, you will be asked to authenticate via Spotify's OAuth. This should open a tab in your browser asking you to sign in with Spotify. The program will not work without this.

## What does this actually even do?

It's quite simple, really. 

> Monkey see *Falling Away With You* by Muse playing, monkey queue *Interlude* by Muse
