extends Node

signal request

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var srv  = TCP_Server.new()
var port = 8080
# Called when the node enters the scene tree for the first time.
func _ready():
	print("ready")

func _init():
	srv.listen(port)
	

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var cn = srv.take_connection()
	if(cn != null):
		var data = str(cn.get_partial_data(64)[1].get_string_from_ascii())
		print("emit request")
		emit_signal("request",data)