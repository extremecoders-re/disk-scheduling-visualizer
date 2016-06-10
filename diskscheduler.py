'''
A python program to implement LOOK and SCAN disk scheduling algorithms.

Author: ExtremeCoders

Input to the program is a list of tuples (request track, request time).
The program computes the way a scheduler would service those requests.
If you have matplotlib installed it would also display a graph.

Sample output

Track Range : 0 - 199
Starting Track : 89
Starting Direction : LOW
Algorithm : LOOK

      TIME      |     TRACK
----------------|----------------
       0        |       89
       11       |       78
       70       |       19
       87       |       2
      175       |       90
      185       |      100
      212       |      127
      225       |      140
      241       |      156
      277       |      192
      409       |       60
'''

import collections

# ==============================================================================
request = collections.namedtuple('request', ['track', 'time'])

DIRN_LO = 0
DIRN_HI = ~DIRN_LO

AL_SCAN = 1
AL_LOOK = 2

# Table cell width
CELL_WIDTH = 16
# ==============================================================================


# Provide your input below

requestQ = [request(2, 0), request(156, 0), request(78, 0), request(192, 0),
            request(19, 30), request(127, 30), request(90, 30), request(100, 150),
            request(140, 150), request(60, 200)]

TRACK_LO = 0
TRACK_HI = 199

STARTING_TRACK = 89
STARTING_DIRN = DIRN_LO

alg = AL_LOOK
# ==============================================================================


def formatstr(val):
    return ('{: ^%ds}' %CELL_WIDTH).format(str(val))


def displayTable(servicedList):
    col1 = formatstr('TIME')
    col2 = formatstr('TRACK')
    line = col1 + '|' + col2
    print line
    print '-'*(len(line) / 2) + '|' + '-'*(len(line) / 2)
    for time, track in servicedList:
        print '%s|%s' %(formatstr(time), formatstr(track))


def displayGraph(servicedList):
    try:
        import matplotlib.pyplot as plt
    except:
        print 'Matplotlib is not installed! Cannot plot'
        return

    X_track = [track for time, track in servicedList]
    Y_time = [-time for time, track in servicedList]

    plt.xlabel('Track no')
    plt.ylabel('Time')
    plt.title('DISK Scheduling Algorithm : %s' %('LOOK' if alg == AL_LOOK else 'SCAN'))
    plt.xticks(X_track[1:])
    plt.yticks(Y_time[1:], map(lambda x: str(-x), Y_time[1:]))
    plt.grid(True)
    plt.plot(X_track, Y_time, marker='o')
    plt.show()

def main():
    dirn = STARTING_DIRN
    track = STARTING_TRACK
    time = 0
    servicedList = []
    servicedList.append((time, track))

    while len(requestQ) > 0:
        time += 1
        track += 1 if dirn == DIRN_HI else -1

        if alg == AL_SCAN:
            # requests remaining to be serviced at the current instant
            pendingRequests = filter(lambda request: request.time <= time, requestQ)
            pendingTracks = map(lambda request: request.track, pendingRequests)

            if pendingTracks.count(track) > 0:
                servicedList.append((time, track))
                requestQ.remove(pendingRequests.pop(pendingTracks.index(track)))

            if dirn == DIRN_LO and track == TRACK_LO:
                servicedList.append((time, track))
                dirn = ~dirn

            elif dirn == DIRN_HI and track == TRACK_HI:
                servicedList.append((time, track))
                dirn = ~dirn

        elif alg == AL_LOOK:
            # requests remaining  to be serviced at the current instant
            pendingRequests = filter(lambda request: request.time <= time, requestQ)

            # requests remaining to be serviced at the current instant in the movement direction
            if dirn == DIRN_LO:
                pendingRequests = filter(lambda request: request.track <= track, pendingRequests)
            else:
                pendingRequests = filter(lambda request: request.track >= track, pendingRequests)

            pendingTracks = map(lambda request: request.track, pendingRequests)

            if pendingTracks.count(track) > 0:
                servicedList.append((time, track))
                requestQ.remove(pendingRequests.pop(pendingTracks.index(track)))

            if len(pendingRequests) == 0 or track == TRACK_LO or track == TRACK_HI:
                dirn = ~dirn

    displayTable(servicedList)
    displayGraph(servicedList)


if __name__ == '__main__':
    print 'Track Range : %d - %d' %(TRACK_LO, TRACK_HI)
    print 'Starting Track : %d' %STARTING_TRACK
    print 'Starting Direction : %s' %('LOW' if STARTING_DIRN == DIRN_LO else 'HIGH')
    print 'Algorithm : %s' %('LOOK' if alg == AL_LOOK else 'SCAN')
    print
    main()
