import argparse
import sys
import random
import time

def write(text, sleeptime=0):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(sleeptime)

def stutter(text, sleeptime):
    individual_sleeptime = sleeptime / len(text)
    for char in text[:-1]:
        write(char, individual_sleeptime)
    write(text[-1], 0)

songs = { }
def song_list(songs_dict):
    return ", ".join([key for key in songs_dict.keys()])

def doop():
    write("doop", 0.4)
    stutter("...\n", 1.2)
    write("doop", 0.4)
    stutter("...\n", 1.2)
    write("doo", 0.15)
    write(" doo", 0.25)
    stutter("...\n", 1.2)
    write("doo", 0.15)
    write(" doo", 0.25)
    stutter("...\n", 1.2)
    stutter("dooooooooooo\n", 1.6)
songs["doop"] = doop

def lala():
    for i in range(0, 400):
        write("la", 0.0025)
        if random.randint(0, 20) == 1:
            write("\n", 0)
        write("\n")
songs["lala"] = lala

def DOOP():
    stutter("...\n", 3)
    write("DOOP\n", 0.05)
songs["DOOP"] = DOOP

def spencersong():
    stutter(["Spencer", " is", " da", " best!", "\n"], 1.4)
    stutter(["I", " love", " him", " lots!", "\n"], 1.4)
    stutter(["la", " la", " la", " la", " la!", "\n"], 1.4)
    stutter(["la", " la", " la", " la", " la!", "\n"], 1.4)
songs["spencersong"] = spencersong

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="ls",
            description='l.s. -> love song.')
    parser.add_argument('song', metavar='s',
        help='Which song to play. Available songs: {}'.format(song_list(songs)))
    args = parser.parse_args()
    try:
        song = songs[args.song]
        song()
    except KeyError:
        print("Song {} not available...".format(args.song))

