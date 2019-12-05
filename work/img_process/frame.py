# -*- coding:utf-8 *-*
import os
import sys


# reload(sys)
# sys.setdefaultencoding('utf-8')

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


videolist = ['.flv', '.mp4', '.mov', '.avi']


def ffm_to_img(src, dst, num):
    for rt, dirs, files in os.walk(src):
        for filename in files:
            name, suffix = os.path.splitext(filename)
            if suffix.lower() in videolist:
                sourcefile = os.path.join(rt, filename)
                outdir = os.path.join(dst, name)
                os.makedirs(outdir)
                outname = os.path.join(outdir, name + '-%d.jpg')
                # cmd = 'ffmpeg -i {0} -r 0.1 -qscale 0 {1}'.format(sourcefile, outname)
                cmd = 'ffmpeg -i "{0}" -r {2} -qscale 0 "{1}"'.format(sourcefile, outname,
                                                                      format(float(1) / float(num), '.3f'))
                os.system(cmd)


if __name__ == '__main__':
    videolist = ['.flv', '.mp4', '.mov', '.avi']
    # src = raw_input(ur'数据路径:'.encode('gbk'))
    src = r'C:\Users\Administrator\Desktop\work\src'
    # dst = raw_input(ur'抽帧路径:'.encode('gbk'))
    dst = r'C:\Users\Administrator\Desktop\work\res'
    # num = raw_input(ur'抽帧间隔(秒):'.encode('gbk'))
    num = str(1)
    ffm_to_img(src, dst, num)
    # for path in os.listdir(src):
    #     if os.path.isdir(os.path.join(src,path)):
    #         ffm_to_img(os.path.join(src,path),os.path.join(dst,path),videolist)
