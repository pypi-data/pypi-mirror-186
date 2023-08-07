import requests

class Tweet:
	def __init__(self, id:int):
		self.id = id
	__data= requests.get("https://cdn.syndication.twimg.com/tweet-result?id="+str(id)).json()
	
	full_text = __data['text']
	text = __data['text'][__data['display_text_range'][0]:__data['display_text_range'][1]]
	created_at = __data['created_at']
	lang = __data['lang']
	possibly_sensitive = __data['possibly_sensitive']
	id_str = __data['id_str']
	
	
	def __str__(self):
		return f"tweet id: {id}"
