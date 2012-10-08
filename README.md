# README

This is an experimental implementation of an API service that supports
a (read-only) subset of the [OSM v0.6 API][osmapi].

The goal for this project is to explore an implementation of the
[OSM API][osmapi] built over a distributed key/value store.  The
service has been designed to be easy to scale horizontally.

The implementation currently uses [Membase][membase] for the data
store; however its design should work with other key/value systems.

## Current Status

* This repository contains a working snapshot of the service.
* The server only supports read queries on map data.

## Future Work

Near term things that need to be done:

* A reimplementation of the front end servers, in C or Haskell.  I
  have come to be truly wary of using the [Twisted][] toolkit :).
* Data representations that are more frugal in memory consumption,
  so as to reduce hosting costs.

In the longer-term:

* Supporting "read/write" operation.
* Supporting multi-datacenter operation; coping with intermittent
  connectivity between data centers.
* Supporting "private" data layers over OSM data.

## Additional Information

The prototype was originally published under my previous employer's
[GitHub namespace][aolgh].  Future work will however be done in this
repository.

Information on how to use this software package may be found in the
project's [documentation][].

<!-- References -->

 [aolgh]: http://github.com/MapQuest/mapquest-osm-server
 [documentation]: https://github.com/MapQuest/mapquest-osm-server/blob/master/doc/Home.md
 [membase]: http://www.membase.org/ "Membase"
 [openissues]: http://github.com/MapQuest/mapquest-osm-server/issues?milestone=6&state=open
 [osmapi]: http://wiki.openstreetmap.org/wiki/API_v0.6 "OSM v0.6 API"
 [Twisted]: http://twistedmatrix.com/
