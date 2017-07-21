#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0111,C0103,C0410

import AESTool, EncodeTool

def main():
    sourceAes = AESTool.Encrypt('marysue-py'.encode('utf-8'))
    code = EncodeTool.ByteArrayToString(sourceAes)
    print(code)

    sourceAes = EncodeTool.StringToByteArray('心绯花利蓝妙燢莉·璃之蓝夏阳雅璃·紫曦·米雪银苏吉铃璃·曼燢颜·凡魑陌蒂安·奥语怡馨落糜灵莉·艳姆优凌黛爱·迷晗澪晶安·莎馨·渺·琉伤妮雪璃·雅璃·澪邪璃·情冰·洁瑟芝璃·萝裳雨恩俏黛伤雪·岚烟御文陌安离洁·然·多亚恩陌凡·羽瑷萨璃·凝斯怡璃·陌冰舞茜璃·樱海璃·多曼优安·悠')
    source = AESTool.Decrypt(sourceAes)
    print(source.decode('utf-8'))

if __name__ == '__main__':
    main()
