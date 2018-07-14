extends RichTextLabel

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	print("label ready")
	var n = get_node("../../server")
	n.connect("request",self,"_on_modify_text")
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func _on_modify_text(text):
	print("request caugh")
	self.text = text
	print (text)
	self.update()
