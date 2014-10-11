#!/usr/bin/env python
import fbconsole #install fbconsol using command "$ sudo pip install fbconsole"
import requests
import json


#Author : RakeshRathi

def commentlikepost(post_limit):
	''' Likes and comments post '''
	fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream']
	fbconsole.authenticate()
	#status = fbconsole.post('/me/feed', {'message':'Hello from python s script'})

	fbconsole.authenticate()
	query = fbconsole.fql("SELECT actor_id, post_id FROM stream WHERE source_id=me() LIMIT %s" % post_limit)
	print query
	for post in query:
		r = requests.get('https://graph.facebook.com/%s' % post['actor_id'])
		user = json.loads(r.text)
		comment = '%s  %s: Like and comment from python script! :)' % (user['first_name'] , user['last_name'])
		print comment
			
		#Reply comment
		comment_id = requests.post("https://graph.facebook.com/" + str(post['post_id'])
			+ "/comments/?access_token=" + fbconsole.ACCESS_TOKEN
			+ "&message=%s" % comment
			)
		print "Comment id: " + comment_id.text
			
		#Like the post
		requests.post("https://graph.facebook.com/" + str(post['post_id']) + "/likes/?access_token=" + fbconsole.ACCESS_TOKEN 
		+ "&method=POST")
		print "Liked"
	fbconsole.logout()
		
if __name__=='__main__':
	#Reply/like on last N (1 here) wallposts
	commentlikepost(1)
	print "Done"
