import paramiko
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--remote_dir')
parser.add_argument('--local_dir')
opt = parser.parse_args()

def remote_scp(host_ip, remote_path, local_path, username, password):
    t = paramiko.Transport((host_ip, 22))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    # 获取当前指定目录下的所有目录及文件，包含属性值
    files = sftp.listdir_attr(remote_path)
    for files_name in files:
        print(files_name.filename)

        remote_file = os.path.join(remote_path, files_name.filename)
        local_file = os.path.join(local_path, files_name.filename)

        src = remote_file
        des = local_file
        sftp.get(src, des)

    t.close()

if __name__ == '__main__':
    host_ip = '0.0.0.0'
    remote_path = opt.remote_dir
    local_path = opt.local_dir
    username = '321'
    password = '123'
    remote_scp(host_ip, remote_path, local_path, username, password)
