#!/usr/bin/env python3

import os
import argparse

from video2audio import AVFile


def main():
    parser = argparse.ArgumentParser(
        description='Extract audio from a video file.  The output is one mp3 file for each chapter in the video.',
    )
    parser.add_argument(
        '-t',
        '--track-number',
        type=int,
        default=0,
        help='which audio track (i.e. stream) to extract (0-indexed) (default: 0)',
    )
    parser.add_argument(
        '-o',
        '--overwrite',
        action='store_true',
        default=False,
        help='overwrite existing files in output dir (default: False)',
    )
    parser.add_argument(
        '--artist',
        type=str,
        help='artist name, to add to output metadata',
    )
    parser.add_argument(
        '--album',
        type=str,
        help='album name, to add to output metadata',
    )
    parser.add_argument('input-file', type=str, help='video filename')
    parser.add_argument(
        'output-path', type=str, help='directory where output mp3(s) will be saved'
    )
    # TODO?: allow specifying output filename(s) somehow
    args = parser.parse_args()
    filename = getattr(args, 'input-file')
    output_dir = getattr(args, 'output-path')
    os.makedirs(output_dir, exist_ok=True)
    f = AVFile(filename)
    metadata_dict = {}
    if args.artist is not None:
        metadata_dict['artist'] = args.artist
        # TODO: should we use 'composer' or 'album_artist' instead of 'artist'?
    if args.album is not None:
        metadata_dict['album'] = args.album
    f.extract_all_chapters_audio(
        output_dir,
        stream=args.track_number,
        overwrite=args.overwrite,
        metadata_dict=metadata_dict,
    )
    # TODO: print result(s) / return exit code


if __name__ == '__main__':
    main()
