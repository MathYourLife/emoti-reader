# Chef Development Environment

I configured my workstation to use chef-dk along with vagrant/virtualbox
for a virtualized testing environment.

## Configuring Workstation

```bash
wget https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/12.04/x86_64/chefdk_0.2.0-2_amd64.deb
sudo dpkg -i chefdk_0.2.0-2_amd64.deb
mkdir -p ~/.chefdk
echo 'eval "$(chef shell-init bash)"' >> ~/.bashrc
echo 'export PATH="/opt/chefdk/embedded/bin:${HOME}/.chefdk/gem/ruby/2.1.0/bin:$PATH"' >> ~/.bashrc
wget https://dl.bintray.com/mitchellh/vagrant/vagrant_1.6.3_x86_64.deb
sudo dpkg -i vagrant_1.6.3_x86_64.deb

source ~/.bashrc
gem install bundler

chef generate cookbook emoti_reader
cd emoti_reader/
echo 'source "https://rubygems.org"' >> Gemfile
echo 'gem "test-kitchen", "=1.2.1"' >> Gemfile
echo 'gem "kitchen-vagrant"' >> Gemfile
echo 'gem "berkshelf",  "=3.1.4"' >> Gemfile

bundle install --path ./vendor/bundle/
bundle exec kitchen list
```
