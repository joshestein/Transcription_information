AUDIO_DIR="/Users/joshstein/Documents/UCT/Engineering/4th_year/Design/Videos/"

function convert_to_wav {
        for i in *.mp4; do
                ffmpeg -loglevel fatal -i "$i" "${i%.*}.wav";
        done
}

function split_into_pieces {
        for i in *.wav; do
                FILE_NAME=${i%.wav};    # remove extension
                OUT_FILE=$FILE_NAME-%03d.wav
                ffmpeg -loglevel fatal -i "$i" -f segment -segment_time 50 -c copy $OUT_FILE;
        done

        find . -type f -name '*[^0-9].wav' -delete # delete original files
}

cd $AUDIO_DIR
convert_to_wav
split_into_pieces
