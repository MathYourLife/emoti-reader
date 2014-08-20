

default["emoti_reader"]["readin"] = {
  "port" => 9326
}
default["emoti_reader"]["kafka"] = {
  "port" => 9092
}
normal[:lein][:user] = "root"
normal[:lein][:group] = "root"
default["emoti_reader"]["nltk"] = {
  "pkgs" => %w{ stopwords book brown punkt }
}