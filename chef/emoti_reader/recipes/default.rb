#
# Cookbook Name:: emoti_reader
# Recipe:: default
#
# Copyright (C) 2014
#
#
#

include_recipe 'heka'
include_recipe 'python::pip'

template '/etc/heka/readin.toml' do
  source 'heka/readin.toml.erb'
  variables(
    :readin_port => node["emoti_reader"]["readin"]["port"]
  )
  notifies :restart, 'service[heka]'
end

include_recipe 'runit'
include_recipe 'zookeeper'
include_recipe 'zookeeper::service'
include_recipe 'kafka'

template '/opt/kafka/config/server.properties' do
  source 'kafka/server.properties.erb'
  variables(
    :kafka_port => node["emoti_reader"]["kafka"]["port"]
  )
  notifies :restart, 'service[kafka]'
end


include_recipe 'leiningen'

python_pip 'streamparse'