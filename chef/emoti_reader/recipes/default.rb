#
# Cookbook Name:: emoti_reader
# Recipe:: default
#
# Copyright (C) 2014
#
#
#

include_recipe 'heka'

template '/etc/heka/readin.toml' do
  source 'heka/readin.toml.erb'
  notifies :restart, 'service[heka]'
end