# rubocop:disable LineLength, SingleSpaceBeforeFirstArg, Style/RescueModifier

name             'emoti_reader'
maintainer       'Daniel Robert Couture'
maintainer_email 'mathyourlife@gmail.com'
license          'MIT'
description      'Installs/Configures emoti_reader'
long_description IO.read(File.join(File.dirname(__FILE__), 'README.md'))
version          IO.read(File.join(File.dirname(__FILE__), 'VERSION')) rescue '0.0.1'

depends 'apt'
depends 'heka'
depends 'runit'
depends 'zookeeper'
depends 'kafka'
depends 'python'
depends 'leiningen'
depends 'storm'
