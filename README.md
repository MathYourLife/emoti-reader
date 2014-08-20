# emoti-reader

My playground for creating a system to track and display the emotion of a book while being read

## Test Books

Based on the suggestions from some trusted former colleagues at Newmarket, these books cover a wide range of emotions from various characters.

* Memoir by Cheryl Strayed called Wild
* a John Irving book
* Ordinary Grace by William Kent Krueger
* Through Black Spruce by Joseph Boyden
* The Art of Fielding
* The Book Thief
* Alena, by Rachel Pastan
* Fault in our Stars, by John Green
* Pillars of the earth


## Current Status

Use heka as an input stream.  Through chef, heka is configured to
listen on port 9326 for any interface (0.0.0.0).  The input stream brakes
the stream into packages with the period `.` delimiter.

Currently the output stream is just writing to a file, but will eventually
feed the sentences to a language parsing service through another of heka's
output streams (possibly AMQP).

## Development Environment

For testing, the emoti-reader service is deployed through a chef
cookbook found in [./chef](chef)

### Chef Provisioning

The [emoti_reader](chef/emoti_reader) cookbook is configured to converge
a host on ubuntu trusty64 with test-kitchen and utilize the following
community cookbooks.

```ruby
cookbook 'heka', git: 'git://github.com/augieschwer/chef-cookbook-heka.git'
cookbook 'zookeeper', git: 'git://github.com/SimpleFinance/chef-zookeeper.git'
cookbook 'kafka', git: 'git://github.com/mthssdrbrg/kafka-cookbook.git'
cookbook 'python'
cookbook 'leiningen', git: 'git://github.com/runa-labs/chef-leiningen.git'
```

```bash
cd chef/emoti_reader
bundle exec kitchen converge default-ubuntu-trusty64
```

## Input


### Heka Parsing

Written in go, so fairly efficient.  May not have the outputs required
in its standard set as of `0.6.0`.

```
$ telnet 127.0.0.1 9326
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
This is the first sentence.
and now the
second is wrapped.
But the 3rd. Is joined with the 4th. and 5th.
^]

telnet> Connection closed.
```

The input string is parsed by the `.` and fed to the LogOutput.

```
$ tail /var/log/hekad.log
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

###


## Kafka

Kafka is installed with the base
[community cookbook](https://github.com/mthssdrbrg/kafka-cookbook). It is
configured to listen for incoming events on port 9092, and use the
localhost [zookeeper service](https://github.com/SimpleFinance/chef-zookeeper)
that is listening on port 2181.

## NLTK

The python nltk library along with supporting corpus (stopwords, book,
brown, punkt) are installed, but not certain how well they would scale
especially in a multi-language environment.

## tf-idf

A more general approach looking at the comparative relative frequency of
terms to determine their importance.  This approach is more language
agnostic, but will need to deal with issues such as varied spellings for the
same term such as verb tense.

### Similarity Scores

**Levenshtein**

The fewer number of character changes required to convert one word into the
other is the measure of their distance.

## StreamParse

Possible candidate for term tf-idf use.
