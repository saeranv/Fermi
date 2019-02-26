require 'openstudio'
require 'json'
require 'open3'

#osmpath = File.join(Dir.pwd, "..", "..", "resources", "office", "office", "run", "in.idf")
osmpath = File.join(Dir.pwd, "..", "resources", "office", "office", "run", "in.osm")

#File.file?(osmpath)

model = OpenStudio::Model::Model.load(osmpath).get
#workspace = OpenStudio::Workspace.load(osmpath).get

#puts model.getSpaces
#puts model.methods
#zones = workspace.getObjectsByType("Zone".to_IddObjectType)

# get model objects
objs = model.getThermalZones

#puts ""
#puts "Print names!"
#puts ""

# do stuff
#objs.each do |obj|
#    puts obj.name
#end 

testjson = {
    objs[0].name => ['hello','world'],
    objs[1].name => 2
}

$stdout.puts JSON[testjson]
