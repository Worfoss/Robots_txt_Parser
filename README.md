# Robots_txt_Parser

Output: 
```
$ python RobotsTxtParser.py --url https://www.youtube.com
** Robots.txt find for : https://www.youtube.com

-----__200__-----
https://www.youtube.com/get_video_info
https://www.youtube.com/results
https://www.youtube.com/signup
https://www.youtube.com/t/terms
https://www.youtube.com/timedtext_video
https://www.youtube.com/verify_age
https://www.youtube.com/watch_ajax

-----__204__-----
https://www.youtube.com/get_video

-----__400__-----
https://www.youtube.com/comment
https://www.youtube.com/watch_queue_ajax

-----__403__-----
https://www.youtube.com/watch_fragments_ajax

-----__404__-----
https://www.youtube.com/channel/*/community
https://www.youtube.com/login
https://www.youtube.com/user/*/community
https://www.youtube.com/watch_popup
```  
Todo:
* csv ouput
* xml output
