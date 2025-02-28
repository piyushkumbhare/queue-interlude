pgrep -f " queue-interlude.py" &>> /dev/null
ret=$?
# echo pgrep returned $ret

if [[ $ret -ne 0 ]]; then
    echo Starting process in background
    echo "NOTE: If you haven't authenticated (aka if this is your first time running the program, you should check your browser)"
    nohup uv run queue-interlude.py &>> /dev/null &
else
    echo Process seems to already be running
    echo "If you wish to kill it, run 'ps -efww | grep queue-interlude' and kill it manually, I ain't holding your hand."
fi
