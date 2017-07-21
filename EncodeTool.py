#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0111,C0103

from random import randint

Characters = '薰璃安莹洁莉樱殇雪羽晗灵血娜丽魑魅塔利亚伤梦儿海蔷玫瑰泪邪凡多姆威恩夏影琉舞雅蕾玥瑷曦月瑟薇蓝岚紫蝶馨琦洛凤颜鸢希玖兮雨烟叶兰凝冰伊如落心语凌爱陌悠千艳优花晶墨阳云筱残莲沫渺琴依然丝可茉黎幽幻银韵倾乐慕文思蕊清碎音芊黛怡莎苏香城萌美迷离白嫩风霜萝妖百合珠喃之倩情恋弥绯芸茜魂澪琪欣呗缈娅吉拉斯基柔惠朵茹妙铃裳纱颖蕴燢浅萦璎糜凪莳娥寂翼巧哀俏涅盘辰芝艾柒曼妲眉御寇妮米菲奥格萨温蒂'
Spliter = '·'

def UlongToString(number):
    result = []
    t = number
    length = len(Characters)

    checkNumber = 0

    while t > 0:
        q = int(t % length)
        result.append(Characters[q])
        checkNumber = checkNumber * length + q
        t = t // length

    return ''.join(result)

def ByteArrayToString(source):
    cursor = 0
    length = 0
    result = []

    while cursor < len(source):
        length = randint(1, 8)
        if cursor + length > len(source):
            length = len(source) - cursor

        if source[cursor + length - 1] == 0: # 如果小数组最后一位是0，会造成生成数字时无法判断此处为0还是空值，需要重新随机选一次
            continue

        bytepiece = bytearray(8)
        for i in range(length): bytepiece[i] = source[cursor + i]
        number = int.from_bytes(bytepiece, byteorder='little')
        result.append(UlongToString(number))
        cursor += length

    return Spliter.join(result)

def StringToUlong(text):
    number = 0
    length = len(Characters)

    i = len(text) - 1
    while i >= 0:
        q = Characters.find(text[i])
        if q == -1: raise ValueError('Illegal characters')
        number = number * length + q
        i -= 1

    return number

def StringToByteArray(code):
    subCodes = code.split(Spliter)
    source = b''
    for subCode in subCodes:
        number = StringToUlong(subCode)
        sourceBytes = number.to_bytes(8, byteorder='little')

        # 去掉数组末尾的0
        trimLength = len(sourceBytes) - 1
        while sourceBytes[trimLength] == 0: trimLength -= 1
        trimLength += 1
        sourceTrim = bytearray(trimLength)
        for i in range(trimLength): sourceTrim[i] = sourceBytes[i]

        source += sourceTrim

    return source
