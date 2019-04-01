# client_server_CartoonGAN

Python客户端上传图片到服务器，调用服务器端的CartoonGAN程序,生成相应风格图片,再下载到本地。

server端
* 服务器端开启一个端口的监听，接收客户端发出的参数请求

start.sh

server.py

client端
* 本地上传图片到服务器指定文件夹下
* 向服务器端发出转化的请求
* 将风格转换好的图片下载到本地

upload.py

client_sendmsg.py

download.py

