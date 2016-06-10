## disk-scheduling-visualizer
A python utility to visualize disk scheduling algorithms

The algorithms implemented are `SCAN` & `LOOK` (not the circular versions i.e. `CSCAN` & `CLOOK`).

You can provide input, by modifying the below lines in the code.

```
requestQ = [request(2, 0), request(156, 0), request(78, 0), request(192, 0),
            request(19, 30), request(127, 30), request(90, 30), request(100, 150),
            request(140, 150), request(60, 200)]
```

Each of the entry is a named tuple consisting of the track number, and the time of request.

You can change the algorithm to look or scan by modifyinh the corresponding line.

    alg = AL_LOOK

It will display a formatted table showing the way the requests are serviced.

#### Sample output
```
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
```

Additionally, if you have matplotlib installed, it will render a graph too.

![screenshot](/screenshot.png?raw=true)
