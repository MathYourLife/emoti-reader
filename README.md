# emoti-reader

My playground for creating a system to track and display the emotion of a book while being read

## Current Status

Use heka as an input stream.  Through chef, heka is configured to
listen on port 9326 for any interface (0.0.0.0).  The input stream brakes
the stream into packages with the period `.` delimiter.

Currently the output stream is just writing to a file, but will eventually
feed the sentences to a language parsing service through another of heka's
output streams (possibly AMQP).

## Functional Testing

### Manually

```
cd chef/emoti_reader
bundle exec kitchen converge default-ubuntu-trusty64
```

wait for node to converge

```
bundle exec kitchen login default-ubuntu-trusty64
vagrant@default-ubuntu-trusty64:/etc/heka$ telnet 127.0.0.1 9326
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
This is the first sentence.
and now the
second is wrapped.
But the 3rd. Is joined with the 4th. and 5th.
^]

telnet> Connection closed.
vagrant@default-ubuntu-trusty64:/etc/heka$ tail /var/log/hekad.log
2014/08/14 04:03:35 MessageRouter started.
2014/08/14 04:03:35 Input started: TcpInput
2014/08/14 04:15:17 This is the first sentence.
2014/08/14 04:15:32
and now the
second is wrapped.
2014/08/14 04:15:52
But the 3rd.
2014/08/14 04:15:52  Is joined with the 4th.
2014/08/14 04:15:52  and 5th.
```

## Development Environment

For testing, the emoti-reader service is deployed through a chef
cookbook found in [./chef](chef)
